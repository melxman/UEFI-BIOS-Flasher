#
# ComponentName.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ComponentName.py is free software: you can redistribute it and/or
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

gEfiComponentNameProtocolGuid           = \
  EFI_GUID (0x107a772c, 0xd5e1, 0x11d4, (0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_COMPONENT_NAME_PROTOCOL (Structure):
  pass

EFI_COMPONENT_NAME_GET_DRIVER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME_PROTOCOL), # IN *This
  PCHAR8,                               # IN *Language
  POINTER (PCHAR16)                     # IN **DriverName
  )

EFI_COMPONENT_NAME_GET_CONTROLLER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME_PROTOCOL), # IN *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  EFI_HANDLE,                           # IN  ChildHandle        OPTIONAL,
  PCHAR8,                               # IN *Language
  POINTER (PCHAR16)                     # IN **ControllerName
  )

EFI_COMPONENT_NAME_PROTOCOL._fields_ = [
    ("GetDriverName",       EFI_COMPONENT_NAME_GET_DRIVER_NAME),
    ("GetControllerName",   EFI_COMPONENT_NAME_GET_CONTROLLER_NAME),
    ("SupportedLanguages",  PCHAR8)
  ]

