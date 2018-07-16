#
# AcpiApicSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiApicSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiApicSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy
import struct
import EfiPyLib.Acpi.AcpiApic             as AcpiApic

if EfiPy.sizeof (AcpiApic.Table) != AcpiApic.Table.Header.Length:
  print 'WARNNING: size are not inconsisten: 0x%04X, 0x%04X' % (EfiPy.sizeof (AcpiApic.Table), AcpiApic.Table.Header.Length)

print "   Signature:        %s"       % struct.pack ("I", AcpiApic.Table.Header.Signature)
print "   Length:           0x%08X"   % AcpiApic.Table.Header.Length
print "   Revision:         0x%02X"   % AcpiApic.Table.Header.Revision
print "   Checksum:         0x%02X"   % AcpiApic.Table.Header.Checksum
print "   OemId:            %s"       % bytearray (AcpiApic.Table.Header.OemId)
print "   OemTableId:       %s"       % struct.pack ("Q", AcpiApic.Table.Header.OemTableId)
print "   OemRevision:      0x%08X"   % AcpiApic.Table.Header.OemRevision
print "   CreatorId:        %s"       % struct.pack ("I", AcpiApic.Table.Header.CreatorId)
print "   CreatorRevision:  0x%08X"   % AcpiApic.Table.Header.CreatorRevision

print "   LocalApicAddress: 0x%08X"   % AcpiApic.Table.LocalApicAddress
print "   Flags:            0x%08X"   % AcpiApic.Table.Flags

import EfiPy
for _fName, _fType in AcpiApic.Table._fields_:

  if isinstance (getattr (AcpiApic.Table, _fName), EfiPy.Structure):
    _item = getattr (AcpiApic.Table, _fName)
    for __fName, __fType in _item._fields_:
      try:
        print "   %s.%s: 0x%08X" % (_fName, __fName, getattr (_item, __fName))
      except:
        print "   %s.%s: " % (_fName, __fName), getattr (_item, __fName)
  else:
    try:
      print "   %s: 0x%08X" % (_fName, getattr (AcpiApic.Table, _fName))
    except:
      print "   %s: " % _fName, getattr (AcpiApic.Table, _fName)

print
from EfiPyLib.EfiPyHexDump import EfiPyHexDump
Memory = (EfiPy.CHAR8 * AcpiApic.Size).from_address (AcpiApic.Address)
EfiPyHexDump (2, AcpiApic.Address, Memory, True, "ACPI: APIC")
