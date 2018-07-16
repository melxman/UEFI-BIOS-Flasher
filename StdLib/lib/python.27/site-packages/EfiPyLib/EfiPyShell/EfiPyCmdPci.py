#!/usr/bin/python

#
# EfiPyCmdPci.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdPci.py is free software: you can redistribute it and/or modify
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

import EfiPy
import EfiPyCmdBase

from EfiPy.MdePkg.IndustryStandard import pci
from EfiPy.MdePkg.IndustryStandard import Acpi
import EfiPy.MdePkg.IndustryStandard as Industry

from EfiPy.MdePkg.Protocol.PciRootBridgeIo  import    \
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL,                    \
  gEfiPciRootBridgeIoProtocolGuid,                    \
  EfiPciWidthUint8,                                   \
  EfiPciWidthUint16,                                  \
  EfiPciWidthUint32,                                  \
  EfiPciWidthUint64

class PCI_COMMON_HEADER (Industry.EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("VendorId",            EfiPy.UINT16),
  ("DeviceId",            EfiPy.UINT16),
  ("Command",             EfiPy.UINT16),
  ("Status",              EfiPy.UINT16),
  ("RevisionId",          EfiPy.UINT8),
  ("ClassCode",           EfiPy.UINT8 * 3),
  ("CacheLineSize",       EfiPy.UINT8),
  ("PrimaryLatencyTimer", EfiPy.UINT8),
  ("HeaderType",          EfiPy.UINT8),
  ("Bist",                EfiPy.UINT8)
  ]

class PCI_DEVICE_HEADER (Industry.EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Bar",             EfiPy.UINT32 * 6),
  ("CardBusCISPtr",   EfiPy.UINT32),
  ("SubVendorId",     EfiPy.UINT16),
  ("SubSystemId",     EfiPy.UINT16),
  ("ROMBar",          EfiPy.UINT32),
  ("CapabilitiesPtr", EfiPy.UINT8),
  ("Reserved",        EfiPy.UINT8 * 3),
  ("Reserved1",       EfiPy.UINT32),
  ("InterruptLine",   EfiPy.UINT8),
  ("InterruptPin",    EfiPy.UINT8),
  ("MinGnt",          EfiPy.UINT8),
  ("MaxLat",          EfiPy.UINT8)
  ]

class PCI_BRIDGE_HEADER (Industry.EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Bar",                   EfiPy.UINT32 * 2),
  ("PrimaryBus",            EfiPy.UINT8),
  ("SecondaryBus",          EfiPy.UINT8),
  ("SubordinateBus",        EfiPy.UINT8),
  ("SecondaryLatencyTimer", EfiPy.UINT8),
  ("IoBase",                EfiPy.UINT8),
  ("IoLimit",               EfiPy.UINT8),
  ("SecondaryStatus",       EfiPy.UINT16),
  ("MemoryBase",            EfiPy.UINT16),
  ("MemoryLimit",           EfiPy.UINT16),
  ("PrefetchableMemBase",   EfiPy.UINT16),
  ("PrefetchableMemLimit",  EfiPy.UINT16),
  ("PrefetchableBaseUpper", EfiPy.UINT32),
  ("PrefetchableLimitUpper",EfiPy.UINT32),
  ("IoBaseUpper",           EfiPy.UINT16),
  ("IoLimitUpper",          EfiPy.UINT16),
  ("CapabilitiesPtr",       EfiPy.UINT8),
  ("Reserved",              EfiPy.UINT8 * 3),
  ("ROMBar",                EfiPy.UINT32),
  ("InterruptLine",         EfiPy.UINT8),
  ("InterruptPin",          EfiPy.UINT8),
  ("BridgeControl",         EfiPy.UINT16),
  ]

class PCI_CARDBUS_HEADER (Industry.EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CardBusSocketReg",      EfiPy.UINT32),
  ("CapabilitiesPtr",       EfiPy.UINT8),
  ("Reserved",              EfiPy.UINT8),
  ("SecondaryStatus",       EfiPy.UINT16),
  ("PciBusNumber",          EfiPy.UINT8),
  ("CardBusBusNumber",      EfiPy.UINT8),
  ("SubordinateBusNumber",  EfiPy.UINT8),
  ("CardBusLatencyTimer",   EfiPy.UINT8),
  ("MemoryBase0",           EfiPy.UINT32),
  ("MemoryLimit0",          EfiPy.UINT32),
  ("MemoryBase1",           EfiPy.UINT32),
  ("MemoryLimit1",          EfiPy.UINT32),
  ("IoBase0",               EfiPy.UINT32),
  ("IoLimit0",              EfiPy.UINT32),
  ("IoBase1",               EfiPy.UINT32),
  ("IoLimit1",              EfiPy.UINT32),
  ("InterruptLine",         EfiPy.UINT8),
  ("InterruptPin",          EfiPy.UINT8),
  ("BridgeControl",         EfiPy.UINT16)
  ]

class NON_COMMON_UNION (Industry.EFIPY_INDUSTRY_UNION):
  _fields_ = [
  ("Device",  PCI_DEVICE_HEADER),
  ("Bridge",  PCI_BRIDGE_HEADER),
  ("CardBus", PCI_CARDBUS_HEADER)
  ]

class PCI_CONFIG_SPACE (Industry.EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Common",      PCI_COMMON_HEADER),
  ("NonCommon",   NON_COMMON_UNION),
  ("Data",        EfiPy.UINT32 * 48)
  ]

#
# EfiPy Command memory dump class
#

class EFIPY_CMD_PCI (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays or modifies MEM/MMIO/IO/PCI/PCIE address space.'''

  name      = u"pci"
  Address   = 0x00
  Length    = 0x00
  Mmio      = False

  def ParaPreBuild (self, args):

    self.Paras.update ({u"-i"   : ["", False, 0, (), []]})
    self.Paras.update ({u"-s"   : ["", False, 1, (), []]})

  def ParaGet (self):

    if len (self.Paras[u"-s"][4]) == 1:
      self.Seg  = int (self.Paras[u"-s"][4][0], 16)
    else:
      self.Seg  = 0x00
    self.Bus    = 0x00
    self.Dev    = 0x00
    self.Func   = 0x00
    self.Verb   = self.Paras[u"-i"][1]
    self.Sum    = False

    if    len (self.args) == 1:

      self.Sum    = False

    elif  len (self.args) == 4:

      self.Bus    = int (self.args[1], 16)
      self.Dev    = int (self.args[2], 16)
      self.Func   = int (self.args[3], 16)

    else:

      raise NameError(u"EFIPY_CMD_PCI._parameters.Parameter error")

  def _CALC_EFI_PCI_ADDRESS (self, Bus, Dev, Func, Reg):

    return (Bus << 24) + (Dev << 16) + (Func << 8) + Reg

  def _CALC_EFI_PCIEX_ADDRESS (self, Bus, Dev, Func, ExReg):

    return (Bus << 24) + (Dev << 16) + (Func << 8) + (ExReg << 32)

  def _GetPciEAddressFromInputAddress (self, InputAddress):

    PciEAddress  = (InputAddress & 0xFFFFFFFFFFFFF000) >> 4
    PciEAddress += (InputAddress & 0x0000000000000FFF) << 32

    return PciEAddress

  def _PciGetNextBusRange (self, Descriptors):

    if Descriptors == None:
      return 0, pci.PCI_MAX_BUS, False

    TempDesc = EfiPy.cast (Descriptors, EfiPy.POINTER (Acpi.EFI_ACPI_ADDRESS_SPACE_DESCRIPTOR))

    # print "2. TempDesc[0].Desc, TempDesc[0].ResType", TempDesc[0].Desc, TempDesc[0].ResType

    Idx = 0
    while  TempDesc[Idx].Desc != Acpi.ACPI_END_TAG_DESCRIPTOR:

      if TempDesc[Idx].ResType == Acpi.ACPI_ADDRESS_SPACE_TYPE_BUS:

        AddrRangeMin = TempDesc[Idx].AddrRangeMin
        AddrRangeMax = TempDesc[Idx].AddrRangeMax

        Descriptors.value += EfiPy.sizeof (Acpi.EFI_ACPI_ADDRESS_SPACE_DESCRIPTOR)
        return Descriptors, TempDesc[Idx].AddrRangeMin, TempDesc[Idx].AddrRangeMax, False

      Descriptors.value += EfiPy.sizeof (Acpi.EFI_ACPI_ADDRESS_SPACE_DESCRIPTOR)
      Idx += 1

    if TempDesc[Idx].Desc == Acpi.ACPI_END_TAG_DESCRIPTOR:

      return Descriptors, 0, pci.PCI_MAX_BUS, True

    return None, None, None, True

  def _PciGetProtocolAndResource (self, Handle):

    TmpDev = EfiPy.PVOID ()

    Status = EfiPy.gBS.HandleProtocol (
                  Handle,
                  EfiPy.byref (gEfiPciRootBridgeIoProtocolGuid),
                  EfiPy.byref (TmpDev)
                 )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf("Locate HandleProtocol Fail (2) (Status = 0x%016X)!\r\n" % Status)
      return None, None

    IoDev = (EfiPy.cast (TmpDev, EfiPy.POINTER(EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL)))[0]

    Descriptors = EfiPy.PVOID ()
    Status = IoDev.Configuration (
               EfiPy.byref (IoDev),
               EfiPy.byref (Descriptors)
               )

    if Status == EfiPy.EFI_UNSUPPORTED:
      self.StdOut.printf("Locate HandleProtocol Fail (2) (Status = 0x%016X)!\r\n" % Status)
      return IoDev, None

    return IoDev, Descriptors

  def _PciFindProtocolInterface (self, HandleBuf, Segment, Bus):

    for Handle in HandleBuf:

      IoDev, Descriptors = self._PciGetProtocolAndResource (Handle)

      if Descriptors == None and Segment == IoDev.SegmentNumber:
        return EFI_SUCCESS, IoDev

      if IoDev.SegmentNumber != Segment:
        continue

      while True:

        Descriptors, MinBus, MaxBus, IsEnd = self._PciGetNextBusRange (Descriptors)

        if IsEnd == True:
          break

        if (MinBus <= Bus) and (MaxBus >= Bus):
          return EfiPy.EFI_SUCCESS, IoDev

    return EfiPy.EFI_NOT_FOUND, None

  #
  # Clear screen working function
  #
  def Run (self):

    SegmentNumber = 0L
    IoDev         = None

    PciHeader     = PCI_COMMON_HEADER()

    BufferSize    = EfiPy.UINTN (0)

    Status = EfiPy.gBS.LocateHandle (
               EfiPy.ByProtocol,
               EfiPy.byref (gEfiPciRootBridgeIoProtocolGuid),
               None,
               EfiPy.byref (BufferSize),
               None
              )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:

      self.StdOut.printf("Locate gEfiPciRootBridgeIoProtocolGuid Fail (1) (Status = 0x%016X)!\r\n" % Status)
      return 0

    TmpBuffer = bytearray (BufferSize.value)
    TmpHandle  = EfiPy.EFI_HANDLE.from_buffer (TmpBuffer)

    Status = EfiPy.gBS.LocateHandle (
               EfiPy.ByProtocol,
               EfiPy.byref (gEfiPciRootBridgeIoProtocolGuid),
               None,
               EfiPy.byref (BufferSize),
               EfiPy.byref (TmpHandle)
              )

    if Status != EfiPy.EFI_SUCCESS:

      self.StdOut.printf("Locate gEfiPciRootBridgeIoProtocolGuid Fail (2) (Status = 0x%016X)!\r\n" % Status)
      return 0

    t_EFI_HANDLE = EfiPy.EFI_HANDLE * 1
    HandleBuffer = t_EFI_HANDLE.from_buffer (TmpHandle)

    #
    # Find all PCI devices
    #

    self.StdOut.printf(" Seg Bus Dev Func\r\n")
    self.StdOut.printf(" --- --- --- ----\r\n")

    for Handle in HandleBuffer:

      # print Handle, type (Handle)

      IoDev, Descriptors = self._PciGetProtocolAndResource (Handle)

      if IoDev == None:
        continue

      while True:

        Descriptors, MinBus, MaxBus, IsEnd = self._PciGetNextBusRange (Descriptors)

        # print "MinBus: 0x%016X, MaxBus: 0x%016X, IsEnd:%s" % (MinBus, MaxBus, IsEnd)

        if IsEnd == True:
          break

        for Bus in range (MinBus, MaxBus + 1):

          for Device in range (0, pci.PCI_MAX_DEVICE + 1):

            for Func in range (0, pci.PCI_MAX_FUNC + 1):

              Address   = self._CALC_EFI_PCI_ADDRESS (Bus, Device, Func, 0)
              VendorId  = EfiPy.UINT16 ()
              IoDev.Pci.Read (
                         EfiPy.byref (IoDev),
                         EfiPciWidthUint16,
                         Address,
                         1,
                         EfiPy.byref (VendorId)
                         )

              if VendorId.value == 0xffff and Func == 0:
                break

              if VendorId.value != 0xffff:

                IoDev.Pci.Read (
                           EfiPy.byref (IoDev),
                           EfiPciWidthUint32,
                           Address,
                           EfiPy.sizeof (PciHeader) / EfiPy.sizeof (EfiPy.UINT32),
                           EfiPy.byref (PciHeader)
                           )

                self.StdOut.printf("  %02X  %02X  %02X  %02X\r\n" % (
                  IoDev.SegmentNumber, Bus, Device, Func
                  ))
                self.StdOut.printf("     Vendor %04X Device %04X Prog Interface  %X\r\n" % (
                  PciHeader.VendorId, PciHeader.DeviceId, PciHeader.ClassCode[0]
                ))

                if (Func == 0) and ((PciHeader.HeaderType & pci.HEADER_TYPE_MULTI_FUNCTION) == 0x00):
                  break

        if Descriptors == None:
          break

    #
    # Find Identified PCI device
    #

    Status, IoDev = self._PciFindProtocolInterface (HandleBuffer, self.Seg, self.Bus)
    Address       = self._CALC_EFI_PCI_ADDRESS (self.Bus, self.Dev, self.Func, 0)
    bConfigSpace  = bytearray (EfiPy.sizeof (PCI_CONFIG_SPACE))
    ConfigSpace   = PCI_CONFIG_SPACE.from_buffer (bConfigSpace)

    Status = IoDev.Pci.Read (
               EfiPy.byref (IoDev),
               EfiPciWidthUint8,
               Address,
               EfiPy.sizeof (ConfigSpace),
               EfiPy.byref (ConfigSpace)
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf("Read Pci data fail 0x%016X\r\n" % (Status))
      return 0

    from   Utility.EfiPyUtility     import EfiPyHexDump

    self.StdOut.printf("Dump Pci %02X %02X %02X memory\r\n" % (self.Bus, self.Dev, self.Func))
    EfiPyHexDump (self.StdOut, 2, 0x0000, bConfigSpace, True)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_PCI.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet = {}

  CmdSet  = CMD_SET ()

  EfiPyCmdObj = EFIPY_CMD_PCI(CmdSet)

  Para    = EfiPyCmdObj.name + " -s 0"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 0 0 0"
  Args    = Para.split()
  
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()
  
  print
  
  Para    = EfiPyCmdObj.name + " 0 0 0 -i"
  Args    = Para.split()
  
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()
  
  print
  
  Para    = EfiPyCmdObj.name + " 0 1 0 -i"
  Args    = Para.split()
  
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()
  
  print
  
  Para    = EfiPyCmdObj.name + " 0 1 1 -i"
  Args    = Para.split()
  
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()
  
  print
  
  Para    = EfiPyCmdObj.name + " 0 1 3 -i"
  Args    = Para.split()
  
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()
  
  print
  
  Para    = EfiPyCmdObj.name + " 0 2 0 -i"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 0 3 0 -i"
  Args    = Para.split()
  
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()
  
  print

  import sys
  sys.exit(ret)
