#
# ComponentName2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ComponentName2.py is free software: you can redistribute it and/or
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

gEfiComponentName2ProtocolGuid          = \
  EFI_GUID (0x6a7a5cff, 0xe8d9, 0x4f70, ( 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14 ))

class EFI_COMPONENT_NAME2_PROTOCOL (Structure):
  pass

EFI_COMPONENT_NAME2_GET_DRIVER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME2_PROTOCOL),  # IN *This
  PCHAR8,                                 # IN *Language
  POINTER (PCHAR16)                       # IN **DriverName
  )

EFI_COMPONENT_NAME2_GET_CONTROLLER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME2_PROTOCOL),  # IN *This
  EFI_HANDLE,                             # IN  ControllerHandle,
  EFI_HANDLE,                             # IN  ChildHandle        OPTIONAL,
  PCHAR8,                                 # IN *Language
  POINTER (PCHAR16)                       # IN **ControllerName
  )

EFI_COMPONENT_NAME2_PROTOCOL._fields_ = [
    ("GetDriverName",       EFI_COMPONENT_NAME2_GET_DRIVER_NAME),
    ("GetControllerName",   EFI_COMPONENT_NAME2_GET_CONTROLLER_NAME),
    ("SupportedLanguages",  PCHAR8)
  ]

