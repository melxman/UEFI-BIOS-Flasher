#
# EsrtManagement.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# EsrtManagement.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Guid.SystemResourceTable import EFI_SYSTEM_RESOURCE_ENTRY

gEsrtManagementProtocolGuid = \
  EFI_GUID (0xa340c064, 0x723c, 0x4a9c, (0xa4, 0xdd, 0xd5, 0xb4, 0x7a, 0x26, 0xfb, 0xb0))

class ESRT_MANAGEMENT_PROTOCOL (Structure):
  pass

GET_ESRT_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),                  # IN      *FwClass,
  POINTER(EFI_SYSTEM_RESOURCE_ENTRY)  # IN OUT  *Entry
  )

UPDATE_ESRT_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SYSTEM_RESOURCE_ENTRY)  # IN *Entry
  )

UNREGISTER_ESRT_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID)  # IN *FwClass
  )

REGISTER_ESRT_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SYSTEM_RESOURCE_ENTRY)  # IN *Entry
  )

SYNC_ESRT_FMP = CFUNCTYPE (
  EFI_STATUS
  )

LOCK_ESRT_REPOSITORY = CFUNCTYPE (
  EFI_STATUS
  )

ESRT_MANAGEMENT_PROTOCOL._fields_ = [
  ("GetEsrtEntry",        GET_ESRT_ENTRY),
  ("UpdateEsrtEntry",     UPDATE_ESRT_ENTRY),
  ("RegisterEsrtEntry",   REGISTER_ESRT_ENTRY),
  ("UnRegisterEsrtEntry", UNREGISTER_ESRT_ENTRY),
  ("SyncEsrtFmp",         SYNC_ESRT_FMP),
  ("LockEsrtRepository",  LOCK_ESRT_REPOSITORY)
  ]

