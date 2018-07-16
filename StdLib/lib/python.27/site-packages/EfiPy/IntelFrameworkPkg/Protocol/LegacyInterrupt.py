#
# LegacyInterrupt.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LegacyInterrupt.py is free software: you can redistribute it and/or
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

gEfiLegacyInterruptProtocolGuid = \
  EFI_GUID (0x31ce593d, 0x108a, 0x485d, (0xad, 0xb2, 0x78, 0xf2, 0x1f, 0x29, 0x66, 0xbe))

class EFI_LEGACY_INTERRUPT_PROTOCOL (Structure):
  pass

EFI_LEGACY_INTERRUPT_GET_NUMBER_PIRQS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_INTERRUPT_PROTOCOL),  # IN  *This,
  POINTER(UINT8)                           # OUT *NumberPirqs
  )

EFI_LEGACY_INTERRUPT_GET_LOCATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_INTERRUPT_PROTOCOL),  # IN  *This,
  POINTER(UINT8),                          #   OUT *Bus,
  POINTER(UINT8),                          #   OUT *Device,
  POINTER(UINT8)                           #   OUT *Function
  )

EFI_LEGACY_INTERRUPT_READ_PIRQ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_INTERRUPT_PROTOCOL),   # IN  *This,
  UINT8,                                    # IN  PirqNumber,
  POINTER(UINT8)                            # OUT *PirqData
  )

EFI_LEGACY_INTERRUPT_WRITE_PIRQ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_INTERRUPT_PROTOCOL),   # IN  *This,
  UINT8,                                    # IN  PirqNumber,
  UINT8                                     # IN  PirqData
  )

EFI_LEGACY_INTERRUPT_PROTOCOL._fields_ = [
    ("GetNumberPirqs",  EFI_LEGACY_INTERRUPT_GET_NUMBER_PIRQS),
    ("GetLocation",     EFI_LEGACY_INTERRUPT_GET_LOCATION),
    ("ReadPirq",        EFI_LEGACY_INTERRUPT_READ_PIRQ),
    ("WritePirq",       EFI_LEGACY_INTERRUPT_WRITE_PIRQ)
  ]

