#
# Msr.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# Msr.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# Msr.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from rUnionOp import COMMON_REG_32BITS_OUTPUT, rUnionOp
from BitOp import _MemArray, _MemCell
from _MsrCode import WrMsrFunc, RdMsrFunc
from EfiPy import *

class EFIPY_MSR_COMMON_Bits (Structure):
  _fields_ = [
    ("Reserved",  UINT64, 64),
  ]

class EFIPY_MSR_COMMON_Reg (Union):
  _fields_ = [
    ("Bits",      EFIPY_MSR_COMMON_Bits),
    ("Uint32",    UINT32),
    ("Uint64",    UINT64),
  ]

class rMsr (rUnionOp):

  def MemGet (self, Key):
    return RdMsrFunc (self, Key)

  def MemSet (self, Key, Value):
    WrMsrFunc (self, Key, Value)

CellArray = {}

CellExt = {
  # "CellUnion": EFIPY_MSR_COMMON_Reg,
  "CellDefault": EFIPY_MSR_COMMON_Reg,
  "CellArray": CellArray,
  "CellType":  'Uint64',
  "CellBits":  'Bits'
}

msr = _MemArray("msr",  64, CellClass = rMsr, CellExt = CellExt)
