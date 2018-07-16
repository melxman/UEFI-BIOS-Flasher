#
# Metronome.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Metronome.py is free software: you can redistribute it and/or
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

gEfiMetronomeArchProtocolGuid = \
  EFI_GUID (0x26baccb2, 0x6f42, 0x11d4, (0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

class EFI_METRONOME_ARCH_PROTOCOL (Structure):
  pass

EFI_METRONOME_WAIT_FOR_TICK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_METRONOME_ARCH_PROTOCOL), # IN *This
  UINT32                                # IN TickNumber
  )

EFI_METRONOME_ARCH_PROTOCOL._fields_ = [
  ("WaitForTick", EFI_METRONOME_WAIT_FOR_TICK),
  ("TickPeriod",  UINT32)
  ]

