#
# BitOpTemplate16.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# BitOpTemplate16.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# BitOpTemplate16.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from BitOpSample import tMem8, tMem16, tMem32, tMem64

#
# Entry for verify BitOp
#
if __name__ == "__main__":

  print "==================================="
  b = tMem16[1, 2, 3]
  print b
  print "0x%X" % b
  print "==================================="
  #           00000001b     00000010b         00110000b
  #                ^^^             ^          ^^^^
  b = tMem16[tMem8[1][2:0], tMem8[2][0], tMem8[0x30][4:7]]
  print b
  print "b = 0x%X" % b, "len:%d" % len (b)
  print "b[0]: %x" % b[0]
  print "b[1]: %x" % b[1]
  print "b[2]: %x" % b[2]
  print "b[3]: %x" % b[3]
  print "b[4]: %x" % b[4]
  print "b[5]: %x" % b[5]
  print "b[6]: %x" % b[6]
  print "b[7]: %x" % b[7]
  print
  print "b[-8]: %x" % b[-8]
  print "b[-7]: %x" % b[-7]
  print "b[-6]: %x" % b[-6]
  print "b[-5]: %x" % b[-5]
  print "b[-4]: %x" % b[-4]
  print "b[-3]: %x" % b[-3]
  print "b[-2]: %x" % b[-2]
  print "b[-1]: %x" % b[-1]

  # for i in b:
  #   print i

  print "================================================="
  print "b[0:0]: %x" % b[0:0]
  print "b[1:1]: %x" % b[1:1]
  print "b[0:1]: %x" % b[0:1]
  print "b[1:0]: %x" % b[1:0]
  print "b[0:7]: %x" % b[0:7]
  print "b[1:7]: %x" % b[1:7]
  print "b[6:7]: %x" % b[6:7]
  print "b[7:7]: %x" % b[7:7]
  print "b[7:6]: %x" % b[7:6]
  print "b[-1:6]: %x" % b[-1:6]
  print "b[1:3]: %x" % b[1:3]
  print "b[3:5]: %x" % b[3:5]
  print "b[3:7]: %x" % b[3:7]
  print "b[4:7]: %x" % b[4:7]
  print "b[3:3]: %x" % b[3:3]
  print "b[0:2]: %x" % b[0:2]
  print "========= for i in c: ==========================="
  c = b[2:7]
  print c
  print c[1:4]
  for i in c:
    print i
  # print "b[8:6]", b[8:6]
  # b[-1:6]
  # b[-8:6]
  # b[-9:6]
  # b[0:-6]
  print "================================================="
  print c[1]
  c[1] = 1
  print c[1]
  print "================================================="
  print b
  print "================================================="
  b[0:0] = 0;     print "b[0:0]: %x" % b[0:0]
  b[1:1] = 1;     print "b[1:1]: %x" % b[1:1]
  b[0:1] = 0;     print "b[0:1]: %x" % b[0:1]
  b[1:0] = 0;     print "b[1:0]: %x" % b[1:0]
  b[0:7] = 0xCF;  print "b[0:7]: %x" % b[0:7]
  b[1:7] = 0x67;  print "b[1:7]: %x" % b[1:7]
  b[6:7] = 1;     print "b[6:7]: %x" % b[6:7]
  b[7:7] = 1;     print "b[7:7]: %x" % b[7:7]
  b[7:6] = 1;     print "b[7:6]: %x" % b[7:6]
  b[-1:6] = 1;    print "b[-1:6]: %x" % b[-1:6]
  b[1:3] = 1;     print "b[1:3]: %x" % b[1:3]
  b[3:5] = 1;     print "b[3:5]: %x" % b[3:5]
  b[3:7] = 0x1C;  print "b[3:7]: %x" % b[3:7]
  b[4:7] = 6;     print "b[4:7]: %x" % b[4:7]
  b[3:3] = 1;     print "b[3:3]: %x" % b[3:3]
  b[0:2] = 0;     print "b[0:2]: %x" % b[0:2]
  print "================================================="
  print b
  print "================================================="
  b[1:7] +=3
  print b, type(b)
  b[0:2] = 3;     print "b[0:2]: %x" % b[0:2]
  print "================================================="
  #print b
  print b[0:-1]
  print b[0:-1][1:4]
  print b[0:-1][1:4][1:2]
  print b[0:-1][1:4][1:2][1:1]
  print b[0:-1][1:4][1:2][1:1][0]
  print tMem16[b[0:-1][1:4][1:2][1:1][0], b[2:2]]
  print tMem8[1]
  print tMem8[1][:]
  print tMem8[1][:][0:6]
  print tMem8[1][:][0:6][0:5]
  print tMem8[1][:][0:6][0:5][0:4]
  print tMem8[1][:][0:6][0:5][0:4][0:3]
  print tMem8[1][:][0:6][0:5][0:4][0:3][0:2]
  print tMem8[1][:][0:6][0:5][0:4][0:3][0:2][0:1]
  print tMem8[1][:][0:6][0:5][0:4][0:3][0:2][0:1][0:0]
