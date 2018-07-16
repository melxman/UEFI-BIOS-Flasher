#
# LegacyRegion2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# LegacyRegion2.py is free software: you can redistribute it and/or
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

gEfiLegacyRegion2ProtocolGuid = \
  EFI_GUID (0x70101eaf, 0x85, 0x440c, (0xb3, 0x56, 0x8e, 0xe3, 0x6f, 0xef, 0x24, 0xf0 ))

class EFI_LEGACY_REGION2_PROTOCOL (Structure):
  pass

EFI_LEGACY_REGION2_DECODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32),                        # OUT *Granularity,
  POINTER(BOOLEAN)                        # IN  *On
  )

EFI_LEGACY_REGION2_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32)                         # OUT *Granularity
  )

EFI_LEGACY_REGION2_BOOT_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32)                         # OUT *Granularity OPTIONAL
  )

EFI_LEGACY_REGION2_UNLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32)                         # OUT *Granularity
  )

LegacyRegionDecoded         = 0
LegacyRegionNotDecoded      = 1
LegacyRegionWriteEnabled    = 2
LegacyRegionWriteDisabled   = 3
LegacyRegionBootLocked      = 4
LegacyRegionNotLocked       = 5 
EFI_LEGACY_REGION_ATTRIBUTE = ENUM

class EFI_LEGACY_REGION_DESCRIPTOR (Structure):
  _fields_ = [
    ("Start",       UINT32),
    ("Length",      UINT32),
    ("Attribute",   EFI_LEGACY_REGION_ATTRIBUTE),
    ("Granularity", UINT32)
  ]

EFI_LEGACY_REGION_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),           # IN *This
  POINTER(UINT32),                                # OUT *DescriptorCount
  POINTER(POINTER(EFI_LEGACY_REGION_DESCRIPTOR))  # OUT **Descriptor
  )

EFI_LEGACY_REGION2_PROTOCOL._fields_ = [
    ("Decode",    EFI_LEGACY_REGION2_DECODE),
    ("Lock",      EFI_LEGACY_REGION2_LOCK),
    ("BootLock",  EFI_LEGACY_REGION2_BOOT_LOCK),
    ("UnLock",    EFI_LEGACY_REGION2_UNLOCK),
    ("GetInfo",   EFI_LEGACY_REGION_GET_INFO)
  ]

