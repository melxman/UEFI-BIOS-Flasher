#
# Hob.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Hob.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiHob  import EFI_HOB_GENERIC_HEADER

EFI_HOB_TYPE_CV           = 0x0008
class EFI_HOB_CAPSULE_VOLUME (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      EFI_HOB_GENERIC_HEADER),
  ("BaseAddress", EFI_PHYSICAL_ADDRESS),
  ("Length",      UINT64)
  ]

