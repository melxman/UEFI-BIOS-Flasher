#
# LoadModuleAtFixedAddress.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LoadModuleAtFixedAddress.py is free software: you can redistribute it and/or
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

from EfiPy  import *

gLoadFixedAddressConfigurationTableGuid         = \
  EFI_GUID (0x2CA88B53,0xD296,0x4080, (0xA4,0xA5,0xCA,0xD9,0xBA,0xE2,0x4B,0x9))

class EFI_LOAD_FIXED_ADDRESS_CONFIGURATION_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("DxeCodeTopAddress", EFI_PHYSICAL_ADDRESS),
  ("SmramBase",         EFI_PHYSICAL_ADDRESS)
  ]

