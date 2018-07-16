#
# FrameworkFirmwareVolumeBlock.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FrameworkFirmwareVolumeBlock.py is free software: you can redistribute it and/or
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

gFramerworkEfiFirmwareVolumeBlockProtocolGuid = \
  EFI_GUID (0xDE28BC59, 0x6228, 0x41BD, (0xBD, 0xF6, 0xA3, 0xB9, 0xAD,0xB5, 0x8D, 0xA1))

class FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL (Structure):
  pass

EFI_FVB_ATTRIBUTES  = UINT32

FRAMEWORK_EFI_FVB_GET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL),  # IN  *This
  POINTER(EFI_FVB_ATTRIBUTES)                             # OUT *Attributes
  )

FRAMEWORK_EFI_FVB_SET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL),  # IN      *This
  POINTER(EFI_FVB_ATTRIBUTES)                             # IN OUT  *Attributes
  )

FRAMEWORK_EFI_FVB_GET_PHYSICAL_ADDRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL),  # IN   *This
  POINTER(EFI_PHYSICAL_ADDRESS)                           # OUT  *Address
  )

FRAMEWORK_EFI_FVB_GET_BLOCK_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL),  # IN  *This
  EFI_LBA,                                                # IN  Lba,
  POINTER(UINTN),                                         # OUT *BlockSize,
  POINTER(UINTN)                                          # OUT *NumberOfBlocks
  )

FRAMEWORK_EFI_FVB_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL),  # IN      *This
  EFI_LBA,                                                # IN      Lba,
  UINTN,                                                  # IN      Offset,
  POINTER(UINTN),                                         # IN OUT  *NumBytes,
  POINTER(UINT8)                                          # IN OUT  *Buffer
  )

FRAMEWORK_EFI_FVB_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL),  # IN      *This
  EFI_LBA,                                                # IN      Lba,
  UINTN,                                                  # IN      Offset,
  POINTER(UINTN),                                         # IN OUT  *NumBytes,
  POINTER(UINT8)                                          # IN      *Buffer
  )

FRAMEWORK_EFI_LBA_LIST_TERMINATOR   = 0xFFFFFFFFFFFFFFFFL

FRAMEWORK_EFI_FVB_ERASE_BLOCKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL)   # IN      *This
  # ...
  )

FRAMEWORK_EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL._fields_ = [
    ("GetAttributes",       FRAMEWORK_EFI_FVB_GET_ATTRIBUTES),
    ("SetAttributes",       FRAMEWORK_EFI_FVB_SET_ATTRIBUTES),
    ("GetPhysicalAddress",  FRAMEWORK_EFI_FVB_GET_PHYSICAL_ADDRESS),
    ("GetBlockSize",        FRAMEWORK_EFI_FVB_GET_BLOCK_SIZE),
    ("Read",                FRAMEWORK_EFI_FVB_READ),
    ("Write",               FRAMEWORK_EFI_FVB_WRITE),
    ("EraseBlocks",         FRAMEWORK_EFI_FVB_ERASE_BLOCKS),
    ("ParentHandle",        EFI_HANDLE)
  ]

