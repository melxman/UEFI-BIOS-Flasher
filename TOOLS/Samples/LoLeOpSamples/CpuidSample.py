#
# CpuidSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# CpuidSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CpuidSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from LoLeOp.CpuId import CPUID

print "=" * 25
CpuId00 = CPUID (0, 0)
print "CpuId00", CpuId00
print "=" * 25
print "CpuId00.EAX: %X" % CpuId00.EAX
print "CpuId00.EAX[0:1]: %X" % CpuId00.EAX[0:1]
print "CpuId00.EAX.MaximumLeaf: %X" % CpuId00.EAX.MaximumLeaf
print "=" * 25
print "CpuId00.EAX:", CpuId00.EAX
print "CpuId00.EBX:", CpuId00.EBX
print "CpuId00.ECX:", CpuId00.ECX
print "CpuId00.EDX:", CpuId00.EDX
print "=" * 25
print CpuId00
print "=" * 25
print "variant information returned by CPUID(index)"
# print "CPUID(0x01).Regs.EAX.Uint32: 0x%08X" % CPUID(0x01).Regs.EAX.Uint32
print "CPUID(0x01).EAX (Hex): 0x%08X" %       CPUID(0x01).EAX
print "CPUID(0x01).EAX (Bin): %s" %           bin(CPUID(0x01).EAX)
print "===> EAX.SteppingId: [Bits 3:0] Stepping ID"
print "CPUID(0x01).EAX[3:0]: 0x%08X" %        CPUID(0x01).EAX[3:0]
print "CPUID(0x01).EAX.SteppingId: 0x%03X" %  CPUID(0x01).EAX.SteppingId
print "CPUID(0x01).EBX.MaximumAddressableIdsForLogicalProcessors 0x%08X" % CPUID(0x01).EBX.MaximumAddressableIdsForLogicalProcessors
print "CPUID(0x01).EAX:", CPUID(0x01).EAX
print "CPUID(0x01).EBX:", CPUID(0x01).EBX
print "CPUID(0x01).ECX:", CPUID(0x01).ECX
print "CPUID(0x01).EDX:", CPUID(0x01).EDX

SteppingId = CPUID(0x01).EAX[3:0]
print "SteppingId: %X" % SteppingId
print "SteppingId:", SteppingId

CacheLineSize = CPUID(0x01).EBX.CacheLineSize
print "CacheLineSize: %X" % CacheLineSize
print "CacheLineSize:", CacheLineSize

CacheLineSize = CPUID(0x01).EBX[8:15]
print "CacheLineSize: %X" % CacheLineSize
print "CacheLineSize:", CacheLineSize
