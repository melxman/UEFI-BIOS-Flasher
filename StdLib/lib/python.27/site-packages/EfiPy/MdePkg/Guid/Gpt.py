# 
# Gpt.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Gpt.py is free software: you can redistribute it and/or
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

gEfiPartTypeUnusedGuid  = \
  EFI_GUID (0x00000000, 0x0000, 0x0000, (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ))

gEfiPartTypeSystemPartGuid  = \
  EFI_GUID (0xc12a7328, 0xf81f, 0x11d2, (0xba, 0x4b, 0x00, 0xa0, 0xc9, 0x3e, 0xc9, 0x3b ))

gEfiPartTypeLegacyMbrGuid = \
  EFI_GUID (0x024dee41, 0x33e7, 0x11d3, (0x9d, 0x69, 0x00, 0x08, 0xc7, 0x81, 0xf3, 0x9f ))

