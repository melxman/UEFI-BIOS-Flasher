#
# FirmwareVolumeBlock.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FirmwareVolumeBlock.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiBaseType   import *
from EfiPy.MdePkg.Uefi.UefiSpec       import *

#
# BUGBUG
# From MdePkg/Include/Pi/PiFirmwareVolume.py
#
EFI_FVB_ATTRIBUTES_2  = UINT32

gEfiFirmwareVolumeBlockProtocolGuid   = \
  EFI_GUID (0x8f644fa9, 0xe850, 0x4db1, (0x9c, 0xe2, 0xb, 0x44, 0x69, 0x8e, 0x8d, 0xa4 ))

gEfiFirmwareVolumeBlock2ProtocolGuid  = \
  EFI_GUID (0x8f644fa9, 0xe850, 0x4db1, (0x9c, 0xe2, 0xb, 0x44, 0x69, 0x8e, 0x8d, 0xa4 ))
class EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL (Structure):
  pass

EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL = EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL

EFI_FVB_GET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL), # IN  *This
  POINTER(EFI_FVB_ATTRIBUTES_2)                 # OUT *Attributes
  )

EFI_FVB_SET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL), # IN  *This
  POINTER(EFI_FVB_ATTRIBUTES_2)                 # OUT *Attributes
  )

EFI_FVB_GET_PHYSICAL_ADDRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL), # IN  *This
  POINTER(EFI_PHYSICAL_ADDRESS)                 # OUT *Address
  )

EFI_FVB_GET_BLOCK_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL), # IN  *This
  EFI_LBA,                                      # IN  Lba,
  POINTER(UINTN),                               # OUT *BlockSize,
  POINTER(UINTN)                                # OUT *NumberOfBlocks
  )

EFI_FVB_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL), # IN      *This
  EFI_LBA,                                      # IN      Lba,
  UINTN,                                        # IN      Offset,
  POINTER(UINTN),                               # IN OUT  *NumBytes,
  POINTER(UINT8)                                # IN OUT  *Buffer
  )

EFI_FVB_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL), # IN      *This
  EFI_LBA,                                      # IN      Lba,
  UINTN,                                        # IN      Offset,
  POINTER(UINTN),                               # IN OUT  *NumBytes,
  POINTER(UINT8)                                # IN      *Buffer
  )

EFI_LBA_LIST_TERMINATOR   = 0xFFFFFFFFFFFFFFFFL

EFI_FVB_ERASE_BLOCKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_BLOCK2_PROTOCOL)  # IN  *This
  )

EFI_FIRMWARE_VOLUME_BLOCK_PROTOCOL._fields_ = [
    ("GetAttributes",       EFI_FVB_GET_ATTRIBUTES),
    ("SetAttributes",       EFI_FVB_SET_ATTRIBUTES),
    ("GetPhysicalAddress",  EFI_FVB_GET_PHYSICAL_ADDRESS),
    ("GetBlockSize",        EFI_FVB_GET_BLOCK_SIZE),
    ("Read",                EFI_FVB_READ),
    ("Write",               EFI_FVB_WRITE),
    ("EraseBlocks",         EFI_FVB_ERASE_BLOCKS),
    ("ParentHandle",        EFI_HANDLE)
  ]

