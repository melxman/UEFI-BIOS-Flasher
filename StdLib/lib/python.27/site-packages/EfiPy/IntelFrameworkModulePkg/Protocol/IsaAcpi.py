#
# IsaAcpi.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IsaAcpi.py is free software: you can redistribute it and/or
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

gEfiIsaAcpiProtocolGuid = \
  EFI_GUID (0x64a892dc, 0x5561, 0x4536, ( 0x92, 0xc7, 0x79, 0x9b, 0xfc, 0x18, 0x33, 0x55))

class EFI_ISA_ACPI_PROTOCOL (Structure):
  pass

EFI_ISA_ACPI_IRQ_TYPE_HIGH_TRUE_EDGE_SENSITIVE   = 0x01
EFI_ISA_ACPI_IRQ_TYPE_LOW_TRUE_EDGE_SENSITIVE    = 0x02
EFI_ISA_ACPI_IRQ_TYPE_HIGH_TRUE_LEVEL_SENSITIVE  = 0x04
EFI_ISA_ACPI_IRQ_TYPE_LOW_TRUE_LEVEL_SENSITIVE   = 0x08

EFI_ISA_ACPI_DMA_SPEED_TYPE_MASK                 = 0x03
EFI_ISA_ACPI_DMA_SPEED_TYPE_COMPATIBILITY        = 0x00
EFI_ISA_ACPI_DMA_SPEED_TYPE_A                    = 0x01
EFI_ISA_ACPI_DMA_SPEED_TYPE_B                    = 0x02
EFI_ISA_ACPI_DMA_SPEED_TYPE_F                    = 0x03
EFI_ISA_ACPI_DMA_COUNT_BY_BYTE                   = 0x04
EFI_ISA_ACPI_DMA_COUNT_BY_WORD                   = 0x08
EFI_ISA_ACPI_DMA_BUS_MASTER                      = 0x10
EFI_ISA_ACPI_DMA_TRANSFER_TYPE_8_BIT             = 0x20
EFI_ISA_ACPI_DMA_TRANSFER_TYPE_8_BIT_AND_16_BIT  = 0x40
EFI_ISA_ACPI_DMA_TRANSFER_TYPE_16_BIT            = 0x80

EFI_ISA_ACPI_MEMORY_WIDTH_MASK                   = 0x03
EFI_ISA_ACPI_MEMORY_WIDTH_8_BIT                  = 0x00
EFI_ISA_ACPI_MEMORY_WIDTH_16_BIT                 = 0x01
EFI_ISA_ACPI_MEMORY_WIDTH_8_BIT_AND_16_BIT       = 0x02
EFI_ISA_ACPI_MEMORY_WRITEABLE                    = 0x04
EFI_ISA_ACPI_MEMORY_CACHEABLE                    = 0x08
EFI_ISA_ACPI_MEMORY_SHADOWABLE                   = 0x10
EFI_ISA_ACPI_MEMORY_EXPANSION_ROM                = 0x20

EFI_ISA_ACPI_IO_DECODE_10_BITS                   = 0x01
EFI_ISA_ACPI_IO_DECODE_16_BITS                   = 0x02

EfiIsaAcpiResourceEndOfList     = 0
EfiIsaAcpiResourceIo            = 1
EfiIsaAcpiResourceMemory        = 2
EfiIsaAcpiResourceDma           = 3
EfiIsaAcpiResourceInterrupt     = 4
EFI_ISA_ACPI_RESOURCE_TYPE      = UINTN

class EFI_ISA_ACPI_RESOURCE (Structure):
  _fields_ = [
    ("Type",        EFI_ISA_ACPI_RESOURCE_TYPE),
    ("Attribute",   UINT32),
    ("StartRange",  UINT32),
    ("EndRange",    UINT32)
  ]

class EFI_ISA_ACPI_DEVICE_ID (Structure):
  _fields_ = [
    ("HID", UINT32),
    ("UID", UINT32)
  ]

class EFI_ISA_ACPI_RESOURCE_LIST (Structure):
  _fields_ = [
    ("Device",        EFI_ISA_ACPI_DEVICE_ID),
    ("ResourceItem",  POINTER(EFI_ISA_ACPI_RESOURCE))
  ]

EFI_ISA_ACPI_DEVICE_ENUMERATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),           # IN  *This
  POINTER(POINTER(EFI_ISA_ACPI_DEVICE_ID))  # OUT **Device
  )

EFI_ISA_ACPI_SET_DEVICE_POWER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),   # IN *This
  POINTER(EFI_ISA_ACPI_DEVICE_ID),  # IN *Device
  BOOLEAN                           # IN OnOff
  )

EFI_ISA_ACPI_GET_CUR_RESOURCE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),               # IN  *This
  POINTER(EFI_ISA_ACPI_DEVICE_ID),              # IN  *Device
  POINTER(POINTER(EFI_ISA_ACPI_RESOURCE_LIST))  # OUT **ResourceList
  )

EFI_ISA_ACPI_GET_POS_RESOURCE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),               # IN  *This
  POINTER(EFI_ISA_ACPI_DEVICE_ID),              # IN  *Device
  POINTER(POINTER(EFI_ISA_ACPI_RESOURCE_LIST))  # OUT **ResourceList
  )

EFI_ISA_ACPI_SET_RESOURCE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),     # IN  *This
  POINTER(EFI_ISA_ACPI_DEVICE_ID),    # IN  *Device
  POINTER(EFI_ISA_ACPI_RESOURCE_LIST) # OUT *ResourceList
  )

EFI_ISA_ACPI_ENABLE_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),   # IN *This
  POINTER(EFI_ISA_ACPI_DEVICE_ID),  # IN *Device
  BOOLEAN                           # IN Enable
  )

EFI_ISA_ACPI_INIT_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL),   # IN *This
  POINTER(EFI_ISA_ACPI_DEVICE_ID)   # IN *Device
  )

EFI_ISA_ACPI_INTERFACE_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_ACPI_PROTOCOL)   # IN *This
  )

EFI_ISA_ACPI_PROTOCOL._fields_ = [
    ("DeviceEnumerate", EFI_ISA_ACPI_DEVICE_ENUMERATE),
    ("SetPower",        EFI_ISA_ACPI_SET_DEVICE_POWER),
    ("GetCurResource",  EFI_ISA_ACPI_GET_CUR_RESOURCE),
    ("GetPosResource",  EFI_ISA_ACPI_GET_POS_RESOURCE),
    ("SetResource",     EFI_ISA_ACPI_SET_RESOURCE),
    ("EnableDevice",    EFI_ISA_ACPI_ENABLE_DEVICE),
    ("InitDevice",      EFI_ISA_ACPI_INIT_DEVICE),
    ("InterfaceInit",   EFI_ISA_ACPI_INTERFACE_INIT)
  ]

