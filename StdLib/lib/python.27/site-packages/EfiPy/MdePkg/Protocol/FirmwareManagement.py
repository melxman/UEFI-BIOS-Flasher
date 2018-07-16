#
# FirmwareManagement.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FirmwareManagement.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Guid.WinCertificate import WIN_CERTIFICATE_UEFI_GUID

gEfiFirmwareManagementProtocolGuid  = \
  EFI_GUID (0x86c77a67, 0xb97, 0x4633, (0xa1, 0x87, 0x49, 0x10, 0x4d, 0x6, 0x85, 0xc7 ))

class EFI_FIRMWARE_MANAGEMENT_PROTOCOL (Structure):
  pass

class EFI_FIRMWARE_IMAGE_DESCRIPTOR (Structure):
  _fields_ = [
    ("ImageIndex",                  UINT8),
    ("ImageTypeId",                 EFI_GUID),
    ("ImageId",                     UINT64),
    ("ImageIdName",                 PCHAR16),
    ("Version",                     UINT32),
    ("VersionName",                 PCHAR16),
    ("Size",                        UINTN),
    ("AttributesSupported",         UINT64),
    ("AttributesSetting",           UINT64),
    ("Compatibilities",             UINT64),
    ("LowestSupportedImageVersion", UINT32),
    ("LastAttemptVersion",          UINT32),
    ("LastAttemptStatus",           UINT32),
    ("HardwareInstance;",           UINT64)
  ]
IMAGE_ATTRIBUTE_IMAGE_UPDATABLE         = 0x0000000000000001
IMAGE_ATTRIBUTE_RESET_REQUIRED          = 0x0000000000000002
IMAGE_ATTRIBUTE_AUTHENTICATION_REQUIRED = 0x0000000000000004
IMAGE_ATTRIBUTE_IN_USE                  = 0x0000000000000008
IMAGE_ATTRIBUTE_UEFI_IMAGE              = 0x0000000000000010
IMAGE_COMPATIBILITY_CHECK_SUPPORTED      = 0x0000000000000001
EFI_FIRMWARE_IMAGE_DESCRIPTOR_VERSION   = 3
class EFI_FIRMWARE_IMAGE_AUTHENTICATION (Structure):
  _fields_ = [
    ("MonotonicCount",  UINT64),
    ("AuthInfo",        WIN_CERTIFICATE_UEFI_GUID)
  ]

IMAGE_UPDATABLE_VALID                     = 0x0000000000000001
IMAGE_UPDATABLE_INVALID                   = 0x0000000000000002
IMAGE_UPDATABLE_INVALID_TYPE              = 0x0000000000000004
IMAGE_UPDATABLE_INVALID_OLD               = 0x0000000000000008
IMAGE_UPDATABLE_VALID_WITH_VENDOR_CODE     = 0x0000000000000010

PACKAGE_ATTRIBUTE_VERSION_UPDATABLE       = 0x0000000000000001
PACKAGE_ATTRIBUTE_RESET_REQUIRED          = 0x0000000000000002
PACKAGE_ATTRIBUTE_AUTHENTICATION_REQUIRED = 0x0000000000000004

EFI_FIRMWARE_MANAGEMENT_UPDATE_IMAGE_PROGRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINTN)        # IN Completion
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL_GET_IMAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_MANAGEMENT_PROTOCOL),# IN      *This
  POINTER(UINTN),                           # IN OUT  *ImageInfoSize,
  POINTER(EFI_FIRMWARE_IMAGE_DESCRIPTOR),   # IN OUT  *ImageInfo,
  POINTER(UINT32),                          # OUT     *DescriptorVersion,
  POINTER(UINT8),                           # OUT     *DescriptorCount,
  POINTER(UINTN),                           # OUT     *DescriptorSize,
  POINTER(UINT32),                          # OUT     *PackageVersion,
  POINTER(PCHAR16)                          # OUT     **PackageVersionName
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL_GET_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_MANAGEMENT_PROTOCOL),# IN       *This
  UINT8,                                    # IN       ImageIndex,
  PVOID,                                    # IN  OUT  *Image,
  POINTER(UINTN)                            # IN  OUT  *ImageSize
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL_SET_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_MANAGEMENT_PROTOCOL),      # IN       *This
  UINT8,                                          # IN  ImageIndex,
  PVOID,                                          # IN  *Image,
  UINTN,                                          # IN  ImageSize,
  PVOID,                                          # IN  *VendorCode,
  EFI_FIRMWARE_MANAGEMENT_UPDATE_IMAGE_PROGRESS,  # IN  Progress,
  POINTER(PCHAR16)                                # OUT **AbortReason
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL_CHECK_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_MANAGEMENT_PROTOCOL),      # IN  *This
  UINT8,                                          # IN  ImageIndex,
  PVOID,                                          # IN  *Image,
  UINTN,                                          # IN  ImageSize,
  POINTER(UINT32)                                 # OUT *ImageUpdatable
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL_GET_PACKAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_MANAGEMENT_PROTOCOL),# IN  *This
  POINTER(UINT32),                          # OUT *PackageVersion,
  POINTER(PCHAR16),                         # OUT **PackageVersionName,
  POINTER(UINT32),                          # OUT *PackageVersionNameMaxLen,
  POINTER(UINT64),                          # OUT *AttributesSupported,
  POINTER(UINT64)                           # OUT *AttributesSetting
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL_SET_PACKAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FIRMWARE_MANAGEMENT_PROTOCOL),# IN        *This
  PVOID,                                    # IN  CONST *Image,
  UINTN,                                    # IN        ImageSize,
  PVOID,                                    # IN  CONST *VendorCode,
  UINT32,                                   # IN        PackageVersion,
  PCHAR16                                   # IN  CONST *PackageVersionName
  )

EFI_FIRMWARE_MANAGEMENT_PROTOCOL._fields_ = [
    ("GetImageInfo",    EFI_FIRMWARE_MANAGEMENT_PROTOCOL_GET_IMAGE_INFO),
    ("GetImage",        EFI_FIRMWARE_MANAGEMENT_PROTOCOL_GET_IMAGE),
    ("SetImage",        EFI_FIRMWARE_MANAGEMENT_PROTOCOL_SET_IMAGE),
    ("CheckImage",      EFI_FIRMWARE_MANAGEMENT_PROTOCOL_CHECK_IMAGE),
    ("GetPackageInfo",  EFI_FIRMWARE_MANAGEMENT_PROTOCOL_GET_PACKAGE_INFO),
    ("SetPackageInfo",  EFI_FIRMWARE_MANAGEMENT_PROTOCOL_SET_PACKAGE_INFO)
  ]

