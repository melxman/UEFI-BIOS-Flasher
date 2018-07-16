#
# FaultTolerantWrite.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FaultTolerantWrite.py is free software: you can redistribute it and/or
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

gEfiFaultTolerantWriteProtocolGuid = \
  EFI_GUID (0x3ebd9e82, 0x2c78, 0x4de6, (0x97, 0x86, 0x8d, 0x4b, 0xfc, 0xb7, 0xc8, 0x81))

class EFI_FAULT_TOLERANT_WRITE_PROTOCOL (Structure):
  pass

EFI_FAULT_TOLERANT_WRITE_GET_MAX_BLOCK_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FAULT_TOLERANT_WRITE_PROTOCOL), # IN      *This,
  POINTER(UINTN)                              #    OUT  *BlockSize
  )

EFI_FAULT_TOLERANT_WRITE_ALLOCATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FAULT_TOLERANT_WRITE_PROTOCOL), # IN *This,
  POINTER(EFI_GUID),                          # IN *CallerId,
  UINTN,                                      # IN PrivateDataSize,
  UINTN                                       # IN NumberOfWrites
  )

EFI_FAULT_TOLERANT_WRITE_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FAULT_TOLERANT_WRITE_PROTOCOL), # IN *This,
  EFI_LBA,                                    # IN Lba,
  UINTN,                                      # IN Offset,
  UINTN,                                      # IN Length,
  PVOID,                                      # IN *PrivateData,
  EFI_HANDLE,                                 # IN FvbHandle,
  PVOID                                       # IN *Buffer
  )

EFI_FAULT_TOLERANT_WRITE_RESTART = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FAULT_TOLERANT_WRITE_PROTOCOL), # IN *This,
  EFI_HANDLE                                  # IN FvbHandle
  )

EFI_FAULT_TOLERANT_WRITE_ABORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FAULT_TOLERANT_WRITE_PROTOCOL)  # IN *This,
  )

EFI_FAULT_TOLERANT_WRITE_GET_LAST_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FAULT_TOLERANT_WRITE_PROTOCOL), # IN      *This,
  POINTER(EFI_GUID),                          # OUT     *CallerId,
  POINTER(EFI_LBA),                           # OUT     *Lba,
  POINTER(UINTN),                             # OUT     *Offset,
  POINTER(UINTN),                             # OUT     *Length,
  POINTER(UINTN),                             # IN OUT  *PrivateDataSize,
  PVOID,                                      # OUT     *PrivateData,
  POINTER(BOOLEAN)                            # OUT     *Complete
  )

EFI_FAULT_TOLERANT_WRITE_PROTOCOL._fields_ = [
  ("GetMaxBlockSize",   EFI_FAULT_TOLERANT_WRITE_GET_MAX_BLOCK_SIZE),
  ("Allocate",          EFI_FAULT_TOLERANT_WRITE_ALLOCATE),
  ("Write",             EFI_FAULT_TOLERANT_WRITE_WRITE),
  ("Restart",           EFI_FAULT_TOLERANT_WRITE_RESTART),
  ("Abort",             EFI_FAULT_TOLERANT_WRITE_ABORT),
  ("GetLastWrite",      EFI_FAULT_TOLERANT_WRITE_GET_LAST_WRITE)
  ]

