#
# LoadFile2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# LoadFile2.py is free software: you can redistribute it and/or
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

gEfiLoadFile2ProtocolGuid = \
  EFI_GUID (0x4006c0c1, 0xfcb3, 0x403e, (0x99, 0x6d, 0x4a, 0x6c, 0x87, 0x24, 0xe0, 0x6d ))

class EFI_LOAD_FILE2_PROTOCOL (Structure):
  pass

EFI_LOAD_FILE2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LOAD_FILE2_PROTOCOL),   # IN      *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),  # IN      *FilePath,
  BOOLEAN,                            # IN      BootPolicy,
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID                               # IN      *Buffer OPTIONAL
  )

EFI_LOAD_FILE2_PROTOCOL._fields_ = [
    ("LoadFile",    EFI_LOAD_FILE2)
  ]

