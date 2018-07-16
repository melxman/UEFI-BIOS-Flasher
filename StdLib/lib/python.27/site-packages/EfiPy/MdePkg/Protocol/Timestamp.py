#
# Timestamp.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Timestamp.py is free software: you can redistribute it and/or
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

gEfiTimestampProtocolGuid = \
  EFI_GUID (0xafbfde41, 0x2e6e, 0x4262, (0xba, 0x65, 0x62, 0xb9, 0x23, 0x6e, 0x54, 0x95 ))

class EFI_TIMESTAMP_PROTOCOL (Structure):
  pass

class EFI_TIMESTAMP_PROPERTIES (Structure):
  _fields_ = [
    ("Frequency", UINT64),
    ("EndValue",  UINT64)
  ]

TIMESTAMP_GET = CFUNCTYPE (
  UINT64
  )

TIMESTAMP_GET_PROPERTIES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIMESTAMP_PROPERTIES)     # OUT *Properties
  )

EFI_TIMESTAMP_PROTOCOL._fields_ = [
    ("GetTimestamp",  TIMESTAMP_GET),
    ("GetProperties", TIMESTAMP_GET_PROPERTIES)
  ]

