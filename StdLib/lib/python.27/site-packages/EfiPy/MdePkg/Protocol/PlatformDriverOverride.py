#
# PlatformDriverOverride.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PlatformDriverOverride.py is free software: you can redistribute it and/or
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

gEfiPlatformDriverOverrideProtocolGuid  = \
  EFI_GUID (0x6b30c738, 0xa391, 0x11d4, (0x9a, 0x3b, 0x00, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL), # IN *This
  EFI_HANDLE,                                     # IN ControllerHandle
  POINTER(EFI_HANDLE)                             # IN OUT
  )

EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL), # IN *This
  EFI_HANDLE,                                     # IN ControllerHandle
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))      # IN OUT **DriverImagePath
  )

EFI_PLATFORM_DRIVER_OVERRIDE_DRIVER_LOADED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL), # IN *This
  EFI_HANDLE,                                     # IN ControllerHandle
  POINTER(EFI_DEVICE_PATH_PROTOCOL),              # IN *DriverImagePath,
  EFI_HANDLE                                      # IN DriverImagePath
  )

EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL._fields_ = [
    ("GetDriver",     EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER),
    ("GetDriverPath", EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER_PATH),
    ("DriverLoaded",  EFI_PLATFORM_DRIVER_OVERRIDE_DRIVER_LOADED)
  ]

