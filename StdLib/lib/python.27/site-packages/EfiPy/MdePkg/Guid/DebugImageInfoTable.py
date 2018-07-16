#
# DebugImageInfoTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DebugImageInfoTable.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol  import LoadedImage

gEfiDebugImageInfoTableGuid = \
  EFI_GUID (0x49152e77, 0x1ada, 0x4764, (0xb7, 0xa2, 0x7a, 0xfe, 0xfe, 0xd9, 0x5e, 0x8b ))

EFI_DEBUG_IMAGE_INFO_UPDATE_IN_PROGRESS = 0x01
EFI_DEBUG_IMAGE_INFO_TABLE_MODIFIED     = 0x02

EFI_DEBUG_IMAGE_INFO_TYPE_NORMAL        = 0x01

class EFI_SYSTEM_TABLE_POINTER (Structure):
  _fields_ = [
    ("Signature",           UINT64),
    ("EfiSystemTableBase",  EFI_PHYSICAL_ADDRESS),
    ("Crc32",               UINT32)
  ]

class EFI_DEBUG_IMAGE_INFO_NORMAL (Structure):
  _fields_ = [
    ("ImageInfoType",               UINT32),
    ("LoadedImageProtocolInstance", POINTER(LoadedImage.EFI_LOADED_IMAGE_PROTOCOL)),
    ("ImageHandle",                 EFI_HANDLE)
  ]

class EFI_DEBUG_IMAGE_INFO (Union):
  _fields_ = [
    ("ImageInfoType", POINTER(UINT32)),
    ("NormalImage",   POINTER(EFI_DEBUG_IMAGE_INFO_NORMAL))
  ]

class EFI_DEBUG_IMAGE_INFO_TABLE_HEADER (Structure):
  _fields_ = [
    ("UpdateStatus",            UINT32),
    ("TableSize",               UINT32),
    ("EfiDebugImageInfoTable",  POINTER(EFI_DEBUG_IMAGE_INFO))
  ]

