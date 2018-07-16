#
# S3SaveState.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# S3SaveState.py is free software: you can redistribute it and/or
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

from EfiPy import *

gEfiS3SaveStateProtocolGuid   = \
  EFI_GUID (0xe857caf6, 0xc046, 0x45dc, ( 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87 ))

EFI_S3_BOOT_SCRIPT_POSITION = PVOID

class EFI_S3_SAVE_STATE_PROTOCOL (Structure):
  pass

EFI_S3_SAVE_STATE_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN  *This
  UINT16                                # IN  OpCode
  )

EFI_S3_SAVE_STATE_INSERT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN      *This
  BOOLEAN,                              # IN      BeforeOrAfter,
  POINTER(EFI_S3_BOOT_SCRIPT_POSITION), # IN OUT  *Position       OPTIONAL,
  UINT16                                # IN      OpCode
  )

EFI_S3_SAVE_STATE_LABEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN        *This
  BOOLEAN,                              # IN        BeforeOrAfter,
  BOOLEAN,                              # IN        CreateIfNotFound,
  POINTER(EFI_S3_BOOT_SCRIPT_POSITION), # IN OUT    *Position       OPTIONAL,
  POINTER(UINT8)                        # IN CONST  *Label  
  )

EFI_S3_SAVE_STATE_COMPARE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN      *This
  EFI_S3_BOOT_SCRIPT_POSITION,          # IN      Position1,
  EFI_S3_BOOT_SCRIPT_POSITION,          # IN      Position2,
  POINTER(UINTN)                        #     OUT *RelativePosition  
  )

EFI_S3_SAVE_STATE_PROTOCOL._fields_ = [
    ("Write",   EFI_S3_SAVE_STATE_WRITE),
    ("Insert",  EFI_S3_SAVE_STATE_INSERT),
    ("Label",   EFI_S3_SAVE_STATE_LABEL),
    ("Compare", EFI_S3_SAVE_STATE_COMPARE)
  ]

