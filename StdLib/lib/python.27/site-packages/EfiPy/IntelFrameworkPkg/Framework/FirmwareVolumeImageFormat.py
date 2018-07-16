#
# FirmwareVolumeImageFormat.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FirmwareVolumeImageFormat.py is free software: you can redistribute it and/or
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

EFI_AGGREGATE_AUTH_STATUS_PLATFORM_OVERRIDE = 0x000001
EFI_AGGREGATE_AUTH_STATUS_IMAGE_SIGNED      = 0x000002
EFI_AGGREGATE_AUTH_STATUS_NOT_TESTED        = 0x000004
EFI_AGGREGATE_AUTH_STATUS_TEST_FAILED       = 0x000008
EFI_AGGREGATE_AUTH_STATUS_ALL               = 0x00000f

EFI_LOCAL_AUTH_STATUS_PLATFORM_OVERRIDE     = 0x010000
EFI_LOCAL_AUTH_STATUS_IMAGE_SIGNED          = 0x020000
EFI_LOCAL_AUTH_STATUS_NOT_TESTED            = 0x040000
EFI_LOCAL_AUTH_STATUS_TEST_FAILED           = 0x080000
EFI_LOCAL_AUTH_STATUS_ALL                   = 0x0f0000

