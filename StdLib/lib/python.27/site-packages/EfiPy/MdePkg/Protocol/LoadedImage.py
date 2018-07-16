#
# LoadedImage.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# LoadedImage.py is free software: you can redistribute it and/or
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

gEfiLoadedImageProtocolGuid           = \
  EFI_GUID (0x5B1B31A1, 0x9562, 0x11d2, (0x8E, 0x3F, 0x00, 0xA0, 0xC9, 0x69, 0x72, 0x3B ))

gEfiLoadedImageDevicePathProtocolGuid = \
  EFI_GUID (0xbc62157e, 0x3e33, 0x4fec, (0x99, 0x20, 0x2d, 0x3b, 0x36, 0xd7, 0x50, 0xdf ))

EFI_LOADED_IMAGE_PROTOCOL_REVISION  = 0x1000

class EFI_LOADED_IMAGE_PROTOCOL (Structure):
  _fields_ = [
    ("Revision",        UINT32),
    ("ParentHandle",    EFI_HANDLE),
    ("SystemTable",     POINTER (EFI_SYSTEM_TABLE)),
    ("DeviceHandle",    EFI_HANDLE),
    ("FilePath",        POINTER (EFI_DEVICE_PATH_PROTOCOL)),
    ("Reserved",        PVOID),
    ("LoadOptionsSize", UINT32),
    ("LoadOptions",     PVOID),
    ("ImageBase",       PVOID),
    ("ImageSize",       UINT64),
    ("ImageCodeType",   EFI_MEMORY_TYPE),
    ("ImageDataType",   EFI_MEMORY_TYPE),
    ("Unload",          EFI_IMAGE_UNLOAD)
  ]

