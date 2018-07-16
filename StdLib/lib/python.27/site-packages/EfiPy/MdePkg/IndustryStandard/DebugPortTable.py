#
# DebugPortTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DebugPortTable.py is free software: you can redistribute it and/or modify
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

class EFI_ACPI_DEBUG_PORT_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("InterfaceType",     UINT8),
    ("Reserved_37",       UINT8 * 3),
    ("BaseAddress",       Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE)
  ]

EFI_ACPI_DEBUG_PORT_TABLE_REVISION      = 0x01

EFI_ACPI_DBGP_INTERFACE_TYPE_FULL_16550                                 = 0
EFI_ACPI_DBGP_INTERFACE_TYPE_16550_SUBSET_COMPATIBLE_WITH_MS_DBGP_SPEC  = 1

