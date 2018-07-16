#
# LegacyBios.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LegacyBios.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Protocol.DevicePath import BBS_BBS_DEVICE_PATH

SERIAL_MODE   = UINT8
PARALLEL_MODE = UINT8

EFI_COMPATIBILITY16_TABLE_SIGNATURE = SIGNATURE_32 ('I', 'F', 'E', '$')

class EFI_COMPATIBILITY16_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Signature",                     UINT32),
  ("TableChecksum",                 UINT8),
  ("TableLength",                   UINT8),
  ("EfiMajorRevision",              UINT8),
  ("EfiMinorRevision",              UINT8),
  ("TableMajorRevision",            UINT8),
  ("TableMinorRevision",            UINT8),
  ("Reserved",                      UINT16),
  ("Compatibility16CallSegment",    UINT16),
  ("Compatibility16CallOffset",     UINT16),
  ("PnPInstallationCheckSegment",   UINT16),
  ("PnPInstallationCheckOffset",    UINT16),
  ("EfiSystemTable",                UINT32),
  ("OemIdStringPointer",            UINT32),
  ("AcpiRsdPtrPointer",             UINT32),
  ("OemRevision",                   UINT16),
  ("E820Pointer",                   UINT32),
  ("E820Length",                    UINT32),
  ("IrqRoutingTablePointer",        UINT32),
  ("IrqRoutingTableLength",         UINT32),
  ("MpTablePtr",                    UINT32),
  ("MpTableLength",                 UINT32),
  ("OemIntSegment",                 UINT16),
  ("OemIntOffset",                  UINT16),
  ("Oem32Segment",                  UINT16),
  ("Oem32Offset",                   UINT16),
  ("Oem16Segment",                  UINT16),
  ("Oem16Offset",                   UINT16),
  ("TpmSegment",                    UINT16),
  ("TpmOffset",                     UINT16),
  ("IbvPointer",                    UINT32),
  ("PciExpressBase",                UINT32),
  ("LastPciBus",                    UINT8),
  ("UmaAddress",                    UINT32),
  ("UmaSize",                       UINT32),
  ("HiPermanentMemoryAddress",      UINT32),
  ("HiPermanentMemorySize",         UINT32)
  ]

Legacy16InitializeYourself    = 0x0000
Legacy16UpdateBbs             = 0x0001
Legacy16PrepareToBoot         = 0x0002
Legacy16Boot                  = 0x0003
Legacy16RetrieveLastBootDevice = 0x0004
Legacy16DispatchOprom         = 0x0005
Legacy16GetTableAddress       = 0x0006
Legacy16SetKeyboardLeds       = 0x0007
Legacy16InstallPciHandler     = 0x0008
EFI_COMPATIBILITY_FUNCTIONS   = UINTN

class EFI_DISPATCH_OPROM_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("PnPInstallationCheckSegment",   UINT16),
    ("PnPInstallationCheckOffset",    UINT16),
    ("OpromSegment",                  UINT16),
    ("PciBus",                        UINT8),
    ("PciDeviceFunction",             UINT8),
    ("NumberBbsEntries",              UINT8),
    ("BbsTablePointer",               UINT32),
    ("RuntimeSegment",                UINT16)
  ]

class EFI_TO_COMPATIBILITY16_INIT_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("BiosLessThan1MB",           UINT32),
  ("HiPmmMemory",               UINT32),
  ("HiPmmMemorySizeInBytes",    UINT32),
  ("ReverseThunkCallSegment",   UINT16),
  ("ReverseThunkCallOffset",    UINT16),
  ("NumberE820Entries",         UINT32),
  ("OsMemoryAbove1Mb",          UINT32),
  ("ThunkStart",                UINT32),
  ("ThunkSizeInBytes",          UINT32),
  ("LowPmmMemory",              UINT32),
  ("LowPmmMemorySizeInBytes",   UINT32)
  ]

class DEVICE_PRODUCER_SERIAL (Structure):
  _pack_   = 1
  _fields_ = [
  ("Address", UINT16),
  ("Irq",     UINT8),
  ("Mode",    SERIAL_MODE)
  ]

DEVICE_SERIAL_MODE_NORMAL               = 0x00
DEVICE_SERIAL_MODE_IRDA                 = 0x01
DEVICE_SERIAL_MODE_ASK_IR               = 0x02
DEVICE_SERIAL_MODE_DUPLEX_HALF          = 0x00
DEVICE_SERIAL_MODE_DUPLEX_FULL          = 0x10

class DEVICE_PRODUCER_PARALLEL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Address", UINT16),
    ("Irq",     UINT8),
    ("Dma",     UINT8),
    ("Mode",    PARALLEL_MODE)
  ]

DEVICE_PARALLEL_MODE_MODE_OUTPUT_ONLY   = 0x00
DEVICE_PARALLEL_MODE_MODE_BIDIRECTIONAL = 0x01
DEVICE_PARALLEL_MODE_MODE_EPP           = 0x02
DEVICE_PARALLEL_MODE_MODE_ECP           = 0x03

class DEVICE_PRODUCER_FLOPPY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Address",         UINT16),
    ("Irq",             UINT8),
    ("Dma",             UINT8),
    ("NumberOfFloppy",  UINT8)
  ]

class LEGACY_DEVICE_FLAGS (Structure):
  _pack_   = 1
  _fields_ = [
    ("A20Kybd",         UINT32, 1),
    ("A20Port90",       UINT32, 1),
    ("Reserved",        UINT32, 30)
  ]

class DEVICE_PRODUCER_DATA_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Serial",        DEVICE_PRODUCER_SERIAL * 4),
    ("Parallel",      DEVICE_PRODUCER_PARALLEL * 3),
    ("Floppy",        DEVICE_PRODUCER_FLOPPY),
    ("MousePresent",  UINT8),
    ("Flags",         LEGACY_DEVICE_FLAGS)
  ]

class ATAPI_IDENTIFY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Raw",        UINT16 * 256)
  ]

class HDD_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Status",              UINT16),
    ("Bus",                 UINT32),
    ("Device",              UINT32),
    ("Function",            UINT32),
    ("CommandBaseAddress",  UINT16),
    ("ControlBaseAddress",  UINT16),
    ("BusMasterAddress",    UINT16),
    ("HddIrq",              UINT8),
    ("IdentifyDrive",       ATAPI_IDENTIFY * 2)
  ]

HDD_PRIMARY               = 0x01
HDD_SECONDARY             = 0x02
HDD_MASTER_ATAPI_CDROM    = 0x04
HDD_SLAVE_ATAPI_CDROM     = 0x08
HDD_MASTER_IDE            = 0x20
HDD_SLAVE_IDE             = 0x40
HDD_MASTER_ATAPI_ZIPDISK  = 0x10
HDD_SLAVE_ATAPI_ZIPDISK   = 0x80

class BBS_STATUS_FLAGS (Structure):
  _pack_   = 1
  _fields_ = [
  ("OldPosition",   UINT16, 4),
  ("Reserved1",     UINT16, 4),
  ("Enabled",       UINT16, 1),
  ("Failed",        UINT16, 1),
  ("MediaPresent",  UINT16, 2),
  ("Reserved2",     UINT16, 4)
  ]

class BBS_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("BootPriority",            UINT16),
  ("Bus",                     UINT32),
  ("Device",                  UINT32),
  ("Function",                UINT32),
  ("Class",                   UINT8),
  ("SubClass",                UINT8),
  ("MfgStringOffset",         UINT16),
  ("MfgStringSegment",        UINT16),
  ("DeviceType",              UINT16),
  ("StatusFlags",             BBS_STATUS_FLAGS),
  ("BootHandlerOffset",       UINT16),
  ("BootHandlerSegment",      UINT16),
  ("DescStringOffset",        UINT16),
  ("DescStringSegment",       UINT16),
  ("InitPerReserved",         UINT32),
  ("AdditionalIrq13Handler",  UINT32),
  ("AdditionalIrq18Handler",  UINT32),
  ("AdditionalIrq19Handler",  UINT32),
  ("AdditionalIrq40Handler",  UINT32),
  ("AssignedDriveNumber",     UINT8),
  ("AdditionalIrq41Handler",  UINT32),
  ("AdditionalIrq46Handler",  UINT32),
  ("IBV1",                    UINT32),
  ("IBV2",                    UINT32)
  ]

BBS_FLOPPY              = 0x01
BBS_HARDDISK            = 0x02
BBS_CDROM               = 0x03
BBS_PCMCIA              = 0x04
BBS_USB                 = 0x05
BBS_EMBED_NETWORK       = 0x06
BBS_BEV_DEVICE          = 0x80
BBS_UNKNOWN             = 0xff

BBS_DO_NOT_BOOT_FROM    = 0xFFFC
BBS_LOWEST_PRIORITY     = 0xFFFD
BBS_UNPRIORITIZED_ENTRY = 0xFFFE
BBS_IGNORE_ENTRY        = 0xFFFF

class SMM_ATTRIBUTES (Structure):
  _pack_   = 1
  _fields_ = [
  ("Type",            UINT16, 3),
  ("PortGranularity", UINT16, 3),
  ("DataGranularity", UINT16, 3),
  ("Reserved",        UINT16, 7)
  ]

STANDARD_IO       = 0x00
STANDARD_MEMORY   = 0x01

PORT_SIZE_8       = 0x00
PORT_SIZE_16      = 0x01
PORT_SIZE_32      = 0x02
PORT_SIZE_64      = 0x03

DATA_SIZE_8       = 0x00
DATA_SIZE_16      = 0x01
DATA_SIZE_32      = 0x02
DATA_SIZE_64      = 0x03

class SMM_FUNCTION (Structure):
  _pack_   = 1
  _fields_ = [
  ("Function",  UINT16, 15),
  ("Owner",     UINT16, 1)
  ]

INT15_D042        = 0x0000
GET_USB_BOOT_INFO = 0x0001
DMI_PNP_50_57     = 0x0002

STANDARD_OWNER    = 0x0
OEM_OWNER         = 0x1

class SMM_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
  ("SmmAttributes", SMM_ATTRIBUTES),
  ("SmmFunction",   SMM_FUNCTION),
  ("SmmPort",       UINT8),
  ("SmmData",       UINT8)
  ]

class SMM_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("NumSmmEntries", UINT16),
  ("SmmEntry",      SMM_ENTRY)
  ]

class UDC_ATTRIBUTES (Structure):
  _pack_   = 1
  _fields_ = [
  ("DirectoryServiceValidity",  UINT8, 1),
  ("RabcaUsedFlag",             UINT8, 1),
  ("ExecuteHddDiagnosticsFlag", UINT8, 1),
  ("Reserved",                  UINT8, 5)
  ]

class UD_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Attributes",                          UDC_ATTRIBUTES),
  ("DeviceNumber",                        UINT8),
  ("BbsTableEntryNumberForParentDevice",  UINT8),
  ("BbsTableEntryNumberForBoot",          UINT8),
  ("BbsTableEntryNumberForHddDiag",       UINT8),
  ("BeerData",                            UINT8 * 128),
  ("ServiceAreaData",                     UINT8 * 64)
  ]

EFI_TO_LEGACY_MAJOR_VERSION = 0x02
EFI_TO_LEGACY_MINOR_VERSION = 0x00
MAX_IDE_CONTROLLER          = 8

class EFI_TO_COMPATIBILITY16_BOOT_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("MajorVersion",              UINT16),
  ("MinorVersion",              UINT16),
  ("AcpiTable",                 UINT32),
  ("SmbiosTable",               UINT32),
  ("SmbiosTableLength",         UINT32),
  ("SioData",                   DEVICE_PRODUCER_DATA_HEADER),
  ("DevicePathType",            UINT16),
  ("PciIrqMask",                UINT16),
  ("NumberE820Entries",         UINT32),
  ("HddInfo",                   HDD_INFO * MAX_IDE_CONTROLLER),
  ("NumberBbsEntries",          UINT32),
  ("BbsTable",                  UINT32),
  ("SmmTable",                  UINT32),
  ("OsMemoryAbove1Mb",          UINT32),
  ("UnconventionalDeviceTable", UINT32)
  ]

class EFI_LEGACY_INSTALL_PCI_HANDLER (Structure):
  _pack_   = 1
  _fields_ = [
  ("PciBus",              UINT8),
  ("PciDeviceFun",        UINT8),
  ("PciSegment",          UINT8),
  ("PciClass",            UINT8),
  ("PciSubclass",         UINT8),
  ("PciInterface",        UINT8),
  ("PrimaryIrq",          UINT8),
  ("PrimaryReserved",     UINT8),
  ("PrimaryControl",      UINT16),
  ("PrimaryBase",         UINT16),
  ("PrimaryBusMaster",    UINT16),
  ("SecondaryIrq",        UINT8),
  ("SecondaryReserved",   UINT8),
  ("SecondaryControl",    UINT16),
  ("SecondaryBase",       UINT16),
  ("SecondaryBusMaster",  UINT16)
  ]

gEfiLegacyBiosProtocolGuid = \
  EFI_GUID (0xdb9a1e3d, 0x45cb, 0x4abb, (0x85, 0x3b, 0xe5, 0x38, 0x7f, 0xdb, 0x2e, 0x2d))

class EFI_LEGACY_BIOS_PROTOCOL (Structure):
  pass

NO_ROM            = 0x00
ROM_FOUND         = 0x01
VALID_LEGACY_ROM  = 0x02
ROM_WITH_CONFIG   = 0x04

def EFI_SEGMENT(_Adr):
  return (_Adr >> 4) & 0xf000

def EFI_OFFSET(_Adr):
  return _Adr & 0xffff

CARRY_FLAG            = 0x01

class EFI_EFLAGS_REG (Structure):
  _fields_ = [
  ("CF",            UINT32, 1),
  ("Reserved1",     UINT32, 1),
  ("PF",            UINT32, 1),
  ("Reserved2",     UINT32, 1),
  ("AF",            UINT32, 1),
  ("Reserved3",     UINT32, 1),
  ("ZF",            UINT32, 1),
  ("SF",            UINT32, 1),
  ("TF",            UINT32, 1),
  ("IF",            UINT32, 1),
  ("DF",            UINT32, 1),
  ("OF",            UINT32, 1),
  ("IOPL",          UINT32, 2),
  ("NT",            UINT32, 1),
  ("Reserved4",     UINT32, 2),
  ("VM",            UINT32, 1),
  ("Reserved5",     UINT32, 14) 
  ]

class EFI_DWORD_REGS (Structure):
  _fields_ = [
  ("EAX",    UINT32),
  ("EBX",    UINT32),
  ("ECX",    UINT32),
  ("EDX",    UINT32),
  ("ESI",    UINT32),
  ("EDI",    UINT32),
  ("EFlags", EFI_EFLAGS_REG),
  ("ES",     UINT16),
  ("CS",     UINT16),
  ("SS",     UINT16),
  ("DS",     UINT16),
  ("FS",     UINT16),
  ("GS",     UINT16),
  ("EBP",    UINT32),
  ("ESP",    UINT32)
  ]

class EFI_FLAGS_REG (Structure):
  _fields_ = [
  ("CF",        UINT16, 1),
  ("Reserved1", UINT16, 1),
  ("PF",        UINT16, 1),
  ("Reserved2", UINT16, 1),
  ("AF",        UINT16, 1),
  ("Reserved3", UINT16, 1),
  ("ZF",        UINT16, 1),
  ("SF",        UINT16, 1),
  ("TF",        UINT16, 1),
  ("IF",        UINT16, 1),
  ("DF",        UINT16, 1),
  ("OF",        UINT16, 1),
  ("IOPL",      UINT16, 2),
  ("NT",        UINT16, 1),
  ("Reserved4", UINT16, 1)
  ]

class EFI_WORD_REGS (Structure):
  _fields_ = [
  ("AX",            UINT16),
  ("ReservedAX",    UINT16),
  ("BX",            UINT16),
  ("ReservedBX",    UINT16),
  ("CX",            UINT16),
  ("ReservedCX",    UINT16),
  ("DX",            UINT16),
  ("ReservedDX",    UINT16),
  ("SI",            UINT16),
  ("ReservedSI",    UINT16),
  ("DI",            UINT16),
  ("ReservedDI",    UINT16),
  ("Flags",         EFI_FLAGS_REG),
  ("ReservedFlags", UINT16),
  ("ES",            UINT16),
  ("CS",            UINT16),
  ("SS",            UINT16),
  ("DS",            UINT16),
  ("FS",            UINT16),
  ("GS",            UINT16),
  ("BP",            UINT16),
  ("ReservedBP",    UINT16),
  ("SP",            UINT16),
  ("ReservedSP",    UINT16)
  ]

class EFI_BYTE_REGS (Structure):
  _fields_ = [
  ("AL",          UINT8),
  ("AH",          UINT8),
  ("ReservedAX",  UINT16),
  ("BL",          UINT8),
  ("BH",          UINT8),
  ("ReservedBX",  UINT16),
  ("CL",          UINT8),
  ("CH",          UINT8),
  ("ReservedCX",  UINT16),
  ("DL",          UINT8),
  ("DH",          UINT8),
  ("ReservedDX",  UINT16)
  ]

class EFI_IA32_REGISTER_SET (Union):
  _fields_ = [
  ("E", EFI_DWORD_REGS),
  ("X", EFI_WORD_REGS),
  ("H", EFI_BYTE_REGS)
  ]

EFI_LEGACY_BIOS_INT86 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN     *This,
  UINT8,                              #   IN     BiosInt,
  POINTER(EFI_IA32_REGISTER_SET)      #   IN OUT *Regs
  )

EFI_LEGACY_BIOS_FARCALL86 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN     *This,
  UINT16,                             #   IN Segment,
  UINT16,                             #   IN Offset,
  POINTER(EFI_IA32_REGISTER_SET),     #   IN *Regs,
  PVOID,                              #   IN *Stack,
  UINTN                               #   IN StackSize
  )

EFI_LEGACY_BIOS_CHECK_ROM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN     *This,
  EFI_HANDLE,                         #   IN  PciHandle,
  POINTER(PVOID),                     #   OUT **RomImage, OPTIONAL
  POINTER(UINTN),                     #   OUT *RomSize, OPTIONAL
  POINTER(UINTN)                      #   OUT *Flags
  )

EFI_LEGACY_BIOS_INSTALL_ROM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN     *This,
  EFI_HANDLE,                         #   IN  PciHandle,
  POINTER(PVOID),                     #   IN  **RomImage, OPTIONAL
  POINTER(UINTN),                     #   OUT *Flags
  POINTER(UINT8),                     #   OUT *DiskStart, OPTIONAL
  POINTER(UINT8),                     #   OUT *DiskEnd, OPTIONAL
  POINTER(PVOID),                     #   OUT **RomShadowAddress, OPTIONAL
  POINTER(UINT32)                     #   OUT *ShadowedRomSize OPTIONAL
  )

EFI_LEGACY_BIOS_BOOT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN     *This,
  POINTER(BBS_BBS_DEVICE_PATH),       #   IN *BootOption,
  UINT32,                             #   IN LoadOptionsSize,
  PVOID                               #   IN *LoadOptions
  )

EFI_LEGACY_BIOS_UPDATE_KEYBOARD_LED_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN *This,
  UINT8,                              #   IN Leds,
  )

EFI_LEGACY_BIOS_GET_BBS_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN *This,
  POINTER(UINT16),                    #   OUT    *HddCount,
  POINTER(POINTER(HDD_INFO)),         #   OUT    **HddInfo,
  POINTER(UINT16),                    #   OUT    *BbsCount,
  POINTER(POINTER(BBS_TABLE))         #   IN OUT **BbsTable
  )

EFI_LEGACY_BIOS_PREPARE_TO_BOOT_EFI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN  *This,
  POINTER(UINT16),                    #   OUT *BbsCount,
  POINTER(POINTER(BBS_TABLE))         #   OUT **BbsTable
  )

EFI_LEGACY_BIOS_BOOT_UNCONVENTIONAL_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN  *This,
  UDC_ATTRIBUTES,                     #   IN Attributes,
  UINTN,                              #   IN BbsEntry,
  PVOID,                              #   IN *BeerData,
  PVOID                               #   IN *ServiceAreaData
  )

EFI_LEGACY_BIOS_SHADOW_ALL_LEGACY_OPROMS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL)   #   IN  *This,
  )

EFI_LEGACY_BIOS_GET_LEGACY_REGION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN  *This,
  UINTN,                              #   IN  LegacyMemorySize,
  UINTN,                              #   IN  Region,
  UINTN,                              #   IN  Alignment,
  POINTER(PVOID)                      #   OUT **LegacyMemoryAddress
  )

EFI_LEGACY_BIOS_COPY_LEGACY_REGION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_BIOS_PROTOCOL),  #   IN  *This,
  UINTN,                              #   IN  LegacyMemorySize,
  PVOID,                              #   IN  *LegacyMemoryAddress,
  PVOID                               #   IN  *LegacyMemorySourceAddress
  )

EFI_LEGACY_BIOS_PROTOCOL._fields_ = [
  ("Int86",                     EFI_LEGACY_BIOS_INT86),
  ("FarCall86",                 EFI_LEGACY_BIOS_FARCALL86),
  ("CheckPciRom",               EFI_LEGACY_BIOS_CHECK_ROM),
  ("InstallPciRom",             EFI_LEGACY_BIOS_INSTALL_ROM),
  ("LegacyBoot",                EFI_LEGACY_BIOS_BOOT),
  ("UpdateKeyboardLedStatus",   EFI_LEGACY_BIOS_UPDATE_KEYBOARD_LED_STATUS),
  ("GetBbsInfo",                EFI_LEGACY_BIOS_GET_BBS_INFO),
  ("ShadowAllLegacyOproms",     EFI_LEGACY_BIOS_SHADOW_ALL_LEGACY_OPROMS),
  ("PrepareToBootEfi",          EFI_LEGACY_BIOS_PREPARE_TO_BOOT_EFI),
  ("GetLegacyRegion",           EFI_LEGACY_BIOS_GET_LEGACY_REGION),
  ("CopyLegacyRegion",          EFI_LEGACY_BIOS_COPY_LEGACY_REGION),
  ("BootUnconventionalDevice",  EFI_LEGACY_BIOS_BOOT_UNCONVENTIONAL_DEVICE)
  ]

