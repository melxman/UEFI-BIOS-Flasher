#
# Mbr.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Mbr.py is free software: you can redistribute it and/or modify
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

MBR_SIGNATURE               = 0xaa55

EXTENDED_DOS_PARTITION      = 0x05
EXTENDED_WINDOWS_PARTITION  = 0x0F

MAX_MBR_PARTITIONS          = 4

PMBR_GPT_PARTITION          = 0xEE
EFI_PARTITION               = 0xEF

MBR_SIZE                    = 512

class MBR_PARTITION_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BootIndicator", UINT8),
    ("StartHead",     UINT8),
    ("StartSector",   UINT8),
    ("StartTrack",    UINT8),
    ("OSIndicator",   UINT8),
    ("EndHead",       UINT8),
    ("EndSector",     UINT8),
    ("EndTrack",      UINT8),
    ("StartingLBA",   UINT8 * 4),
    ("SizeInLBA",     UINT8 * 4)
  ]

class MASTER_BOOT_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BootStrapCode",       UINT8 * 440),
    ("UniqueMbrSignature",  UINT8 * 4),
    ("Unknown",             UINT8 * 2),
    ("Partition",           MBR_PARTITION_RECORD * MAX_MBR_PARTITIONS),
    ("Signature",           UINT16)
  ]

