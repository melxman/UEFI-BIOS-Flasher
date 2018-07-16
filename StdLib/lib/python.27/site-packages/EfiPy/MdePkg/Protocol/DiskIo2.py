#
# DiskIo2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DiskIo2.py is free software: you can redistribute it and/or
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

gEfiDiskIo2ProtocolGuid = \
  EFI_GUID (0x151c8eae, 0x7f2c, 0x472c, (0x9e, 0x54, 0x98, 0x28, 0x19, 0x4f, 0x6a, 0x88))

class EFI_DISK_IO2_PROTOCOL (Structure):
  pass

class EFI_DISK_IO2_TOKEN (Structure):
  _fields_ = [
    ("Event",             EFI_EVENT),
    ("TransactionStatus", EFI_STATUS)
  ]

EFI_DISK_CANCEL_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO2_PROTOCOL)  # IN *This
  )

EFI_DISK_READ_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO2_PROTOCOL),   # IN     *This
  UINT32,                           # IN     MediaId,
  UINT64,                           # IN     Offset,
  POINTER(EFI_DISK_IO2_TOKEN),      # IN OUT *Token,
  UINTN,                            # IN     BufferSize,
  PVOID                             #    OUT *Buffer
  )

EFI_DISK_WRITE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO2_PROTOCOL),   # IN     *This
  UINT32,                           # IN     MediaId,
  UINT64,                           # IN     Offset,
  POINTER(EFI_DISK_IO2_TOKEN),      # IN OUT *Token,
  UINTN,                            # IN     BufferSize,
  PVOID                             # IN     *Buffer
  )

EFI_DISK_FLUSH_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO2_PROTOCOL),   # IN *This,
  POINTER(EFI_DISK_IO2_TOKEN),      # IN *Token
  )

EFI_DISK_IO2_PROTOCOL_REVISION = 0x00020000
EFI_DISK_IO2_PROTOCOL._fields_ = [
    ("Revision",    UINT64),
    ("Cancel",      EFI_DISK_CANCEL_EX),
    ("ReadDiskEx",  EFI_DISK_READ_EX),
    ("WriteDiskEx", EFI_DISK_WRITE_EX),
    ("FlushDiskEx", EFI_DISK_FLUSH_EX)
  ]

