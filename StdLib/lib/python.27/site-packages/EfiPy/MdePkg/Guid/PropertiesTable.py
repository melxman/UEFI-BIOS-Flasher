#
# PropertiesTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PropertiesTable.py is free software: you can redistribute it and/or
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

gEfiPropertiesTableGuid = \
  EFI_GUID (0x880aaca3, 0x4adc, 0x4a04, (0x90, 0x79, 0xb7, 0x47, 0x34, 0x8, 0x25, 0xe5))

class EFI_PROPERTIES_TABLE (Structure):
  _fields_ = [
    ("Version",                   UINT32),
    ("Length",                    UINT32),
    ("MemoryProtectionAttribute", UINT64)
  ]

EFI_PROPERTIES_TABLE_VERSION  = 0x00010000

EFI_PROPERTIES_RUNTIME_MEMORY_PROTECTION_NON_EXECUTABLE_PE_DATA        = 0x1

