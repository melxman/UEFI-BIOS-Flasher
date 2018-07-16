#
# StorageSecurityCommand.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# StorageSecurityCommand.py is free software: you can redistribute it and/or
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

gEfiStorageSecurityCommandProtocolGuid  = \
  EFI_GUID (0xC88B0B6D, 0x0DFC, 0x49A7, (0x9C, 0xB4, 0x49, 0x07, 0x4B, 0x4C, 0x3A, 0x78 ))
class EFI_STORAGE_SECURITY_COMMAND_PROTOCOL (Structure):
  pass

EFI_STORAGE_SECURITY_RECEIVE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_STORAGE_SECURITY_COMMAND_PROTOCOL),   # IN  *This
  UINT32,                                           # IN  MediaId,
  UINT64,                                           # IN  Timeout,
  UINT8,                                            # IN  SecurityProtocolId,
  UINT16,                                           # IN  SecurityProtocolSpecificData,
  UINTN,                                            # IN  PayloadBufferSize,
  PVOID,                                            # OUT *PayloadBuffer,
  POINTER(UINTN)                                    # OUT *PayloadTransferSize
  )

EFI_STORAGE_SECURITY_SEND_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_STORAGE_SECURITY_COMMAND_PROTOCOL),   # IN  *This
  UINT32,                                           # IN  MediaId,
  UINT64,                                           # IN  Timeout,
  UINT8,                                            # IN  SecurityProtocolId,
  UINT16,                                           # IN  SecurityProtocolSpecificData,
  UINTN,                                            # IN  PayloadBufferSize,
  PVOID                                             # OUT *PayloadBuffer,
  )

EFI_STORAGE_SECURITY_COMMAND_PROTOCOL._fields_ = [
    ("ReceiveData", EFI_STORAGE_SECURITY_RECEIVE_DATA),
    ("SendData",    EFI_STORAGE_SECURITY_SEND_DATA)
  ]

