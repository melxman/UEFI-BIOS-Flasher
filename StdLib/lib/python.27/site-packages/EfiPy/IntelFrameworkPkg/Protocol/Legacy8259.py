#
# Legacy8259.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Legacy8259.py is free software: you can redistribute it and/or
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

gEfiLegacy8259ProtocolGuid = \
  EFI_GUID (0x38321dba, 0x4fe0, 0x4e17, (0x8a, 0xec, 0x41, 0x30, 0x55, 0xea, 0xed, 0xc1))

class EFI_LEGACY_8259_PROTOCOL (Structure):
  pass

Efi8259Irq0   =  0
Efi8259Irq1   =  1
Efi8259Irq2   =  2
Efi8259Irq3   =  3
Efi8259Irq4   =  4
Efi8259Irq5   =  5
Efi8259Irq6   =  6
Efi8259Irq7   =  7
Efi8259Irq8   =  8
Efi8259Irq9   =  9
Efi8259Irq10  = 10
Efi8259Irq11  = 11
Efi8259Irq12  = 12
Efi8259Irq13  = 13
Efi8259Irq14  = 14
Efi8259Irq15  = 15
Efi8259IrqMax = 16
EFI_8259_IRQ  = UINTN

Efi8259LegacyMode     = 0
Efi8259ProtectedMode  = 1
Efi8259MaxMode        = 2
EFI_8259_MODE         = UINTN

EFI_LEGACY_8259_SET_VECTOR_BASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  # IN *This,
  UINT8,                              # IN MasterBase
  UINT8                               # IN SlaveBase
  )

EFI_LEGACY_8259_GET_MASK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN  *This,
  POINTER(UINT16),                    #   OUT *LegacyMask, OPTIONAL
  POINTER(UINT16),                    #   OUT *LegacyEdgeLevel, OPTIONAL
  POINTER(UINT16),                    #   OUT *ProtectedMask, OPTIONAL
  POINTER(UINT16)                     #   OUT *ProtectedEdgeLevel OPTIONAL
  )

EFI_LEGACY_8259_SET_MASK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN *This,
  POINTER(UINT16),                    #   IN *LegacyMask, OPTIONAL
  POINTER(UINT16),                    #   IN *LegacyEdgeLevel, OPTIONAL
  POINTER(UINT16),                    #   IN *ProtectedMask, OPTIONAL
  POINTER(UINT16)                     #   IN *ProtectedEdgeLevel OPTIONAL
  )

EFI_LEGACY_8259_SET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN *This,
  EFI_8259_MODE,                      #   IN  Mode,
  POINTER(UINT16),                    #   IN  *Mask, OPTIONAL
  POINTER(UINT16)                     #   IN  *EdgeLevel OPTIONAL
  )

EFI_LEGACY_8259_GET_VECTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN  *This,
  EFI_8259_IRQ,                       #   IN  Irq,
  POINTER(UINT8)                      #   OUT *Vector
  )

EFI_LEGACY_8259_ENABLE_IRQ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN  *This,
  EFI_8259_IRQ,                       #   IN  Irq,
  BOOLEAN                             #   IN  LevelTriggered
  )

EFI_LEGACY_8259_DISABLE_IRQ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN  *This,
  EFI_8259_IRQ                        #   IN  Irq,
  )

EFI_LEGACY_8259_GET_INTERRUPT_LINE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN  *This,
  EFI_HANDLE,                         #   IN  PciHandle,
  POINTER(UINT8)                      #   OUT *Vector
  )

EFI_LEGACY_8259_END_OF_INTERRUPT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_8259_PROTOCOL),  #   IN  *This,
  EFI_8259_IRQ                        #   IN  Irq
  )

EFI_LEGACY_8259_PROTOCOL._fields_ = [
  ("SetVectorBase",     EFI_LEGACY_8259_SET_VECTOR_BASE),
  ("GetMask",           EFI_LEGACY_8259_GET_MASK),
  ("SetMask",           EFI_LEGACY_8259_SET_MASK),
  ("SetMode",           EFI_LEGACY_8259_SET_MODE),
  ("GetVector",         EFI_LEGACY_8259_GET_VECTOR),
  ("EnableIrq",         EFI_LEGACY_8259_ENABLE_IRQ),
  ("DisableIrq",        EFI_LEGACY_8259_DISABLE_IRQ),
  ("GetInterruptLine",  EFI_LEGACY_8259_GET_INTERRUPT_LINE),
  ("EndOfInterrupt",    EFI_LEGACY_8259_END_OF_INTERRUPT)
  ]

