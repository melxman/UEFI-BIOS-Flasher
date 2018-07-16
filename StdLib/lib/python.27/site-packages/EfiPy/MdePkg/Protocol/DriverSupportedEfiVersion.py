#
# DriverSupportedEfiVersion.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DriverSupportedEfiVersion.py is free software: you can redistribute it and/or
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


gEfiDriverSupportedEfiVersionProtocolGuid = \
  EFI_GUID (0x5c198761, 0x16a8, 0x4e69, ( 0x97, 0x2c, 0x89, 0xd6, 0x79, 0x54, 0xf8, 0x1d ))

class EFI_DRIVER_SUPPORTED_EFI_VERSION_PROTOCOL (Structure):
  _fields_ = [
    ("Length",          UINT32),
    ("FirmwareVersion", UINT32)
  ]

