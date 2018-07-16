#
# UsbHostController.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UsbHostController.py is free software: you can redistribute it and/or
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

import UsbIo
import Usb2HostController

gEfiUsbHcProtocolGuid = \
  EFI_GUID (0xf5089266, 0x1aa0, 0x4953, (0x97, 0xd8, 0x56, 0x2f, 0x8a, 0x73, 0xb5, 0x19 ))

class EFI_USB_HC_PROTOCOL (Structure):
  pass

EFI_USB_HC_PROTOCOL_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),   # IN  *This
  UINT16                          # IN  Attributes
  )

EFI_USB_HC_PROTOCOL_GET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),                 # IN      *This
  POINTER(Usb2HostController.EFI_USB_HC_STATE)  #    OUT  *State
  )

EFI_USB_HC_PROTOCOL_SET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),         # IN      *This
  Usb2HostController.EFI_USB_HC_STATE   # IN      State
  )

EFI_USB_HC_PROTOCOL_CONTROL_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),         # IN      *This
  UINT8,                                # IN      DeviceAddress,
  BOOLEAN,                              # IN      IsSlowDevice,
  UINT8,                                # IN      MaximumPacketLength,
  POINTER(UsbIo.EFI_USB_DEVICE_REQUEST),# IN      *Request,
  UsbIo.EFI_USB_DATA_DIRECTION,         # IN      TransferDirection,
  PVOID,                                # IN OUT  *Data       OPTIONAL,
  POINTER(UINTN),                       # IN OUT  *DataLength OPTIONAL,
  UINTN,                                # IN      TimeOut,
  POINTER(UINT32)                       # OUT     *TransferResult
  )

EFI_USB_HC_PROTOCOL_BULK_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),   # IN      *This
  UINT8,                          # IN      DeviceAddress,
  UINT8,                          # IN      EndPointAddress,
  UINT8,                          # IN      MaximumPacketLength,
  PVOID,                          # IN OUT  *Data,
  POINTER(UINTN),                 # IN OUT  *DataLength,
  UINT8,                          # IN OUT  *DataToggle,
  UINTN,                          # IN      TimeOut,
  POINTER(UINT32)                 # OUT     *TransferResult
  )

EFI_USB_HC_PROTOCOL_ASYNC_INTERRUPT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),         # IN      *This
  UINT8,                                # IN      DeviceAddress,
  UINT8,                                # IN      EndPointAddress,
  BOOLEAN,                              # IN      IsSlowDevice,
  UINT8,                                # IN      MaximumPacketLength,
  BOOLEAN,                              # IN      IsNewTransfer
  UINT8,                                # IN OUT  *DataToggle,
  UINTN,                                # IN      PollingInterval  OPTIONAL,
  UINTN,                                # IN      DataLength       OPTIONAL,
  UsbIo.EFI_ASYNC_USB_TRANSFER_CALLBACK,# IN      CallBackFunction OPTIONAL,
  PVOID                                 # IN      *Context         OPTIONAL
  )

EFI_USB_HC_PROTOCOL_SYNC_INTERRUPT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),   # IN      *This
  UINT8,                          # IN      DeviceAddress,
  UINT8,                          # IN      EndPointAddress,
  BOOLEAN,                        # IN      IsSlowDevice,
  UINT8,                          # IN      MaximumPacketLength,
  PVOID,                          # IN OUT  *Data,
  POINTER(UINTN),                 # IN OUT  *DataLength,
  POINTER(UINT8),                 # IN OUT  *DataToggle,
  UINTN,                          # IN      TimeOut,
  POINTER(UINT32)                 # OUT     *TransferResult
  )

EFI_USB_HC_PROTOCOL_ISOCHRONOUS_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),   # IN      *This
  UINT8,                          # IN      DeviceAddress,
  UINT8,                          # IN      EndPointAddress,
  UINT8,                          # IN      MaximumPacketLength,
  PVOID,                          # IN OUT  *Data,
  UINTN,                          # IN      DataLength,
  POINTER(UINT32)                 # OUT     *TransferResult
  )

EFI_USB_HC_PROTOCOL_ASYNC_ISOCHRONOUS_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),         # IN      *This
  UINT8,                                # IN      DeviceAddress,
  UINT8,                                # IN      EndPointAddress,
  UINT8,                                # IN      MaximumPacketLength,
  PVOID,                                # IN OUT  *Data,
  UINTN,                                # IN      DataLength,
  UsbIo.EFI_ASYNC_USB_TRANSFER_CALLBACK,# IN      IsochronousCallBack,
  PVOID                                 # IN      *Context OPTIONAL
  )

EFI_USB_HC_PROTOCOL_GET_ROOTHUB_PORT_NUMBER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),   # IN      *This
  POINTER(UINT8)                  #     OUT *PortNumber
  )

EFI_USB_HC_PROTOCOL_GET_ROOTHUB_PORT_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),           # IN      *This
  UINT8,                                  # IN      PortNumber
  Usb2HostController.EFI_USB_PORT_STATUS  #     OUT *PortStatus
  )

EFI_USB_HC_PROTOCOL_SET_ROOTHUB_PORT_FEATURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),           # IN      *This
  UINT8,                                  # IN      PortNumber
  Usb2HostController.EFI_USB_PORT_FEATURE # IN      PortFeature
  )

EFI_USB_HC_PROTOCOL_CLEAR_ROOTHUB_PORT_FEATURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_HC_PROTOCOL),           # IN      *This
  UINT8,                                  # IN      PortNumber
  Usb2HostController.EFI_USB_PORT_FEATURE # IN      PortFeature
  )

EFI_USB_HC_PROTOCOL._fields_ = [
    ("Reset",                     EFI_USB_HC_PROTOCOL_RESET),
    ("GetState",                  EFI_USB_HC_PROTOCOL_GET_STATE),
    ("SetState",                  EFI_USB_HC_PROTOCOL_SET_STATE),
    ("ControlTransfer",           EFI_USB_HC_PROTOCOL_CONTROL_TRANSFER),
    ("BulkTransfer",              EFI_USB_HC_PROTOCOL_BULK_TRANSFER),
    ("AsyncInterruptTransfer",    EFI_USB_HC_PROTOCOL_ASYNC_INTERRUPT_TRANSFER),
    ("SyncInterruptTransfer",     EFI_USB_HC_PROTOCOL_SYNC_INTERRUPT_TRANSFER),
    ("IsochronousTransfer",       EFI_USB_HC_PROTOCOL_ISOCHRONOUS_TRANSFER),
    ("AsyncIsochronousTransfer",  EFI_USB_HC_PROTOCOL_ASYNC_ISOCHRONOUS_TRANSFER),
    ("GetRootHubPortNumber",      EFI_USB_HC_PROTOCOL_GET_ROOTHUB_PORT_NUMBER),
    ("GetRootHubPortStatus",      EFI_USB_HC_PROTOCOL_GET_ROOTHUB_PORT_STATUS),
    ("SetRootHubPortFeature",     EFI_USB_HC_PROTOCOL_SET_ROOTHUB_PORT_FEATURE),
    ("ClearRootHubPortFeature",   EFI_USB_HC_PROTOCOL_CLEAR_ROOTHUB_PORT_FEATURE),
    ("MajorRevision",             UINT16),
    ("MinorRevision",             UINT16)
  ]

