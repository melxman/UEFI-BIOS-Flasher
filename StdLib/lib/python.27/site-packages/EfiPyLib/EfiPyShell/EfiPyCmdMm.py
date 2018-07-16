#!/usr/bin/python

#
# EfiPyCmdMm.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdMm.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.Protocol.PciRootBridgeIo  import    \
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL,                    \
  gEfiPciRootBridgeIoProtocolGuid,                    \
  EfiPciWidthUint8,                                   \
  EfiPciWidthUint16,                                  \
  EfiPciWidthUint32,                                  \
  EfiPciWidthUint64

#
# EfiPy Command memory dump class
#

class EFIPY_CMD_MM (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays or modifies MEM/MMIO/IO/PCI/PCIE address space.'''

  name      = u"mm"
  Address   = 0x00
  Length    = 0x00
  Mmio      = False

  def ParaPreBuild (self, args):

    self.Paras.update ({u"-w"   : ["", False, 1, (), []]})
    self.Paras.update ({u"-mem" : ["", False, 0, (), []]})
    self.Paras.update ({u"-mmio": ["", False, 0, (), []]})
    self.Paras.update ({u"-io"  : ["", False, 0, (), []]})
    self.Paras.update ({u"-pci" : ["", False, 0, (), []]})
    self.Paras.update ({u"-pcie": ["", False, 0, (), []]})

  def ParaGet (self):

    self.Address      = 0x00
    self.Length       = 0x01
    self.Width        = EfiPciWidthUint8
    self.Write        = False
    self.Value        = 0xAAAAAAAAAAAAAAAA
    self.MemRw        = self.Paras[u"-mem"][1]
    self.MmioRw       = self.Paras[u"-mmio"][1]
    self.IoRw         = self.Paras[u"-io"][1]
    self.PciRw        = self.Paras[u"-pci"][1]
    self.PcieRw       = self.Paras[u"-pcie"][1]

    if self.Paras[u"-w"][1]:

      self.Length = int (self.Paras[u"-w"][4][0])

      if    self.Length == 1:
        self.Width = EfiPciWidthUint8
      elif  self.Length == 2:
        self.Width = EfiPciWidthUint16
      elif  self.Length == 4:
        self.Width = EfiPciWidthUint32
      elif  self.Length == 8:
        self.Width = EfiPciWidthUint64

    if not (self.MmioRw or self.IoRw or self.PciRw or self.PcieRw):

      self.MemRw = True

    if len (self.args) > 3 or len (self.args) < 2:

      raise NameError(u"EFIPY_CMD_MM._parameters.Parameter error")

    self.Address = int (self.args[1], 16)

    if len (self.args) == 3:

      self.Write = True
      self.Value = int (self.args[2], 16)

    # print self.args
    # print "self.Address, self.Value, self.Length, self.MemRw, self.MmioRw, self.IoRw, self.PciRw, self.PcieRw, self.Write"
    # print "0x%016X, 0x%016X" % (self.Address, self.Value), self.Length, self.MemRw, self.MmioRw, self.IoRw, self.PciRw, self.PcieRw, self.Write

  def _GetPciEAddressFromInputAddress (self, InputAddress):

    PciEAddress  = (InputAddress & 0xFFFFFFFFFFFFF000) >> 4
    PciEAddress += (InputAddress & 0x0000000000000FFF) << 32

    return PciEAddress

  #
  # Clear screen working function
  #
  def Run (self):

    SegmentNumber = 0L

    IoDev = None

    if self.PciRw == True:
      SegmentNumber = (self.Address >> 32) & 0xFF
      self.Address &= 0xFFFFFFFFL

    if self.PcieRw == True:
      SegmentNumber = (self.Address >> 36) & 0xFF
      self.Address &= 0XFFFFFFFFFL
      self.Address = self._GetPciEAddressFromInputAddress (self.Address)

    if self.MemRw == False:

      BufferSize    = EfiPy.UINTN (0)
      HandleBuffer  = EfiPy.POINTER (EfiPy.EFI_HANDLE) ()

      Status = EfiPy.gBS.LocateHandleBuffer (
                 EfiPy.ByProtocol,
                 EfiPy.byref (gEfiPciRootBridgeIoProtocolGuid),
                 None,
                 EfiPy.byref (BufferSize),
                 EfiPy.byref (HandleBuffer)
                )

      if Status != EfiPy.EFI_SUCCESS:

        self.StdOut.printf("Locate gEfiPciRootBridgeIoProtocolGuid Fail (Status = 0x%016X)!\r\n" % Status)
        return 0

      # print "type (HandleBuffer)", BufferSize.value, type (HandleBuffer)

      for Index in range (BufferSize.value):

        TmpDev = EfiPy.PVOID ()

        Status = EfiPy.gBS.HandleProtocol (
                       HandleBuffer[Index],
                       EfiPy.byref (gEfiPciRootBridgeIoProtocolGuid),
                       EfiPy.byref (TmpDev)
                      )
        if EfiPy.EFI_ERROR (Status):
          continue

        IoDev = (EfiPy.cast (TmpDev, EfiPy.POINTER(EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL)))[0]

        if IoDev.SegmentNumber != SegmentNumber:
          IoDev = None


      if IoDev == None:
        self.StdOut.printf("Find IoDev Fail!\r\n")

    if    self.Width == EfiPciWidthUint8:
      Buffer = EfiPy.UINT8 (self.Value)
    elif  self.Width == EfiPciWidthUint16:
      Buffer = EfiPy.UINT16 (self.Value)
    elif  self.Width == EfiPciWidthUint32:
      Buffer = EfiPy.UINT32 (self.Value)
    elif  self.Width == EfiPciWidthUint64:
      Buffer = EfiPy.UINT64 (self.Value)

    if self.Write == True:

      if    self.MemRw  == True:

        if    self.Width == EfiPciWidthUint8:
          Buffer = EfiPy.UINT8.from_address (self.Address)
        elif  self.Width == EfiPciWidthUint16:
          Buffer = EfiPy.UINT16.from_address (self.Address)
        elif  self.Width == EfiPciWidthUint32:
          Buffer = EfiPy.UINT32.from_address (self.Address)
        elif  self.Width == EfiPciWidthUint64:
          Buffer = EfiPy.UINT64.from_address (self.Address)

        Buffer.value = self.Value

      elif  self.MmioRw == True:

        IoDev.Mem.Write (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

      elif  self.IoRw   == True:

        IoDev.Io.Write (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

      elif  self.PciRw  == True:

        IoDev.Pci.Write (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

      elif  self.PcieRw == True:

        IoDev.Pci.Write (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

    else:

      if    self.MemRw  == True:

        if    self.Width == EfiPciWidthUint8:
          Buffer = EfiPy.UINT8.from_address (self.Address)
        elif  self.Width == EfiPciWidthUint16:
          Buffer = EfiPy.UINT16.from_address (self.Address)
        elif  self.Width == EfiPciWidthUint32:
          Buffer = EfiPy.UINT32.from_address (self.Address)
        elif  self.Width == EfiPciWidthUint64:
          Buffer = EfiPy.UINT64.from_address (self.Address)

        self.StdOut.printf ("MEM (R) 0x%016X : " % (self.Address))

      elif  self.MmioRw == True:

        IoDev.Mem.Read (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

        self.StdOut.printf ("MMIO (R) 0x%016X : " % (self.Address))

      elif  self.IoRw   == True:

        IoDev.Io.Read (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

        self.StdOut.printf ("IO (R) 0x%016X : " % (self.Address))

      elif  self.PciRw  == True:

        IoDev.Pci.Read (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

        self.StdOut.printf ("PCI (R) 0x%016X : " % (self.Address))

      elif  self.PcieRw == True:

        IoDev.Pci.Read (
          EfiPy.byref (IoDev),
          self.Width,
          self.Address,
          1,
          EfiPy.cast (EfiPy.byref (Buffer), EfiPy.PVOID)
          )

        self.StdOut.printf ("PCIE (R) 0x%016X : " % (self.Address))

      if    self.Width == EfiPciWidthUint8:
        self.StdOut.printf ("0x%02X\r\n" % (Buffer.value))
      elif  self.Width == EfiPciWidthUint16:
        self.StdOut.printf ("0x%04X\r\n" % (Buffer.value))
      elif  self.Width == EfiPciWidthUint32:
        self.StdOut.printf ("0x%08X\r\n" % (Buffer.value))
      elif  self.Width == EfiPciWidthUint64:
        self.StdOut.printf ("0x%016X\r\n" % (Buffer.value))

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_MM.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_MM(CmdSet)

  Para    = EfiPyCmdObj.name + " A000000 -w 8 0x0123456789ABCDEF"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " A000000 -w 8"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " -mem 82020000 -w 8"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " -mmio 82020000 -w 1"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " -mmio 82020000 -w 8"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " -mmio 82000000 -w 8 0x0123456789ABCDEF"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " -mmio 82000000 -w 8"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 70 -io -w 1"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 71 -io"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 0 -pci -w 4"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 0 -pcie"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 0 -pci -w 8"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  print Para
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
