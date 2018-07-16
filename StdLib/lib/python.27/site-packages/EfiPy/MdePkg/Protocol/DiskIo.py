#
# DiskIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DiskIo.py is free software: you can redistribute it and/or
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

gEfiDiskIoProtocolGuid      = \
  EFI_GUID (0xce345171, 0xba0b, 0x11d2, (0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_DISK_IO_PROTOCOL (Structure):
  pass

EFI_DISK_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO_PROTOCOL),    # IN  *This
  UINT32,                           # IN  MediaId,
  UINT64,                           # IN  Offset,
  UINTN,                            # IN  BufferSize,
  PVOID                             # OUT *Buffer
  )

EFI_DISK_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO_PROTOCOL),    # IN  *This
  UINT32,                           # IN  MediaId,
  UINT64,                           # IN  Offset,
  UINTN,                            # IN  BufferSize,
  PVOID                             # IN  *Buffer
  )

EFI_DISK_IO_PROTOCOL_REVISION = 0x00010000

EFI_DISK_IO_PROTOCOL._fields_ = [
    ("Revision",  UINT64),
    ("ReadDisk",  EFI_DISK_READ),
    ("WriteDisk", EFI_DISK_WRITE)
  ]

