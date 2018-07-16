#
# StatusCodeDataTypeDebug.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# StatusCodeDataTypeDebug.py is free software: you can redistribute it and/or
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

EFI_STATUS_CODE_DATA_MAX_SIZE = 200

class EFI_DEBUG_INFO (Structure):
  _fields_ = [
  ("ErrorLevel",      UINT32)
  ]

gEfiStatusCodeDataTypeDebugGuid         = \
  EFI_GUID (0x9A4E9246, 0xD553, 0x11D5, (0x87, 0xE2, 0x00, 0x06, 0x29, 0x45, 0xC3, 0xb9))

