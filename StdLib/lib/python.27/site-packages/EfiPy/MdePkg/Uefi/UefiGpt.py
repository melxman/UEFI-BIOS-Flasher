#
# UefiGpt.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UefiGpt.py is free software: you can redistribute it and/or modify
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

from EfiPy import *

PRIMARY_PART_HEADER_LBA = 1
EFI_PTAB_HEADER_ID      = SIGNATURE_64 ('E','F','I',' ','P','A','R','T')

class EFI_PARTITION_TABLE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                    EFI_TABLE_HEADER),
    ("MyLBA",                     EFI_LBA),
    ("AlternateLBA",              EFI_LBA),
    ("FirstUsableLBA",            EFI_LBA),
    ("LastUsableLBA",             EFI_LBA),
    ("DiskGUID",                  EFI_GUID),
    ("PartitionEntryLBA",         EFI_LBA),
    ("NumberOfPartitionEntries",  UINT32),
    ("SizeOfPartitionEntry",      UINT32),
    ("PartitionEntryArrayCRC32",  UINT32)
  ]

class EFI_PARTITION_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
    ("PartitionTypeGUID",   EFI_GUID),
    ("UniquePartitionGUID", EFI_GUID),
    ("StartingLBA",         EFI_LBA),
    ("EndingLBA",           EFI_LBA),
    ("Attributes",          UINT64),
    ("PartitionName",       CHAR16 * 36)
  ]

