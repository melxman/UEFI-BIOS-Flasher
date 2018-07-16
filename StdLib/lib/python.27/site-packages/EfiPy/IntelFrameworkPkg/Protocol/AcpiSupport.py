#
# AcpiSupport.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# AcpiSupport.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.AcpiSystemDescriptionTable import EFI_ACPI_TABLE_VERSION

class EFI_ACPI_SUPPORT_PROTOCOL (Structure):
  pass

gEfiAcpiSupportProtocolGuid = \
  EFI_GUID (0xdbff9d55, 0x89b7, 0x46da, (0xbd, 0xdf, 0x67, 0x7d, 0x3d, 0xc0, 0x24, 0x1d))

EFI_ACPI_GET_ACPI_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_SUPPORT_PROTOCOL),   # IN  *This
  INTN,                                 # IN  index,
  POINTER(PVOID),                       # OUT **Table,
  POINTER(EFI_ACPI_TABLE_VERSION),      # OUT *Version,
  POINTER(UINTN)                        # OUT *Handle
  )

EFI_ACPI_SET_ACPI_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_SUPPORT_PROTOCOL),   # IN      *This
  PVOID,                                # IN      *Table OPTIONAL,
  BOOLEAN,                              # IN      Checksum,
  EFI_ACPI_TABLE_VERSION,               # IN      Version,
  POINTER(UINTN)                        # IN OUT  *Handle
  )

EFI_ACPI_PUBLISH_TABLES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_SUPPORT_PROTOCOL),   # IN *This
  EFI_ACPI_TABLE_VERSION                # IN Version
  )

EFI_ACPI_SUPPORT_PROTOCOL._fields_ = [
    ("GetAcpiTable",  EFI_ACPI_GET_ACPI_TABLE),
    ("SetAcpiTable",  EFI_ACPI_SET_ACPI_TABLE),
    ("PublishTables", EFI_ACPI_PUBLISH_TABLES)
  ]

