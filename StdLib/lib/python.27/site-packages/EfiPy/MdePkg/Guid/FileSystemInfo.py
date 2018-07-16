#
# FileSystemInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FileSystemInfo.py is free software: you can redistribute it and/or modify
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

from EfiPy  import *

gEfiFileSystemInfoGuid = EFI_GUID( 0x9576e93, 0x6d3f, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_FILE_SYSTEM_INFO (Structure):
  _fields_ = [
    ("Size",        UINT64),    # 8 Byte, offset 0x00
    ("ReadOnly",    BOOLEAN),   # 8 byte, offset 0x08
    ("VolumeSize",  UINT64),    # 8 byte, offset 0x10
    ("FreeSpace",   UINT64),    # 8 byte, offset 0x18
    ("BlockSize",   UINT32),    # 4 byte, offset 0x20
    ("VolumeLabel", CHAR16 * 1) # 2 byte, offset 0x24
    ]

