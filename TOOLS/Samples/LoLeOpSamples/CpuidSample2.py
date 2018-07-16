#
# CpuidSample2.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# CpuidSample2.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CpuidSample2.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy import Structure, Union, UINT32
# from LoLeOp.rUnionOp import COMMON_REG_32BITS
from LoLeOp.CpuId import CPUID, CpuIdIndex, COMMON_REG_32BITS

class CPUID_SIGNATURE_EAX_Bits (Structure):
  _fields_ = [
    ("MaximumLeaf", UINT32, 32),
  ]

class CPUID_SIGNATURE_EAX (Union):
  _fields_ = [
    ("Bits",      CPUID_SIGNATURE_EAX_Bits),
    ("Uint32",    UINT32)
  ]

class EFIPY_CPUID_TIME_STAMP_COUNTER_Regs (Structure):
  _fields_ = [
    ('EAX',  CPUID_SIGNATURE_EAX),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  COMMON_REG_32BITS)
  ]

CpuIdIndex[(0x15, 0x00)] = EFIPY_CPUID_TIME_STAMP_COUNTER_Regs

print "=" * 25
CpuId0x15 = CPUID (0x15, 0)
print "CpuId0x15.EAX:", CpuId0x15.EAX
print "CpuId0x15.EBX:", CpuId0x15.EBX
print "CpuId0x15.ECX:", CpuId0x15.ECX
print "CpuId0x15.EDX:", CpuId0x15.EDX
print "CpuId0x15.EAX.MaximumLeaf: 0x%08X" % CpuId0x15.EAX.MaximumLeaf
print "CpuId0x15.EAX[:]: 0x%08X" % CpuId0x15.EAX[:]