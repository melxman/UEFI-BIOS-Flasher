#
# PciOverride.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PciOverride.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
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

from EfiPy import *

import PciPlatform

gEfiPciOverrideProtocolGuid = \
  EFI_GUID (0xb5b35764, 0x460c, 0x4a06, (0x99, 0xfc, 0x77, 0xa1, 0x7c, 0x1b, 0x5c, 0xeb))

EFI_PCI_OVERRIDE_PROTOCOL = PciPlatform.EFI_PCI_PLATFORM_PROTOCOL
