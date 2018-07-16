#
# DataHubStatusCodeRecord.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# DataHubStatusCodeRecord.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiStatusCode import EFI_STATUS_CODE_TYPE, EFI_STATUS_CODE_VALUE, EFI_STATUS_CODE_DATA

gEfiDataHubStatusCodeRecordGuid = \
  EFI_GUID (0xd083e94c, 0x6560, 0x42e4, (0xb6, 0xd4, 0x2d, 0xf7, 0x5a, 0xdf, 0x6a, 0x2a))

class DATA_HUB_STATUS_CODE_DATA_RECORD (Structure):
  _fields_ = [
    ("CodeType",  EFI_STATUS_CODE_TYPE),
    ("Value",     EFI_STATUS_CODE_VALUE),
    ("Instance",  UINT32),
    ("CallerId",  EFI_GUID),
    ("Data",      EFI_STATUS_CODE_DATA)
  ]

