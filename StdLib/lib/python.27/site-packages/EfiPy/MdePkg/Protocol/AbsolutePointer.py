#
# AbsolutePointer.py
#
# Copyright (C) 2015-2016 efipy.core@gmail.com All rights reserved.
#
# AbsolutePointer.py is free software: you can redistribute it and/or
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

gEfiAbsolutePointerProtocolGuid           = \
  EFI_GUID (0x8D59D32B, 0xC655, 0x4AE9, ( 0x9B, 0x15, 0xF2, 0x59, 0x04, 0x99, 0x2A, 0x43 ))

class EFI_ABSOLUTE_POINTER_PROTOCOL (Structure):
  pass

class EFI_ABSOLUTE_POINTER_MODE (Structure):
  _fields_ = [
    ("AbsoluteMinX", UINT64),
    ("AbsoluteMinY", UINT64),
    ("AbsoluteMinZ", UINT64),
    ("AbsoluteMaxX", UINT64),
    ("AbsoluteMaxY", UINT64),
    ("AbsoluteMaxZ", UINT64),
    ("Attributes",   UINT32)
  ]

EFI_ABSP_SupportsAltActive    = 0x00000001
EFI_ABSP_SupportsPressureAsZ  = 0x00000002

EFI_ABSOLUTE_POINTER_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ABSOLUTE_POINTER_PROTOCOL), # IN *This
  BOOLEAN                                 # IN ExtendedVerification
  )

EFI_ABSP_TouchActive  = 0x00000001
EFI_ABS_AltActive     = 0x00000002

class EFI_ABSOLUTE_POINTER_STATE (Structure):
  _fields_ = [
    ("CurrentX",      UINT64),
    ("CurrentY",      UINT64),
    ("CurrentZ",      UINT64),
    ("ActiveButtons", UINT32)
  ]

EFI_ABSOLUTE_POINTER_GET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ABSOLUTE_POINTER_PROTOCOL),  # IN *This
  POINTER (EFI_ABSOLUTE_POINTER_STATE),     # IN *State
  )

EFI_ABSOLUTE_POINTER_PROTOCOL._fields_ = [
    ("Reset",         EFI_ABSOLUTE_POINTER_RESET),
    ("GetState",      EFI_ABSOLUTE_POINTER_GET_STATE),
    ("WaitForInput",  EFI_EVENT),
    ("Mode",          POINTER (EFI_ABSOLUTE_POINTER_MODE))
  ]

