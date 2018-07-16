#
# DriverBinding.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DriverBinding.py is free software: you can redistribute it and/or
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

gEfiDriverBindingProtocolGuid           = \
  EFI_GUID (0x18a031ab, 0xb443, 0x4d1a, (0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71 ))

class EFI_DRIVER_BINDING_PROTOCOL (Structure):
  pass

EFI_DRIVER_BINDING_SUPPORTED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_BINDING_PROTOCOL), # IN  *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN  *RemainingDevicePath OPTIONAL
  )

EFI_DRIVER_BINDING_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_BINDING_PROTOCOL), # IN  *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN  *RemainingDevicePath OPTIONAL
  )

EFI_DRIVER_BINDING_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_BINDING_PROTOCOL), # IN  *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  UINTN,                                # IN  NumberOfChildren,
  POINTER(EFI_HANDLE)                   # IN  *ChildHandleBuffer OPTIONAL
  )

EFI_DRIVER_BINDING_PROTOCOL._fields_ = [
    ("Supported",           EFI_DRIVER_BINDING_SUPPORTED),
    ("Start",               EFI_DRIVER_BINDING_START),
    ("Stop",                EFI_DRIVER_BINDING_STOP),
    ("Version",             UINT32),
    ("ImageHandle",         EFI_HANDLE),
    ("DriverBindingHandle", EFI_HANDLE)
  ]

