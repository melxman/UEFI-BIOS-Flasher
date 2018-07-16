#
# DriverConfiguration.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DriverConfiguration.py is free software: you can redistribute it and/or
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


import DriverConfiguration2

gEfiDriverConfigurationProtocolGuid     = \
  EFI_GUID (0x107a772b, 0xd5e1, 0x11d4, (0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_DRIVER_CONFIGURATION_PROTOCOL (Structure):
  pass

EFI_DRIVER_CONFIGURATION_SET_OPTIONS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION_PROTOCOL),       # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE,                                       # IN  ChildHandle  OPTIONAL,
  PCHAR8,                                           # IN  *Language,
  POINTER(DriverConfiguration2.EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED) # OUT *ActionRequired
  )

EFI_DRIVER_CONFIGURATION_OPTIONS_VALID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION_PROTOCOL),       # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE                                        # IN  ChildHandle  OPTIONAL,
  )

EFI_DRIVER_CONFIGURATION_FORCE_DEFAULTS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION_PROTOCOL),       # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE,                                       # IN  ChildHandle  OPTIONAL,
  UINT32,                                           # IN  DefaultType,
  POINTER(DriverConfiguration2.EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED) # OUT *ActionRequired
  )

EFI_DRIVER_CONFIGURATION_PROTOCOL._fields_ = [
    ("SetOptions",          EFI_DRIVER_CONFIGURATION_SET_OPTIONS),
    ("OptionsValid",        EFI_DRIVER_CONFIGURATION_OPTIONS_VALID),
    ("ForceDefaults",       EFI_DRIVER_CONFIGURATION_FORCE_DEFAULTS),
    ("SupportedLanguages",  PCHAR8)
  ]

