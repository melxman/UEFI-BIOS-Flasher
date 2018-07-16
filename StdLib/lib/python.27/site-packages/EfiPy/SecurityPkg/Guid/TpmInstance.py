#
# TpmInstance.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# TpmInstance.py is free software: you can redistribute it and/or
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

gEfiTpmDeviceInstanceNoneGuid = \
  EFI_GUID (0x00000000, 0x0000, 0x0000, (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))

gEfiTpmDeviceInstanceTpm12Guid = \
  EFI_GUID (0x8b01e5b6, 0x4f19, 0x46e8, (0xab, 0x93, 0x1c, 0x53, 0x67, 0x1b, 0x90, 0xcc))

gEfiTpmDeviceInstanceTpm20DtpmGuid = \
  EFI_GUID (0x286bf25a, 0xc2c3, 0x408c, (0xb3, 0xb4, 0x25, 0xe6, 0x75, 0x8b, 0x73, 0x17))

gEfiTpmDeviceSelectedGuid = \
  EFI_GUID (0x7f4158d3, 0x74d, 0x456d, (0x8c, 0xb2, 0x1, 0xf9, 0xc8, 0xf7, 0x9d, 0xaa))

