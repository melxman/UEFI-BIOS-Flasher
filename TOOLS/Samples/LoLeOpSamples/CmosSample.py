#
# CmosSample.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# CmosSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CmosSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from LoLeOp.Cmos import Cmos

CmosIndex2 = {
  'sec'   : ((0x00), slice(0,7)), # tuple (0, 7, 1)
  'min'   : ((0x02), slice(0,7)), # tuple (0, 7, 1)
  'hour'  : ((0x04), slice(0,7)), # tuple (0, 7, 1)
  'date'  : ((0x07), slice(0,7)), # tuple (0, 7, 1)
  'month' : ((0x08), slice(0,7)), # tuple (0, 7, 1)
  'year'  : ((0x09), slice(0,7)), # tuple (0, 7, 1)
  # 'year' : ((0x09), (0,7))  # tuple (0, 7)
  }
Cmos.DictKey.update (CmosIndex2)

print "===> Cmos Test..."
print "Cmos[0x00]: %02X" % Cmos[0x00]
print "Cmos[0x02]: %02X" % Cmos[0x02]
print "Cmos[0x04]: %02X" % Cmos[0x04]
print "Cmos[0x07]: %02X" % Cmos[0x07]
print "Cmos[0x08]: %02X" % Cmos[0x08]
print "Cmos[0x09]: %02X" % Cmos[0x09]
print "==== year is 0x12 ==============="
Cmos.year = 0x12
print "Cmos[0x09]: %02X" % Cmos[0x09]
print "Cmos.year: %02X" % Cmos.year
print "==== year is 0x13 ==============="
Cmos.year = 0x13
print "Cmos[0x09]:  %02X" % Cmos[0x09]
print "Cmos.year:   %02X" % Cmos.year
print "Cmos.month:  %02X" % Cmos.month
print "Cmos.date:   %02X" % Cmos.date
print "Cmos.hour:   %02X" % Cmos.hour
print "Cmos.min:    %02X" % Cmos.min
print "Cmos.sec:    %02X" % Cmos.sec
print "Cmos.sec[0:3]:    %01X" % Cmos.sec[0:3]
print "Cmos.sec[4:7]:    %01X" % Cmos.sec[7:4]
print "==== attribute test ==============="
Cmos.ask = 'aas'
print 'Cmos.ask:', Cmos.ask
