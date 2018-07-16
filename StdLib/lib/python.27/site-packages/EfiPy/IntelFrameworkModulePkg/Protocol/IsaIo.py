#
# IsaIo.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IsaIo.py is free software: you can redistribute it and/or
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

from EfiPy.IntelFrameworkModulePkg.Protocol.IsaAcpi import EFI_ISA_ACPI_RESOURCE_LIST

gEfiIsaIoProtocolGuid = \
  EFI_GUID (0x7ee2bd44, 0x3da0, 0x11d4, ( 0x9a, 0x38, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d))

class EFI_ISA_IO_PROTOCOL (Structure):
  pass

EfiIsaIoWidthUint8          =  0
EfiIsaIoWidthUint16         =  1
EfiIsaIoWidthUint32         =  2
EfiIsaIoWidthReserved       =  3
EfiIsaIoWidthFifoUint8      =  4
EfiIsaIoWidthFifoUint16     =  5
EfiIsaIoWidthFifoUint32     =  6
EfiIsaIoWidthFifoReserved   =  7
EfiIsaIoWidthFillUint8      =  8
EfiIsaIoWidthFillUint16     =  9
EfiIsaIoWidthFillUint32     = 10
EfiIsaIoWidthFillReserved   = 11
EfiIsaIoWidthMaximum        = 12
EFI_ISA_IO_PROTOCOL_WIDTH   = UINTN

EFI_ISA_IO_ATTRIBUTE_MEMORY_WRITE_COMBINE  = 0x080
EFI_ISA_IO_ATTRIBUTE_MEMORY_CACHED         = 0x800
EFI_ISA_IO_ATTRIBUTE_MEMORY_DISABLE        = 0x1000

EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_SPEED_COMPATIBLE  = 0x001
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_SPEED_A           = 0x002
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_SPEED_B           = 0x004
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_SPEED_C           = 0x008
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_WIDTH_8           = 0x010
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_WIDTH_16          = 0x020
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_SINGLE_MODE       = 0x040
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_DEMAND_MODE       = 0x080
EFI_ISA_IO_SLAVE_DMA_ATTRIBUTE_AUTO_INITIALIZE   = 0x100

EfiIsaIoOperationBusMasterRead          = 0
EfiIsaIoOperationBusMasterWrite         = 1
EfiIsaIoOperationBusMasterCommonBuffer  = 2
EfiIsaIoOperationSlaveRead              = 3
EfiIsaIoOperationSlaveWrite             = 4
EfiIsaIoOperationMaximum                = 5
EFI_ISA_IO_PROTOCOL_OPERATION           = UINTN

EFI_ISA_IO_PROTOCOL_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL), # IN      *This
  EFI_ISA_IO_PROTOCOL_WIDTH,    # IN      Width,
  UINT32,                       # IN      Offset,
  UINTN,                        # IN      Count,
  PVOID                         # IN OUT  *Buffer
  )

class EFI_ISA_IO_PROTOCOL_ACCESS (Structure):
  _fields_ = [
    ("Read",  EFI_ISA_IO_PROTOCOL_IO_MEM),
    ("Write", EFI_ISA_IO_PROTOCOL_IO_MEM)
  ]

EFI_ISA_IO_PROTOCOL_COPY_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL), # IN      *This
  EFI_ISA_IO_PROTOCOL_WIDTH,    # IN      Width,
  UINT32,                       # IN      DestOffset,
  UINT32,                       # IN      SrcOffset,
  UINTN                         # IN      Count
  )

EFI_ISA_IO_PROTOCOL_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL),   # IN     *This
  EFI_ISA_IO_PROTOCOL_OPERATION,  # IN     Operation,
  UINT8,                          # IN     ChannelNumber      OPTIONAL,
  UINT32,                         # IN     ChannelAttributes,
  PVOID,                          # IN     *HostAddress,
  POINTER(UINTN),                 # IN OUT *NumberOfBytes,
  POINTER(EFI_PHYSICAL_ADDRESS),  # OUT    *DeviceAddress,
  POINTER(PVOID)                  # OUT    **Mapping
  )

EFI_ISA_IO_PROTOCOL_UNMAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL), # IN  *This
  PVOID                         # IN  *Mapping
  )

EFI_ISA_IO_PROTOCOL_ALLOCATE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL), # IN  *This
  EFI_ALLOCATE_TYPE,            # IN  Type,
  EFI_MEMORY_TYPE,              # IN  MemoryType,
  UINTN,                        # IN  Pages,
  POINTER(PVOID),               # OUT **HostAddress,
  UINT64                        # IN  Attributes
  )

EFI_ISA_IO_PROTOCOL_FREE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL), # IN *This
  UINTN,                        # IN Pages,
  PVOID                         # IN *HostAddress
  )

EFI_ISA_IO_PROTOCOL_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_IO_PROTOCOL)  # IN *This
  )

EFI_ISA_IO_PROTOCOL._fields_ = [
    ("Mem",             EFI_ISA_IO_PROTOCOL_ACCESS),
    ("Io",              EFI_ISA_IO_PROTOCOL_ACCESS),
    ("CopyMem",         EFI_ISA_IO_PROTOCOL_COPY_MEM),
    ("Map",             EFI_ISA_IO_PROTOCOL_MAP),
    ("Unmap",           EFI_ISA_IO_PROTOCOL_UNMAP),
    ("AllocateBuffer",  EFI_ISA_IO_PROTOCOL_ALLOCATE_BUFFER),
    ("FreeBuffer",      EFI_ISA_IO_PROTOCOL_FREE_BUFFER),
    ("Flush",           EFI_ISA_IO_PROTOCOL_FLUSH),
    ("ResourceList",    POINTER(EFI_ISA_ACPI_RESOURCE_LIST)),
    ("RomSize",         UINT32),
    ("RomImage",        PVOID)
  ]

