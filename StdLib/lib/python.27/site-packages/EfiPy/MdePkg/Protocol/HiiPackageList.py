#
# HiiPackageList.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HiiPackageList.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiBaseType   import *
from EfiPy.MdePkg.Uefi.UefiSpec       import *

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
        EFI_HII_PACKAGE_LIST_HEADER

gEfiHiiPackageListProtocolGuid  = \
  EFI_GUID (0x6a1ee763, 0xd47a, 0x43b4, (0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc))
EFI_HII_PACKAGE_LIST_PROTOCOL   = POINTER (EFI_HII_PACKAGE_LIST_HEADER)
