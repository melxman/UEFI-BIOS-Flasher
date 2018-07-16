#
# FirmwareVolumeHeader.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FirmwareVolumeHeader.py is free software: you can redistribute it and/or
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

EFI_FVB_READ_DISABLED_CAP   = 0x00000001
EFI_FVB_READ_ENABLED_CAP    = 0x00000002
EFI_FVB_READ_STATUS         = 0x00000004

EFI_FVB_WRITE_DISABLED_CAP  = 0x00000008
EFI_FVB_WRITE_ENABLED_CAP   = 0x00000010
EFI_FVB_WRITE_STATUS        = 0x00000020

EFI_FVB_LOCK_CAP            = 0x00000040
EFI_FVB_LOCK_STATUS         = 0x00000080

EFI_FVB_STICKY_WRITE        = 0x00000200
EFI_FVB_MEMORY_MAPPED       = 0x00000400
EFI_FVB_ERASE_POLARITY      = 0x00000800

EFI_FVB_ALIGNMENT_CAP       = 0x00008000
EFI_FVB_ALIGNMENT_2         = 0x00010000
EFI_FVB_ALIGNMENT_4         = 0x00020000
EFI_FVB_ALIGNMENT_8         = 0x00040000
EFI_FVB_ALIGNMENT_16        = 0x00080000
EFI_FVB_ALIGNMENT_32        = 0x00100000
EFI_FVB_ALIGNMENT_64        = 0x00200000
EFI_FVB_ALIGNMENT_128       = 0x00400000
EFI_FVB_ALIGNMENT_256       = 0x00800000
EFI_FVB_ALIGNMENT_512       = 0x01000000
EFI_FVB_ALIGNMENT_1K        = 0x02000000
EFI_FVB_ALIGNMENT_2K        = 0x04000000
EFI_FVB_ALIGNMENT_4K        = 0x08000000
EFI_FVB_ALIGNMENT_8K        = 0x10000000
EFI_FVB_ALIGNMENT_16K       = 0x20000000
EFI_FVB_ALIGNMENT_32K       = 0x40000000
EFI_FVB_ALIGNMENT_64K       = 0x80000000

EFI_FVB_CAPABILITIES  = EFI_FVB_READ_DISABLED_CAP  | \
                        EFI_FVB_READ_ENABLED_CAP   | \
                        EFI_FVB_WRITE_DISABLED_CAP | \
                        EFI_FVB_WRITE_ENABLED_CAP  | \
                        EFI_FVB_LOCK_CAP \


def EFI_TEST_FFS_ATTRIBUTES_BIT( FvbAttributes, TestAttributes, Bit):
      if FvbAttributes & EFI_FVB_ERASE_POLARITY != 0:
        return ((~TestAttributes) & Bit) == Bit
      else:
        return (TestAttributes & Bit) == Bit

EFI_FVB_STATUS    = (EFI_FVB_READ_STATUS | EFI_FVB_WRITE_STATUS | EFI_FVB_LOCK_STATUS)
