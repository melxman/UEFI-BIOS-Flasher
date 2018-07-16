#
# IScsiInitiatorName.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# IScsiInitiatorName.py is free software: you can redistribute it and/or
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

gEfiIScsiInitiatorNameProtocolGuid  = \
  EFI_GUID (0x59324945, 0xec44, 0x4c0d, (0xb1, 0xcd, 0x9d, 0xb1, 0x39, 0xdf, 0x7, 0xc ))

class EFI_ISCSI_INITIATOR_NAME_PROTOCOL (Structure):
  pass

EFI_ISCSI_INITIATOR_NAME_GET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISCSI_INITIATOR_NAME_PROTOCOL), # IN      *This,
  POINTER(UINTN),                             # IN OUT  *BufferSize,
  PVOID                                       # OUT     *Buffer
  )

EFI_ISCSI_INITIATOR_NAME_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISCSI_INITIATOR_NAME_PROTOCOL), # IN      *This,
  POINTER(UINTN),                             # IN OUT  *BufferSize,
  PVOID                                       # IN      *Buffer
  )

EFI_ISCSI_INITIATOR_NAME_PROTOCOL._fields_ = [
    ("Get", EFI_ISCSI_INITIATOR_NAME_GET),
    ("Set", EFI_ISCSI_INITIATOR_NAME_SET)
  ]

