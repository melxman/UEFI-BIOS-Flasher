#
# BluetoothConfig.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BluetoothConfig.py is free software: you can redistribute it and/or
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
gEfiBluetoothConfigProtocolGuid     = \
  EFI_GUID (0x62960cf3, 0x40ff, 0x4263, ( 0xa7, 0x7c, 0xdf, 0xde, 0xbd, 0x19, 0x1b, 0x4b ))

class EFI_BLUETOOTH_CONFIG_PROTOCOL (Structure):
  pass

EFI_BLUETOOTH_CONFIG_REMOTE_DEVICE_STATE_TYPE         = UINT32
EFI_BLUETOOTH_CONFIG_REMOTE_DEVICE_STATE_CONNECTED    = 0x1
EFI_BLUETOOTH_CONFIG_REMOTE_DEVICE_STATE_PAIRED       = 0x2

class EFI_BLUETOOTH_SCAN_CALLBACK_INFORMATION (Structure):
  _fields_ = [
    ("BDAddr",            Bluetooth.BLUETOOTH_ADDRESS),
    ("RemoteDeviceState", UINT8),
    ("ClassOfDevice",     Bluetooth.BLUETOOTH_CLASS_OF_DEVICE),
    ("RemoteDeviceName",  UINT8 * Bluetooth.BLUETOOTH_HCI_COMMAND_LOCAL_READABLE_NAME_MAX_SIZE)
  ]

EfiBluetoothConfigDataTypeDeviceName                        = 0
EfiBluetoothConfigDataTypeClassOfDevice                     = 1
EfiBluetoothConfigDataTypeRemoteDeviceState                 = 2
EfiBluetoothConfigDataTypeSdpInfo                           = 3
EfiBluetoothConfigDataTypeBDADDR                            = 4
EfiBluetoothConfigDataTypeDiscoverable                      = 5
EfiBluetoothConfigDataTypeControllerStoredPairedDeviceList  = 6
EfiBluetoothConfigDataTypeAvailableDeviceList               = 7
EfiBluetoothConfigDataTypeMax                               = 8
EFI_BLUETOOTH_CONFIG_DATA_TYPE                              = ENUM

EfiBluetoothCallbackTypeUserPasskeyNotification = 0
EfiBluetoothCallbackTypeUserConfirmationRequest = 1
EfiBluetoothCallbackTypeOOBDataRequest          = 2
EfiBluetoothCallbackTypePinCodeRequest          = 3
EfiBluetoothCallbackTypeMax                     = 4
EFI_BLUETOOTH_PIN_CALLBACK_TYPE                 = ENUM

EfiBluetoothConnCallbackTypeDisconnected      = 0
EfiBluetoothConnCallbackTypeConnected         = 1
EfiBluetoothConnCallbackTypeAuthenticated     = 2
EfiBluetoothConnCallbackTypeEncrypted         = 3
EFI_BLUETOOTH_CONNECT_COMPLETE_CALLBACK_TYPE  = ENUM

EFI_BLUETOOTH_CONFIG_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_CONFIG_PROTOCOL)  # IN *This
  )

EFI_BLUETOOTH_CONFIG_SCAN_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),          # IN *This
  PVOID,                                            # IN *Context
  POINTER (EFI_BLUETOOTH_SCAN_CALLBACK_INFORMATION) # IN *CallbackInfo
  )

EFI_BLUETOOTH_CONFIG_SCAN = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),          # IN *This
  BOOLEAN,                                          # IN ReScan,
  UINT8,                                            # IN ScanType,
  EFI_BLUETOOTH_CONFIG_SCAN_CALLBACK_FUNCTION,      # IN Callback,
  PVOID                                             # IN *Context
  )

EFI_BLUETOOTH_CONFIG_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),          # IN *This
  POINTER (Bluetooth.BLUETOOTH_ADDRESS)             # IN *BD_ADDR
  )

EFI_BLUETOOTH_CONFIG_DISCONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),          # IN *This
  POINTER (Bluetooth.BLUETOOTH_ADDRESS),            # IN *BD_ADDR
  UINT8                                             # IN Reason
  )

EFI_BLUETOOTH_CONFIG_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),          # IN     *This
  EFI_BLUETOOTH_CONFIG_DATA_TYPE,                   # IN     DataType,
  POINTER (UINTN),                                  # IN OUT *DataSize,
  PVOID                                             # IN OUT *Data
  )

EFI_BLUETOOTH_CONFIG_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),  # IN *This
  EFI_BLUETOOTH_CONFIG_DATA_TYPE,           # IN DataType,
  UINTN,                                    # IN DataSize,
  PVOID                                     # IN *Data
  )

EFI_BLUETOOTH_CONFIG_GET_REMOTE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),  # IN      *This
  EFI_BLUETOOTH_CONFIG_DATA_TYPE,           # IN      DataType,
  Bluetooth.BLUETOOTH_ADDRESS,              # IN      BDAddr,
  POINTER (UINTN),                          # IN OUT  *DataSize,
  PVOID                                     # IN OUT  *Data
  )

EFI_BLUETOOTH_CONFIG_REGISTER_PIN_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),  # IN  *This
  PVOID,                                    # IN  *Context,
  EFI_BLUETOOTH_PIN_CALLBACK_TYPE,          # IN  CallbackType,
  PVOID,                                    # IN  *InputBuffer,
  UINTN,                                    # IN  InputBufferSize,
  POINTER (PVOID),                          # OUT **OutputBuffer,
  POINTER (UINTN)                           # OUT *OutputBufferSize
  )

EFI_BLUETOOTH_CONFIG_REGISTER_PIN_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),              # IN  *This
  EFI_BLUETOOTH_CONFIG_REGISTER_PIN_CALLBACK_FUNCTION,  # IN  Callback,
  PVOID                                                 # IN  *Context
  )

EFI_BLUETOOTH_CONFIG_REGISTER_GET_LINK_KEY_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),              # IN  *This
  PVOID,                                                # IN  *Context
  POINTER (Bluetooth.BLUETOOTH_ADDRESS),                # IN  *BDAddr,
  UINT8 * Bluetooth.BLUETOOTH_HCI_LINK_KEY_SIZE         # OUT  LinkKey
  )

EFI_BLUETOOTH_CONFIG_REGISTER_GET_LINK_KEY_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),                      # IN  *This
  EFI_BLUETOOTH_CONFIG_REGISTER_GET_LINK_KEY_CALLBACK_FUNCTION, # IN  Callback
  PVOID                                                         # IN  *Context
  )

EFI_BLUETOOTH_CONFIG_REGISTER_SET_LINK_KEY_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),      # IN  *This
  PVOID,                                        # IN  *Context
  POINTER (Bluetooth.BLUETOOTH_ADDRESS),        # IN  *BDAddr,
  UINT8 * Bluetooth.BLUETOOTH_HCI_LINK_KEY_SIZE # IN   LinkKey
  )

EFI_BLUETOOTH_CONFIG_REGISTER_SET_LINK_KEY_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),                      # IN *This
  EFI_BLUETOOTH_CONFIG_REGISTER_SET_LINK_KEY_CALLBACK_FUNCTION, # IN Callback,
  PVOID                                                         # IN *Context
  )

EFI_BLUETOOTH_CONFIG_REGISTER_CONNECT_COMPLETE_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),      # IN  *This
  PVOID,                                        # IN  *Context
  EFI_BLUETOOTH_CONNECT_COMPLETE_CALLBACK_TYPE, # IN  CallbackType,
  POINTER (Bluetooth.BLUETOOTH_ADDRESS),        # IN  *BDAddr,
  PVOID,                                        # IN  *InputBuffer,
  UINTN                                         # IN  InputBufferSize
  )

EFI_BLUETOOTH_CONFIG_REGISTER_CONNECT_COMPLETE_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_CONFIG_PROTOCOL),                          # IN  *This
  EFI_BLUETOOTH_CONFIG_REGISTER_CONNECT_COMPLETE_CALLBACK_FUNCTION, # IN  Callback,
  PVOID                                                             # IN  *Context
  )

EFI_BLUETOOTH_CONFIG_PROTOCOL._fields_ = [
    ("Init",                                EFI_BLUETOOTH_CONFIG_INIT),
    ("Scan",                                EFI_BLUETOOTH_CONFIG_SCAN),
    ("Connect",                             EFI_BLUETOOTH_CONFIG_CONNECT),
    ("Disconnect",                          EFI_BLUETOOTH_CONFIG_DISCONNECT),
    ("GetData",                             EFI_BLUETOOTH_CONFIG_GET_DATA),
    ("SetData",                             EFI_BLUETOOTH_CONFIG_SET_DATA),
    ("GetRemoteData",                       EFI_BLUETOOTH_CONFIG_GET_REMOTE_DATA),
    ("RegisterPinCallback",                 EFI_BLUETOOTH_CONFIG_REGISTER_PIN_CALLBACK),
    ("RegisterGetLinkKeyCallback",          EFI_BLUETOOTH_CONFIG_REGISTER_GET_LINK_KEY_CALLBACK),
    ("RegisterSetLinkKeyCallback",          EFI_BLUETOOTH_CONFIG_REGISTER_SET_LINK_KEY_CALLBACK),
    ("RegisterLinkConnectCompleteCallback", EFI_BLUETOOTH_CONFIG_REGISTER_CONNECT_COMPLETE_CALLBACK)
  ]

