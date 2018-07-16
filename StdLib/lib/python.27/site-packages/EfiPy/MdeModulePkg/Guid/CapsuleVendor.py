#
# CapsuleVendor.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# CapsuleVendor.py is free software: you can redistribute it and/or
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

EFI_CAPSULE_VARIABLE_NAME = u"CapsuleUpdateData"

class CAPSULE_HOB_INFO (Structure):
  _fields_ = [
  ("BaseAddress",  EFI_PHYSICAL_ADDRESS)
  ]

class EFI_CAPSULE_LONG_MODE_BUFFER (Structure):
  _fields_ = [
  ("PageTableAddress",  EFI_PHYSICAL_ADDRESS),
  ("StackBaseAddress",  EFI_PHYSICAL_ADDRESS),
  ("StackSize",         UINT64)
  ]

gEfiCapsuleVendorGuid         = \
  EFI_GUID (0x711C703F, 0xC285, 0x4B10, (0xA3, 0xB0, 0x36, 0xEC, 0xBD, 0x3C, 0x8B, 0xE2))

