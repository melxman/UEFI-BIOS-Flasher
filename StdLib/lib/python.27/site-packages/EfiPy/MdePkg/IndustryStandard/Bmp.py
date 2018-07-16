#
# Bmp.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Bmp.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.IndustryStandard import *

class BMP_COLOR_MAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Blue",      UINT8),
    ("Green",     UINT8),
    ("Red",       UINT8),
    ("Reserved",  UINT8)
  ]

class BMP_IMAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CharB",           CHAR8),
    ("CharM",           CHAR8),
    ("Size",            UINT32),
    ("Reserved",        UINT16 * 2),
    ("ImageOffset",     UINT32),
    ("HeaderSize",      UINT32),
    ("PixelWidth",      UINT32),
    ("PixelHeight",     UINT32),
    ("Planes",          UINT16),
    ("BitPerPixel",     UINT16),
    ("CompressionType", UINT32),
    ("ImageSize",       UINT32),
    ("XPixelsPerMeter", UINT32),
    ("YPixelsPerMeter", UINT32),
    ("NumberOfColors",  UINT32),
    ("ImportantColors", UINT32)
  ]

