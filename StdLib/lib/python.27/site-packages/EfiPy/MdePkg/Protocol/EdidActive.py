#
# EdidActive.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EdidActive.py is free software: you can redistribute it and/or
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

gEfiEdidActiveProtocolGuid    = \
  EFI_GUID (0xbd8c1056, 0x9f36, 0x44ec, (0x92, 0xa8, 0xa6, 0x33, 0x7f, 0x81, 0x79, 0x86 ))

class EFI_EDID_ACTIVE_PROTOCOL (Structure):
  _fields_ = [
    ("SizeOfEdid",  UINT32),
    ("Edid",        POINTER(UINT8))
  ]

