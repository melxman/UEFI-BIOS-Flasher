#
# TcpaAcpi.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# TcpaAcpi.py is free software: you can redistribute it and/or modify
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

class EFI_TCG_CLIENT_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",        Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformClass", UINT16),
    ("Laml",          UINT32),
    ("Lasa",          UINT64)
  ]

class EFI_TCG_SERVER_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",          Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformClass",   UINT16),
    ("Reserved0",       UINT16),
    ("Laml",            UINT64),
    ("Lasa",            UINT64),
    ("SpecRev",         UINT16),
    ("DeviceFlags",     UINT8),
    ("InterruptFlags",  UINT8),
    ("Gpe",             UINT8),
    ("Reserved1",       UINT8 * 3),
    ("GlobalSysInt",    UINT32),
    ("BaseAddress",     Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("Reserved2",       UINT32),
    ("ConfigAddress",   Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("PciSegNum",       UINT8),
    ("PciBusNum",       UINT8),
    ("PciDevNum",       UINT8),
    ("PciFuncNum",      UINT8),
  ]

TCG_PLATFORM_TYPE_CLIENT   = 0
TCG_PLATFORM_TYPE_SERVER   = 1

