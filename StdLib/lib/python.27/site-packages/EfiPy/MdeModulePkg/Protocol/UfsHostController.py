#
# UfsHostController.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# UfsHostController.py is free software: you can redistribute it and/or
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

gEdkiiUfsHostControllerProtocolGuid = \
  EFI_GUID (0xebc01af5, 0x7a9, 0x489e, (0xb7, 0xce, 0xdc, 0x8, 0x9e, 0x45, 0x9b, 0x2f))

class EDKII_UFS_HOST_CONTROLLER_PROTOCOL (Structure):
  pass

EDKII_UFS_HC_GET_MMIO_BAR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL), # IN  *This,
  POINTER(UINTN)                               # OUT *MmioBar
  )

EdkiiUfsHcOperationBusMasterRead          = 1
EdkiiUfsHcOperationBusMasterWrite         = 2
EdkiiUfsHcOperationBusMasterCommonBuffer  = 3
EdkiiUfsHcOperationMaximum                = 4
EDKII_UFS_HOST_CONTROLLER_OPERATION       = UINTN

EDKII_UFS_HC_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL),  # IN     *This,
  EDKII_UFS_HOST_CONTROLLER_OPERATION,          # IN     Operation,
  PVOID,                                        # IN     *HostAddress,
  POINTER(UINTN),                               # IN OUT *NumberOfBytes,
  POINTER(EFI_PHYSICAL_ADDRESS),                #    OUT *DeviceAddress,
  POINTER(PVOID)                                #    OUT **Mapping
  )

EDKII_UFS_HC_UNMAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL),  # IN *This,
  PVOID                                         # IN *Mapping
  )

EDKII_UFS_HC_ALLOCATE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL),  # IN     *This,
  EFI_ALLOCATE_TYPE,                            # IN     Type,
  EFI_MEMORY_TYPE,                              # IN     MemoryType,
  UINTN,                                        # IN     Pages,
  POINTER(PVOID),                               #    OUT **HostAddress,
  UINT64                                        # IN     Attributes
  )

EDKII_UFS_HC_FREE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL),  # IN *This,
  UINTN,                                        # IN Pages,
  PVOID                                         # IN *HostAddress
  )

EDKII_UFS_HC_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL)   # IN *This,
  )

EfiUfsHcWidthUint8                        = 0
EfiUfsHcWidthUint16                       = 1
EfiUfsHcWidthUint32                       = 2
EfiUfsHcWidthUint64                       = 3
EfiUfsHcWidthMaximum                      = 4
EDKII_UFS_HOST_CONTROLLER_PROTOCOL_WIDTH  = UINTN

EDKII_UFS_HC_MMIO_READ_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_UFS_HOST_CONTROLLER_PROTOCOL),  # IN     *This,
  EDKII_UFS_HOST_CONTROLLER_PROTOCOL_WIDTH,     # IN     Width,
  UINT64,                                       # IN     Offset,
  UINTN,                                        # IN     Count,
  PVOID                                         # IN OUT *Buffer
  )

EDKII_UFS_HOST_CONTROLLER_PROTOCOL._fields_ = [
  ("GetUfsHcMmioBar", EDKII_UFS_HC_GET_MMIO_BAR),
  ("AllocateBuffer",  EDKII_UFS_HC_ALLOCATE_BUFFER),
  ("FreeBuffer",      EDKII_UFS_HC_FREE_BUFFER),
  ("Map",             EDKII_UFS_HC_MAP),
  ("Unmap",           EDKII_UFS_HC_UNMAP),
  ("Flush",           EDKII_UFS_HC_FLUSH),
  ("Read",            EDKII_UFS_HC_MMIO_READ_WRITE),
  ("Write",           EDKII_UFS_HC_MMIO_READ_WRITE)
  ]

