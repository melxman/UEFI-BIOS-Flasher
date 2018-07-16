#
# EventGroup.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EventGroup.py is free software: you can redistribute it and/or
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

from EfiPy import *

gEfiEventExitBootServicesGuid = \
  EFI_GUID (0x27abf055, 0xb1b8, 0x4c26, ( 0x80, 0x48, 0x74, 0x8f, 0x37, 0xba, 0xa2, 0xdf))

gEfiEventVirtualAddressChangeGuid = \
  EFI_GUID (0x13fa7698, 0xc831, 0x49c7, ( 0x87, 0xea, 0x8f, 0x43, 0xfc, 0xc2, 0x51, 0x96))

gEfiEventMemoryMapChangeGuid  = \
  EFI_GUID (0x78bee926, 0x692f, 0x48fd, ( 0x9e, 0xdb, 0x1, 0x42, 0x2e, 0xf0, 0xd7, 0xab))

gEfiEventReadyToBootGuid  = \
  EFI_GUID (0x7ce88fb3, 0x4bd7, 0x4679, ( 0x87, 0xa8, 0xa8, 0xd8, 0xde, 0xe5, 0x0d, 0x2b))

gEfiEventDxeDispatchGuid  = \
  EFI_GUID (0x7081e22f, 0xcac6, 0x4053, ( 0x94, 0x68, 0x67, 0x57, 0x82, 0xcf, 0x88, 0xe5 ))

gEfiEndOfDxeEventGroupGuid  = \
  EFI_GUID (0x2ce967a, 0xdd7e, 0x4ffc, ( 0x9e, 0xe7, 0x81, 0xc, 0xf0, 0x47, 0x8, 0x80 ))

