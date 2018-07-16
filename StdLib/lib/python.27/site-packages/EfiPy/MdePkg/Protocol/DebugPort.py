#
# DebugPort.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DebugPort.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL

gEfiDebugPortProtocolGuid               = \
  EFI_GUID (0xEBA4E8D2, 0x3858, 0x41EC, (0xA2, 0x81, 0x26, 0x47, 0xBA, 0x96, 0x60, 0xD0 ))

class EFI_DEBUGPORT_PROTOCOL (Structure):
  pass

EFI_DEBUGPORT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL) # IN *This
  )

EFI_DEBUGPORT_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL),  # IN     *This
  UINT32,                           # IN     Timeout,
  POINTER (UINTN),                  # IN OUT *BufferSize,
  PVOID                             # IN     *Buffer
  )

EFI_DEBUGPORT_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL),  # IN     *This
  UINT32,                           # IN     Timeout,
  POINTER (UINTN),                  # IN OUT *BufferSize,
  PVOID                             #    OUT *Buffer
  )

EFI_DEBUGPORT_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL)   # IN     *This
  )

EFI_DEBUGPORT_PROTOCOL._fields_ = [
    ("Reset",   EFI_DEBUGPORT_RESET),
    ("Write",   EFI_DEBUGPORT_WRITE),
    ("Read",    EFI_DEBUGPORT_READ),
    ("Poll",    EFI_DEBUGPORT_POLL)
  ]

EFI_DEBUGPORT_VARIABLE_NAME = u"DEBUGPORT"
gEfiDebugPortVariableGuid   = gEfiDebugPortProtocolGuid

gEfiDebugPortDevicePathGuid = gEfiDebugPortProtocolGuid

class DEBUGPORT_DEVICE_PATH (Structure):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Guid",    EFI_GUID)
  ]

