#
# FileSystemVolumeLabelInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FileSystemVolumeLabelInfo.py is free software: you can redistribute it and/or
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

from EfiPy import *

gEfiFileSystemVolumeLabelInfoIdGuid = \
  EFI_GUID (0xDB47D7D3, 0xFE81, 0x11d3, (0x9A, 0x35, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_FILE_SYSTEM_VOLUME_LABEL (Structure):
  _fields_ = [
    ("VolumeLabel", CHAR16 * 1)
  ]

