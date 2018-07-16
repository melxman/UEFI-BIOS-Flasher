#
# BitOpSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# BitOpSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# BitOpSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from LoLeOp.BitOp import _MemArray, _MemCell

mList   = list  (xrange (0, 0x1000))
mTuple  = tuple (xrange (0, 0x1000))

class tOp (_MemCell):

  def MemSet (self, index, value):
    mList[index] = value

  def MemGet (self, index):
    return mList[index]

#
# Object zone
#

tMem8  = _MemArray("tMem8",  8,  CellClass = tOp)
tMem16 = _MemArray("tMem16", 16, CellClass = tOp)
tMem32 = _MemArray("tMem32", 32, CellClass = tOp)
tMem64 = _MemArray("tMem64", 64, CellClass = tOp)

#
# Entry for verify BitOp
#
if __name__ == "__main__":

  b = tMem64[0x02]
  print "tMem64[0x02]", b
  b = tMem32[0x02]
  print "tMem32[0x02]", b
  b = tMem16[0x02]
  print "tMem16[0x02]", b
  b = tMem8[0x02]
  print "tMem8[0x02]", b
  print "=========================================="
  print b
  print "b[0]", b[0]
  print "b[1]", b[1]
  print "b[2]", b[2]
  print "tMem8[0x0B]: 0x%02X" %  tMem8[0x0B]
  print "tMem8[0x0B][0]:", tMem8[0x0B][0]
  print "tMem8[0x0B][1]:", tMem8[0x0B][1]
  print "tMem8[0x0B][2]:", tMem8[0x0B][2]
  print "tMem8[0x0B][3]:", tMem8[0x0B][3]
  print "=========================================="
  print "tMem8[0x0B][0:1]:", tMem8[0x0B][0:1]
  print "tMem8[0x0B][0:1]:", tMem8[0x0B][0:1]
  print "tMem8[0x0B][1:1]:", tMem8[0x0B][1:1]
  print "tMem8[0x0B][1:3]:", tMem8[0x0B][1:3]
  print "tMem8[0x0B][1:3]:", tMem8[0x0B][1:3]
  print "tMem8[0x0B][3:1]:", tMem8[0x0B][3:1]
  print "tMem8[0x0B][3:1]:", tMem8[0x0B][3:1]
  print "tMem8[0x0B][1:1]:", tMem8[0x0B][1:1]
  print "tMem8[0x0B][1:1]:", tMem8[0x0B][1:1]
  print "tMem8[0x0B][ -1]:", tMem8[0x0B][-1]
  print "tMem8[0x0B][ -2]:", tMem8[0x0B][-2]
  print "tMem8[0x0B][ -3]:", tMem8[0x0B][-3]
  print "tMem8[0x0B][ -4]:", tMem8[0x0B][-4]
  print "tMem8[0x0B][ -5]:", tMem8[0x0B][-5]
  print "tMem8[0x0B][ -6]:", tMem8[0x0B][-6]
  print "tMem8[0x0B][ -7]:", tMem8[0x0B][-7]
  print "tMem8[0x0B][ -8]:", tMem8[0x0B][-8]
  print "=========================================="
  print "=========================================="
  c = tMem8[0x03][3:1]  # 00000011b, 001
  d = tMem8[0x03]
  print "c[0]", c[0]
  print "c[1]", c[1]
  print "c[0:1]", c[0:1]
  print "c[2]", c[2]
  # print "c[3]", c[3]
  print "c[-1]", c[-1]
  print "c[-2]", c[-2]
  print "c[-3]", c[-3]
  # print "c[-4]", c[-4]
  print "=========================================="
  c = tMem8[0x03][0:3] # 00000011b, 0011
  print c[0]
  print c[1]
  print c[0:1]
  print "=========================================="
  c = tMem8[0x03][1:3]
  print b, c
  print str (b), str(c)
  print "3 < c", 3 < c
  print "c < 3", c < 3
  print "b < c", b < c
  print "3 <= c", 3 <= c
  print "c <= 3", c <= 3
  print "b <= c", b <= c
  print "3 > c", 3 > c
  print "c > 3", c > 3
  print "b > c", b > c
  print "3 >= c", 3 >= c
  print "c >= 3", c >= 3
  print "b >= c", b >= c
  print "3 == c", 3 == c
  print "c == 3", c == 3
  print "b == c", b == c
  print "3 != c", 3 != c
  print "c != 3", c != 3
  print "b != c", b != c
  print "=========================================="
  print tMem8[0x03]         # 00000011b,  0x03
  tMem8[0x03] = 0x40
  print tMem8[0x03]         # 01000000b,  0x40
  tMem8[0x03][0x01] = 0x01
  print tMem8[0x03]         # 01000010b,  0x42
  tMem8[0x03][0x02] = 0x01
  print tMem8[0x03]         # 01000110b,  0x46
  print c                   # 00000011b,  0x03
  print d                   # 01000110b,  0x46
  tMem8[0x03][-1]   = 0x01
  print tMem8[0x03]         # 11000110b,  0xC6
  print d                   # 11000110b,  0xC6
  tMem8[0x03][-8]   = 0x01
  print tMem8[0x03]         # 11000111b,  0xC7
  print d                   # 11000111b,  0xC7
  print "=========================================="
  print c                   # c = tMem8[0x03][1:3]
  c[0] = 0
  print tMem8[0x03]         # 1100 0101b,  0xC5
  c[-1] = 1
  print tMem8[0x03]         # 1100 1101b,  0xCD
  c[1] = 0
  print c
  c[2] = 0
  print c
  print tMem8[0x03]         # 1100 0001b,  0xCF
  # c[3] = 0
  c[-1] = 1                                # 1100 1001b,
  print c
  c[-2] = 1
  print c
  c[-3] = 1
  print c
  # c[-4] = 1
  print tMem8[0x03]         # 11001111b,  0xCF

  c[0:1] = 0x00
  print tMem8[0x03]         # 11001001b,  0xC9
  c[0:1] = 0x03
  print tMem8[0x03]         # 11001001b,  0xCF
  c[0:1] = 3

  print "=========================================="
  a = c[0:1] + 3
  print a                   # 6
  # print a[0:1]              # 6
  print tMem8[3]            # 0xCF
  a = tMem8[3] + 3
  print "0x%02X" % a        # 0xD2
  # print "0x%02X" % a[0:4], 0x02)   # 0xD2
  print tMem8[3]            # 0xCF
  tMem8[3] = tMem8[3] + 3
  print "0x%02X" % tMem8[3] # 0xD2, 11010010, 210
  # print bin(-tMem8[3])
  # print bin(~tMem8[3])
  # print "%b" % -tMem8[3]                 # -D2, 0x2E, 00101110
  print "=========================================="
  tMem8[3] = 3
  print tMem8[3]            # 0x03
  tMem8[3] +=3
  print tMem8[3]            # 0x06
  print tMem8[3][0:7]       # 0x06
  tMem8[3][4:7] += 3
  print tMem8[3]            # 0x36
  tMem8[3][4:7] -= 3
  print tMem8[3]            # 0x06
  c = tMem8[3][4:7]
  c[3:0] += 5
  print tMem8[3]            # 0x56
  c[1:0] |= 3
  print tMem8[3]            # 0x76
  tMem8[3][4:7] &= tMem8[3][3:0]
  print tMem8[3]            # 0x66
  tMem8[3] += tMem8[4][2]
  print tMem8[3]            # 0x67
  tMem8[3] -= tMem8[4][2]
  print tMem8[3]            # 0x66
  print tMem8[3][:]
  print tMem8[3][1:]
  print "=========================================="
  print c
  print c[:]
  c[:] = 2
  print c
  print c[1:]
  # print tMem8[3][1,2,3]
  # print tMem8[3][tMem8[5][0:7],2,3]
  # print tMem8[3][tMem8[5][0:7] & 0xE,2,3]
  # print tMem8[3][(1,1),2,3]
  # print c[1:2:2]
