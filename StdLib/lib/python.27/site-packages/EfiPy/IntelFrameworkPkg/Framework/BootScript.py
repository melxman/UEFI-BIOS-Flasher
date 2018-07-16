#
# BootScript.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# BootScript.py is free software: you can redistribute it and/or
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

FRAMEWORK_EFI_ACPI_S3_RESUME_SCRIPT_TABLE               = 0x00
FRAMEWORK_EFI_BOOT_SCRIPT_MEM_POLL_OPCODE               = 0x09
FRAMEWORK_EFI_BOOT_SCRIPT_DISPATCH_2_OPCODE             = 0x0D
FRAMEWORK_EFI_BOOT_SCRIPT_TABLE_OPCODE                  = 0xAA
FRAMEWORK_EFI_BOOT_SCRIPT_TERMINATE_OPCODE              = 0xFF

