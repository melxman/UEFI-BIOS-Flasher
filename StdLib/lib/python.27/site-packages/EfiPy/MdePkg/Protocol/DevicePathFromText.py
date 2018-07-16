#
# DevicePathFromText.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DevicePathFromText.py is free software: you can redistribute it and/or
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

gEfiDevicePathFromTextProtocolGuid      = \
  EFI_GUID (0x5c99a21, 0xc70f, 0x4ad2, (0x8a, 0x5f, 0x35, 0xdf, 0x33, 0x43, 0xf5, 0x1e  ))

EFI_DEVICE_PATH_FROM_TEXT_NODE = CFUNCTYPE (
  POINTER (EFI_DEVICE_PATH_PROTOCOL),
  PCHAR16                             # IN *TextDeviceNode
  )

EFI_DEVICE_PATH_FROM_TEXT_PATH = CFUNCTYPE (
  POINTER (EFI_DEVICE_PATH_PROTOCOL),
  PCHAR16                             # IN *TextDeviceNode
  )

class EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL (Structure):
  _fields_ = [
    ("ConvertTextToDeviceNode",  EFI_DEVICE_PATH_FROM_TEXT_NODE),
    ("ConvertTextToDevicePath",  EFI_DEVICE_PATH_FROM_TEXT_PATH)
  ]

