#
# BluetoothHc.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BluetoothHc.py is free software: you can redistribute it and/or
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

gEfiBluetoothHcProtocolGuid         = \
  EFI_GUID (0xb3930571, 0xbeba, 0x4fc5, ( 0x92, 0x3, 0x94, 0x27, 0x24, 0x2e, 0x6a, 0x43 ))

class EFI_BLUETOOTH_HC_PROTOCOL (Structure):
  pass

EFI_BLUETOOTH_HC_SEND_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL), # IN      *This
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID,                              # IN      *Buffer,
  UINTN                               # IN      Timeout
  )

EFI_BLUETOOTH_HC_RECEIVE_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL), # IN      *This
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID,                              #    OUT  *Buffer,
  UINTN                               # IN      Timeout
  )

EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  PVOID,      # IN  *Data,
  UINTN,      # IN  DataLength,
  PVOID       # IN  *Context
  )

EFI_BLUETOOTH_HC_ASYNC_RECEIVE_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL),   # IN *This
  BOOLEAN,                              # IN IsNewTransfer,
  UINTN,                                # IN PollingInterval,
  UINTN,                                # IN DataLength,
  EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK, # IN Callback,
  PVOID                                 # IN *Context
  )

EFI_BLUETOOTH_HC_SEND_ACL_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL),   # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                # IN      *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_RECEIVE_ACL_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                #    OUT  *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_ASYNC_RECEIVE_ACL_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN  *This
  BOOLEAN,                              # IN  IsNewTransfer,
  UINTN,                                # IN  PollingInterval,
  UINTN,                                # IN  DataLength,
  EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK, # IN  Callback,
  PVOID                                 # IN  *Context
  )

EFI_BLUETOOTH_HC_SEND_SCO_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                # IN      *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_RECEIVE_SCO_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                #    OUT  *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_ASYNC_RECEIVE_SCO_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN  *This
  BOOLEAN,                              # IN  IsNewTransfer,
  UINTN,                                # IN  PollingInterval,
  UINTN,                                # IN  DataLength,
  EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK, # IN  Callback,
  PVOID                                 # IN  *Context
  )

EFI_BLUETOOTH_HC_PROTOCOL._fields_ = [
    ("SendCommand",         EFI_BLUETOOTH_HC_SEND_COMMAND),
    ("ReceiveEvent",        EFI_BLUETOOTH_HC_RECEIVE_EVENT),
    ("AsyncReceiveEvent",   EFI_BLUETOOTH_HC_ASYNC_RECEIVE_EVENT),
    ("SendACLData",         EFI_BLUETOOTH_HC_SEND_ACL_DATA),
    ("ReceiveACLData",      EFI_BLUETOOTH_HC_RECEIVE_ACL_DATA),
    ("AsyncReceiveACLData", EFI_BLUETOOTH_HC_ASYNC_RECEIVE_ACL_DATA),
    ("SendSCOData",         EFI_BLUETOOTH_HC_SEND_SCO_DATA),
    ("ReceiveSCOData",      EFI_BLUETOOTH_HC_RECEIVE_SCO_DATA),
    ("AsyncReceiveSCOData", EFI_BLUETOOTH_HC_ASYNC_RECEIVE_SCO_DATA)
  ]

