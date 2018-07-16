#
# DeferredImageLoad.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DeferredImageLoad.py is free software: you can redistribute it and/or
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

gEfiDeferredImageLoadProtocolGuid   = \
  EFI_GUID (0x15853d7c, 0x3ddf, 0x43e0, ( 0xa1, 0xcb, 0xeb, 0xf8, 0x5b, 0x8f, 0x87, 0x2c ))

class EFI_DEFERRED_IMAGE_LOAD_PROTOCOL (Structure):
  pass

EFI_DEFERRED_IMAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEFERRED_IMAGE_LOAD_PROTOCOL),    # IN      *This
  UINTN,                                        # IN      ImageIndex
  POINTER (POINTER (EFI_DEVICE_PATH_PROTOCOL)), #    OUT  **ImageDevicePath,
  POINTER(PVOID),                               #    OUT  **Image,
  POINTER(UINTN),                               #    OUT  *ImageSize
  POINTER(BOOLEAN)                              #    OUT  *BootOption
  )

EFI_DEFERRED_IMAGE_LOAD_PROTOCOL._fields_ = [
    ("GetImageInfo",  EFI_DEFERRED_IMAGE_INFO)
  ]

