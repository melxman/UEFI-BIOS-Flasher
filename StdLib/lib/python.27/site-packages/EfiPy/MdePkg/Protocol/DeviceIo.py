#
# DeviceIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DeviceIo.py is free software: you can redistribute it and/or
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

gEfiDeviceIoProtocolGuid                = \
  EFI_GUID (0xaf6ac311, 0x84c3, 0x11d2, (0x8e, 0x3c, 0x00, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_DEVICE_IO_PROTOCOL (Structure):
  pass

EFI_DEVICE_IO_INTERFACE = EFI_DEVICE_IO_PROTOCOL
IO_UINT8  = 0
IO_UINT16 = 1
IO_UINT32 = 2
IO_UINT64 = 3
MMIO_COPY_UINT8  = 4
MMIO_COPY_UINT16 = 5
MMIO_COPY_UINT32 = 6
MMIO_COPY_UINT64 = 7
EFI_IO_WIDTH     = ENUM

EFI_DEVICE_IO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL),  # IN     *This
  EFI_IO_WIDTH,                     # IN     Width,
  UINT64,                           # IN     Address,
  UINTN,                            # IN     Count,
  PVOID                             # IN OUT *Buffer
  )

class EFI_IO_ACCESS (Structure):
  _fields_ = [
    ("Read",  EFI_DEVICE_IO),
    ("Write", EFI_DEVICE_IO)
  ]

EFI_PCI_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL),            # IN     *This
  UINT64,                                     # IN     PciAddress,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))  # IN OUT **PciDevicePath
  )

EfiBusMasterRead              = 0
EfiBusMasterWrite             = 1
EfiBusMasterCommonBuffer      = 2
EFI_IO_OPERATION_TYPE         = ENUM

EFI_IO_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL),  # IN     *This
  EFI_IO_OPERATION_TYPE,            # IN     Operation,
  POINTER(EFI_PHYSICAL_ADDRESS),    # IN     *HostAddress,
  POINTER(UINTN),                   # IN OUT *NumberOfBytes,
  POINTER(EFI_PHYSICAL_ADDRESS),    #    OUT *DeviceAddress,
  POINTER(PVOID)                    #    OUT **Mapping
  )

EFI_IO_UNMAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL),  # IN *This
  PVOID                             # IN *Mapping
  )

EFI_IO_ALLOCATE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL),  # IN     *This
  EFI_ALLOCATE_TYPE,                # IN     Type,
  EFI_MEMORY_TYPE,                  # IN     MemoryType,
  UINTN,                            # IN     Pages,
  POINTER(EFI_PHYSICAL_ADDRESS)     # IN OUT *HostAddress
  )

EFI_IO_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL)   # IN     *This
  )

EFI_IO_FREE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_IO_PROTOCOL),# IN *This
  UINTN,                          # IN Pages,
  EFI_PHYSICAL_ADDRESS            # IN HostAddress
  )

EFI_DEVICE_IO_PROTOCOL._fields_ = [
    ("Mem",             EFI_IO_ACCESS),
    ("Io",              EFI_IO_ACCESS),
    ("Pci",             EFI_IO_ACCESS),
    ("Map",             EFI_IO_MAP),
    ("PciDevicePath",   EFI_PCI_DEVICE_PATH),
    ("Unmap",           EFI_IO_UNMAP),
    ("AllocateBuffer",  EFI_IO_ALLOCATE_BUFFER),
    ("Flush",           EFI_IO_FLUSH),
    ("FreeBuffer",      EFI_IO_FREE_BUFFER)
  ]

