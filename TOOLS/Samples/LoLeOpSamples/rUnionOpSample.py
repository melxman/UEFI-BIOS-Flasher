#
# rUnionOpSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# rUnionOpSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# rUnionOpSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy as e
from LoLeOp.rUnionOp import rUnionOp, COMMON_REG_32BITS

print "*****************************"
EAX = rUnionOp('EAX', 0, 0, 32, 32, Value = 5, CellUnion = COMMON_REG_32BITS, CellType = 'Uint32', CellBits = 'Bits')
print EAX
print "EAX: %X" % EAX, type (EAX)
print "int(EAX)", int(EAX)
print "EAX.Reserved %X" % EAX.Reserved
print "*****************************"
print "EAX[0]: %X" % EAX[0]
print "EAX[1]: %X" % EAX[1]
print "EAX[2]: %X" % EAX[2]
print "EAX[3]: %X" % EAX[3]
print "EAX[4]: %X" % EAX[4]
print "EAX[5]: %X" % EAX[5]
print "EAX[6]: %X" % EAX[6]
print "EAX[7]: %X" % EAX[7]
print "EAX[8]: %X" % EAX[8]
print "*****************************"
print "==> Command EAX[1] = 1"
EAX[1] = 1
print "EAX[0]: %X" % EAX[0]
print "EAX[1]: %X" % EAX[1]
print "EAX[2]: %X" % EAX[2]
print "EAX[3]: %X" % EAX[3]
print "EAX[4]: %X" % EAX[4]
print "EAX[5]: %X" % EAX[5]
print "EAX[6]: %X" % EAX[6]
print "EAX[7]: %X" % EAX[7]
print "EAX[8]: %X" % EAX[8]
print "*****************************"
print "==> Command EAX[10:11] |= 3"
EAX[10:11] |= 3
print EAX
print "EAX[0]: %X" % EAX[0]
print "EAX[1]: %X" % EAX[1]
print "EAX[2]: %X" % EAX[2]
print "EAX[3]: %X" % EAX[3]
print "EAX[4]: %X" % EAX[4]
print "EAX[5]: %X" % EAX[5]
print "EAX[6]: %X" % EAX[6]
print "EAX[7]: %X" % EAX[7]
print "EAX[8]: %X" % EAX[8]
print "EAX[9]: %X" % EAX[9]
print "EAX[A]: %X" % EAX[0xA]
print "EAX[B]: %X" % EAX[0xB]
print "EAX[C]: %X" % EAX[0xC]
print "EAX[0]: %X" % EAX[1]
print "EAX.Reserved %X" % EAX.Reserved
print "*****************************"
print "==> Command EAX[10:11] &= 2"
EAX[10:11] &= 2
print EAX
print "EAX[0]: %X" % EAX[0]
print "EAX[1]: %X" % EAX[1]
print "EAX[2]: %X" % EAX[2]
print "EAX[3]: %X" % EAX[3]
print "EAX[4]: %X" % EAX[4]
print "EAX[5]: %X" % EAX[5]
print "EAX[6]: %X" % EAX[6]
print "EAX[7]: %X" % EAX[7]
print "EAX[8]: %X" % EAX[8]
print "EAX[9]: %X" % EAX[9]
print "EAX[A]: %X" % EAX[0xA]
print "EAX[B]: %X" % EAX[0xB]
print "EAX[C]: %X" % EAX[0xC]
print "EAX[0]: %X" % EAX[1]
print "EAX.Reserved %X" % EAX.Reserved
print "*****************************"
print "==> Command EAX.Reserved = 0x103"
EAX.Reserved = 0x103
print EAX
print "EAX[0]: %X" % EAX[0]
print "EAX[1]: %X" % EAX[1]
print "EAX[2]: %X" % EAX[2]
print "EAX[3]: %X" % EAX[3]
print "EAX[4]: %X" % EAX[4]
print "EAX[5]: %X" % EAX[5]
print "EAX[6]: %X" % EAX[6]
print "EAX[7]: %X" % EAX[7]
print "EAX[8]: %X" % EAX[8]
print "EAX[9]: %X" % EAX[9]
print "EAX[A]: %X" % EAX[0xA]
print "EAX[B]: %X" % EAX[0xB]
print "EAX[C]: %X" % EAX[0xC]
# print "EAX[D]: %X" % EAX[0xD]
print "EAX[0]: %X" % EAX[1]
print "EAX.Reserved %X" % EAX.Reserved
print "*****************************"
print EAX
print "EAX[0]: %X" % EAX[0]
print "EAX[1]: %X" % EAX[1]
print "EAX[2]: %X" % EAX[2]
print "EAX[3]: %X" % EAX[3]
print "EAX[4]: %X" % EAX[4]
print "EAX[5]: %X" % EAX[5]
print "EAX[6]: %X" % EAX[6]
print "EAX[7]: %X" % EAX[7]
print "EAX[8]: %X" % EAX[8]
print "EAX[9]: %X" % EAX[9]
print "EAX[A]: %X" % EAX[0xA]
print "EAX[B]: %X" % EAX[0xB]
print "EAX[C]: %X" % EAX[0xC]
print "EAX[D]: %X" % EAX[0xD]
print "EAX[0]: %X" % EAX[1]

print "EAX.Reserved %X" % EAX.Reserved
print "EAX", EAX
print "EAX.Reserved", EAX.Reserved
print "EAX[1]", EAX[1]
print "type (EAX)", type (EAX)
print "type (EAX[1])", type (EAX[1])
