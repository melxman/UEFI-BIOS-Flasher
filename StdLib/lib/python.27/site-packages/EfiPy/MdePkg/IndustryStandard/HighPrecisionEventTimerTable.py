#
# HighPrecisionEventTimerTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HighPrecisionEventTimerTable.py is free software: you can redistribute it and/or modify
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
class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                    Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("EventTimerBlockId",                         UINT32),
    ("BaseAddressLower32Bit",                     Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("HpetNumber",                                UINT8),
    ("MainCounterMinimumClockTickInPeriodicMode", UINT16),
    ("PageProtectionAndOemAttribute",             UINT8)
  ]

EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_REVISION  = 0x01

EFI_ACPI_NO_PAGE_PROTECTION   = 0
EFI_ACPI_4KB_PAGE_PROTECTION  = 1
EFI_ACPI_64KB_PAGE_PROTECTION = 2

