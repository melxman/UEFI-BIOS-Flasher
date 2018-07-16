#
# BootManagerPolicy.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# BootManagerPolicy.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH

gEfiBootManagerPolicyProtocolGuid       = \
  EFI_GUID (0xFEDF8E0C, 0xE147, 0x11E3, ( 0x99, 0x03, 0xB8, 0xE8, 0x56, 0x2C, 0xBA, 0xFA ))

gEfiBootManagerPolicyConsoleGuid        = \
  EFI_GUID (0xCAB0E94C, 0xE15F, 0x11E3, ( 0x91, 0x8D, 0xB8, 0xE8, 0x56, 0x2C, 0xBA, 0xFA ))

gEfiBootManagerPolicyNetworkGuid        = \
  EFI_GUID (0xD04159DC, 0xE15F, 0x11E3, ( 0xB2, 0x61, 0xB8, 0xE8, 0x56, 0x2C, 0xBA, 0xFA ))

gEfiBootManagerPolicyConnectAllGuid     = \
  EFI_GUID (0x113B2126, 0xFC8A, 0x11E3, ( 0xBD, 0x6C, 0xB8, 0xE8, 0x56, 0x2C, 0xBA, 0xFA ))

class EFI_BOOT_MANAGER_POLICY_PROTOCOL (Structure):
  pass

EFI_BOOT_MANAGER_POLICY_PROTOCOL_REVISION = 0x00010000

EFI_BOOT_MANAGER_POLICY_CONNECT_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BOOT_MANAGER_POLICY_PROTOCOL),  # IN *This
  POINTER(EFI_DEVICE_PATH),                   # IN *DevicePath
  BOOLEAN                                     # IN Recursive,
  )

EFI_BOOT_MANAGER_POLICY_CONNECT_DEVICE_CLASS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BOOT_MANAGER_POLICY_PROTOCOL),  # IN *This
  POINTER(EFI_GUID)                           # IN *Class
  )

EFI_BOOT_MANAGER_POLICY_PROTOCOL._fields_ = [
    ("Revision",            UINT64),
    ("ConnectDevicePath",   EFI_BOOT_MANAGER_POLICY_CONNECT_DEVICE_PATH),
    ("ConnectDeviceClass",  EFI_BOOT_MANAGER_POLICY_CONNECT_DEVICE_CLASS)
  ]

