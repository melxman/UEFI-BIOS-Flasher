#
# SdbgSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# SdbgSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# SdbgSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from LoLeOp.CpuId import CPUID

from LoLeOp.Msr import rMsr, EFIPY_MSR_COMMON_Reg
from LoLeOp.BitOp import _MemArray

CellExt = {
  # "CellUnion": EFIPY_MSR_COMMON_Reg,
  "CellDefault": EFIPY_MSR_COMMON_Reg,
  "CellArray": {},
  "CellType":  'Uint64',
  "CellBits":  'Bits'
}

print "Looking for platform IA32_DEBUG_INTERFACE status..."

CpuId01 = CPUID (0x01)
if CpuId01.ECX.SDBG != 1:
  print "This platform does not support IA32_DEBUG_INTERFACE...exit."
  exit (0)

print "This platform supports IA32_DEBUG_INTERFACE"
print "SDBG value:            %X" % CpuId01.ECX[11]

msr = _MemArray("msr",  64, CellClass = rMsr, CellExt = CellExt)
print "Enable (R/W):          %x" % msr[0xC80][0]
print "Lock (R/W):            %x" % msr[0xC80][30]
print "Debug Occurred (R/O):  %x" % msr[0xC80][31]
print
print "Try to enable IA32_DEBUG_INTERFACE::Enable bit..."
msr[0xC80][0] = 1
print "dump IA32_DEBUG_INTERFACE again..."
print "This bit shouldn't be changed on shell..."
print "msr[0xC80]", msr[0xC80]
print "Enable (R/W):          %x" % msr[0xC80][0]
print "Lock (R/W):            %x" % msr[0xC80][30]
print "Debug Occurred (R/O):  %x" % msr[0xC80][31]
