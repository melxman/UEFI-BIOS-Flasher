#
# SmramMemoryReserve.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# SmramMemoryReserve.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiMultiPhase import EFI_SMRAM_DESCRIPTOR

gEfiSmmPeiSmramMemoryReserveGuid = \
  EFI_GUID (0x6dadf1d1, 0xd4cc, 0x4910, (0xbb, 0x6e, 0x82, 0xb1, 0xfd, 0x80, 0xff, 0x3d))

class EFI_SMRAM_HOB_DESCRIPTOR_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("NumberOfSmmReservedRegions",  UINT32),
    ("Descriptor",                  EFI_SMRAM_DESCRIPTOR * 1)
  ]

