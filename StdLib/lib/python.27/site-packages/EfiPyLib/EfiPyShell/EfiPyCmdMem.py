#!/usr/bin/python

#
# EfiPyCmdMem.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdMem.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.Guid.SmBios import gEfiSmbiosTableGuid

from EfiPy.MdePkg.Guid.Mps    import gEfiMpsTableGuid

from EfiPy.MdePkg.Guid.SalSystemTable import gEfiSalSystemTableGuid

from EfiPy.MdePkg.Guid.Acpi   import  \
  gEfiAcpi10TableGuid,                \
  gEfiAcpi20TableGuid

from EfiPy.MdePkg.Protocol.PciRootBridgeIo  import    \
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL,                    \
  gEfiPciRootBridgeIoProtocolGuid,                    \
  EfiPciWidthUint8

from Utility.EfiPyUtility     import EfiPyHexDump

#
# EfiPy Command memory dump class
#

class EFIPY_CMD_MEM (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays the contents of system or device memory.'''

  name      = u"mem"
  # Address   = 0x00
  # Length    = 0x00
  # Mmio      = False

  def ParaPreBuild (self, args):

    self.Paras.update ({u"-mmio": ["--mmio", False, 0, (), []]})

  #
  # Get parameter from list to command specific function
  #
  def ParaGet(self):

    self.Address      = 0x00
    self.Length       = 0x00
    self.Mmio         = self.Paras[u"-mmio"][1]

    CheckRight = True

    self.Address = EfiPy.addressof (EfiPy.gST)
    self.Length  = 16 * 32

    if type(self.args) is not list:
      raise NameError(u"EFIPY_CMD_MEM._parameters.TypeError1")

    try:

      if  len(self.args) > 3:
        raise NameError(u"EFIPY_CMD_MEM._parameters.TypeError2")

      self.Address = int(self.args[1], 16)

      if  len(self.args) == 3:
        self.Length  = int(self.args[2], 16)

      if 0 == self.Length:
        self.StdOut.printf("Memory Length can not be zeor, set as dafault 0x%20X\r\n" % (16 * 32))
        self.Length = 16 * 32

    except:
      self.StdOut.printf("Invalide parameter %s\r\n" % str(self.args))

  #
  # Clear screen working function
  #
  def Run (self):

    # Address, Length, Mmio = self._parameters()

    if self.Mmio == True:

      Interface = EfiPy.PVOID ()
      Status = EfiPy.gBS.LocateProtocol(
                 EfiPy.byref (gEfiPciRootBridgeIoProtocolGuid),
                 None,
                 EfiPy.byref (Interface)
                 )

      if EfiPy.RETURN_ERROR (Status):
        self.StdOut.printf("Locate gEfiPciRootBridgeIoProtocolGuid Fail (Status = 0x%016X)!\r\n" % Status)
        return 0

      PciProtocol = EfiPy.cast (Interface, EfiPy.POINTER(EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL))

      Memory = (EfiPy.CHAR8 * self.Length)()
      Status = PciProtocol[0].Mem.Read (
                 PciProtocol,
                 EfiPciWidthUint8,
                 self.Address,
                 self.Length,
                 EfiPy.byref (Memory)
                 )

      if EfiPy.RETURN_ERROR (Status):
        self.StdOut.printf("PciRootBridgeIo error:! (Status = 0x%016X)!\r\n" % Status)
        return 0

      self.StdOut.printf("Memory Mapped IO Address %016X %X Bytes\r\n" % (self.Address, self.Length))
      EfiPyHexDump (self.StdOut, 2, self.Address, Memory, True)

      return 0

    else:

      self.StdOut.printf("Memory Address %016X %X Bytes\r\n" % (self.Address, self.Length))

      Memory = (EfiPy.CHAR8 * self.Length).from_address (self.Address)

      EfiPyHexDump (self.StdOut, 2, self.Address, Memory, True)

    if self.Address != EfiPy.addressof (EfiPy.gST):
      return 0

    RuntimeServices     = EfiPy.addressof(EfiPy.gRT)
    BootServices        = EfiPy.addressof(EfiPy.gBS)
    SalTableAddress     = 0
    AcpiTableAddress    = 0
    Acpi20TableAddress  = 0
    MpsTableAddress     = 0
    SmbiosTableAddress  = 0

    for i in range (EfiPy.gST.NumberOfTableEntries):

      ComGuid   = EfiPy.gST.ConfigurationTable[i].VendorGuid
      ComHandle = EfiPy.gST.ConfigurationTable[i].VendorTable

      if    ComGuid == gEfiSalSystemTableGuid:
        SalTableAddress     = ComHandle

      elif  ComGuid == gEfiAcpi10TableGuid:
        AcpiTableAddress    = ComHandle

      elif  ComGuid == gEfiAcpi20TableGuid:
        Acpi20TableAddress  = ComHandle

      elif  ComGuid == gEfiMpsTableGuid:
        MpsTableAddress     = ComHandle

      elif  ComGuid == gEfiSmbiosTableGuid:
        SmbiosTableAddress  = ComHandle

    self.StdOut.printf("Valid EFI Header at Address %016X\r\n" % self.Address)
    self.StdOut.printf("---------------------------------------------\r\n")

    self.StdOut.printf("System: Table Structure size %08X revision %08X\r\n" % (
      EfiPy.gST.Hdr.HeaderSize,
      EfiPy.gST.Hdr.Revision)
      )

    self.StdOut.printf("ConIn (%016X) ConOut (%016X) StdErr (%016X)\r\n" % (
      EfiPy.addressof (EfiPy.gST.ConIn[0]),
      EfiPy.addressof (EfiPy.gST.ConOut[0]),
      EfiPy.addressof (EfiPy.gST.StdErr[0]))
      )

    self.StdOut.printf("Runtime Services %016X\r\n" % RuntimeServices)
    self.StdOut.printf("Boot Services    %016X\r\n" % BootServices)
    self.StdOut.printf("SAL System Table %016X\r\n" % SalTableAddress)
    self.StdOut.printf("ACPI Table       %016X\r\n" % AcpiTableAddress)
    self.StdOut.printf("ACPI 2.0 Table   %016X\r\n" % Acpi20TableAddress)
    self.StdOut.printf("MPS Table        %016X\r\n" % MpsTableAddress)
    self.StdOut.printf("SMBIOS Table     %016X\r\n" % SmbiosTableAddress)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_MEM.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_MEM(CmdSet)

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  ret = EfiPyCmdObj.Run()

  Para    = EfiPyCmdObj.name + " -mmio 82020000"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  ret = EfiPyCmdObj.Run()

  Para    = EfiPyCmdObj.name + " -mmio 82020000 20"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)
  EfiPyCmdObj.ParaGet ()
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
