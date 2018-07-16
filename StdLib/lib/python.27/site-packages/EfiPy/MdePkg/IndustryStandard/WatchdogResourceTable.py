#
# WatchdogResourceTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# WatchdogResourceTable.py is free software: you can redistribute it and/or modify
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

class EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("ControlRegisterAddress",  Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("CountRegisterAddress",    Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("PCIDeviceID",             UINT16),
    ("PCIVendorID",             UINT16),
    ("PCIBusNumber",            UINT8),
    ("PCIDeviceNumber",         UINT8),
    ("PCIFunctionNumber",       UINT8),
    ("PCISegment",              UINT8),
    ("MaxCount",                UINT16),
    ("Units",                   UINT8)
  ]

EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE_REVISION  = 0x01

EFI_ACPI_WDRT_1_0_COUNT_UNIT_1_SEC_PER_COUNT        = 1
EFI_ACPI_WDRT_1_0_COUNT_UNIT_100_MILLISEC_PER_COUNT = 2
EFI_ACPI_WDRT_1_0_COUNT_UNIT_10_MILLISEC_PER_COUNT  = 3

