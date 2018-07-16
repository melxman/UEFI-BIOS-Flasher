#
# Bds.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Bds.py is free software: you can redistribute it and/or
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

gEfiBdsArchProtocolGuid                 = \
  EFI_GUID (0x665E3FF6, 0x46CC, 0x11d4, (0x9A, 0x38, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_BDS_ARCH_PROTOCOL (Structure):
  pass

EFI_BDS_ENTRY = CFUNCTYPE (
  VOID,
  POINTER (EFI_BDS_ARCH_PROTOCOL) # IN  *This
  )

EFI_BDS_ARCH_PROTOCOL._fields_ = [
    ("Entry", EFI_BDS_ENTRY)
  ]

