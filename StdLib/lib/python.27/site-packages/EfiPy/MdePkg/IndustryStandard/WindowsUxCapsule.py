#
# WindowsUxCapsule.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# WindowsUxCapsule.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from EfiPy.MdePkg.IndustryStandard  import *
from EfiPy.MdePkg.Uefi.UefiSpec     import EFI_CAPSULE_HEADER

class DISPLAY_DISPLAY_PAYLOAD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",   UINT8),
    ("Checksum",  UINT8),
    ("ImageType", UINT8),
    ("Reserved",  UINT8),
    ("Mode",      UINT32),
    ("OffsetX",   UINT32),
    ("OffsetY",   UINT32)
    # ("Image",     UINT8 * N)
  ]

class EFI_DISPLAY_CAPSULE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CapsuleHeader", EFI_CAPSULE_HEADER),
    ("ImagePayload",  DISPLAY_DISPLAY_PAYLOAD)
  ]

gWindowsUxCapsuleGuid = EFI_GUID (0x3b8c8162, 0x188c, 0x46a4, ( 0xae, 0xc9, 0xbe, 0x43, 0xf1, 0xd6, 0x56, 0x97))
