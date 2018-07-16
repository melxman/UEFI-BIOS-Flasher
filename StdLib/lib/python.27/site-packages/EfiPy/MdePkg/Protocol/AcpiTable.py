#
# AcpiTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# AcpiTable.py is free software: you can redistribute it and/or
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

gEfiAcpiTableProtocolGuid               = \
  EFI_GUID (0xffe06bdd, 0x6107, 0x46a6, ( 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c ))

class EFI_ACPI_TABLE_PROTOCOL (Structure):
  pass

EFI_ACPI_TABLE_INSTALL_ACPI_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_TABLE_PROTOCOL), # IN  *This
  PVOID,                            # IN  *AcpiTableBuffer
  UINTN,                            # IN  AcpiTableBufferSize
  POINTER (UINTN)                   # OUT *TableKey
  )

EFI_ACPI_TABLE_UNINSTALL_ACPI_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_TABLE_PROTOCOL), # IN  *This
  UINTN                             # IN  TableKey
  )

EFI_ACPI_TABLE_PROTOCOL._fields_ = [
    ("InstallAcpiTable",    EFI_ACPI_TABLE_INSTALL_ACPI_TABLE),
    ("UninstallAcpiTable",  EFI_ACPI_TABLE_UNINSTALL_ACPI_TABLE)
  ]

