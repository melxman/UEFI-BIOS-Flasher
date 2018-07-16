#
# PciSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# PciSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PciSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import  EfiPyLib.PciEmulate as PciEmulate
from    EfiPyLib.PciStructure import PciDeviceS, PciBridgeS, PciCardBusS
from    EfiPyLib.PciIo import PciIo8, PciIo16, PciIo32, PciMmioConfigOffset

PciList = PciEmulate.PciEmulate ()
print "==" * 10
print "PciList:", PciList

#
# 1. List all pci device vendor id, device id, device type and if miltifunction
# 2. update PCI structure by device type
#
