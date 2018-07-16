#
# SystemNvDataGuid.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# SystemNvDataGuid.py is free software: you can redistribute it and/or
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

gEfiSystemNvDataFvGuid         = \
  EFI_GUID (0xfff12b8d, 0x7696, 0x4c8b, (0xa9, 0x85, 0x27, 0x47, 0x7, 0x5b, 0x4f, 0x50))

gEdkiiWorkingBlockSignatureGuid         = \
  EFI_GUID (0x9e58292b, 0x7c68, 0x497d, (0xa0, 0xce, 0x65,  0x0, 0xfd, 0x9f, 0x1b, 0x95))

WORKING_BLOCK_VALID   = 0x1
WORKING_BLOCK_INVALID = 0x2

class EFI_FAULT_TOLERANT_WORKING_BLOCK_HEADER (Structure):
  _fields_ = [
  ("Signature",             EFI_GUID),
  ("Crc",                   UINT32),
  ("WorkingBlockValid",     UINT8, 1),
  ("WorkingBlockInvalid",   UINT8, 1),
  ("Reserved",              UINT8, 6),
  ("Reserved3",             UINT8 * 3),
  ("WriteQueueSize",        UINT64)
  ]

FTW_VALID_STATE     = 0
FTW_INVALID_STATE   = 1

class EFI_FAULT_TOLERANT_WRITE_HEADER (Structure):
  _fields_ = [
  ("HeaderAllocated", UINT8, 1),
  ("WritesAllocated", UINT8, 1),
  ("Complete",        UINT8, 1),
  ("Reserved",        UINT8, 5),
  ("CallerId",        EFI_GUID),
  ("NumberOfWrites",  UINT64),
  ("PrivateDataSize", UINT64)
  ]

class EFI_FAULT_TOLERANT_WRITE_RECORD (Structure):
  _fields_ = [
  ("BootBlockUpdate",     UINT8, 1),
  ("SpareComplete",       UINT8, 1),
  ("DestinationComplete", UINT8, 1),
  ("Reserved",            UINT8, 5),
  ("Lba",                 EFI_LBA),
  ("Offset",              UINT64),
  ("Length",              UINT64),
  ("RelativeOffset",      INT64)
  # ("PrivateData",         UINT8[PrivateDataSize])
  ]

def FTW_RECORD_SIZE(PrivateDataSize):
  return sizeof (EFI_FAULT_TOLERANT_WRITE_RECORD) + PrivateDataSize
def FTW_RECORD_TOTAL_SIZE(NumberOfWrites, PrivateDataSize):
  return NumberOfWrites * (sizeof (EFI_FAULT_TOLERANT_WRITE_RECORD) + PrivateDataSize)

def FTW_WRITE_TOTAL_SIZE(NumberOfWrites, PrivateDataSize):
  return sizeof (EFI_FAULT_TOLERANT_WRITE_HEADER) + NumberOfWrites * \
        (sizeof (EFI_FAULT_TOLERANT_WRITE_RECORD) + PrivateDataSize) \

