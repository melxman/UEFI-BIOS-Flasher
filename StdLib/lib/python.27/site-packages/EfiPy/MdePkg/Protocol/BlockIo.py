#
# BlockIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BlockIo.py is free software: you can redistribute it and/or
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

gEfiBlockIoProtocolGuid = EFI_GUID( 0x964e5b21, 0x6459, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))
EFI_BLOCK_IO_PROTOCOL_GUID  = gEfiBlockIoProtocolGuid

class EFI_BLOCK_IO_PROTOCOL (Structure):
  pass

EFI_BLOCK_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLOCK_IO_PROTOCOL),       # IN *This
  BOOLEAN                               # IN ExtendedVerification
  )

EFI_BLOCK_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLOCK_IO_PROTOCOL),       # IN  *This
  UINT32,                               # IN  MediaId
  EFI_LBA,                              # IN  Lba
  UINTN,                                # IN  BufferSize
  PVOID                                 # OUT *Buffer
  )

EFI_BLOCK_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLOCK_IO_PROTOCOL),       # IN *This
  UINT32,                               # IN MediaId
  EFI_LBA,                              # IN Lba
  UINTN,                                # IN BufferSize
  PVOID                                 # IN *Buffer
  )

EFI_BLOCK_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLOCK_IO_PROTOCOL)        # IN *This
  )

class EFI_BLOCK_IO_MEDIA (Structure):
  _fields_ = [
    ("MediaId",                         UINT32),
    ("RemovableMedia",                  BOOLEAN),
    ("MediaPresent",                    BOOLEAN),
    ("LogicalPartition",                BOOLEAN),
    ("ReadOnly",                        BOOLEAN),
    ("WriteCaching",                    BOOLEAN),
    ("BlockSize",                       UINT32),
    ("IoAlign",                         UINT32),
    ("LastBlock",                       EFI_LBA),
    ("LowestAlignedLba",                EFI_LBA),
    ("LogicalBlocksPerPhysicalBlock",   UINT32),
    ("OptimalTransferLengthGranularity",UINT32)
    ]

EFI_BLOCK_IO_PROTOCOL_REVISION  = 0x00010000L
EFI_BLOCK_IO_PROTOCOL_REVISION2 = 0x00020001L
EFI_BLOCK_IO_PROTOCOL_REVISION3 = 0x00020031L

EFI_BLOCK_IO_PROTOCOL._fields_ = [
  ("Revision",    UINT64),
  ("Media",       POINTER(EFI_BLOCK_IO_MEDIA)),
  ("Reset",       EFI_BLOCK_RESET),
  ("ReadBlocks",  EFI_BLOCK_READ),
  ("WriteBlocks", EFI_BLOCK_WRITE),
  ("FlushBlocks", EFI_BLOCK_FLUSH)
  ]

