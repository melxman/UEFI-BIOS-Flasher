#
# VariableLock.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# VariableLock.py is free software: you can redistribute it and/or
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

gEdkiiVariableLockProtocolGuid = \
  EFI_GUID (0xcd3d0a05, 0x9e24, 0x437c, ( 0xa8, 0x91, 0x1e, 0xe0, 0x53, 0xdb, 0x76, 0x38))

class EDKII_VARIABLE_LOCK_PROTOCOL (Structure):
  pass

EDKII_VARIABLE_LOCK_PROTOCOL_REQUEST_TO_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_VARIABLE_LOCK_PROTOCOL),  # IN CONST *This,
  POINTER(CHAR16),                        # IN       *VariableName,
  POINTER(EFI_GUID)                       # IN       *VendorGuid
  )

EDKII_VARIABLE_LOCK_PROTOCOL._fields_ = [
  ("RequestToLock",   EDKII_VARIABLE_LOCK_PROTOCOL_REQUEST_TO_LOCK)
  ]

