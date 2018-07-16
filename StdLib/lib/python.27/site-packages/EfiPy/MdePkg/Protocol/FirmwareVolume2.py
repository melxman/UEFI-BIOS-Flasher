#
# FirmwareVolume2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FirmwareVolume2.py is free software: you can redistribute it and/or
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

gEfiFirmwareVolume2ProtocolGuid = \
  EFI_GUID (0x220e73b6, 0x6bdb, 0x4413, ( 0x84, 0x5, 0xb9, 0x74, 0xb1, 0x8, 0x61, 0x9a ))

class EFI_FIRMWARE_VOLUME2_PROTOCOL (Structure):
  pass

EFI_FV_ATTRIBUTES = UINT64

#
# BUGBUG
# From MdePkg/Include/Pi/PiFirmwareFile.py
#
EFI_FV_FILETYPE         = UINT8 
EFI_FFS_FILE_ATTRIBUTES = UINT8 
EFI_FFS_FILE_STATE      = UINT8 
EFI_SECTION_TYPE        = UINT8

#
# BUGBUG
# From MdePkg/Include/Pi/PiFirmwareVolume.py
#
EFI_FV_FILE_ATTRIBUTES  = UINT32

EFI_FV2_READ_DISABLE_CAP        = 0x0000000000000001L
EFI_FV2_READ_ENABLE_CAP         = 0x0000000000000002L
EFI_FV2_READ_STATUS             = 0x0000000000000004L
EFI_FV2_WRITE_DISABLE_CAP       = 0x0000000000000008L
EFI_FV2_WRITE_ENABLE_CAP        = 0x0000000000000010L
EFI_FV2_WRITE_STATUS            = 0x0000000000000020L
EFI_FV2_LOCK_CAP                = 0x0000000000000040L
EFI_FV2_LOCK_STATUS             = 0x0000000000000080L
EFI_FV2_WRITE_POLICY_RELIABLE   = 0x0000000000000100L
EFI_FV2_READ_LOCK_CAP           = 0x0000000000001000L
EFI_FV2_READ_LOCK_STATUS        = 0x0000000000002000L
EFI_FV2_WRITE_LOCK_CAP          = 0x0000000000004000L
EFI_FV2_WRITE_LOCK_STATUS       = 0x0000000000008000L
EFI_FV2_ALIGNMENT               = 0x00000000001F0000L
EFI_FV2_ALIGNMENT_1             = 0x0000000000000000L
EFI_FV2_ALIGNMENT_2             = 0x0000000000010000L
EFI_FV2_ALIGNMENT_4             = 0x0000000000020000L
EFI_FV2_ALIGNMENT_8             = 0x0000000000030000L
EFI_FV2_ALIGNMENT_16            = 0x0000000000040000L
EFI_FV2_ALIGNMENT_32            = 0x0000000000050000L
EFI_FV2_ALIGNMENT_64            = 0x0000000000060000L
EFI_FV2_ALIGNMENT_128           = 0x0000000000070000L
EFI_FV2_ALIGNMENT_256           = 0x0000000000080000L
EFI_FV2_ALIGNMENT_512           = 0x0000000000090000L
EFI_FV2_ALIGNMENT_1K            = 0x00000000000A0000L
EFI_FV2_ALIGNMENT_2K            = 0x00000000000B0000L
EFI_FV2_ALIGNMENT_4K            = 0x00000000000C0000L
EFI_FV2_ALIGNMENT_8K            = 0x00000000000D0000L
EFI_FV2_ALIGNMENT_16K           = 0x00000000000E0000L
EFI_FV2_ALIGNMENT_32K           = 0x00000000000F0000L
EFI_FV2_ALIGNMENT_64K           = 0x0000000000100000L
EFI_FV2_ALIGNMENT_128K          = 0x0000000000110000L
EFI_FV2_ALIGNMENT_256K          = 0x0000000000120000L
EFI_FV2_ALIGNMENT_512K          = 0x0000000000130000L
EFI_FV2_ALIGNMENT_1M            = 0x0000000000140000L
EFI_FV2_ALIGNMENT_2M            = 0x0000000000150000L
EFI_FV2_ALIGNMENT_4M            = 0x0000000000160000L
EFI_FV2_ALIGNMENT_8M            = 0x0000000000170000L
EFI_FV2_ALIGNMENT_16M           = 0x0000000000180000L
EFI_FV2_ALIGNMENT_32M           = 0x0000000000190000L
EFI_FV2_ALIGNMENT_64M           = 0x00000000001A0000L
EFI_FV2_ALIGNMENT_128M          = 0x00000000001B0000L
EFI_FV2_ALIGNMENT_256M          = 0x00000000001C0000L
EFI_FV2_ALIGNMENT_512M          = 0x00000000001D0000L
EFI_FV2_ALIGNMENT_1G            = 0x00000000001E0000L
EFI_FV2_ALIGNMENT_2G            = 0x00000000001F0000L

EFI_FV_GET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN      *This
  POINTER(EFI_FV_ATTRIBUTES)              #    OUT  *FvAttributes
  )

EFI_FV_SET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN      *This
  POINTER(EFI_FV_ATTRIBUTES)              # IN OUT  *FvAttributes
  )

EFI_FV_READ_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN        *This
  POINTER(EFI_GUID),                      # IN CONST  *NameGuid,
  POINTER(PVOID),                         # IN OUT    **Buffer,
  POINTER(UINTN),                         # IN OUT    *BufferSize,
  POINTER(EFI_FV_FILETYPE),               # OUT       *FoundType,
  POINTER(EFI_FV_FILE_ATTRIBUTES),        # OUT       *FileAttributes,
  POINTER(UINT32)                         # OUT       *AuthenticationStatus
  )

EFI_FV_READ_SECTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN        *This
  POINTER(EFI_GUID),                      # IN CONST  *NameGuid,
  EFI_SECTION_TYPE,                       # IN        SectionType,
  UINTN,                                  # IN        SectionInstance,
  POINTER(PVOID),                         # IN OUT    **Buffer,
  POINTER(UINTN),                         # IN OUT    *BufferSize,
  POINTER(UINT32)                         # OUT       *AuthenticationStatus
  )

EFI_FV_WRITE_POLICY = UINT32
EFI_FV_UNRELIABLE_WRITE   = 0x00000000
EFI_FV_RELIABLE_WRITE     = 0x00000001

class EFI_FV_WRITE_FILE_DATA (Structure):
  _fields_ = [
    ("NameGuid",        POINTER(EFI_GUID)),
    ("Type",            EFI_FV_FILETYPE),
    ("FileAttributes",  EFI_FV_FILE_ATTRIBUTES),
    ("Buffer",          PVOID),
    ("BufferSize",      UINT32)
  ]

EFI_FV_WRITE_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN *This
  UINT32,                                 # IN NumberOfFiles,
  EFI_FV_WRITE_POLICY,                    # IN WritePolicy,
  POINTER(EFI_FV_WRITE_FILE_DATA)         # IN *FileData
  )

EFI_FV_GET_NEXT_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN      *This
  PVOID,                                  # IN OUT  *Key,
  POINTER(EFI_FV_FILETYPE),               # IN OUT  *FileType,
  POINTER(EFI_GUID),                      # OUT     *NameGuid,
  POINTER(EFI_FV_FILE_ATTRIBUTES),        # OUT     *Attributes,
  POINTER(UINTN)                          # OUT     *Size
  )

EFI_FV_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN        *This
  POINTER(EFI_GUID),                      # IN CONST  *InformationType,
  POINTER(UINTN),                         # IN OUT    *BufferSize,
  PVOID                                   # OUT       *Buffer
  )

EFI_FV_SET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME2_PROTOCOL), # IN        *This
  POINTER(EFI_GUID),                      # IN CONST  *InformationType,
  UINTN,                                  # IN        BufferSize,
  PVOID                                   # IN CONST  *Buffer
  )

EFI_FIRMWARE_VOLUME2_PROTOCOL._fields_ = [
    ("GetVolumeAttributes", EFI_FV_GET_ATTRIBUTES),
    ("SetVolumeAttributes", EFI_FV_SET_ATTRIBUTES),
    ("ReadFile",            EFI_FV_READ_FILE),
    ("ReadSection",         EFI_FV_READ_SECTION),
    ("WriteFile",           EFI_FV_WRITE_FILE),
    ("GetNextFile",         EFI_FV_GET_NEXT_FILE),
    ("KeySize",             UINT32),
    ("ParentHandle",        EFI_HANDLE),
    ("GetInfo",             EFI_FV_GET_INFO),
    ("SetInfo",             EFI_FV_SET_INFO)
  ]

