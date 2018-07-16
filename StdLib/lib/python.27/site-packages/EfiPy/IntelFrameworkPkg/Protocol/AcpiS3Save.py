#
# AcpiS3Save.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# AcpiS3Save.py is free software: you can redistribute it and/or
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

class EFI_ACPI_S3_SAVE_PROTOCOL (Structure):
  pass

gEfiAcpiS3SaveProtocolGuid = \
  EFI_GUID (0x125f2de1, 0xfb85, 0x440c, (0xa5, 0x4c, 0x4d, 0x99, 0x35, 0x8a, 0x8d, 0x38 ))

EFI_ACPI_S3_SAVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_S3_SAVE_PROTOCOL),   # IN *This
  PVOID                                 # IN *LegacyMemoryAddress
  )

EFI_ACPI_GET_LEGACY_MEMORY_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_S3_SAVE_PROTOCOL),   # IN  *This
  POINTER(UINTN)                        # OUT *Size
  )

EFI_ACPI_S3_SAVE_PROTOCOL._fields_ = [
  ("GetLegacyMemorySize", EFI_ACPI_GET_LEGACY_MEMORY_SIZE),
  ("S3Save",              EFI_ACPI_S3_SAVE)
  ]

