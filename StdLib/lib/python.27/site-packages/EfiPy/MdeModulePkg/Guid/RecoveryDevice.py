#
# RecoveryDevice.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# RecoveryDevice.py is free software: you can redistribute it and/or
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

gRecoveryOnDataCdGuid         = \
  EFI_GUID (0x5cac0099, 0x0dc9, 0x48e5, (0x80, 0x68, 0xbb, 0x95, 0xf5, 0x40, 0x0a, 0x9f))

gRecoveryOnFatFloppyDiskGuid         = \
  EFI_GUID (0x2e3d2e75, 0x9b2e, 0x412d, (0xb4, 0xb1, 0x70, 0x41, 0x6b, 0x87, 0x0, 0xff))

gRecoveryOnFatIdeDiskGuid         = \
  EFI_GUID (0xb38573b6, 0x6200, 0x4ac5, (0xb5, 0x1d, 0x82, 0xe6, 0x59, 0x38, 0xd7, 0x83))

gRecoveryOnFatUsbDiskGuid         = \
  EFI_GUID (0x0ffbce19, 0x324c, 0x4690, (0xa0, 0x09, 0x98, 0xc6, 0xae, 0x2e, 0xb1, 0x86))

