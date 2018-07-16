#
# EdidOverride.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EdidOverride.py is free software: you can redistribute it and/or
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

gEfiEdidOverrideProtocolGuid  = \
  EFI_GUID (0x48ecb431, 0xfb72, 0x45c0, (0xa9, 0x22, 0xf4, 0x58, 0xfe, 0x4, 0xb, 0xd5 ))

class EFI_EDID_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_EDID_OVERRIDE_DONT_OVERRIDE   = 0x01
EFI_EDID_OVERRIDE_ENABLE_HOT_PLUG = 0x02

EFI_EDID_OVERRIDE_PROTOCOL_GET_EDID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EDID_OVERRIDE_PROTOCOL),  # IN     *This
  POINTER(EFI_HANDLE),                  # IN     *ChildHandle,
  POINTER(UINT32),                      # OUT    *Attributes,
  POINTER(UINTN),                       # IN OUT *EdidSize,
  POINTER(POINTER(UINT8))               # IN OUT **Edid
  )

EFI_EDID_OVERRIDE_PROTOCOL._fields_ = [
    ("GetEdid", EFI_EDID_OVERRIDE_PROTOCOL_GET_EDID)
  ]

