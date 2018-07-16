#
# EdidDiscovered.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EdidDiscovered.py is free software: you can redistribute it and/or
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

gEfiEdidDiscoveredProtocolGuid  = \
  EFI_GUID (0x1c0c34f6, 0xd380, 0x41fa, (0xa0, 0x49, 0x8a, 0xd0, 0x6c, 0x1a, 0x66, 0xaa ))

class EFI_EDID_DISCOVERED_PROTOCOL (Structure):
  _fields_ = [
    ("SizeOfEdid",  UINT32),
    ("Edid",        POINTER(UINT8))
  ]

