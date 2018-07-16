#!/usr/bin/python

#
# EfiPyCmdMemMap.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdMemMap.py is free software: you can redistribute it and/or modify
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

#
# EfiPy Command shell version class
#

class EFIPY_CMD_MEMMAP (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays the memory map maintained by the UEFI environment.'''

  name     = u"memmap"

  #
  # Shell version working function
  #
  def Run (self):

    Size      = EfiPy.UINTN (0)
    MapKey    = EfiPy.UINTN ()
    ItemSize  = EfiPy.UINTN ()
    Version   = EfiPy.UINT32 ()

    Status = EfiPy.gBS.GetMemoryMap (
               EfiPy.byref (Size),
               None,
               EfiPy.byref (MapKey),
               EfiPy.byref (ItemSize),
               EfiPy.byref (Version)
               )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      self.StdOut.printf(u"Get Memory map error 0x%016X\r\n" % Status)
      return 0

    TmpBuffer = bytearray (Size.value + EfiPy.SIZE_1KB)
    MemMap    = EfiPy.EFI_MEMORY_DESCRIPTOR.from_buffer (TmpBuffer)

    Status = EfiPy.gBS.GetMemoryMap (
               EfiPy.byref (Size),
               EfiPy.byref (MemMap),
               EfiPy.byref (MapKey),
               EfiPy.byref (ItemSize),
               EfiPy.byref (Version)
               )

    if Status != EfiPy.EFI_SUCCESS:
      self.StdOut.printf(u"Get Memory map error 0x%016X\r\n" % Status)
      return 0

    self.StdOut.printf(    u"Type       Start            End              # Pages          Attributes\r\n")

    MemTypeName = {
      EfiPy.EfiReservedMemoryType:      u"Reserved   ",
      EfiPy.EfiLoaderCode:              u"LoaderCode ",
      EfiPy.EfiLoaderData:              u"LoaderData ",
      EfiPy.EfiBootServicesCode:        u"BS_Code    ",
      EfiPy.EfiBootServicesData:        u"BS_Data    ",
      EfiPy.EfiRuntimeServicesCode:     u"RT_Code    ",
      EfiPy.EfiRuntimeServicesData:     u"RT_Data    ",
      EfiPy.EfiConventionalMemory:      u"Available  ",
      EfiPy.EfiUnusableMemory:          u"Unusable   ",
      EfiPy.EfiACPIReclaimMemory:       u"ACPI_Recl  ",
      EfiPy.EfiACPIMemoryNVS:           u"ACPI_NVS   ",
      EfiPy.EfiMemoryMappedIO:          u"MMIO       ",
      EfiPy.EfiMemoryMappedIOPortSpace: u"MMIO_Port  ",
      EfiPy.EfiPalCode:                 u"PalCode    "
    }

    for BufOffset in range (0, Size.value, ItemSize.value):

      MemMap    = EfiPy.EFI_MEMORY_DESCRIPTOR.from_buffer (TmpBuffer [BufOffset:])

      if MemMap.Type not in MemTypeName.keys():
        self.StdOut.printf(u"Memory Type error 0x%016X\r\n" % MemMap.Type)
        return 0

      OutStr  = MemTypeName [MemMap.Type]
      OutStr += u"%016X-" % (MemMap.PhysicalStart)
      OutStr += u"%016X " % (MemMap.PhysicalStart + EfiPy.SIZE_4KB * (MemMap.NumberOfPages) - 1)
      OutStr += u"%016X " % (MemMap.NumberOfPages)
      OutStr += u"%016X " % (MemMap.Attribute)
      OutStr += u"\r\n"
      self.StdOut.printf (OutStr)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_MEMMAP.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet = {}

  CmdSet  = CMD_SET ()

  EfiPyCmdObj = EFIPY_CMD_MEMMAP(CmdSet)

  Para    = EfiPyCmdObj.name + ""
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
