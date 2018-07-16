#
# StatusCodeDataTypeVariable.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# StatusCodeDataTypeVariable.py is free software: you can redistribute it and/or
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

class EDKII_SET_VARIABLE_STATUS (Structure):
  _fields_ = [
  ("Guid",        EFI_GUID),
  ("NameSize",    UINTN),
  ("DataSize",    UINTN),
  ("SetStatus",   EFI_STATUS),
  ("Attributes",  UINT32)
  # ("Name",        CHAR16 * N),
  # ("Data",        UINT8 * N)
  ]

gEdkiiStatusCodeDataTypeVariableGuid         = \
  EFI_GUID (0xf6ee6dbb, 0xd67f, 0x4ea0, (0x8b, 0x96, 0x6a, 0x71, 0xb1, 0x9d, 0x84, 0xad))

