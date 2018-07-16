#
# BluetoothIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BluetoothIo.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard  import Bluetooth

gEfiBluetoothIoServiceBindingProtocolGuid = \
  EFI_GUID (0x388278d3, 0x7b85, 0x42f0, ( 0xab, 0xa9, 0xfb, 0x4b, 0xfd, 0x69, 0xf5, 0xab   ))

gEfiBluetoothIoProtocolGuid               = \
  EFI_GUID (0x467313de, 0x4e30, 0x43f1, ( 0x94, 0x3e, 0x32, 0x3f, 0x89, 0x84, 0x5d, 0xb5  ))

class EFI_BLUETOOTH_IO_PROTOCOL (Structure):
  pass

class EFI_BLUETOOTH_DEVICE_INFO (Structure):
  _fields_ = [
    ("Version",                 UINT32),
    ("BD_ADDR",                 Bluetooth.BLUETOOTH_ADDRESS),
    ("PageScanRepetitionMode",  UINT8),
    ("ClassOfDevice",           Bluetooth.BLUETOOTH_CLASS_OF_DEVICE),
    ("ClockOffset",             UINT16),
    ("RSSI",                    UINT8),
    ("ExtendedInquiryResponse", UINT8 * 240)
  ]

EFI_BLUETOOTH_IO_GET_DEVICE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_IO_PROTOCOL), # IN     *This
  POINTER (UINTN),                    #    OUT *DeviceInfoSize,
  POINTER (PVOID)                     #    OUT **DeviceInfo
  )

EFI_BLUETOOTH_IO_GET_SDP_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_IO_PROTOCOL), # IN     *This
  POINTER(UINTN),                     #    OUT *SdpInfoSize,
  POINTER(PVOID)                      #    OUT **SdpInfo
  )

EFI_BLUETOOTH_IO_L2CAP_RAW_SEND = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),  # IN     *This
  POINTER (UINTN),                      # IN OUT *BufferSize,
  PVOID,                                # IN     *Buffer,
  UINTN                                 # IN     Timeout
  )

EFI_BLUETOOTH_IO_L2CAP_RAW_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),  # IN     *This
  POINTER (UINTN),                      # IN OUT *BufferSize,
  PVOID,                                #    OUT *Buffer,
  UINTN                                 # IN     Timeout
  )

EFI_BLUETOOTH_IO_ASYNC_FUNC_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  UINT16,                         # IN ChannelID,
  PVOID,                          # IN *Data,
  UINTN,                          # IN DataLength,
  PVOID                           # IN *Context
  )

EFI_BLUETOOTH_IO_L2CAP_RAW_ASYNC_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),  # IN *This,
  BOOLEAN,                              # IN IsNewTransfer,
  UINTN,                                # IN PollingInterval,
  UINTN,                                # IN DataLength,
  EFI_BLUETOOTH_IO_ASYNC_FUNC_CALLBACK, # IN Callback,
  PVOID                                 # IN *Context
  )

EFI_BLUETOOTH_IO_L2CAP_SEND = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),  # IN      *This,
  EFI_HANDLE,                           # IN      Handle,
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                # IN      *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_IO_L2CAP_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),  # IN      *This,
  EFI_HANDLE,                           # IN      Handle,
  POINTER (UINTN),                      #    OUT  *BufferSize,
  POINTER (PVOID),                      #    OUT  **Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_IO_CHANNEL_SERVICE_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  PVOID,             # IN *Data,
  UINTN,             # IN DataLength,
  PVOID              # IN *Context
  )

EFI_BLUETOOTH_IO_L2CAP_ASYNC_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),        # IN *This,
  EFI_HANDLE,                                 # IN Handle,
  EFI_BLUETOOTH_IO_CHANNEL_SERVICE_CALLBACK,  # IN Callback,
  PVOID                                       # IN *Context
  )

EFI_BLUETOOTH_IO_L2CAP_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),        # IN     *This,
  POINTER (EFI_HANDLE),                       #    OUT *Handle,
  UINT16,                                     # IN      Psm,
  UINT16,                                     # IN      Mtu,
  EFI_BLUETOOTH_IO_CHANNEL_SERVICE_CALLBACK,  # IN      Callback,
  PVOID                                       # IN      *Context
  )

EFI_BLUETOOTH_IO_L2CAP_DISCONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),        # IN *This,
  EFI_HANDLE                                  # IN Handle
  )

EFI_BLUETOOTH_IO_L2CAP_REGISTER_SERVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_IO_PROTOCOL),        # IN     *This,
  POINTER (EFI_HANDLE),                       #    OUT *Handle,
  UINT16,                                     # IN     Psm,
  UINT16,                                     # IN     Mtu,
  EFI_BLUETOOTH_IO_CHANNEL_SERVICE_CALLBACK,  # IN     Callback,
  PVOID                                       # IN     *Context
  )

EFI_BLUETOOTH_IO_PROTOCOL._fields_ = [
    ("GetDeviceInfo",         EFI_BLUETOOTH_IO_GET_DEVICE_INFO),
    ("GetSdpInfo",            EFI_BLUETOOTH_IO_GET_SDP_INFO),
    ("L2CapRawSend",          EFI_BLUETOOTH_IO_L2CAP_RAW_SEND),
    ("L2CapRawReceive",       EFI_BLUETOOTH_IO_L2CAP_RAW_RECEIVE),
    ("L2CapRawAsyncReceive",  EFI_BLUETOOTH_IO_L2CAP_RAW_ASYNC_RECEIVE),
    ("L2CapSend",             EFI_BLUETOOTH_IO_L2CAP_SEND),
    ("L2CapReceive",          EFI_BLUETOOTH_IO_L2CAP_RECEIVE),
    ("L2CapAsyncReceive",     EFI_BLUETOOTH_IO_L2CAP_ASYNC_RECEIVE),
    ("L2CapConnect",          EFI_BLUETOOTH_IO_L2CAP_CONNECT),
    ("L2CapDisconnect",       EFI_BLUETOOTH_IO_L2CAP_DISCONNECT),
    ("L2CapRegisterService",  EFI_BLUETOOTH_IO_L2CAP_REGISTER_SERVICE)
  ]

