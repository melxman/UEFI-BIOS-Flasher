# 
# FmpCapsule.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FmpCapsule.py is free software: you can redistribute it and/or
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

gEfiFmpCapsuleGuid  = \
  EFI_GUID (0x6dcbd5ed, 0xe82d, 0x4c44, (0xbd, 0xa1, 0x71, 0x94, 0x19, 0x9a, 0xd9, 0x2a ))

class EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",             UINT32),
    ("EmbeddedDriverCount", UINT16),
    ("PayloadItemCount",    UINT16),
    # ("ItemOffsetList",      UINT64 * N)
  ]

class EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",                 UINT32),
    ("UpdateImageTypeId",       EFI_GUID),
    ("UpdateImageIndex",        UINT8),
    ("reserved_bytes",          UINT8 * 3),
    ("UpdateImageSize",         UINT32),
    ("UpdateVendorCodeSize",    UINT32),
    ("UpdateHardwareInstance",  UINT64)
  ]

EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER_INIT_VERSION       = 0x00000001
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER_INIT_VERSION = 0x00000002
