#
# MeasuredFvHob.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# MeasuredFvHob.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard.UefiTcgPlatform import EFI_PLATFORM_FIRMWARE_BLOB

gMeasuredFvHobGuid = \
  EFI_GUID (0xb2360b42, 0x7173, 0x420a, (0x86, 0x96, 0x46, 0xca, 0x6b, 0xab, 0x10, 0x60))

class MEASURED_HOB_DATA (Structure):
  _fields_ = [
  ("Num",           UINT32),
  ("MeasuredFvBuf", EFI_PLATFORM_FIRMWARE_BLOB * 1)
  ]

