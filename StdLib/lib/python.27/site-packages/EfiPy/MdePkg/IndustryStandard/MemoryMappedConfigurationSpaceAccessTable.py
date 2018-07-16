#
# MemoryMappedConfigurationSpaceAccessTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# MemoryMappedConfigurationSpaceAccessTable.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from EfiPy.MdePkg.IndustryStandard import *

import Acpi

class EFI_ACPI_MEMORY_MAPPED_ENHANCED_CONFIGURATION_SPACE_BASE_ADDRESS_ALLOCATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BaseAddress",           UINT64),
    ("PciSegmentGroupNumber", UINT16),
    ("StartBusNumber",        UINT8),
    ("EndBusNumber",          UINT8),
    ("Reserved",              UINT32)
  ]

class EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_BASE_ADDRESS_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",  UINT64)
  ]

EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_TABLE_REVISION  = 0x01

