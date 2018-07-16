#
# BusSpecificDriverOverride.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BusSpecificDriverOverride.py is free software: you can redistribute it and/or
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

gEfiBusSpecificDriverOverrideProtocolGuid = \
  EFI_GUID (0x3bc1b285, 0x8a15, 0x4a82, (0xaa, 0xbf, 0x4d, 0x7d, 0x13, 0xfb, 0x32, 0x65 ))

class EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_GET_DRIVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL),   # IN     *This
  POINTER(EFI_HANDLE)                                   # IN OUT *DriverImageHandle
  )

EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL._fields_ = [
    ("GetDriver", EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_GET_DRIVER)
  ]

