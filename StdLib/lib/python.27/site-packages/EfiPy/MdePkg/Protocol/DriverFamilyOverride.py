#
# DriverFamilyOverride.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DriverFamilyOverride.py is free software: you can redistribute it and/or
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

gEfiDriverFamilyOverrideProtocolGuid    = \
  EFI_GUID (0xb1ee129e, 0xda36, 0x4181, ( 0x91, 0xf8, 0x4, 0xa4, 0x92, 0x37, 0x66, 0xa7 ))

class EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_DRIVER_FAMILY_OVERRIDE_GET_VERSION = CFUNCTYPE (
  UINT32,
  POINTER(EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL)  # IN  *This
  )

EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL._fields_ = [
    ("GetVersion",  EFI_DRIVER_FAMILY_OVERRIDE_GET_VERSION)
  ]

