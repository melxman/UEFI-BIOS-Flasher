#
# VgaMiniPort.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# VgaMiniPort.py is free software: you can redistribute it and/or
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

gEfiVgaMiniPortProtocolGuid = \
  EFI_GUID (0xc7735a2f, 0x88f5, 0x4882, (0xae, 0x63, 0xfa, 0xac, 0x8c, 0x8b, 0x86, 0xb3))

class EFI_VGA_MINI_PORT_PROTOCOL (Structure):
  pass

EFI_VGA_MINI_PORT_SET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VGA_MINI_PORT_PROTOCOL),  # IN *This
  UINTN                                 # IN ModeNumber
  )

EFI_VGA_MINI_PORT_PROTOCOL._fields_ = [
    ("SetMode",                   EFI_VGA_MINI_PORT_SET_MODE),
    ("VgaMemoryOffset",           UINT64),
    ("CrtcAddressRegisterOffset", UINT64),
    ("CrtcDataRegisterOffset",    UINT64),
    ("VgaMemoryBar",              UINT8),
    ("CrtcAddressRegisterBar",    UINT8),
    ("CrtcDataRegisterBar",       UINT8),
    ("MaxMode",                   UINT8)
  ]

