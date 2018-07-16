#
# AcpiHpetSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiHpetSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiHpetSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy
import struct
import EfiPyLib.Acpi.AcpiHpet             as AcpiHpet

if EfiPy.sizeof (AcpiHpet.Table) != AcpiHpet.Table.Header.Length:
  print 'WARNNING: size are not inconsisten: 0x%04X, 0x%04X' % (EfiPy.sizeof (AcpiHpet.Table), AcpiHpet.Table.Header.Length)

print "   Signature:                                %s"       % struct.pack ("I", AcpiHpet.Table.Header.Signature)
print "   Length:                                   0x%08X"   % AcpiHpet.Table.Header.Length
print "   Revision:                                 0x%02X"   % AcpiHpet.Table.Header.Revision
print "   Checksum:                                 0x%02X"   % AcpiHpet.Table.Header.Checksum
print "   OemId:                                    %s"       % bytearray (AcpiHpet.Table.Header.OemId)
print "   OemTableId:                               %s"       % struct.pack ("Q", AcpiHpet.Table.Header.OemTableId)
print "   OemRevision:                              0x%08X"   % AcpiHpet.Table.Header.OemRevision
print "   CreatorId:                                %s"       % struct.pack ("I", AcpiHpet.Table.Header.CreatorId)
print "   CreatorRevision:                          0x%08X"   % AcpiHpet.Table.Header.CreatorRevision

print "   EventTimerBlockID:                        0x%08X"   % AcpiHpet.Table.EventTimerBlockID
print "   BaseAddressLower32Bit.AddressSpaceId:     0x%08X"   % AcpiHpet.Table.BaseAddressLower32Bit.AddressSpaceId
print "   BaseAddressLower32Bit.RegisterBitWidth:   0x%08X"   % AcpiHpet.Table.BaseAddressLower32Bit.RegisterBitWidth
print "   BaseAddressLower32Bit.RegisterBitOffset:  0x%08X"   % AcpiHpet.Table.BaseAddressLower32Bit.RegisterBitOffset
print "   BaseAddressLower32Bit.AccessSize:         0x%08X"   % AcpiHpet.Table.BaseAddressLower32Bit.AccessSize
print "   BaseAddressLower32Bit.Address:            0x%016X"  % AcpiHpet.Table.BaseAddressLower32Bit.Address
print "   HpetNumber:                               0x%02X"   % AcpiHpet.Table.HpetNumber
print "   Mode:                                     0x%04X"   % AcpiHpet.Table.Mode
print "   Attribute:                                0x%02X"   % AcpiHpet.Table.Attribute

print
from EfiPyLib.EfiPyHexDump import EfiPyHexDump
Memory = (EfiPy.CHAR8 * AcpiHpet.Size).from_address (AcpiHpet.Address)
EfiPyHexDump (2, AcpiHpet.Address, Memory, True, "ACPI: HPET")
