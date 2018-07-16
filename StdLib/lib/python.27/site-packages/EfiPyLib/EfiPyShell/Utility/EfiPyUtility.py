#!/usr/bin/python

#
# EfiPyUtility.py
#
# Copyright (C) 2014 - 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyUtility.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

def EfiPyHexDump (EfiPyIo, PreSpace, offset, HexBuff, AsciiDump):

  DumpCount = 0
  DumpLine  = 0
  DumpHex   = ""
  DumpChar  = ""

  for char in HexBuff:

    if type(char) is int:
      char = chr (char)

    if   (DumpCount % 16) == 0:

      if DumpHex != "":
        if AsciiDump == True:
          EfiPyIo.printf(DumpHex + DumpChar + "*\r\n")
        else:
          EfiPyIo.printf(DumpHex + "\r\n")

      DumpHex   = " " * PreSpace
      DumpHex   = DumpHex + "%08X: %02X" % (offset + DumpLine * 16, ord(char))
      DumpLine  = DumpLine + 1

      if char >= ' ' and char <= '~':
        DumpChar  = "  *%c" % char
      else:
        DumpChar  = "  *."

    elif (DumpCount %  8) == 0:

      DumpHex   = DumpHex  + "-%02X" % ord(char)

      if char >= ' ' and char <= '~':
        DumpChar  = DumpChar + char
      else:
        DumpChar  = DumpChar + "."

    else:

      DumpHex   = DumpHex + " %02X" % ord(char)

      if char >= ' ' and char <= '~':
        DumpChar  = DumpChar + char
      else:
        DumpChar  = DumpChar + "."

    DumpCount = DumpCount + 1

  if DumpHex != "":

    if AsciiDump == True:
      if DumpCount % 16 == 0:
        TabSpace = ""
      else:
        TabSpace = "   " * (16 - DumpCount % 16)

      EfiPyIo.printf(DumpHex + TabSpace + DumpChar + "*\r\n")

    else:
      EfiPyIo.printf(DumpHex + "\r\n")

if __name__ == '__main__':

  sample = '\n\x00\x00\x00\x04\x00\x00\x00\t\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00/\x00\x00\x00\x05\x00\x00\x000\x00\x00\x00\x03\x00\x00\x00\x80\x01\x00\x00\x04\x00\x00\x00\xc5\x18\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00'
  EfiPyHexDump (2, 0x0102, sample, True)
  print
  sample = '\x01\x00\x00\x00\x1e\x00E\x00F\x00I\x00 \x00D\x00V\x00D\x00/\x00C\x00D\x00R\x00O\x00M\x00\x00\x00\x02\x01\x0c\x00\xd0A\x03\n\x00\x00\x00\x00\x01\x01\x06\x00\x01\x01\x03\x01\x08\x00\x01\x00\x00\x00\x7f\xff\x04'
  EfiPyHexDump (2, 0x0102, sample, True)
  print
  sample = '\x01\x37a\x00\x00'
  EfiPyHexDump (2, 0x0102, sample, True)

  import sys

  sys.exit(0)
