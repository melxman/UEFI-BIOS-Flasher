#
# DriverDiagnostics.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DriverDiagnostics.py is free software: you can redistribute it and/or
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

gEfiDriverDiagnosticsProtocolGuid       = \
  EFI_GUID (0x0784924f, 0xe296, 0x11d4, (0x9a, 0x49, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_DRIVER_DIAGNOSTICS_PROTOCOL (Structure):
  pass

EfiDriverDiagnosticTypeStandard     = 0
EfiDriverDiagnosticTypeExtended     = 1
EfiDriverDiagnosticTypeManufacturing= 2
EfiDriverDiagnosticTypeCancel       = 3
EfiDriverDiagnosticTypeMaximum      = 4
EFI_DRIVER_DIAGNOSTIC_TYPE          = ENUM

EFI_DRIVER_DIAGNOSTICS_RUN_DIAGNOSTICS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_DIAGNOSTICS_PROTOCOL), # IN  *This
  EFI_HANDLE,                               # IN  ControllerHandle,
  EFI_HANDLE,                               # IN  ChildHandle  OPTIONAL,
  EFI_DRIVER_DIAGNOSTIC_TYPE,               # IN  DiagnosticType,
  PCHAR8,                                   # IN  *Language,
  POINTER(POINTER(EFI_GUID)),               # OUT **ErrorType,
  POINTER(UINTN),                           # OUT *BufferSize,
  POINTER(PCHAR16)                          # OUT **Buffer
  )

EFI_DRIVER_DIAGNOSTICS_PROTOCOL._fields_ = [
    ("RunDiagnostics",      EFI_DRIVER_DIAGNOSTICS_RUN_DIAGNOSTICS),
    ("SupportedLanguages",  PCHAR8)
  ]

