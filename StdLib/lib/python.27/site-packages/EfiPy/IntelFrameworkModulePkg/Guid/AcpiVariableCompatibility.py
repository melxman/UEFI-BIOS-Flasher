#
# AcpiVariableCompatibility.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# AcpiVariableCompatibility.py is free software: you can redistribute it and/or
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

gEfiAcpiVariableCompatiblityGuid = \
  EFI_GUID (0xc020489e, 0x6db2, 0x4ef2, (0x9a, 0xa5, 0xca, 0x6, 0xfc, 0x11, 0xd3, 0x6a ))

ACPI_GLOBAL_VARIABLE  = u"AcpiGlobalVariable"

class ACPI_CPU_DATA_COMPATIBILITY (Structure):
  _fields_ = [
    ("APState",                 BOOLEAN),
    ("S3BootPath",              BOOLEAN),
    ("WakeUpBuffer",            EFI_PHYSICAL_ADDRESS),
    ("GdtrProfile",             EFI_PHYSICAL_ADDRESS),
    ("IdtrProfile",             EFI_PHYSICAL_ADDRESS),
    ("CpuPrivateData",          EFI_PHYSICAL_ADDRESS),
    ("StackAddress",            EFI_PHYSICAL_ADDRESS),
    ("MicrocodePointerBuffer",  EFI_PHYSICAL_ADDRESS),
    ("SmramBase",               EFI_PHYSICAL_ADDRESS),
    ("SmmStartImageBase",       EFI_PHYSICAL_ADDRESS),
    ("SmmStartImageSize",       UINT32),
    ("NumberOfCpus",            UINT32)
  ]

class ACPI_VARIABLE_SET_COMPATIBILITY (Structure):
  _fields_ = [
    ("AcpiReservedMemoryBase",    EFI_PHYSICAL_ADDRESS),
    ("AcpiReservedMemorySize",    UINT32),
    ("S3ReservedLowMemoryBase",   EFI_PHYSICAL_ADDRESS),
    ("AcpiBootScriptTable",       EFI_PHYSICAL_ADDRESS),
    ("RuntimeScriptTableBase",    EFI_PHYSICAL_ADDRESS),
    ("AcpiFacsTable",             EFI_PHYSICAL_ADDRESS),
    ("SystemMemoryLength",        UINT64),
    ("AcpiCpuData",               ACPI_CPU_DATA_COMPATIBILITY),
    ("VideoOpromAddress",         EFI_PHYSICAL_ADDRESS),
    ("VideoOpromSize",            UINT32),
    ("S3DebugBufferAddress",      EFI_PHYSICAL_ADDRESS),
    ("S3ResumeNvsEntryPoint",     EFI_PHYSICAL_ADDRESS)
  ]

