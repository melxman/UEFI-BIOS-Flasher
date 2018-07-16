#
# MemoryTypeInformation.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# MemoryTypeInformation.py is free software: you can redistribute it and/or
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

EFI_MEMORY_TYPE_INFORMATION_VARIABLE_NAME = u"MemoryTypeInformation"
gEfiMemoryTypeInformationGuid         = \
  EFI_GUID (0x4c19049f,0x4137,0x4dd3, ( 0x9c,0x10,0x8b,0x97,0xa8,0x3f,0xfd,0xfa))

class EFI_MEMORY_TYPE_INFORMATION (Structure):
  _fields_ = [
  ("Type",          UINT32),
  ("NumberOfPages", UINT32)
  ]

