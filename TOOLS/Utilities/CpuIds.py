
#
# CpuIds.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# CpuIds.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CpuIds.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPyLib.EfiPyCpuId import *
import struct as _struct

EAX = CPUID (0).__para__[0]

print "============================================"
print "   Input      EAX      EBX      ECX      EDX"
print "%08X %08X %08X %08X %08X" % (EAX,
                                    CPUID (0).EAX,
                                    CPUID (0).EBX,
                                    CPUID (0).ECX,
                                    CPUID (0).EDX)

s = _struct.pack("III", CPUID (0).EBX, CPUID (0).EDX, CPUID (0).ECX)
print s
print 
print "Vendor:", vendor ()
print "Stepping ID:", stepping_id()
print "Model: %08X" % model()
print "Family:", family()
print "Processor Type:", processor_type()
print "Brand ID:", hex(brand_id())
print "Brand String:", brand_string()
print "Features:", features()
