#
# DevicePathUtilities.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DevicePathUtilities.py is free software: you can redistribute it and/or
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

gEfiDevicePathUtilitiesProtocolGuid     = \
  EFI_GUID (0x379be4e, 0xd706, 0x437d, (0xb0, 0x37, 0xed, 0xb8, 0x2f, 0xb7, 0x72, 0xa4 ))

EFI_DEVICE_PATH_UTILS_GET_DEVICE_PATH_SIZE = CFUNCTYPE (
  UINTN,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN *DevicePath
  )

EFI_DEVICE_PATH_UTILS_DUP_DEVICE_PATH = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN *DevicePath
  )

EFI_DEVICE_PATH_UTILS_APPEND_PATH = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *Src1
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN *Src2
  )

EFI_DEVICE_PATH_UTILS_APPEND_NODE = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *DevicePath
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN *DeviceNode
  )

EFI_DEVICE_PATH_UTILS_APPEND_INSTANCE = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *DevicePath
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN *DevicePathInstance
  )

EFI_DEVICE_PATH_UTILS_GET_NEXT_INSTANCE = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL)), # IN **DevicePathInstance
  POINTER(UINTN)                              # IN *DevicePathInstanceSize
  )

EFI_DEVICE_PATH_UTILS_CREATE_NODE = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  UINT8,                              # IN NodeType,
  UINT8,                              # IN NodeSubType, 
  UINT16                              # IN NodeLength   
  )

EFI_DEVICE_PATH_UTILS_IS_MULTI_INSTANCE = CFUNCTYPE (
  BOOLEAN,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)
  )

class EFI_DEVICE_PATH_UTILITIES_PROTOCOL (Structure):
  _fields_ = [
    ("GetDevicePathSize",         EFI_DEVICE_PATH_UTILS_GET_DEVICE_PATH_SIZE),
    ("DuplicateDevicePath",       EFI_DEVICE_PATH_UTILS_DUP_DEVICE_PATH),
    ("AppendDevicePath",          EFI_DEVICE_PATH_UTILS_APPEND_PATH),
    ("AppendDeviceNode",          EFI_DEVICE_PATH_UTILS_APPEND_NODE),
    ("AppendDevicePathInstance",  EFI_DEVICE_PATH_UTILS_APPEND_INSTANCE),
    ("GetNextDevicePathInstance", EFI_DEVICE_PATH_UTILS_GET_NEXT_INSTANCE),
    ("IsDevicePathMultiInstance", EFI_DEVICE_PATH_UTILS_IS_MULTI_INSTANCE),
    ("CreateDeviceNode",          EFI_DEVICE_PATH_UTILS_CREATE_NODE)
  ]

