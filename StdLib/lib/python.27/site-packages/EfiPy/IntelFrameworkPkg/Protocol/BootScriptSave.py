#
# BootScriptSave.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# BootScriptSave.py is free software: you can redistribute it and/or
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

gEfiBootScriptSaveProtocolGuid = \
  EFI_GUID (0x470e1529, 0xb79e, 0x4e32, (0xa0, 0xfe, 0x6a, 0x15, 0x6d, 0x29, 0xf9, 0xb2))

class EFI_BOOT_SCRIPT_SAVE_PROTOCOL (Structure):
  pass

EFI_BOOT_SCRIPT_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BOOT_SCRIPT_SAVE_PROTOCOL), # IN  *This
  UINT16,                                 # IN  TableName,
  UINT16                                  # IN  OpCode
  # ...
  )

EFI_BOOT_SCRIPT_CLOSE_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BOOT_SCRIPT_SAVE_PROTOCOL), # IN  *This
  UINT16,                                 # IN  TableName,
  POINTER(EFI_PHYSICAL_ADDRESS)           # OUT *Address
  )

EFI_BOOT_SCRIPT_SAVE_PROTOCOL._fields_ = [
    ("Write",       EFI_BOOT_SCRIPT_WRITE),
    ("CloseTable",  EFI_BOOT_SCRIPT_CLOSE_TABLE)
  ]

