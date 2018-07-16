#
# VariableIndexTable.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# VariableIndexTable.py is free software: you can redistribute it and/or
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
from EfiPy.MdeModulePkg.Guid.VariableFormat import VARIABLE_HEADER

class VARIABLE_POINTER_TRACK (Structure):
  _fields_ = [
  ("CurrPtr",   POINTER(VARIABLE_HEADER)),
  ("EndPtr",    POINTER(VARIABLE_HEADER)),
  ("StartPtr",  POINTER(VARIABLE_HEADER))
  ]

VARIABLE_INDEX_TABLE_VOLUME = 122
gEfiVariableIndexTableGuid         = \
  EFI_GUID (0x8cfdb8c8, 0xd6b2, 0x40f3, (0x8e, 0x97, 0x02, 0x30, 0x7c, 0xc9, 0x8b, 0x7c))

class VARIABLE_INDEX_TABLE (Structure):
  _fields_ = [
  ("Length",      UINT16),
  ("GoneThrough", UINT16),
  ("EndPtr",      POINTER(VARIABLE_HEADER)),
  ("StartPtr",    POINTER(VARIABLE_HEADER)),
  ("Index",       UINT16 * VARIABLE_INDEX_TABLE_VOLUME)
  ]

