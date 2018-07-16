#
# AcpiBgrtSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiBgrtSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiBgrtSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy
import struct
import EfiPyLib.Acpi.AcpiBgrt             as AcpiBgrt

if EfiPy.sizeof (AcpiBgrt.Table) != AcpiBgrt.Table.Header.Length:
  print 'WARNNING: size are not inconsisten: 0x%04X, 0x%04X' % (EfiPy.sizeof (AcpiBgrt.Table), AcpiBgrt.Table.Header.Length)

print "   Signature:        %s"       % struct.pack ("I", AcpiBgrt.Table.Header.Signature)
print "   Length:           0x%08X"   % AcpiBgrt.Table.Header.Length
print "   Revision:         0x%02X"   % AcpiBgrt.Table.Header.Revision
print "   Checksum:         0x%02X"   % AcpiBgrt.Table.Header.Checksum
print "   OemId:            %s"       % bytearray (AcpiBgrt.Table.Header.OemId)
print "   OemTableId:       %s"       % struct.pack ("Q", AcpiBgrt.Table.Header.OemTableId)
print "   OemRevision:      0x%08X"   % AcpiBgrt.Table.Header.OemRevision
print "   CreatorId:        %s"       % struct.pack ("I", AcpiBgrt.Table.Header.CreatorId)
print "   CreatorRevision:  0x%08X"   % AcpiBgrt.Table.Header.CreatorRevision
print "   Version:          0x%08X"   % AcpiBgrt.Table.Version
print "   Status:           0x%08X"   % AcpiBgrt.Table.Status
print "   ImageType:        0x%08X"   % AcpiBgrt.Table.ImageType
print "   ImageAddress:     0x%08X"   % AcpiBgrt.Table.ImageAddress
print "   ImageOffsetX:     0x%08X"   % AcpiBgrt.Table.ImageOffsetX
print "   ImageOffsetY:     0x%08X"   % AcpiBgrt.Table.ImageOffsetY

print
from EfiPyLib.EfiPyHexDump import EfiPyHexDump
Memory = (EfiPy.CHAR8 * AcpiBgrt.Size).from_address (AcpiBgrt.Address)
EfiPyHexDump (2, AcpiBgrt.Address, Memory, True, "ACPI: BGRT")
