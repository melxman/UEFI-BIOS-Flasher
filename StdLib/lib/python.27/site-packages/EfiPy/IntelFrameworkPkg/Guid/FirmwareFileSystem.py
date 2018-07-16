#
# FirmwareFileSystem.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FirmwareFileSystem.py is free software: you can redistribute it and/or
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

gEfiFirmwareFileSystemGuid = \
  EFI_GUID (0x7A9354D9, 0x0468, 0x444a, (0x81, 0xCE, 0x0B, 0xF6, 0x17, 0xD8, 0x90, 0xDF))

EFI_FFS_FILE_TAIL = UINT16
FFS_ATTRIB_TAIL_PRESENT     = 0x01
FFS_ATTRIB_RECOVERY         = 0x02
FFS_ATTRIB_HEADER_EXTENSION = 0x04

