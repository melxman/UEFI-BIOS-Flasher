#
# LegacyBiosPlatform.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LegacyBiosPlatform.py is free software: you can redistribute it and/or
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
from EfiPy.IntelFrameworkPkg.Protocol.LegacyBios import EFI_COMPATIBILITY16_TABLE
from EfiPy.MdePkg.Protocol.DevicePath import BBS_BBS_DEVICE_PATH

gEfiLegacyBiosPlatformProtocolGuid = \
  EFI_GUID (0xc35f272c, 0x97c2, 0x465a, (0xa2, 0x16, 0x69, 0x6b, 0x66, 0x8a, 0x8c, 0xfe))

class EFI_LEGACY_BIOS_PLATFORM_PROTOCOL (Structure):
  pass

EfiGetPlatformBinaryMpTable      = 0
EfiGetPlatformBinaryOemIntData   = 1
EfiGetPlatformBinaryOem16Data    = 2
EfiGetPlatformBinaryOem32Data    = 3
EfiGetPlatformBinaryTpmBinary    = 4
EfiGetPlatformBinarySystemRom    = 5
EfiGetPlatformPciExpressBase     = 6
EfiGetPlatformPmmSize            = 7
EfiGetPlatformEndOpromShadowAddr = 8
EFI_GET_PLATFORM_INFO_MODE       = UINTN

EfiGetPlatformVgaHandle       = 0
EfiGetPlatformIdeHandle       = 1
EfiGetPlatformIsaBusHandle    = 2
EfiGetPlatformUsbHandle       = 3
EFI_GET_PLATFORM_HANDLE_MODE  = UINTN

EfiPlatformHookPrepareToScanRom = 0
EfiPlatformHookShadowServiceRoms= 1
EfiPlatformHookAfterRomInit     = 2
EFI_GET_PLATFORM_HOOK_MODE      = UINTN

PCI_UNUSED        = 0x00
PCI_USED          = 0xFF
LEGACY_USED       = 0xFE

class EFI_LEGACY_IRQ_PRIORITY_TABLE_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
  ("Irq",     UINT8),
  ("Used",    UINT8)
  ]

EFI_LEGACY_PIRQ_TABLE_SIGNATURE = SIGNATURE_32 ('$', 'P', 'I', 'R')
class EFI_LEGACY_PIRQ_TABLE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("Signature",     UINT32),
  ("MinorVersion",  UINT8),
  ("MajorVersion",  UINT8),
  ("TableSize",     UINT16),
  ("Bus",           UINT8),
  ("DevFun",        UINT8),
  ("PciOnlyIrq",    UINT16),
  ("CompatibleVid", UINT16),
  ("CompatibleDid", UINT16),
  ("Miniport",      UINT32),
  ("Reserved",      UINT8 * 11),
  ("Checksum",      UINT8)
  ]

class EFI_LEGACY_PIRQ_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
  ("Pirq",     UINT8),
  ("IrqMask",  UINT16)
  ]

class EFI_LEGACY_IRQ_ROUTING_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
  ("Bus",       UINT8),
  ("Device",    UINT8),
  ("PirqEntry", EFI_LEGACY_PIRQ_ENTRY * 4),
  ("Slot",      UINT8),
  ("Reserved",  UINT8)
  ]

EFI_LEGACY_BIOS_PLATFORM_GET_PLATFORM_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN  *This,
  EFI_GET_PLATFORM_INFO_MODE,                 # IN  Mode,
  POINTER(PVOID),                             # OUT **Table,
  POINTER(UINTN),                             # OUT *TableSize,
  POINTER(UINTN),                             # OUT *Location,
  POINTER(UINTN),                             # OUT *Alignment,
  UINT16,                                     # IN  LegacySegment,
  UINT16                                      # IN  LegacyOffset
  )

EFI_LEGACY_BIOS_PLATFORM_GET_PLATFORM_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN  *This,
  EFI_GET_PLATFORM_HANDLE_MODE,               # IN  Mode,
  UINT16,                                     # IN  Type,
  POINTER(POINTER(EFI_HANDLE)),               # OUT **HandleBuffer,
  UINTN,                                      # OUT *HandleCount,
  POINTER(PVOID)                              # IN  **AdditionalData OPTIONAL
  )

EFI_LEGACY_BIOS_PLATFORM_SMM_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN  *This,
  PVOID                                       # IN  *EfiToLegacy16BootTable
  )

EFI_LEGACY_BIOS_PLATFORM_HOOKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN  *This,
  EFI_GET_PLATFORM_HOOK_MODE,                 # IN      Mode,
  UINT16,                                     # IN      Type,
  EFI_HANDLE,                                 # IN      DeviceHandle, OPTIONAL
  POINTER(UINTN),                             # IN  OUT *ShadowAddress, OPTIONAL
  POINTER(EFI_COMPATIBILITY16_TABLE),         # IN      *Compatibility16Table, OPTIONAL
  POINTER(PVOID)                              # OUT     **AdditionalData OPTIONAL
  )

EFI_LEGACY_BIOS_PLATFORM_GET_ROUTING_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN    *This,
  POINTER(PVOID),                             #   OUT **RoutingTable,
  POINTER(UINTN),                             #   OUT *RoutingTableEntries,
  POINTER(PVOID),                             #   OUT **LocalPirqTable, OPTIONAL
  POINTER(UINTN),                             #   OUT *PirqTableSize, OPTIONAL
  POINTER(PVOID),                             #   OUT **LocalIrqPriorityTable, OPTIONAL
  POINTER(UINTN)                              #   OUT *IrqPriorityTableEntries OPTIONAL
  )

EFI_LEGACY_BIOS_PLATFORM_TRANSLATE_PIRQ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN      *This,
  UINTN,                                      # IN      PciBus,
  UINTN,                                      # IN      PciDevice,
  UINTN,                                      # IN      PciFunction,
  POINTER(UINT8),                             # IN  OUT *Pirq,
  POINTER(UINT8)                              # OUT     *PciIrq
  )

EFI_LEGACY_BIOS_PLATFORM_PREPARE_TO_BOOT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PLATFORM_PROTOCOL), # IN  *This,
  POINTER(BBS_BBS_DEVICE_PATH),               # IN  *BbsDevicePath,
  PVOID,                                      # IN  *BbsTable,
  UINT32,                                     # IN  LoadOptionsSize,
  PVOID,                                      # IN  *LoadOptions,
  PVOID                                       # IN  *EfiToLegacy16BootTable
  )

EFI_LEGACY_BIOS_PLATFORM_PROTOCOL._fields_ = [
  ("GetPlatformInfo",   EFI_LEGACY_BIOS_PLATFORM_GET_PLATFORM_INFO),
  ("GetPlatformHandle", EFI_LEGACY_BIOS_PLATFORM_GET_PLATFORM_HANDLE),
  ("SmmInit",           EFI_LEGACY_BIOS_PLATFORM_SMM_INIT),
  ("PlatformHooks",     EFI_LEGACY_BIOS_PLATFORM_HOOKS),
  ("GetRoutingTable",   EFI_LEGACY_BIOS_PLATFORM_GET_ROUTING_TABLE),
  ("TranslatePirq",     EFI_LEGACY_BIOS_PLATFORM_TRANSLATE_PIRQ),
  ("PrepareToBoot",     EFI_LEGACY_BIOS_PLATFORM_PREPARE_TO_BOOT)
  ]

