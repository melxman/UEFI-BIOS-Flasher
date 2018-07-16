#
# ExtendedSalBootService.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ExtendedSalBootService.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
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

from EfiPy  import *

from EfiPy.MdePkg.IndustryStandard import Sal

gEfiExtendedSalBootServiceProtocolGuid  = \
  EFI_GUID (0xde0ee9a4, 0x3c7a, 0x44f2, (0xb7, 0x8b, 0xe3, 0xcc, 0xd6, 0x9c, 0x3a, 0xf7 ))

class EXTENDED_SAL_BOOT_SERVICE_PROTOCOL (Structure):
  pass

EXTENDED_SAL_ADD_SST_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EXTENDED_SAL_BOOT_SERVICE_PROTOCOL),  # IN *This
  UINT16,                                       # IN SalAVersion,
  UINT16,                                       # IN SalBVersion,
  PCHAR8,                                       # IN *OemId,
  PCHAR8                                        # IN *ProductId
  )

EXTENDED_SAL_ADD_SST_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EXTENDED_SAL_BOOT_SERVICE_PROTOCOL),  # IN *This
  POINTER(UINT8),                               # IN *TableEntry,
  UINTN                                         # IN EntrySize
  )

SAL_INTERNAL_EXTENDED_SAL_PROC = CFUNCTYPE (
  Sal.SAL_RETURN_REGS,
  UINT64,           # IN  FunctionId,
  UINT64,           # IN  Arg2,
  UINT64,           # IN  Arg3,
  UINT64,           # IN  Arg4,
  UINT64,           # IN  Arg5,
  UINT64,           # IN  Arg6,
  UINT64,           # IN  Arg7,
  UINT64,           # IN  Arg8,
  BOOLEAN,          # IN  VirtualMode,
  PVOID             # IN  *ModuleGlobal  OPTIONAL
  )

EXTENDED_SAL_REGISTER_INTERNAL_PROC = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EXTENDED_SAL_BOOT_SERVICE_PROTOCOL),  # IN *This
  UINT64,                                       # IN ClassGuidLo,
  UINT64,                                       # IN ClassGuidHi,
  UINT64,                                       # IN FunctionId,
  SAL_INTERNAL_EXTENDED_SAL_PROC,               # IN InternalSalProc,
  PVOID                                         # IN *PhysicalModuleGlobal  OPTIONAL
  )

EXTENDED_SAL_PROC = CFUNCTYPE (
  Sal.SAL_RETURN_REGS,
  UINT64,           # IN ClassGuidLo,
  UINT64,           # IN ClassGuidHi,
  UINT64,           # IN FunctionId,
  UINT64,           # IN Arg2,
  UINT64,           # IN Arg3,
  UINT64,           # IN Arg4,
  UINT64,           # IN Arg5,
  UINT64,           # IN Arg6,
  UINT64,           # IN Arg7,
  UINT64            # IN Arg8
  )

EXTENDED_SAL_BOOT_SERVICE_PROTOCOL._fields_ = [
    ("AddSalSystemTableInfo",   EXTENDED_SAL_ADD_SST_INFO),
    ("AddSalSystemTableEntry",  EXTENDED_SAL_ADD_SST_ENTRY),
    ("RegisterExtendedSalProc", EXTENDED_SAL_REGISTER_INTERNAL_PROC), 
    ("ExtendedSalProc",         EXTENDED_SAL_PROC)
  ]

