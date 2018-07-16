#
# SmbusHc.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SmbusHc.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard  import SmBus

gEfiSmbusHcProtocolGuid     = \
  EFI_GUID (0xe49d33ed, 0x513d, 0x4634, ( 0xb6, 0x98, 0x6f, 0x55, 0xaa, 0x75, 0x1c, 0x1b))

class EFI_SMBUS_HC_PROTOCOL (Structure):
  pass

EFI_SMBUS_HC_EXECUTE_OPERATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),       # IN      *This
  SmBus.EFI_SMBUS_DEVICE_ADDRESS,       # IN      SlaveAddress,
  SmBus.EFI_SMBUS_DEVICE_COMMAND,       # IN      Command,
  SmBus.EFI_SMBUS_OPERATION,            # IN      Operation,
  BOOLEAN,                              # IN      PecCheck,
  POINTER(UINTN),                       # IN OUT  *Length,
  PVOID                                 # IN OUT  *Buffer
  )

EFI_SMBUS_HC_PROTOCOL_ARP_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),         # IN      *This
  BOOLEAN,                                # IN      ArpAll,
  POINTER(SmBus.EFI_SMBUS_UDID),          # IN      *SmbusUdid,   OPTIONAL
  POINTER(SmBus.EFI_SMBUS_DEVICE_ADDRESS) # IN OUT  *SlaveAddress OPTIONAL
  )

EFI_SMBUS_HC_PROTOCOL_GET_ARP_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),               # IN      *This
  POINTER(UINTN),                               # IN OUT  *Length,
  POINTER(POINTER(SmBus.EFI_SMBUS_DEVICE_MAP))  # IN OUT  **SmbusDeviceMap
  )

EFI_SMBUS_NOTIFY_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(SmBus.EFI_SMBUS_DEVICE_ADDRESS),  # IN  SlaveAddress,
  UINTN                                     # IN  Data
  )

EFI_SMBUS_HC_PROTOCOL_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),       # IN  *This,
  SmBus.EFI_SMBUS_DEVICE_ADDRESS,       # IN  SlaveAddress,
  UINTN,                                # IN  Data,
  EFI_SMBUS_NOTIFY_FUNCTION             # IN  NotifyFunction
  )

EFI_SMBUS_HC_PROTOCOL._fields_ = [
    ("Execute",   EFI_SMBUS_HC_EXECUTE_OPERATION),
    ("ArpDevice", EFI_SMBUS_HC_PROTOCOL_ARP_DEVICE),
    ("GetArpMap", EFI_SMBUS_HC_PROTOCOL_GET_ARP_MAP),
    ("Notify",    EFI_SMBUS_HC_PROTOCOL_NOTIFY)
  ]

