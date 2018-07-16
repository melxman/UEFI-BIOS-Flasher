#
# AcpiMcfgSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiMcfgSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiMcfgSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

print "Dump MCFG table"
import struct
import EfiPyLib.Acpi.AcpiMcfg             as AcpiMcfg
print "   MCFG Revision:  0x%02X" % AcpiMcfg.Revision
print "   MCFG Address:   0x%08X" % AcpiMcfg.Address
print "   MCFG Size:      0x%08X" % AcpiMcfg.Size
print "   AcpiMcfg:Signature:        %s"       % struct.pack ("I", AcpiMcfg.Table.Header.Header.Signature)
print "   AcpiMcfg:Length:           0x%08X"   % AcpiMcfg.Table.Header.Header.Length
print "   AcpiMcfg:Revision:         0x%02X"   % AcpiMcfg.Table.Header.Header.Revision
print "   AcpiMcfg:Checksum:         0x%02X"   % AcpiMcfg.Table.Header.Header.Checksum
print "   AcpiMcfg:OemId:            %s"       % bytearray (AcpiMcfg.Table.Header.Header.OemId)
print "   AcpiMcfg:OemTableId:       %s"       % struct.pack ("Q", AcpiMcfg.Table.Header.Header.OemTableId)
print "   AcpiMcfg:OemRevision:      0x%08X"   % AcpiMcfg.Table.Header.Header.OemRevision
print "   AcpiMcfg:CreatorId:        %s"       % struct.pack ("I", AcpiMcfg.Table.Header.Header.CreatorId)
print "   AcpiMcfg:CreatorRevision:  0x%08X"   % AcpiMcfg.Table.Header.Header.CreatorRevision

for dTable in AcpiMcfg.Table.McfgEntry:
  print "   Mcfg: " + "=" * 10
  print "   Mcfg.BaseAddress:           0x%016X"  % dTable.BaseAddress
  print "   Mcfg.PciSegmentGroupNumber: 0x%08X"   % dTable.PciSegmentGroupNumber
  print "   Mcfg.StartBusNumber:        0x%08X"   % dTable.StartBusNumber
  print "   Mcfg.EndBusNumber:          0x%08X"   % dTable.EndBusNumber

import EfiPy
if AcpiMcfg.Size != EfiPy.sizeof (AcpiMcfg.Table):
  print "WARNNING: MCFG size and Spec defined size are inconsistent."
  print "          MCFG size: %d, Spec defined size: %d" % (AcpiMcfg.Size, EfiPy.sizeof (AcpiMcfg.Table))

print
from EfiPyLib.EfiPyHexDump import EfiPyHexDump
Memory = (EfiPy.CHAR8 * AcpiMcfg.Size).from_address (AcpiMcfg.Address)
EfiPyHexDump (2, AcpiMcfg.Address, Memory, True, "ACPI: MCFP")
