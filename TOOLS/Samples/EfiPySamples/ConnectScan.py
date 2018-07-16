#
# ConnectScan.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# ConnectScan.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy as e
import pAnalyzer.bFinder as bf

#
# Device type modules
#
import EfiPy.MdePkg.Protocol.DevicePath as DevP
import EfiPy.MdePkg.Library.DevicePathLib as DevPathLib

from EfiPy.MdePkg.Protocol.DevicePath import gEfiDevicePathProtocolGuid
from EfiPy.MdePkg.Protocol.DevicePathFromText import gEfiDevicePathFromTextProtocolGuid, EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL
from EfiPy.MdePkg.Protocol.DevicePathUtilities import gEfiDevicePathUtilitiesProtocolGuid, EFI_DEVICE_PATH_UTILITIES_PROTOCOL

#
# Bus type modules
#
from EfiPy.MdePkg.Protocol.PciRootBridgeIo import gEfiPciRootBridgeIoProtocolGuid
from EfiPy.MdePkg.Protocol.PciIo import gEfiPciIoProtocolGuid, EFI_PCI_IO_PROTOCOL, EfiPciIoWidthUint8
import EfiPy.MdePkg.IndustryStandard.pci as pci

#
# ConnectScan class for finding binding driver
# which supported function return EFI_SUCCESS
#
class ConnectScan (bf.bFinder):

  #
  # class __init__ function
  #
  def __init__ (self, DevPathName, OutFile = None):

    bf.bFinder.__init__ (self, DevPathName, OutFile)

    # Locate EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL protocol
    Interface = e.PVOID()

    Status = e.gBS.LocateProtocol (
               e.byref (gEfiDevicePathFromTextProtocolGuid),
               None,
               e.byref (Interface)
               )

    if e.EFI_ERROR (Status):
      self.dOut.ExtraOut ("Locate EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL Protocol Error (Status:%x)\n" % Status)
      self.dOut.terminate ()
      exit(0)

    self.DevPathFromText = e.cast (
                             Interface,
                             e.POINTER(EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL)
                             )[0]

    # Locate EFI_DEVICE_PATH_UTILITIES_PROTOCOL protocol

    Interface = e.PVOID()
    Status = e.gBS.LocateProtocol(
               e.byref(gEfiDevicePathUtilitiesProtocolGuid),
               None,
               Interface
               )
    if e.EFI_ERROR (Status):
      self.dOut.ExtraOut ("Locate EFI_DEVICE_PATH_UTILITIES_PROTOCOL Protocol Error (Status:%x)\n" % Status)
      self.dOut.terminate ()
      exit(0)

    self.DevPathUtilities = e.cast (
                              Interface,
                              e.POINTER(EFI_DEVICE_PATH_UTILITIES_PROTOCOL)
                              )[0]

    #
    # ConnectScan class inner members
    #
    self.DevPathName = DevPathName
    self.DevPath = self.DevPathFromText.ConvertTextToDevicePath (DevPathName)
    self.dOut.ExtraOut ("\nDevice Path String: %s\n" % self.DevPathName)
    self.dOut.ExtraOut ("Result...\n")

    self.DevConnect = self.DevConnectDefault

  #
  # ConnectScan default function for calling gBS.ConnectController()
  #
  # This function is referenced from UEFI spec: EFI_BOOT_SERVICES.ConnectController()
  #
  def ConnectDevicePath (self, DevicePathToConnect = None):

    if DevicePathToConnect == None:
      DevicePathToConnect = self.DevPath
    if DevicePathToConnect == None:
      return e.EFI_INVALID_PARAMETER

    PreviousHandle = e.PVOID()
    Handle = e.EFI_HANDLE ()

    while True:

      RemainingDevicePath = DevicePathToConnect
      Status = e.gBS.LocateDevicePath (
                 e.byref (gEfiDevicePathProtocolGuid),
                 e.byref (RemainingDevicePath),
                 e.byref (Handle)
                 )

      if not e.EFI_ERROR (Status) and Handle != None:
        if PreviousHandle.value == Handle.value:
          Status = e.EFI_NOT_FOUND
        else:
          PreviousHandle = Handle;
          self.dOut.ExtraOut ("1. ConnectController Handle... 0x%08X\n" % Handle.value)
          Status = e.gBS.ConnectController (
                     Handle,
                     None,
                     RemainingDevicePath,
                     True
                     )

      if e.EFI_ERROR (Status) or RemainingDevicePath[0].IsDevicePathEnd():
        break

  def _ConnectPciRootBridge (self):

    RootBridgeHandleCount = e.UINTN(0)
    RootBridgeHandleBuffer = e.POINTER(e.EFI_HANDLE) ()

    Status = e.gBS.LocateHandleBuffer (
               e.ByProtocol,  
               e.byref (gEfiPciRootBridgeIoProtocolGuid),
               None,  
               e.byref (RootBridgeHandleCount),
               e.byref (RootBridgeHandleBuffer)
               );
    if e.EFI_ERROR (Status):
      return Status

    for RootBridgeIndex in range (RootBridgeHandleCount.value):
      self.dOut.ExtraOut ("2. ConnectController Handle... 0x%08X\n" % RootBridgeHandleBuffer[RootBridgeIndex].value)
      e.gBS.ConnectController (RootBridgeHandleBuffer[RootBridgeIndex], None, None, False)

    return e.EFI_SUCCESS

  #
  # ConnectScan 2nd function for calling gBS.ConnectController()
  #
  # This function is referenced from EDK2
  # ShellPkg/Library/UefiShellDriver1CommandsLib/Connect.c::ShellConnectFromDevPaths()
  #
  def DevConnect2 (self):

    CopyOfDevPath = self.DevPath
    Size = e.UINTN()
    Class = (e.UINT8 *3)()

    while True:

      Instance = self.DevPathUtilities.GetNextDevicePathInstance (
                   e.byref (CopyOfDevPath),
                   e.byref (Size)
                   )

      if Size.value == 0:
        break
      if Instance == None:
        return e.EFI_UNSUPPORTED

      Next = Instance
      while Next[0].Type != DevP.END_DEVICE_PATH_TYPE:
        Next = DevPathLib.NextDevicePathNode(Next)

      DevPathLib.SetDevicePathEndNode (Next)

      if Instance[0].Type == DevP.MESSAGING_DEVICE_PATH and \
        (Instance[0].SubType == DevP.MSG_USB_CLASS_DP or    \
         Instance[0].SubType == DevP.MSG_USB_WWID_DP):

        Status = self._ConnectPciRootBridge ()
        if e.EFI_ERROR (Status):
          return Status

        HandleArrayCount = e.UINTN()
        HandleArray      = e.POINTER (e.EFI_HANDLE)()
        Status = e.gBS.LocateHandleBuffer (
                  e.ByProtocol,
                  e.byref (gEfiPciIoProtocolGuid),
                  None,
                  e.byref (HandleArrayCount),
                  e.byref (HandleArray)
                  )
        if e.EFI_ERROR (Status):
          continue

        for Index in range (HandleArrayCount.value):
          TempV = e.PVOID ()
          Status = e.gBS.HandleProtocol (
                    HandleArray[Index],
                    e.byref (gEfiPciIoProtocolGuid),
                    e.byref (TempV)
                    )
          if e.EFI_ERROR (Status):
            continue
          PciIo = e.cast (TempV, e.POINTER (EFI_PCI_IO_PROTOCOL))
          Status = PciIo[0].Pci.Read (
                     PciIo,
                     EfiPciIoWidthUint8,
                     0x09,
                     3,
                     e.byref (Class)
                     )
          if e.EFI_ERROR (Status):
            continue

        # print "Class[2]", Class[2], type (Class[2])
          if Class[2] == pci.PCI_CLASS_SERIAL and \
             Class[1] == pci.PCI_CLASS_SERIAL_USB:

            self.dOut.ExtraOut ("3. ConnectController Handle... 0x%08X\n" % HandleArray[Index].value)
            Status = e.gBS.ConnectController (
                       HandleArray[Index],
                       None,
                       Instance,
                       False
                       )

      else:
        self.ConnectDevicePath (Instance)

      if CopyOfDevPath == None:
        break

  def DevConnectDefault (self):

    self.ConnectDevicePath (self.DevPath)


if __name__ == '__main__':

  DevPathText = u"PciRoot(0x0)/Pci(0x1,0x0)/Serial(0x1)"

  # Cs = ConnectScan (DevPathText, 'ConnectScan.txt')
  Cs = ConnectScan (DevPathText)
  # Cs.DevConnect = Cs.DevConnect2
  Cs.finding ()
