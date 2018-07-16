#
# DriverDiagnostics2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DriverDiagnostics2.py is free software: you can redistribute it and/or
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

import DriverDiagnostics
gEfiDriverDiagnostics2ProtocolGuid       = \
  EFI_GUID (0x4d330321, 0x025f, 0x4aac, (0x90, 0xd8, 0x5e, 0xd9, 0x00, 0x17, 0x3b, 0x63 ))

class EFI_DRIVER_DIAGNOSTICS2_PROTOCOL (Structure):
  pass

EFI_DRIVER_DIAGNOSTICS2_RUN_DIAGNOSTICS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_DIAGNOSTICS2_PROTOCOL),    # IN  *This
  EFI_HANDLE,                                   # IN  ControllerHandle,
  EFI_HANDLE,                                   # IN  ChildHandle  OPTIONAL,
  DriverDiagnostics.EFI_DRIVER_DIAGNOSTIC_TYPE, # IN  DiagnosticType,
  PCHAR8,                                       # IN  *Language,
  POINTER(POINTER(EFI_GUID)),                   # OUT **ErrorType,
  POINTER(UINTN),                               # OUT *BufferSize,
  POINTER(PCHAR16)                              # OUT **Buffer
  )

EFI_DRIVER_DIAGNOSTICS2_PROTOCOL._fields_ = [
    ("RunDiagnostics",      EFI_DRIVER_DIAGNOSTICS2_RUN_DIAGNOSTICS),
    ("SupportedLanguages",  PCHAR8)
  ]

