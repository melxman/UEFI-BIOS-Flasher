#
# PiS3BootScript.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiS3BootScript.py is free software: you can redistribute it and/or
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

from EfiPy import *

EFI_BOOT_SCRIPT_IO_WRITE_OPCODE                 = 0x00
EFI_BOOT_SCRIPT_IO_READ_WRITE_OPCODE            = 0x01
EFI_BOOT_SCRIPT_MEM_WRITE_OPCODE                = 0x02
EFI_BOOT_SCRIPT_MEM_READ_WRITE_OPCODE           = 0x03
EFI_BOOT_SCRIPT_PCI_CONFIG_WRITE_OPCODE         = 0x04
EFI_BOOT_SCRIPT_PCI_CONFIG_READ_WRITE_OPCODE    = 0x05
EFI_BOOT_SCRIPT_SMBUS_EXECUTE_OPCODE            = 0x06
EFI_BOOT_SCRIPT_STALL_OPCODE                    = 0x07
EFI_BOOT_SCRIPT_DISPATCH_OPCODE                 = 0x08
EFI_BOOT_SCRIPT_DISPATCH_2_OPCODE               = 0x09
EFI_BOOT_SCRIPT_INFORMATION_OPCODE              = 0x0A
EFI_BOOT_SCRIPT_PCI_CONFIG2_WRITE_OPCODE        = 0x0B
EFI_BOOT_SCRIPT_PCI_CONFIG2_READ_WRITE_OPCODE   = 0x0C
EFI_BOOT_SCRIPT_IO_POLL_OPCODE                  = 0x0D
EFI_BOOT_SCRIPT_MEM_POLL_OPCODE                 = 0x0E
EFI_BOOT_SCRIPT_PCI_CONFIG_POLL_OPCODE          = 0x0F
EFI_BOOT_SCRIPT_PCI_CONFIG2_POLL_OPCODE         = 0x10

EfiBootScriptWidthUint8       = 0
EfiBootScriptWidthUint16      = 1
EfiBootScriptWidthUint32      = 2
EfiBootScriptWidthUint64      = 3
EfiBootScriptWidthFifoUint8   = 4
EfiBootScriptWidthFifoUint16  = 5
EfiBootScriptWidthFifoUint32  = 6
EfiBootScriptWidthFifoUint64  = 7
EfiBootScriptWidthFillUint8   = 8
EfiBootScriptWidthFillUint16  = 9
EfiBootScriptWidthFillUint32  = 10
EfiBootScriptWidthFillUint64  = 11
EfiBootScriptWidthMaximum     = 12
EFI_BOOT_SCRIPT_WIDTH         = ENUM

