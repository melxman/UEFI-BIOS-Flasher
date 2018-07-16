#
# FaultTolerantWrite.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FaultTolerantWrite.py is free software: you can redistribute it and/or
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

class FAULT_TOLERANT_WRITE_LAST_WRITE_DATA (Structure):
  _fields_ = [
  ("TargetAddress", EFI_PHYSICAL_ADDRESS),
  ("SpareAddress",  EFI_PHYSICAL_ADDRESS),
  ("Length",        UINT64)
  ]

gEdkiiFaultTolerantWriteGuid         = \
  EFI_GUID (0x1d3e9cb8, 0x43af, 0x490b, (0x83,  0xa, 0x35, 0x16, 0xaa, 0x53, 0x20, 0x47))

