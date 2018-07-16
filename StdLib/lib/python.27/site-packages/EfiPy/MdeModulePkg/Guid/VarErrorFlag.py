#
# VarErrorFlag.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# VarErrorFlag.py is free software: you can redistribute it and/or
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

VAR_ERROR_FLAG_NAME             = u"VarErrorFlag"
VAR_ERROR_FLAG_NO_ERROR         = 0xFF
VAR_ERROR_FLAG_SYSTEM_ERROR     = 0xEF
VAR_ERROR_FLAG_USER_ERROR       = 0xFE

VAR_ERROR_FLAG  = UINT8

gEdkiiVarErrorFlagGuid         = \
  EFI_GUID (0x4b37fe8, 0xf6ae, 0x480b, (0xbd, 0xd5, 0x37, 0xd9, 0x8c, 0x5e, 0x89, 0xaa))

