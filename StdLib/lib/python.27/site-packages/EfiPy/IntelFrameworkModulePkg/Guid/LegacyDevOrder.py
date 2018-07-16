#
# LegacyDevOrder.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LegacyDevOrder.py is free software: you can redistribute it and/or
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

gEfiLegacyDevOrderVariableGuid = \
  EFI_GUID (0xa56074db, 0x65fe, 0x45f7, (0xbd, 0x21, 0x2d, 0x2b, 0xdd, 0x8e, 0x96, 0x52))

BBS_TYPE = UINT8

class LEGACY_DEV_ORDER_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
    ("BbsType", BBS_TYPE),
    ("Length",  UINT16),
    ("Data",    UINT16 * 1)
  ]

VAR_LEGACY_DEV_ORDER = u"LegacyDevOrder"

