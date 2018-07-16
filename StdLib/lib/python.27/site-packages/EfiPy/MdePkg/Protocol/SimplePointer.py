#
# SimplePointer.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SimplePointer.py is free software: you can redistribute it and/or
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

gEfiSimplePointerProtocolGuid = \
  EFI_GUID (0x31878c87, 0xb75, 0x11d5, (0x9a, 0x4f, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_SIMPLE_POINTER_PROTOCOL (Structure):
  pass

class EFI_SIMPLE_POINTER_STATE (Structure):
  _fields_ = [
    ("RelativeMovementX", INT32),
    ("RelativeMovementY", INT32),
    ("RelativeMovementZ", INT32),
    ("LeftButton",        BOOLEAN),
    ("RightButton",       BOOLEAN)
  ]

class EFI_SIMPLE_POINTER_MODE (Structure):
  _fields_ = [
    ("ResolutionX", UINT64),
    ("ResolutionY", UINT64),
    ("ResolutionZ", UINT64),
    ("LeftButton",  BOOLEAN),
    ("RightButton", BOOLEAN)
  ]

EFI_SIMPLE_POINTER_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_POINTER_PROTOCOL), # IN *This
  BOOLEAN                               # IN ExtendedVerification
  )

EFI_SIMPLE_POINTER_GET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_POINTER_PROTOCOL), # IN      *This
  POINTER(EFI_SIMPLE_POINTER_STATE)     # IN OUT  *State
  )

EFI_SIMPLE_POINTER_PROTOCOL._fields_ = [
    ("Reset",         EFI_SIMPLE_POINTER_RESET),
    ("GetState",      EFI_SIMPLE_POINTER_GET_STATE),
    ("WaitForInput",  EFI_EVENT),
    ("Mode",          POINTER(EFI_SIMPLE_POINTER_MODE))
  ]

