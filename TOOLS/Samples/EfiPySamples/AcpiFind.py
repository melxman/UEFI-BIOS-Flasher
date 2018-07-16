#
# AcpiFind.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiFind.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiFind.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPyLib.acpi.EfiPyAcpiBase        as AcpiBase

print '================================================================================'
for _Signature, _Address, _Length in AcpiBase.AcpiTables:
  print "%s at 0x%08X (Length: 0x%08X)" % (_Signature, _Address, _Length)

import EfiPyLib.acpi.EfiPyAcpiLib as AcpiLib
print '================================================================================'
for _Signature, _Address, _Length in AcpiBase.AcpiTables:
  print '_Signature: "%s"' % _Signature
  AcpiLib.AcpiDump (_Signature, True)
  print "Checksum: 0x%02X" % AcpiLib.AcpiCheckSum (_Signature)
  print
