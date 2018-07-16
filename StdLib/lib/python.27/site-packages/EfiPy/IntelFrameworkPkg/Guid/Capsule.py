#
# Capsule.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Capsule.py is free software: you can redistribute it and/or
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

gEfiCapsuleGuid         = \
  EFI_GUID (0x3B6686BD, 0x0D76, 0x4030, (0xB7, 0x0E, 0xB5, 0x51, 0x9E, 0x2F, 0xC5, 0xA0))

gEfiConfigFileNameGuid  = \
  EFI_GUID (0x98B8D59B, 0xE8BA, 0x48EE, (0x98, 0xDD, 0xC2, 0x95, 0x39, 0x2F, 0x1E, 0xDB))
  
EFI_CAPSULE_HEADER_FLAG_SETUP = 0x00000001
CAPSULE_BLOCK_DESCRIPTOR_SIGNATURE  = SIGNATURE_32 ('C', 'B', 'D', 'S')

class FRAMEWORK_EFI_CAPSULE_BLOCK_DESCRIPTOR (Structure):
  _fields_ = [
    ("Length",      UINT64),
    ("Data",        EFI_PHYSICAL_ADDRESS),
    ("Signature",   UINT32),
    ("CheckSum",    UINT32)
  ]

class EFI_CAPSULE_OEM_HEADER (Structure):
  _fields_ = [
    ("OemGuid",      EFI_GUID),
    ("HeaderSize",   UINT32)
    # ("OemHdrData",   UINT8 * N)
  ]

class FRAMEWORK_EFI_CAPSULE_HEADER (Structure):
  _fields_ = [
    ("CapsuleGuid",                 EFI_GUID),
    ("HeaderSize",                  UINT32),
    ("Flags",                       UINT32),
    ("CapsuleImageSize",            UINT32),
    ("SequenceNumber",              UINT32),
    ("InstanceId",                  EFI_GUID),
    ("OffsetToSplitInformation",    UINT32),
    ("OffsetToCapsuleBody",         UINT32),
    ("OffsetToOemDefinedHeader",    UINT32),
    ("OffsetToAuthorInformation",   UINT32),
    ("OffsetToRevisionInformation", UINT32),
    ("OffsetToShortDescription",    UINT32),
    ("OffsetToLongDescription",     UINT32),
    ("OffsetToApplicableDevices",   UINT32)
  ]

