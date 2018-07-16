# 
# MemoryAllocationHob.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# MemoryAllocationHob.py is free software: you can redistribute it and/or
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

gEfiHobMemoryAllocBspStoreGuid  = \
  EFI_GUID (0x564b33cd, 0xc92a, 0x4593, (0x90, 0xbf, 0x24, 0x73, 0xe4, 0x3c, 0x63, 0x22))

gEfiHobMemoryAllocStackGuid     = \
  EFI_GUID (0x4ed4bf27, 0x4092, 0x42e9, (0x80, 0x7d, 0x52, 0x7b, 0x1d, 0x0, 0xc9, 0xbd))

gEfiHobMemoryAllocModuleGuid    = \
  EFI_GUID (0xf8e21975, 0x899, 0x4f58, (0xa4, 0xbe, 0x55, 0x25, 0xa9, 0xc6, 0xd7, 0x7a))

