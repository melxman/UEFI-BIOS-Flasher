#
# MemoryOverwriteControl.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# MemoryOverwriteControl.py is free software: you can redistribute it and/or
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

gEfiMemoryOverwriteControlDataGuid  = \
  EFI_GUID (0xe20939be, 0x32d4, 0x41be, (0xa1, 0x50, 0x89, 0x7f, 0x85, 0xd4, 0x98, 0x29))

MEMORY_OVERWRITE_REQUEST_VARIABLE_NAME = u"MemoryOverwriteRequestControl"
MOR_CLEAR_MEMORY_BIT_MASK        = 0x01
MOR_DISABLEAUTODETECT_BIT_MASK   = 0x10

MOR_CLEAR_MEMORY_BIT_OFFSET      = 0
MOR_DISABLEAUTODETECT_BIT_OFFSET = 4

def MOR_CLEAR_MEMORY_VALUE(mor):
  return (mor & MOR_CLEAR_MEMORY_BIT_MASK) >> MOR_CLEAR_MEMORY_BIT_OFFSET

def MOR_DISABLE_AUTO_DETECT_VALUE(mor):
  return (mor & MOR_DISABLEAUTODETECT_BIT_MASK) >> MOR_DISABLEAUTODETECT_BIT_OFFSETa

