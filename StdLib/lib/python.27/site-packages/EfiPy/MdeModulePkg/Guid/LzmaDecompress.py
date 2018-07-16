#
# LzmaDecompress.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LzmaDecompress.py is free software: you can redistribute it and/or
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

gLzmaCustomDecompressGuid         = \
  EFI_GUID (0xEE4E5898, 0x3914, 0x4259, (0x9D, 0x6E, 0xDC, 0x7B, 0xD7, 0x94, 0x03, 0xCF))

gLzmaF86CustomDecompressGuid         = \
  EFI_GUID (0xD42AE6BD, 0x1352, 0x4bfb, (0x90, 0x9A, 0xCA, 0x72, 0xA6, 0xEA, 0xE8, 0x89))

