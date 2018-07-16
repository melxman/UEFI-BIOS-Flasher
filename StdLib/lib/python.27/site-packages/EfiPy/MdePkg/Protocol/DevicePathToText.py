#
# DevicePathToText.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DevicePathToText.py is free software: you can redistribute it and/or
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

gEfiDevicePathToTextProtocolGuid        = \
  EFI_GUID (0x8b843e20, 0x8132, 0x4852, (0x90, 0xcc, 0x55, 0x1a, 0x4e, 0x4a, 0x7f, 0x1c ))

EFI_DEVICE_PATH_TO_TEXT_NODE = CFUNCTYPE (
  PCHAR16,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *DeviceNode
  BOOLEAN,                              # IN DisplayOnly,
  BOOLEAN                               # IN AllowShortcuts
  )

EFI_DEVICE_PATH_TO_TEXT_PATH = CFUNCTYPE (
  PCHAR16,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *DeviceNode
  BOOLEAN,                              # IN DisplayOnly,
  BOOLEAN                               # IN AllowShortcuts
  )

class EFI_DEVICE_PATH_TO_TEXT_PROTOCOL (Structure):
  _fields_ = [
    ("ConvertDeviceNodeToText",  EFI_DEVICE_PATH_TO_TEXT_NODE),
    ("ConvertDevicePathToText",  EFI_DEVICE_PATH_TO_TEXT_PATH)
  ]

