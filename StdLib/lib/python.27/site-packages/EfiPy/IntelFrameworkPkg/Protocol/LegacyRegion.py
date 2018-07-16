#
# LegacyRegion.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LegacyRegion.py is free software: you can redistribute it and/or
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

gEfiLegacyRegionProtocolGuid = \
  EFI_GUID (0xfc9013a, 0x568, 0x4ba9, (0x9b, 0x7e, 0xc9, 0xc3, 0x90, 0xa6, 0x60, 0x9b))

class EFI_LEGACY_REGION_PROTOCOL (Structure):
  pass

EFI_LEGACY_REGION_DECODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION_PROTOCOL),  # IN  *This,
  UINT32,                               # IN  Start,
  UINT32,                               # IN  Length,
  POINTER(BOOLEAN)                      # IN  *On
  )

EFI_LEGACY_REGION_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION_PROTOCOL),  # IN  *This,
  UINT32,                               # IN  Start,
  UINT32,                               # IN  Length,
  POINTER(UINT32)                       # OUT *Granularity OPTIONAL
  )

EFI_LEGACY_REGION_BOOT_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION_PROTOCOL),  # IN  *This,
  UINT32,                               # IN  Start,
  UINT32,                               # IN  Length,
  POINTER(UINT32)                       # OUT *Granularity OPTIONAL
  )

EFI_LEGACY_REGION_UNLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION_PROTOCOL),  # IN  *This,
  UINT32,                               # IN  Start,
  UINT32,                               # IN  Length,
  POINTER(UINT32)                       # OUT *Granularity OPTIONAL
  )

EFI_LEGACY_REGION_PROTOCOL._fields_ = [
    ("Decode",    EFI_LEGACY_REGION_DECODE),
    ("Lock",      EFI_LEGACY_REGION_LOCK),
    ("BootLock",  EFI_LEGACY_REGION_BOOT_LOCK),
    ("UnLock",    EFI_LEGACY_REGION_UNLOCK)
  ]

