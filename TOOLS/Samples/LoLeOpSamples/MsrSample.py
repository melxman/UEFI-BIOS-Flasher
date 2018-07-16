#
# MsrSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# MsrSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# MsrSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy.UefiCpuPkg.Register.Msr.SkylakeMsr import  MSR_SKYLAKE_TURBO_RATIO_LIMIT_REGISTER, MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_REGISTER

from LoLeOp.Msr import CellArray, msr

CellArray[0x000001AD] = MSR_SKYLAKE_TURBO_RATIO_LIMIT_REGISTER
CellArray[0x0000038E] = MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_REGISTER

print "*" * 25
print "msr[0x200]", msr[0x200]
print "*" * 25
print "msr[0x200] 0x%016X" % msr[0x200]
print "*" * 25
print "msr[0x200][10]: 0x%X" % msr[0x200][10]
print "msr[0x200][30]:", msr[0x200][10]
print "type (msr[0x200]) ", type (msr[0x200])
print "type (msr[0x200][30]) ", type (msr[0x200][30])
print "*" * 25
print "msr[0x200].Reserved", msr[0x200].Reserved
print "*" * 25
print "msr[0x200].Reserved 0x%016X" % msr[0x200].Reserved
print "*" * 25
print "msr[0x000001AD]", msr[0x000001AD]
print "msr[0x0000038E]", msr[0x0000038E]
print "msr[0x000001AD]", msr[0x000001AD]
print "msr[0x000001AD][0:7]: 0x%02X" % msr[0x000001AD][0:7]
print "msr[0x000001AD].Maximum1C: 0x%02X" % msr[0x000001AD].Maximum1C
