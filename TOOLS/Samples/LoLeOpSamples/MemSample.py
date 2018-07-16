#
# MemSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# MemSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# MemSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from LoLeOp.Mem import Mem8, Mem16, Mem32, Mem64

print "========================="
print "===> Memory basic Demo..."
print Mem8[0x3FF39018]
print " Mem8[0x3FF39018]: 0x%02X  (0x49)"               %  Mem8[0x3FF39018]
print "Mem16[0x3FF39018]: 0x%04X  (0x4249)"             % Mem16[0x3FF39018]
print "Mem32[0x3FF39018]: 0x%08X  (0x20494249)"         % Mem32[0x3FF39018]
print "Mem64[0x3FF39018]: 0x%016X (0x5453595320494249)" % Mem64[0x3FF39018]
print " Mem8[0x00]: 0x%02X"                             %  Mem8[0x00]
print " Mem8[0x0C000000]: 0x%02X"                       %  Mem8[0x0C000000]
Mem8[0x0C000000] = 0xFF
print " Mem8[0x0C000000]: 0x%02X"                       %  Mem8[0x0C000000]
print
print "==================================="
print "===> Memory Bit Operation Demo 1..."
Mem8[0x0C000000] = 0xA4
print Mem8[0x0C000000]
print Mem8[0x0C000000][0]
print Mem8[0x0C000000][1]
print Mem8[0x0C000000][2]
print Mem8[0x0C000000][3]
print Mem8[0x0C000000][4]
print Mem8[0x0C000000][5]
print Mem8[0x0C000000][6]
print Mem8[0x0C000000][7]
print Mem8[0x0C000000][-1]
print Mem8[0x0C000000][-2]
print Mem8[0x0C000000][-3]
print Mem8[0x0C000000][-4]
print Mem8[0x0C000000][-5]
print Mem8[0x0C000000][-6]
print Mem8[0x0C000000][-7]
print Mem8[0x0C000000][-8]
print "==================================="
print "===> Memory Bit Operation Demo 2..."
print Mem8[0x0C000000]
print Mem8[0x0C000000][0:3]
print Mem8[0x0C000000][3:0]
print Mem8[0x0C000000][4:-2]
print "===> Assign Value 0x02 at address 0x0C000000"
Mem8[0x0C000000][3:0] = 0x02
print Mem8[0x0C000000]
print Mem8[0x0C000000][0:3]
print "===> address 0x0C000000 bit 2 or 0x01"
Mem8[0x0C000000][2] |= 0x01
print Mem8[0x0C000000]   # The result should be 0xA6
print "==================================="
print "===> Memory Bit Operation Demo 3..."
mGroup = Mem8[Mem8[0x0C000000][1], Mem8[0x0C000004][4:7], Mem16[0x0C000010]]
print "mGroup", mGroup
Mem16[0x0C000010] = 0xFFFF
print "mGroup", mGroup
print "mGroup[6:3]", mGroup[6:3]
mGroup[6:3] = 0x03
print "mGroup[6:3]", mGroup[6:3]
print "==================================="
print "===> Memory Bit Operation Demo 4..."
mGroup[6:3] |= 0x0C
print "mGroup[6:3]", mGroup[6:3]
print "mGroup", mGroup
