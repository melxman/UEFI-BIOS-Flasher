#
# FileInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FileInfo.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

gEfiFileInfoGuid = EFI_GUID( 0x9576e92, 0x6d3f, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_FILE_INFO (Structure):
  _pack_   = 1            # BUF in X64 platform
  _fields_ = [
      ("Size",              UINT64),
      ("FileSize",          UINT64),
      ("PhysicalSize",      UINT64),
      ("CreateTime",        EFI_TIME),
      ("LastAccessTime",    EFI_TIME),
      ("ModificationTime",  EFI_TIME),
      ("Attribute",         UINT64),
      ("FileName",          CHAR16 * 1)
    ]

