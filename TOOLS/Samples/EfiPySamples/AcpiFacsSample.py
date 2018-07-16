#
# AcpiFacsSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiFacsSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiFacsSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

print "==== FACS Table"
import EfiPyLib.Acpi.AcpiFacs             as AcpiFacs
print "   FACS Revision:  0x%02X" % AcpiFacs.Revision
print "   FACS Address:   0x%08X" % AcpiFacs.Address
print "   FACS Size:      0x%08X" % AcpiFacs.Size

#
# FACS dump, style one.
#
for _fName, _type in AcpiFacs.Table._fields_:
  try:
    print "   FACS %s: 0x%08X" % (_fName, getattr(AcpiFacs.Table, _fName))
  except:
    print "   FACS %s: %s" % (_fName, getattr(AcpiFacs.Table, _fName))

print
#
# FACS dump, style two.
#
import struct
print "   AcpiFacs:Signature:               %s"       % struct.pack ("I", AcpiFacs.Table.Signature)
print "   AcpiFacs:Length:                  0x%08X"   % AcpiFacs.Table.Length
print "   AcpiFacs:HardwareSignature:       0x%08X"   % AcpiFacs.Table.HardwareSignature
print "   AcpiFacs:FirmwareWakingVector:    0x%08X"   % AcpiFacs.Table.FirmwareWakingVector
print "   AcpiFacs:GlobalLock:              0x%08X"   % AcpiFacs.Table.GlobalLock
print "   AcpiFacs:Flags:                   0x%08X"   % AcpiFacs.Table.Flags

if  AcpiFacs.Revision >= 0x01:
  print "   AcpiFacs:XFirmwareWakingVector:    0x%016X"   % AcpiFacs.Table.XFirmwareWakingVector
  print "   AcpiFacs:Version:                  0x%02X"    % AcpiFacs.Table.Version
if  AcpiFacs.Revision >= 0x02:
  print "   AcpiFacs:OspmFlags:                0x%08X"    % AcpiFacs.Table.OspmFlags

import EfiPy
if AcpiFacs.Size != EfiPy.sizeof (AcpiFacs.Table):
  print "WARNNING: FACS size and Spec defined size are inconsistent."
  print "          FACS size: %d, Spec defined size: %d" % (AcpiFacs.Size, EfiPy.sizeof (AcpiFacs.Table))

print
from EfiPyLib.EfiPyHexDump import EfiPyHexDump
Memory = (EfiPy.CHAR8 * AcpiFacs.Size).from_address (AcpiFacs.Address)
EfiPyHexDump (2, AcpiFacs.Address, Memory, True, "ACPI: FACS")
