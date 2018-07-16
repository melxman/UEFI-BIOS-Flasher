#
# FirmwareVolume.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FirmwareVolume.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.FirmwareVolume2 import EFI_FV_FILETYPE, EFI_FV_FILE_ATTRIBUTES, EFI_SECTION_TYPE

gEfiFirmwareVolumeProtocolGuid = \
  EFI_GUID (0x389F751F, 0x1838, 0x4388, (0x83, 0x90, 0xCD, 0x81, 0x54, 0xBD, 0x27, 0xF8))

FV_DEVICE_SIGNATURE = SIGNATURE_32 ('_', 'F', 'V', '_')

class EFI_FIRMWARE_VOLUME_PROTOCOL (Structure):
  pass

FRAMEWORK_EFI_FV_ATTRIBUTES = UINT64
EFI_FV_READ_DISABLE_CAP       = 0x0000000000000001L
EFI_FV_READ_ENABLE_CAP        = 0x0000000000000002L
EFI_FV_READ_STATUS            = 0x0000000000000004L
EFI_FV_WRITE_DISABLE_CAP      = 0x0000000000000008L
EFI_FV_WRITE_ENABLE_CAP       = 0x0000000000000010L
EFI_FV_WRITE_STATUS           = 0x0000000000000020L
EFI_FV_LOCK_CAP               = 0x0000000000000040L
EFI_FV_LOCK_STATUS            = 0x0000000000000080L
EFI_FV_WRITE_POLICY_RELIABLE  = 0x0000000000000100L
EFI_FV_ALIGNMENT_CAP          = 0x0000000000008000L
EFI_FV_ALIGNMENT_2            = 0x0000000000010000L
EFI_FV_ALIGNMENT_4            = 0x0000000000020000L
EFI_FV_ALIGNMENT_8            = 0x0000000000040000L
EFI_FV_ALIGNMENT_16           = 0x0000000000080000L
EFI_FV_ALIGNMENT_32           = 0x0000000000100000L
EFI_FV_ALIGNMENT_64           = 0x0000000000200000L
EFI_FV_ALIGNMENT_128          = 0x0000000000400000L
EFI_FV_ALIGNMENT_256          = 0x0000000000800000L
EFI_FV_ALIGNMENT_512          = 0x0000000001000000L
EFI_FV_ALIGNMENT_1K           = 0x0000000002000000L
EFI_FV_ALIGNMENT_2K           = 0x0000000004000000L
EFI_FV_ALIGNMENT_4K           = 0x0000000008000000L
EFI_FV_ALIGNMENT_8K           = 0x0000000010000000L
EFI_FV_ALIGNMENT_16K          = 0x0000000020000000L
EFI_FV_ALIGNMENT_32K          = 0x0000000040000000L
EFI_FV_ALIGNMENT_64K          = 0x0000000080000000L

FRAMEWORK_EFI_FV_GET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_PROTOCOL), # IN  *This
  POINTER(FRAMEWORK_EFI_FV_ATTRIBUTES)   # OUT *Attributes
  )

FRAMEWORK_EFI_FV_SET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_PROTOCOL), # IN *This
  POINTER(FRAMEWORK_EFI_FV_ATTRIBUTES)   # IN *Attributes
  )

FRAMEWORK_EFI_FV_READ_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_PROTOCOL),  # IN      *This,
  POINTER(EFI_GUID),                      # IN      *NameGuid,
  POINTER(PVOID),                         # IN OUT  **Buffer,
  POINTER(UINTN),                         # IN OUT  *BufferSize,
  POINTER(EFI_FV_FILETYPE),               # OUT     *FoundType,
  POINTER(EFI_FV_FILE_ATTRIBUTES),        # OUT     *FileAttributes,
  POINTER(UINT32)                         # OUT     *AuthenticationStatus
  )

FRAMEWORK_EFI_FV_READ_SECTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_PROTOCOL),  # IN      *This,
  POINTER(EFI_GUID),                      # IN      *NameGuid,
  EFI_SECTION_TYPE,                       # IN      SectionType,
  UINTN,                                  # IN      SectionInstance,
  POINTER(PVOID),                         # IN OUT  **Buffer,
  POINTER(UINTN),                         # IN OUT  *BufferSize,
  POINTER(UINT32),                        # OUT     *AuthenticationStatus
  )

FRAMEWORK_EFI_FV_WRITE_POLICY = UINT32

FRAMEWORK_EFI_FV_UNRELIABLE_WRITE = 0x00000000
FRAMEWORK_EFI_FV_RELIABLE_WRITE   = 0x00000001

class FRAMEWORK_EFI_FV_WRITE_FILE_DATA (Structure):
  _fields_ = [
    ("NameGuid",        POINTER(EFI_GUID)),
    ("Type",            EFI_FV_FILETYPE),
    ("FileAttributes",  EFI_FV_FILE_ATTRIBUTES),
    ("Buffer",          PVOID),
    ("BufferSize",      UINT32)
  ]

FRAMEWORK_EFI_FV_WRITE_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_PROTOCOL),    # IN *This,
  UINT32,                                   # IN NumberOfFiles,
  FRAMEWORK_EFI_FV_WRITE_POLICY,            # IN WritePolicy,
  POINTER(FRAMEWORK_EFI_FV_WRITE_FILE_DATA) # IN *FileData
  )

FRAMEWORK_EFI_FV_GET_NEXT_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_VOLUME_PROTOCOL),    # IN      *This,
  PVOID,                                    # IN OUT  *Key,
  POINTER(EFI_FV_FILETYPE),                 # IN OUT  *FileType,
  POINTER(EFI_GUID),                        # OUT     *NameGuid,
  POINTER(EFI_FV_FILE_ATTRIBUTES),          # OUT     *Attributes,
  POINTER(UINTN)                            # OUT     *Size
  )

EFI_FIRMWARE_VOLUME_PROTOCOL._fields_ = [
    ("GetVolumeAttributes",   FRAMEWORK_EFI_FV_GET_ATTRIBUTES),
    ("SetVolumeAttributes",   FRAMEWORK_EFI_FV_SET_ATTRIBUTES),
    ("ReadFile",              FRAMEWORK_EFI_FV_READ_FILE),
    ("ReadSection",           FRAMEWORK_EFI_FV_READ_SECTION),
    ("WriteFile",             FRAMEWORK_EFI_FV_WRITE_FILE),
    ("GetNextFile",           FRAMEWORK_EFI_FV_GET_NEXT_FILE ),
    ("KeySize",               UINT32),
    ("ParentHandle",          EFI_HANDLE)
  ]

