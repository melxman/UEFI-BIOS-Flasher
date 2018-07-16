#
# DataHubRecords.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# DataHubRecords.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.DevicePath import ACPI_HID_DEVICE_PATH, PCI_DEVICE_PATH, EFI_DEVICE_PATH_PROTOCOL
from EfiPy.MdePkg.Guid.StatusCodeDataTypeId import EFI_EXP_BASE10_DATA
from EfiPy.IntelFrameworkPkg.Framework.FrameworkInternalFormRepresentation import STRING_REF

gEfiProcessorSubClassGuid = \
  EFI_GUID (0x26fdeb7e, 0xb8af, 0x4ccf, (0xaa, 0x97, 0x02, 0x63, 0x3c, 0xe4, 0x8c, 0xa7))

gEfiCacheSubClassGuid = \
  EFI_GUID (0x7f0013a7, 0xdc79, 0x4b22, (0x80, 0x99, 0x11, 0xf7, 0x5f, 0xdc, 0x82, 0x9d))

gEfiMemorySubClassGuid  = \
  EFI_GUID (0x4E8F4EBB, 0x64B9, 0x4e05, (0x9B, 0x18, 0x4C, 0xFE, 0x49, 0x23, 0x50, 0x97))

gEfiMiscSubClassGuid  = \
  EFI_GUID (0x772484B2, 0x7482, 0x4b91, (0x9F, 0x9A, 0xAD, 0x43, 0xF8, 0x1C, 0x58, 0x81))

EFI_PROCESSOR_SUBCLASS_VERSION    = 0x00010000

class USB_PORT_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("PciBusDevicePath",        PCI_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class IDE_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("PciBusDevicePath",        PCI_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class RMC_CONN_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("PciBridgeDevicePath",     PCI_DEVICE_PATH),
    ("PciBusDevicePath",        PCI_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class RIDE_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("PciBridgeDevicePath",     PCI_DEVICE_PATH),
    ("PciBusDevicePath",        PCI_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class GB_NIC_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("PciBridgeDevicePath",     PCI_DEVICE_PATH),
    ("PciXBridgeDevicePath",    PCI_DEVICE_PATH),
    ("PciXBusDevicePath",       PCI_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class PS2_CONN_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("LpcBridgeDevicePath",     PCI_DEVICE_PATH),
    ("LpcBusDevicePath",        ACPI_HID_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class SERIAL_CONN_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("LpcBridgeDevicePath",     PCI_DEVICE_PATH),
    ("LpcBusDevicePath",        ACPI_HID_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class PARALLEL_CONN_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("LpcBridgeDevicePath",     PCI_DEVICE_PATH),
    ("LpcBusDevicePath",        ACPI_HID_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class FLOOPY_CONN_DEVICE_PATH (Structure):
  _pack_   = 1
  _fields_ = [
    ("PciRootBridgeDevicePath", ACPI_HID_DEVICE_PATH),
    ("LpcBridgeDevicePath",     PCI_DEVICE_PATH),
    ("LpcBusDevicePath",        ACPI_HID_DEVICE_PATH),
    ("EndDevicePath",           EFI_DEVICE_PATH_PROTOCOL)
  ]

class EFI_MISC_PORT_DEVICE_PATH (Union):
  _pack_   = 1
  _fields_ = [
    ("UsbDevicePath",           USB_PORT_DEVICE_PATH),
    ("IdeDevicePath",           IDE_DEVICE_PATH),
    ("RmcConnDevicePath",       RMC_CONN_DEVICE_PATH),
    ("RideDevicePath",          RIDE_DEVICE_PATH),
    ("GbNicDevicePath",         GB_NIC_DEVICE_PATH),
    ("Ps2ConnDevicePath",       PS2_CONN_DEVICE_PATH),
    ("SerialConnDevicePath",    SERIAL_CONN_DEVICE_PATH),
    ("ParallelConnDevicePath",  PARALLEL_CONN_DEVICE_PATH),
    ("FloppyConnDevicePath",    FLOOPY_CONN_DEVICE_PATH)
  ]

EFI_STRING_TOKEN          = UINT16

class EFI_SUBCLASS_TYPE1_HEADER (Structure):
  _fields_ = [
    ("Version",       UINT32),
    ("HeaderSize",    UINT32),
    ("Instance",      UINT16),
    ("SubInstance",   UINT16),
    ("RecordType",    UINT32)
  ]

class EFI_INTER_LINK_DATA (Structure):
  _fields_ = [
    ("ProducerName",  EFI_GUID),
    ("Instance",      UINT16),
    ("SubInstance",   UINT16)
  ]

class EFI_EXP_BASE2_DATA (Structure):
  _fields_ = [
    ("Value",     UINT16),
    ("Exponent",  UINT16)
  ]

EFI_PROCESSOR_MAX_CORE_FREQUENCY_DATA   = EFI_EXP_BASE10_DATA
EFI_PROCESSOR_MAX_FSB_FREQUENCY_DATA    = EFI_EXP_BASE10_DATA
EFI_PROCESSOR_CORE_FREQUENCY_DATA       = EFI_EXP_BASE10_DATA

EFI_PROCESSOR_CORE_FREQUENCY_LIST_DATA  = POINTER (EFI_EXP_BASE10_DATA)
EFI_PROCESSOR_FSB_FREQUENCY_LIST_DATA = POINTER (EFI_EXP_BASE10_DATA)
EFI_PROCESSOR_FSB_FREQUENCY_DATA  = EFI_EXP_BASE10_DATA
EFI_PROCESSOR_VERSION_DATA        = STRING_REF
EFI_PROCESSOR_MANUFACTURER_DATA   = STRING_REF
EFI_PROCESSOR_SERIAL_NUMBER_DATA  = STRING_REF
EFI_PROCESSOR_ASSET_TAG_DATA      = STRING_REF
EFI_PROCESSOR_PART_NUMBER_DATA    = STRING_REF

class EFI_PROCESSOR_SIGNATURE (Structure):
  _fields_ = [
    ("ProcessorSteppingId", UINT32, 4),
    ("ProcessorModel",      UINT32, 4),
    ("ProcessorFamily",     UINT32, 4),
    ("ProcessorType",       UINT32, 2),
    ("ProcessorReserved1",  UINT32, 2),
    ("ProcessorXModel",     UINT32, 4),
    ("ProcessorXFamily",    UINT32, 8),
    ("ProcessorReserved2",  UINT32, 4)
  ]

class EFI_PROCESSOR_MISC_INFO (Structure):
  _fields_ = [
    ("ProcessorBrandIndex", UINT32, 8),
    ("ProcessorClflush",    UINT32, 8),
    ("ProcessorReserved",   UINT32, 8),
    ("ProcessorDfltApicId", UINT32, 8)
  ]

class EFI_PROCESSOR_FEATURE_FLAGS (Structure):
  _fields_ = [
    ("ProcessorFpu",        UINT32, 1),
    ("ProcessorVme",        UINT32, 1),
    ("ProcessorDe",         UINT32, 1),
    ("ProcessorPse",        UINT32, 1),
    ("ProcessorTsc",        UINT32, 1),
    ("ProcessorMsr",        UINT32, 1),
    ("ProcessorPae",        UINT32, 1),
    ("ProcessorMce",        UINT32, 1),
    ("ProcessorCx8",        UINT32, 1),
    ("ProcessorApic",       UINT32, 1),
    ("ProcessorReserved1",  UINT32, 1),
    ("ProcessorSep",        UINT32, 1),
    ("ProcessorMtrr",       UINT32, 1),
    ("ProcessorPge",        UINT32, 1),
    ("ProcessorMca",        UINT32, 1),
    ("ProcessorCmov",       UINT32, 1),
    ("ProcessorPat",        UINT32, 1),
    ("ProcessorPse36",      UINT32, 1),
    ("ProcessorPsn",        UINT32, 1),
    ("ProcessorClfsh",      UINT32, 1),
    ("ProcessorReserved2",  UINT32, 1),
    ("ProcessorDs",         UINT32, 1),
    ("ProcessorAcpi",       UINT32, 1),
    ("ProcessorMmx",        UINT32, 1),
    ("ProcessorFxsr",       UINT32, 1),
    ("ProcessorSse",        UINT32, 1),
    ("ProcessorSse2",       UINT32, 1),
    ("ProcessorSs",         UINT32, 1),
    ("ProcessorReserved3",  UINT32, 1),
    ("ProcessorTm",         UINT32, 1),
    ("ProcessorReserved4",  UINT32, 2)
  ]

class EFI_PROCESSOR_ID_DATA (Structure):
  _fields_ = [
    ("Signature",     EFI_PROCESSOR_SIGNATURE),
    ("MiscInfo",      EFI_PROCESSOR_MISC_INFO),
    ("Reserved",      UINT32),
    ("FeatureFlags",  EFI_PROCESSOR_FEATURE_FLAGS)
  ]

EfiProcessorOther    = 1
EfiProcessorUnknown  = 2
EfiCentralProcessor  = 3
EfiMathProcessor     = 4
EfiDspProcessor      = 5
EfiVideoProcessor    = 6
EFI_PROCESSOR_TYPE_DATA = UINTN

EfiProcessorFamilyOther                  = 0x01
EfiProcessorFamilyUnknown                = 0x02
EfiProcessorFamily8086                   = 0x03
EfiProcessorFamily80286                  = 0x04
EfiProcessorFamilyIntel386               = 0x05
EfiProcessorFamilyIntel486               = 0x06
EfiProcessorFamily8087                   = 0x07
EfiProcessorFamily80287                  = 0x08
EfiProcessorFamily80387                  = 0x09
EfiProcessorFamily80487                  = 0x0A
EfiProcessorFamilyPentium                = 0x0B
EfiProcessorFamilyPentiumPro             = 0x0C
EfiProcessorFamilyPentiumII              = 0x0D
EfiProcessorFamilyPentiumMMX             = 0x0E
EfiProcessorFamilyCeleron                = 0x0F
EfiProcessorFamilyPentiumIIXeon          = 0x10
EfiProcessorFamilyPentiumIII             = 0x11
EfiProcessorFamilyM1                     = 0x12
EfiProcessorFamilyM2                     = 0x13
EfiProcessorFamilyM1Reserved2            = 0x14
EfiProcessorFamilyM1Reserved3            = 0x15
EfiProcessorFamilyM1Reserved4            = 0x16
EfiProcessorFamilyM1Reserved5            = 0x17
EfiProcessorFamilyAmdDuron               = 0x18
EfiProcessorFamilyK5                     = 0x19
EfiProcessorFamilyK6                     = 0x1A
EfiProcessorFamilyK6_2                   = 0x1B
EfiProcessorFamilyK6_3                   = 0x1C
EfiProcessorFamilyAmdAthlon              = 0x1D
EfiProcessorFamilyAmd29000               = 0x1E
EfiProcessorFamilyK6_2Plus               = 0x1F
EfiProcessorFamilyPowerPC                = 0x20
EfiProcessorFamilyPowerPC601             = 0x21
EfiProcessorFamilyPowerPC603             = 0x22
EfiProcessorFamilyPowerPC603Plus         = 0x23
EfiProcessorFamilyPowerPC604             = 0x24
EfiProcessorFamilyPowerPC620             = 0x25
EfiProcessorFamilyPowerPCx704            = 0x26
EfiProcessorFamilyPowerPC750             = 0x27
EfiProcessorFamilyAlpha3                 = 0x30
EfiProcessorFamilyAlpha21064             = 0x31
EfiProcessorFamilyAlpha21066             = 0x32
EfiProcessorFamilyAlpha21164             = 0x33
EfiProcessorFamilyAlpha21164PC           = 0x34
EfiProcessorFamilyAlpha21164a            = 0x35
EfiProcessorFamilyAlpha21264             = 0x36
EfiProcessorFamilyAlpha21364             = 0x37
EfiProcessorFamilyMips                   = 0x40
EfiProcessorFamilyMIPSR4000              = 0x41
EfiProcessorFamilyMIPSR4200              = 0x42
EfiProcessorFamilyMIPSR4400              = 0x43
EfiProcessorFamilyMIPSR4600              = 0x44
EfiProcessorFamilyMIPSR10000             = 0x45
EfiProcessorFamilySparc                  = 0x50
EfiProcessorFamilySuperSparc             = 0x51
EfiProcessorFamilymicroSparcII           = 0x52
EfiProcessorFamilymicroSparcIIep         = 0x53
EfiProcessorFamilyUltraSparc             = 0x54
EfiProcessorFamilyUltraSparcII           = 0x55
EfiProcessorFamilyUltraSparcIIi          = 0x56
EfiProcessorFamilyUltraSparcIII          = 0x57
EfiProcessorFamilyUltraSparcIIIi         = 0x58
EfiProcessorFamily68040                  = 0x60
EfiProcessorFamily68xxx                  = 0x61
EfiProcessorFamily68000                  = 0x62
EfiProcessorFamily68010                  = 0x63
EfiProcessorFamily68020                  = 0x64
EfiProcessorFamily68030                  = 0x65
EfiProcessorFamilyHobbit                 = 0x70
EfiProcessorFamilyCrusoeTM5000           = 0x78
EfiProcessorFamilyCrusoeTM3000           = 0x79
EfiProcessorFamilyEfficeonTM8000         = 0x7A
EfiProcessorFamilyWeitek                 = 0x80
EfiProcessorFamilyItanium                = 0x82
EfiProcessorFamilyAmdAthlon64            = 0x83
EfiProcessorFamilyAmdOpteron             = 0x84
EfiProcessorFamilyAmdSempron             = 0x85
EfiProcessorFamilyAmdTurion64Mobile      = 0x86
EfiProcessorFamilyDualCoreAmdOpteron     = 0x87
EfiProcessorFamilyAmdAthlon64X2DualCore  = 0x88
EfiProcessorFamilyAmdTurion64X2Mobile    = 0x89
EfiProcessorFamilyPARISC                 = 0x90
EfiProcessorFamilyPaRisc8500             = 0x91
EfiProcessorFamilyPaRisc8000             = 0x92
EfiProcessorFamilyPaRisc7300LC           = 0x93
EfiProcessorFamilyPaRisc7200             = 0x94
EfiProcessorFamilyPaRisc7100LC           = 0x95
EfiProcessorFamilyPaRisc7100             = 0x96
EfiProcessorFamilyV30                    = 0xA0
EfiProcessorFamilyPentiumIIIXeon         = 0xB0
EfiProcessorFamilyPentiumIIISpeedStep    = 0xB1
EfiProcessorFamilyPentium4               = 0xB2
EfiProcessorFamilyIntelXeon              = 0xB3
EfiProcessorFamilyAS400                  = 0xB4
EfiProcessorFamilyIntelXeonMP            = 0xB5
EfiProcessorFamilyAMDAthlonXP            = 0xB6
EfiProcessorFamilyAMDAthlonMP            = 0xB7
EfiProcessorFamilyIntelItanium2          = 0xB8
EfiProcessorFamilyIntelPentiumM          = 0xB9
EfiProcessorFamilyIntelCeleronD          = 0xBA
EfiProcessorFamilyIntelPentiumD          = 0xBB
EfiProcessorFamilyIntelPentiumEx         = 0xBC
EfiProcessorFamilyIntelCoreSolo          = 0xBD
EfiProcessorFamilyReserved               = 0xBE
EfiProcessorFamilyIntelCore2             = 0xBF
EfiProcessorFamilyIBM390                 = 0xC8
EfiProcessorFamilyG4                     = 0xC9
EfiProcessorFamilyG5                     = 0xCA
EfiProcessorFamilyG6                     = 0xCB
EfiProcessorFamilyzArchitectur           = 0xCC
EfiProcessorFamilyViaC7M                 = 0xD2
EfiProcessorFamilyViaC7D                 = 0xD3
EfiProcessorFamilyViaC7                  = 0xD4
EfiProcessorFamilyViaEden                = 0xD5
EfiProcessorFamilyi860                   = 0xFA
EfiProcessorFamilyi960                   = 0xFB
EfiProcessorFamilyIndicatorFamily2       = 0xFE
EfiProcessorFamilyReserved1              = 0xFF
EFI_PROCESSOR_FAMILY_DATA                = UINTN

EfiProcessorFamilySh3           = 0x104
EfiProcessorFamilySh4           = 0x105
EfiProcessorFamilyArm           = 0x118
EfiProcessorFamilyStrongArm     = 0x119
EfiProcessorFamily6x86          = 0x12C
EfiProcessorFamilyMediaGx       = 0x12D
EfiProcessorFamilyMii           = 0x12E
EfiProcessorFamilyWinChip       = 0x140
EfiProcessorFamilyDsp           = 0x15E
EfiProcessorFamilyVideo         = 0x1F4
EFI_PROCESSOR_FAMILY2_DATA      = UINTN

EFI_PROCESSOR_VOLTAGE_DATA              = EFI_EXP_BASE10_DATA

EFI_PROCESSOR_APIC_BASE_ADDRESS_DATA    = EFI_PHYSICAL_ADDRESS
EFI_PROCESSOR_APIC_ID_DATA              = UINT32
EFI_PROCESSOR_APIC_VERSION_NUMBER_DATA  = UINT32

EfiProcessorIa32Microcode    = 1
EfiProcessorIpfPalAMicrocode = 2
EfiProcessorIpfPalBMicrocode = 3
EFI_PROCESSOR_MICROCODE_TYPE = UINTN

class EFI_PROCESSOR_MICROCODE_REVISION_DATA (Structure):
  _fields_ = [
    ("ProcessorMicrocodeType",            EFI_PROCESSOR_MICROCODE_TYPE),
    ("ProcessorMicrocodeRevisionNumber",  UINT32)
  ]

class EFI_PROCESSOR_STATUS_DATA (Structure):
  _fields_ = [
    ("CpuStatus",                 UINT32, 3),
    ("Reserved1",                 UINT32, 3),
    ("SocketPopulated",           UINT32, 1),
    ("Reserved2",                 UINT32, 1),
    ("ApicEnable",                UINT32, 1),
    ("BootApplicationProcessor",  UINT32, 1),
    ("Reserved3",                 UINT32, 22)
  ]

EfiCpuStatusUnknown        = 0
EfiCpuStatusEnabled        = 1
EfiCpuStatusDisabledByUser = 2
EfiCpuStatusDisabledbyBios = 3
EfiCpuStatusIdle           = 4
EfiCpuStatusOther          = 7
EFI_CPU_STATUS             = UINTN

EfiProcessorSocketOther            = 1
EfiProcessorSocketUnknown          = 2
EfiProcessorSocketDaughterBoard    = 3
EfiProcessorSocketZIF              = 4
EfiProcessorSocketReplacePiggyBack = 5
EfiProcessorSocketNone             = 6
EfiProcessorSocketLIF              = 7
EfiProcessorSocketSlot1            = 8
EfiProcessorSocketSlot2            = 9
EfiProcessorSocket370Pin           = 0xA
EfiProcessorSocketSlotA            = 0xB
EfiProcessorSocketSlotM            = 0xC
EfiProcessorSocket423              = 0xD
EfiProcessorSocketA462             = 0xE
EfiProcessorSocket478              = 0xF
EfiProcessorSocket754              = 0x10
EfiProcessorSocket940              = 0x11
EfiProcessorSocket939              = 0x12
EfiProcessorSocketmPGA604          = 0x13
EfiProcessorSocketLGA771           = 0x14
EfiProcessorSocketLGA775           = 0x15
EFI_PROCESSOR_SOCKET_TYPE_DATA     = UINTN

EFI_PROCESSOR_SOCKET_NAME_DATA     = STRING_REF

EFI_CACHE_ASSOCIATION_DATA         = EFI_INTER_LINK_DATA
EfiProcessorHealthy         = 1
EfiProcessorPerfRestricted  = 2
EfiProcessorFuncRestricted  = 3
EFI_PROCESSOR_HEALTH_STATUS = UINTN

EFI_PROCESSOR_PACKAGE_NUMBER_DATA     = UINTN
EFI_PROCESSOR_CORE_COUNT_DATA         = UINT8
EFI_PROCESSOR_ENABLED_CORE_COUNT_DATA = UINT8
EFI_PROCESSOR_THREAD_COUNT_DATA       = UINT8

class EFI_PROCESSOR_CHARACTERISTICS_DATA (Structure):
  _fields_ = [
    ("Reserved",     UINT16, 1),
    ("Unknown",      UINT16, 1),
    ("Capable64Bit", UINT16, 1),
    ("Reserved2",    UINT16, 13)
  ]

ProcessorCoreFrequencyRecordType     = 1
ProcessorFsbFrequencyRecordType      = 2
ProcessorVersionRecordType           = 3
ProcessorManufacturerRecordType      = 4
ProcessorSerialNumberRecordType      = 5
ProcessorIdRecordType                = 6
ProcessorTypeRecordType              = 7
ProcessorFamilyRecordType            = 8
ProcessorVoltageRecordType           = 9
ProcessorApicBaseAddressRecordType   = 10
ProcessorApicIdRecordType            = 11
ProcessorApicVersionNumberRecordType = 12
CpuUcodeRevisionDataRecordType       = 13
ProcessorStatusRecordType            = 14
ProcessorSocketTypeRecordType        = 15
ProcessorSocketNameRecordType        = 16
CacheAssociationRecordType           = 17
ProcessorMaxCoreFrequencyRecordType  = 18
ProcessorAssetTagRecordType          = 19
ProcessorMaxFsbFrequencyRecordType   = 20
ProcessorPackageNumberRecordType     = 21
ProcessorCoreFrequencyListRecordType = 22
ProcessorFsbFrequencyListRecordType  = 23
ProcessorHealthStatusRecordType      = 24
ProcessorCoreCountRecordType         = 25
ProcessorEnabledCoreCountRecordType  = 26
ProcessorThreadCountRecordType       = 27
ProcessorCharacteristicsRecordType   = 28
ProcessorFamily2RecordType           = 29
ProcessorPartNumberRecordType        = 30
EFI_CPU_VARIABLE_RECORD_TYPE         = UINTN

class EFI_CPU_VARIABLE_RECORD (Union):
  _fields_ = [
    ("ProcessorCoreFrequencyList",  EFI_PROCESSOR_CORE_FREQUENCY_LIST_DATA),
    ("ProcessorFsbFrequencyList",   EFI_PROCESSOR_FSB_FREQUENCY_LIST_DATA),
    ("ProcessorSerialNumber",       EFI_PROCESSOR_SERIAL_NUMBER_DATA),
    ("ProcessorCoreFrequency",      EFI_PROCESSOR_CORE_FREQUENCY_DATA),
    ("ProcessorFsbFrequency",       EFI_PROCESSOR_FSB_FREQUENCY_DATA),
    ("ProcessorMaxCoreFrequency",   EFI_PROCESSOR_MAX_CORE_FREQUENCY_DATA),
    ("ProcessorMaxFsbFrequency",    EFI_PROCESSOR_MAX_FSB_FREQUENCY_DATA),
    ("ProcessorVersion",            EFI_PROCESSOR_VERSION_DATA),
    ("ProcessorManufacturer",       EFI_PROCESSOR_MANUFACTURER_DATA),
    ("ProcessorId",                 EFI_PROCESSOR_ID_DATA),
    ("ProcessorType",               EFI_PROCESSOR_TYPE_DATA),
    ("ProcessorFamily",             EFI_PROCESSOR_FAMILY_DATA),
    ("ProcessorVoltage",            EFI_PROCESSOR_VOLTAGE_DATA),
    ("ProcessorApicBase",           EFI_PROCESSOR_APIC_BASE_ADDRESS_DATA),
    ("ProcessorApicId",             EFI_PROCESSOR_APIC_ID_DATA),
    ("ProcessorApicVersionNumber",  EFI_PROCESSOR_APIC_VERSION_NUMBER_DATA),
    ("CpuUcodeRevisionData",        EFI_PROCESSOR_MICROCODE_REVISION_DATA),
    ("ProcessorStatus",             EFI_PROCESSOR_STATUS_DATA),
    ("ProcessorSocketType",         EFI_PROCESSOR_SOCKET_TYPE_DATA),
    ("ProcessorSocketName",         EFI_PROCESSOR_SOCKET_NAME_DATA),
    ("ProcessorAssetTag",           EFI_PROCESSOR_ASSET_TAG_DATA),
    ("ProcessorPartNumber",         EFI_PROCESSOR_PART_NUMBER_DATA),
    ("ProcessorHealthStatus",       EFI_PROCESSOR_HEALTH_STATUS),
    ("ProcessorPackageNumber",      EFI_PROCESSOR_PACKAGE_NUMBER_DATA),
    ("ProcessorCoreCount",          EFI_PROCESSOR_CORE_COUNT_DATA),
    ("ProcessorEnabledCoreCount",   EFI_PROCESSOR_ENABLED_CORE_COUNT_DATA ),
    ("ProcessorThreadCount",        EFI_PROCESSOR_THREAD_COUNT_DATA),
    ("ProcessorCharacteristics",    EFI_PROCESSOR_CHARACTERISTICS_DATA),
    ("ProcessorFamily2",            EFI_PROCESSOR_FAMILY2_DATA)
  ]

class EFI_CPU_DATA_RECORD (Structure):
  _fields_ = [
    ("DataRecordHeader",  EFI_SUBCLASS_TYPE1_HEADER),
    ("VariableRecord",    EFI_CPU_VARIABLE_RECORD)
  ]

EFI_CACHE_SUBCLASS_VERSION    = 0x00010000
EFI_CACHE_SIZE_DATA           = EFI_EXP_BASE2_DATA

EFI_MAXIMUM_CACHE_SIZE_DATA   = EFI_EXP_BASE2_DATA
EFI_CACHE_SPEED_DATA          = EFI_EXP_BASE10_DATA
EFI_CACHE_SOCKET_DATA         = STRING_REF 

class EFI_CACHE_SRAM_TYPE_DATA (Structure):
  _fields_ = [
    ("Other",         UINT32, 1),
    ("Unknown",       UINT32, 1),
    ("NonBurst",      UINT32, 1),
    ("Burst",         UINT32, 1),
    ("PipelineBurst", UINT32, 1),
    ("Asynchronous",  UINT32, 1),
    ("Synchronous",   UINT32, 1),
    ("Reserved",      UINT32, 25)
  ]

EFI_CACHE_SRAM_INSTALL_DATA   = EFI_CACHE_SRAM_TYPE_DATA

EfiCacheErrorOther     = 1
EfiCacheErrorUnknown   = 2
EfiCacheErrorNone      = 3
EfiCacheErrorParity    = 4
EfiCacheErrorSingleBit = 5
EfiCacheErrorMultiBit  = 6
EFI_CACHE_ERROR_TYPE_DATA = UINTN

EfiCacheTypeOther       = 1
EfiCacheTypeUnknown     = 2
EfiCacheTypeInstruction = 3
EfiCacheTypeData        = 4
EfiCacheTypeUnified     = 5
EFI_CACHE_TYPE_DATA     = UINTN

EfiCacheAssociativityOther        = 1
EfiCacheAssociativityUnknown      = 2
EfiCacheAssociativityDirectMapped = 3
EfiCacheAssociativity2Way         = 4
EfiCacheAssociativity4Way         = 5
EfiCacheAssociativityFully        = 6
EfiCacheAssociativity8Way         = 7
EfiCacheAssociativity16Way        = 8
EFI_CACHE_ASSOCIATIVITY_DATA      = UINTN

class EFI_CACHE_CONFIGURATION_DATA (Structure):
  _fields_ = [
    ("Level",           UINT32, 3),
    ("Socketed",        UINT32, 1),
    ("Reserved2",       UINT32, 1),
    ("Location",        UINT32, 2),
    ("Enable",          UINT32, 1),
    ("OperationalMode", UINT32, 2),
    ("Reserved1",       UINT32, 22)
  ]

EFI_CACHE_L1            = 1
EFI_CACHE_L2            = 2
EFI_CACHE_L3            = 3
EFI_CACHE_L4            = 4
EFI_CACHE_LMAX          = EFI_CACHE_L4
EFI_CACHE_SOCKETED      = 1
EFI_CACHE_NOT_SOCKETED  = 0

EfiCacheInternal = 0
EfiCacheExternal = 1
EfiCacheReserved = 2
EfiCacheUnknown  = 3
EFI_CACHE_LOCATION  = UINTN

EFI_CACHE_ENABLED       = 1
EFI_CACHE_DISABLED      = 0

EfiCacheWriteThrough = 0
EfiCacheWriteBack    = 1
EfiCacheDynamicMode  = 2
EfiCacheUnknownMode  = 3
EFI_CACHE_OPERATIONAL_MODE = UINTN

CacheSizeRecordType              = 1
MaximumSizeCacheRecordType       = 2
CacheSpeedRecordType             = 3
CacheSocketRecordType            = 4
CacheSramTypeRecordType          = 5
CacheInstalledSramTypeRecordType = 6
CacheErrorTypeRecordType         = 7
CacheTypeRecordType              = 8
CacheAssociativityRecordType     = 9
CacheConfigRecordType            = 10
EFI_CACHE_VARIABLE_RECORD_TYPE  = UINTN

class EFI_CACHE_VARIABLE_RECORD (Union):
  _fields_ = [
    ("CacheSize",               EFI_CACHE_SIZE_DATA),
    ("MaximumCacheSize",        EFI_MAXIMUM_CACHE_SIZE_DATA),
    ("CacheSpeed",              EFI_CACHE_SPEED_DATA),
    ("CacheSocket",             EFI_CACHE_SOCKET_DATA),
    ("CacheSramType",           EFI_CACHE_SRAM_TYPE_DATA),
    ("CacheInstalledSramType",  EFI_CACHE_SRAM_TYPE_DATA),
    ("CacheErrorType",          EFI_CACHE_ERROR_TYPE_DATA),
    ("CacheType",               EFI_CACHE_TYPE_DATA),
    ("CacheAssociativity",      EFI_CACHE_ASSOCIATIVITY_DATA),
    ("CacheConfig",             EFI_CACHE_CONFIGURATION_DATA),
    ("CacheAssociation",        EFI_CACHE_ASSOCIATION_DATA)
  ]

class EFI_CACHE_DATA_RECORD (Structure):
  _fields_ = [
    ("DataRecordHeader",  EFI_SUBCLASS_TYPE1_HEADER),
    ("VariableRecord",    EFI_CACHE_VARIABLE_RECORD)
  ]

EFI_MEMORY_SUBCLASS_VERSION     = 0x0100
EFI_MEMORY_SIZE_RECORD_NUMBER   = 0x00000001

EfiMemoryRegionMemory             = 0x01
EfiMemoryRegionReserved           = 0x02
EfiMemoryRegionAcpi               = 0x03
EfiMemoryRegionNvs                = 0x04
EFI_MEMORY_REGION_TYPE            = UINTN

class EFI_MEMORY_SIZE_DATA (Structure):
  _fields_ = [
    ("ProcessorNumber",     UINT32),
    ("StartBusNumber",      UINT16),
    ("EndBusNumber",        UINT16),
    ("MemoryRegionType",    EFI_MEMORY_REGION_TYPE),
    ("MemorySize",          EFI_EXP_BASE2_DATA),
    ("MemoryStartAddress",  EFI_PHYSICAL_ADDRESS)
  ]

EFI_MEMORY_ARRAY_LOCATION_RECORD_NUMBER    = 0x00000002

EfiMemoryArrayLocationOther                 = 0x01
EfiMemoryArrayLocationUnknown               = 0x02
EfiMemoryArrayLocationSystemBoard           = 0x03
EfiMemoryArrayLocationIsaAddonCard          = 0x04
EfiMemoryArrayLocationEisaAddonCard         = 0x05
EfiMemoryArrayLocationPciAddonCard          = 0x06
EfiMemoryArrayLocationMcaAddonCard          = 0x07
EfiMemoryArrayLocationPcmciaAddonCard       = 0x08
EfiMemoryArrayLocationProprietaryAddonCard  = 0x09
EfiMemoryArrayLocationNuBus                 = 0x0A
EfiMemoryArrayLocationPc98C20AddonCard      = 0xA0
EfiMemoryArrayLocationPc98C24AddonCard      = 0xA1
EfiMemoryArrayLocationPc98EAddonCard        = 0xA2
EfiMemoryArrayLocationPc98LocalBusAddonCard = 0xA3
EFI_MEMORY_ARRAY_LOCATION                   = UINTN

EfiMemoryArrayUseOther                      = 0x01
EfiMemoryArrayUseUnknown                    = 0x02
EfiMemoryArrayUseSystemMemory               = 0x03
EfiMemoryArrayUseVideoMemory                = 0x04
EfiMemoryArrayUseFlashMemory                = 0x05
EfiMemoryArrayUseNonVolatileRam             = 0x06
EfiMemoryArrayUseCacheMemory                = 0x07
EFI_MEMORY_ARRAY_USE                        = UINTN

EfiMemoryErrorCorrectionOther               = 0x01
EfiMemoryErrorCorrectionUnknown             = 0x02
EfiMemoryErrorCorrectionNone                = 0x03
EfiMemoryErrorCorrectionParity              = 0x04
EfiMemoryErrorCorrectionSingleBitEcc        = 0x05
EfiMemoryErrorCorrectionMultiBitEcc         = 0x06
EfiMemoryErrorCorrectionCrc                 = 0x07
EFI_MEMORY_ERROR_CORRECTION                 = UINTN

class EFI_MEMORY_ARRAY_LOCATION_DATA (Structure):
  _fields_ = [
    ("MemoryArrayLocation",     EFI_MEMORY_ARRAY_LOCATION),
    ("MemoryArrayUse",          EFI_MEMORY_ARRAY_USE),
    ("MemoryErrorCorrection",   EFI_MEMORY_ERROR_CORRECTION),
    ("MaximumMemoryCapacity",   EFI_EXP_BASE2_DATA),
    ("NumberMemoryDevices",     UINT16)
  ]

EFI_MEMORY_ARRAY_LINK_RECORD_NUMBER    = 0x00000003

EfiMemoryFormFactorOther                    = 0x01
EfiMemoryFormFactorUnknown                  = 0x02
EfiMemoryFormFactorSimm                     = 0x03
EfiMemoryFormFactorSip                      = 0x04
EfiMemoryFormFactorChip                     = 0x05
EfiMemoryFormFactorDip                      = 0x06
EfiMemoryFormFactorZip                      = 0x07
EfiMemoryFormFactorProprietaryCard          = 0x08
EfiMemoryFormFactorDimm                     = 0x09
EfiMemoryFormFactorTsop                     = 0x0A
EfiMemoryFormFactorRowOfChips               = 0x0B
EfiMemoryFormFactorRimm                     = 0x0C
EfiMemoryFormFactorSodimm                   = 0x0D
EfiMemoryFormFactorSrimm                    = 0x0E
EfiMemoryFormFactorFbDimm                   = 0x0F
EFI_MEMORY_FORM_FACTOR                      = UINTN

EfiMemoryTypeOther                          = 0x01
EfiMemoryTypeUnknown                        = 0x02
EfiMemoryTypeDram                           = 0x03
EfiMemoryTypeEdram                          = 0x04
EfiMemoryTypeVram                           = 0x05
EfiMemoryTypeSram                           = 0x06
EfiMemoryTypeRam                            = 0x07
EfiMemoryTypeRom                            = 0x08
EfiMemoryTypeFlash                          = 0x09
EfiMemoryTypeEeprom                         = 0x0A
EfiMemoryTypeFeprom                         = 0x0B
EfiMemoryTypeEprom                          = 0x0C
EfiMemoryTypeCdram                          = 0x0D
EfiMemoryType3Dram                          = 0x0E
EfiMemoryTypeSdram                          = 0x0F
EfiMemoryTypeSgram                          = 0x10
EfiMemoryTypeRdram                          = 0x11
EfiMemoryTypeDdr                            = 0x12
EfiMemoryTypeDdr2                           = 0x13
EfiMemoryTypeDdr2FbDimm                     = 0x14
EFI_MEMORY_ARRAY_TYPE                       = UINTN

class EFI_MEMORY_TYPE_DETAIL (Structure):
  _fields_ = [
    ("Reserved",      UINT32, 1),
    ("Other",         UINT32, 1),
    ("Unknown",       UINT32, 1),
    ("FastPaged",     UINT32, 1),
    ("StaticColumn",  UINT32, 1),
    ("PseudoStatic",  UINT32, 1),
    ("Rambus",        UINT32, 1),
    ("Synchronous",   UINT32, 1),
    ("Cmos",          UINT32, 1),
    ("Edo",           UINT32, 1),
    ("WindowDram",    UINT32, 1),
    ("CacheDram",     UINT32, 1),
    ("Nonvolatile",   UINT32, 1),
    ("Reserved1",     UINT32, 19)
  ]

EfiMemoryStateEnabled      = 0
EfiMemoryStateUnknown      = 1
EfiMemoryStateUnsupported  = 2
EfiMemoryStateError        = 3
EfiMemoryStateAbsent       = 4
EfiMemoryStateDisabled     = 5
EfiMemoryStatePartial      = 6
EFI_MEMORY_STATE           = UINTN

class EFI_MEMORY_ARRAY_LINK_DATA (Structure):
  _fields_ = [
    ("MemoryDeviceLocator", STRING_REF),
    ("MemoryBankLocator",   STRING_REF),
    ("MemoryManufacturer",  STRING_REF),
    ("MemorySerialNumber",  STRING_REF),
    ("MemoryAssetTag",      STRING_REF),
    ("MemoryPartNumber",    STRING_REF),
    ("MemoryArrayLink",     EFI_INTER_LINK_DATA),
    ("MemorySubArrayLink",  EFI_INTER_LINK_DATA),
    ("MemoryTotalWidth",    UINT16),
    ("MemoryDataWidth",     UINT16),
    ("MemoryDeviceSize",    EFI_EXP_BASE2_DATA),
    ("MemoryFormFactor",    EFI_MEMORY_FORM_FACTOR),
    ("MemoryDeviceSet",     UINT8),
    ("MemoryType",          EFI_MEMORY_ARRAY_TYPE ),
    ("MemoryTypeDetail",    EFI_MEMORY_TYPE_DETAIL),
    ("MemorySpeed",         EFI_EXP_BASE10_DATA),
    ("MemoryState",         EFI_MEMORY_STATE)
  ]

EFI_MEMORY_ARRAY_START_ADDRESS_RECORD_NUMBER    = 0x00000004

class EFI_MEMORY_ARRAY_START_ADDRESS_DATA (Structure):
  _fields_ = [
    ("MemoryArrayStartAddress",   EFI_PHYSICAL_ADDRESS),
    ("MemoryArrayEndAddress",     EFI_PHYSICAL_ADDRESS),
    ("PhysicalMemoryArrayLink",   EFI_INTER_LINK_DATA),
    ("MemoryArrayPartitionWidth", UINT16)
  ]

EFI_MEMORY_DEVICE_START_ADDRESS_RECORD_NUMBER    = 0x00000005

class EFI_MEMORY_DEVICE_START_ADDRESS_DATA (Structure):
  _fields_ = [
    ("MemoryDeviceStartAddress",          EFI_PHYSICAL_ADDRESS),
    ("MemoryDeviceEndAddress",            EFI_PHYSICAL_ADDRESS),
    ("PhysicalMemoryDeviceLink",          EFI_INTER_LINK_DATA),
    ("PhysicalMemoryArrayLink",           EFI_INTER_LINK_DATA),
    ("MemoryDevicePartitionRowPosition",  UINT8),
    ("MemoryDeviceInterleavePosition",    UINT8),
    ("MemoryDeviceInterleaveDataDepth",   UINT8)
  ]

EfiMemoryChannelTypeOther                   = 1
EfiMemoryChannelTypeUnknown                 = 2
EfiMemoryChannelTypeRambus                  = 3
EfiMemoryChannelTypeSyncLink                = 4
EFI_MEMORY_CHANNEL_TYPE                     = UINTN

class EFI_MEMORY_CHANNEL_TYPE_DATA (Structure):
  _fields_ = [
    ("MemoryChannelType",         EFI_MEMORY_CHANNEL_TYPE),
    ("MemoryChannelMaximumLoad",  UINT8),
    ("MemoryChannelDeviceCount",  UINT8)
  ]

EFI_MEMORY_CHANNEL_DEVICE_RECORD_NUMBER    = 0x00000007

class EFI_MEMORY_CHANNEL_DEVICE_DATA (Structure):
  _fields_ = [
    ("DeviceId",                UINT8),
    ("DeviceLink",              EFI_INTER_LINK_DATA),
    ("MemoryChannelDeviceLoad", UINT8)
  ]

EFI_MEMORY_CONTROLLER_INFORMATION_RECORD_NUMBER    = 0x00000008

EfiErrorDetectingMethodOther   = 1
EfiErrorDetectingMethodUnknown = 2
EfiErrorDetectingMethodNone    = 3
EfiErrorDetectingMethodParity  = 4
EfiErrorDetectingMethod32Ecc   = 5
EfiErrorDetectingMethod64Ecc   = 6
EfiErrorDetectingMethod128Ecc  = 7
EfiErrorDetectingMethodCrc     = 8
EFI_MEMORY_ERROR_DETECT_METHOD_TYPE = UINTN

class EFI_MEMORY_ERROR_CORRECT_CAPABILITY (Structure):
  _fields_ = [
    ("Other",                 UINT8, 1),
    ("Unknown",               UINT8, 1),
    ("None",                  UINT8, 1),
    ("SingleBitErrorCorrect", UINT8, 1),
    ("DoubleBitErrorCorrect", UINT8, 1),
    ("ErrorScrubbing",        UINT8, 1),
    ("Reserved",              UINT8, 2)
  ]

EfiMemoryInterleaveOther      = 1
EfiMemoryInterleaveUnknown    = 2
EfiMemoryInterleaveOneWay     = 3
EfiMemoryInterleaveTwoWay     = 4
EfiMemoryInterleaveFourWay    = 5
EfiMemoryInterleaveEightWay   = 6
EfiMemoryInterleaveSixteenWay = 7
EFI_MEMORY_SUPPORT_INTERLEAVE_TYPE  = UINTN

class EFI_MEMORY_SPEED_TYPE (Structure):
  _fields_ = [
    ("Other",     UINT16, 1),
    ("Unknown",   UINT16, 1),
    ("SeventyNs", UINT16, 1),
    ("SixtyNs",   UINT16, 1),
    ("FiftyNs",   UINT16, 1),
    ("Reserved",  UINT16, 11)
  ]

class EFI_MEMORY_SUPPORTED_TYPE (Structure):
  _fields_ = [
    ("Other",         UINT16, 1),
    ("Unknown",       UINT16, 1),
    ("Standard",      UINT16, 1),
    ("FastPageMode",  UINT16, 1),
    ("EDO",           UINT16, 1),
    ("Parity",        UINT16, 1),
    ("ECC",           UINT16, 1),
    ("SIMM",          UINT16, 1),
    ("DIMM",          UINT16, 1),
    ("BurstEdo",      UINT16, 1),
    ("SDRAM",         UINT16, 1),
    ("Reserved",      UINT16, 5)
  ]

class EFI_MEMORY_MODULE_VOLTAGE_TYPE (Structure):
  _fields_ = [
    ("Five",      UINT8, 1),
    ("Three",     UINT8, 1),
    ("Two",       UINT8, 1),
    ("Reserved",  UINT8, 5)
  ]

class EFI_MEMORY_CONTROLLER_INFORMATION (Structure):
  _fields_ = [
    ("ErrorDetectingMethod",          EFI_MEMORY_ERROR_DETECT_METHOD_TYPE),
    ("ErrorCorrectingCapability",     EFI_MEMORY_ERROR_CORRECT_CAPABILITY),
    ("MemorySupportedInterleave",     EFI_MEMORY_SUPPORT_INTERLEAVE_TYPE),
    ("MemoryCurrentInterleave",       EFI_MEMORY_SUPPORT_INTERLEAVE_TYPE),
    ("MaxMemoryModuleSize",           UINT8),
    ("MemorySpeedType",               EFI_MEMORY_SPEED_TYPE),
    ("MemorySupportedType",           EFI_MEMORY_SUPPORTED_TYPE),
    ("MemoryModuleVoltage",           EFI_MEMORY_MODULE_VOLTAGE_TYPE),
    ("NumberofMemorySlot",            UINT8),
    ("EnabledCorrectingCapability",   EFI_MEMORY_ERROR_CORRECT_CAPABILITY),
    ("MemoryModuleConfigHandles",     POINTER(UINT16))
  ]

class EFI_MEMORY_CONTROLLER_INFORMATION_DATA (Structure):
  _fields_ = [
    ("ErrorDetectingMethod",        EFI_MEMORY_ERROR_DETECT_METHOD_TYPE),
    ("ErrorCorrectingCapability",   EFI_MEMORY_ERROR_CORRECT_CAPABILITY),
    ("MemorySupportedInterleave",   EFI_MEMORY_SUPPORT_INTERLEAVE_TYPE),
    ("MemoryCurrentInterleave",     EFI_MEMORY_SUPPORT_INTERLEAVE_TYPE),
    ("MaxMemoryModuleSize",         UINT8),
    ("MemorySpeedType",             EFI_MEMORY_SPEED_TYPE),
    ("MemorySupportedType",         EFI_MEMORY_SUPPORTED_TYPE),
    ("MemoryModuleVoltage",         EFI_MEMORY_MODULE_VOLTAGE_TYPE),
    ("NumberofMemorySlot",          UINT8),
    ("EnabledCorrectingCapability", EFI_MEMORY_ERROR_CORRECT_CAPABILITY),
    ("MemoryModuleConfig",          EFI_INTER_LINK_DATA * 1)
  ]

EFI_MEMORY_32BIT_ERROR_INFORMATION_RECORD_NUMBER    = 0x00000009

EfiMemoryErrorOther             = 1
EfiMemoryErrorUnknown           = 2
EfiMemoryErrorOk                = 3
EfiMemoryErrorBadRead           = 4
EfiMemoryErrorParity            = 5
EfiMemoryErrorSigleBit          = 6
EfiMemoryErrorDoubleBit         = 7
EfiMemoryErrorMultiBit          = 8
EfiMemoryErrorNibble            = 9
EfiMemoryErrorChecksum          = 10
EfiMemoryErrorCrc               = 11
EfiMemoryErrorCorrectSingleBit  = 12
EfiMemoryErrorCorrected         = 13
EfiMemoryErrorUnCorrectable     = 14
EFI_MEMORY_ERROR_TYPE           = UINTN

EfiMemoryGranularityOther               = 1
EfiMemoryGranularityOtherUnknown        = 2
EfiMemoryGranularityDeviceLevel         = 3
EfiMemoryGranularityMemPartitionLevel   = 4
EFI_MEMORY_ERROR_GRANULARITY_TYPE       = UINTN

EfiMemoryErrorOperationOther            = 1
EfiMemoryErrorOperationUnknown          = 2
EfiMemoryErrorOperationRead             = 3
EfiMemoryErrorOperationWrite            = 4
EfiMemoryErrorOperationPartialWrite     = 5
EFI_MEMORY_ERROR_OPERATION_TYPE         = UINTN

class EFI_MEMORY_32BIT_ERROR_INFORMATION (Structure):
  _fields_ = [
    ("MemoryErrorType",         EFI_MEMORY_ERROR_TYPE),
    ("MemoryErrorGranularity",  EFI_MEMORY_ERROR_GRANULARITY_TYPE),
    ("MemoryErrorOperation",    EFI_MEMORY_ERROR_OPERATION_TYPE),
    ("VendorSyndrome",          UINT32),
    ("MemoryArrayErrorAddress", UINT32),
    ("DeviceErrorAddress",      UINT32),
    ("DeviceErrorResolution",   UINT32)
  ]

EFI_MEMORY_64BIT_ERROR_INFORMATION_RECORD_NUMBER    = 0x0000000A

class EFI_MEMORY_64BIT_ERROR_INFORMATION (Structure):
  _fields_ = [
    ("MemoryErrorType",         EFI_MEMORY_ERROR_TYPE),
    ("MemoryErrorGranularity",  EFI_MEMORY_ERROR_GRANULARITY_TYPE),
    ("MemoryErrorOperation",    EFI_MEMORY_ERROR_OPERATION_TYPE),
    ("VendorSyndrome",          UINT32),
    ("MemoryArrayErrorAddress", UINT64),
    ("DeviceErrorAddress",      UINT64),
    ("DeviceErrorResolution",   UINT32)
  ]

class EFI_MEMORY_SUBCLASS_RECORDS (Union):
  _fields_ = [
    ("SizeData",              EFI_MEMORY_SIZE_DATA),
    ("ArrayLocationData",     EFI_MEMORY_ARRAY_LOCATION_DATA),
    ("ArrayLink",             EFI_MEMORY_ARRAY_LINK_DATA),
    ("ArrayStartAddress",     EFI_MEMORY_ARRAY_START_ADDRESS_DATA),
    ("DeviceStartAddress",    EFI_MEMORY_DEVICE_START_ADDRESS_DATA),
    ("ChannelTypeData",       EFI_MEMORY_CHANNEL_TYPE_DATA),
    ("ChannelDeviceData",     EFI_MEMORY_CHANNEL_DEVICE_DATA),
    ("MemoryControllerInfo",  EFI_MEMORY_CONTROLLER_INFORMATION),
    ("Memory32bitErrorInfo",  EFI_MEMORY_32BIT_ERROR_INFORMATION),
    ("Memory64bitErrorInfo",  EFI_MEMORY_64BIT_ERROR_INFORMATION)
  ]

class EFI_MEMORY_SUBCLASS_DRIVER_DATA (Structure):
  _fields_ = [
    ("Header",  EFI_SUBCLASS_TYPE1_HEADER),
    ("Record",  EFI_MEMORY_SUBCLASS_RECORDS)
  ]

EFI_MISC_SUBCLASS_VERSION     = 0x0100

EFI_MISC_LAST_PCI_BUS_RECORD_NUMBER    = 0x00000001

class EFI_MISC_LAST_PCI_BUS_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("LastPciBus",  UINT8)
  ]

EFI_MISC_BIOS_VENDOR_RECORD_NUMBER    = 0x00000002

class EFI_MISC_BIOS_CHARACTERISTICS (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                             UINT64, 2),
    ("Unknown",                               UINT64, 1),
    ("BiosCharacteristicsNotSupported",       UINT64, 1),
    ("IsaIsSupported",                        UINT64, 1),
    ("McaIsSupported",                        UINT64, 1),
    ("EisaIsSupported",                       UINT64, 1),
    ("PciIsSupported",                        UINT64, 1),
    ("PcmciaIsSupported",                     UINT64, 1),
    ("PlugAndPlayIsSupported",                UINT64, 1),
    ("ApmIsSupported",                        UINT64, 1),
    ("BiosIsUpgradable",                      UINT64, 1),
    ("BiosShadowingAllowed",                  UINT64, 1),
    ("VlVesaIsSupported",                     UINT64, 1),
    ("EscdSupportIsAvailable",                UINT64, 1),
    ("BootFromCdIsSupported",                 UINT64, 1),
    ("SelectableBootIsSupported",             UINT64, 1),
    ("RomBiosIsSocketed",                     UINT64, 1),
    ("BootFromPcmciaIsSupported",             UINT64, 1),
    ("EDDSpecificationIsSupported",           UINT64, 1),
    ("JapaneseNecFloppyIsSupported",          UINT64, 1),
    ("JapaneseToshibaFloppyIsSupported",      UINT64, 1),
    ("Floppy525_360IsSupported",              UINT64, 1),
    ("Floppy525_12IsSupported",               UINT64, 1),
    ("Floppy35_720IsSupported",               UINT64, 1),
    ("Floppy35_288IsSupported",               UINT64, 1),
    ("PrintScreenIsSupported",                UINT64, 1),
    ("Keyboard8042IsSupported",               UINT64, 1),
    ("SerialIsSupported",                     UINT64, 1),
    ("PrinterIsSupported",                    UINT64, 1),
    ("CgaMonoIsSupported",                    UINT64, 1),
    ("NecPc98",                               UINT64, 1),
    ("AcpiIsSupported",                       UINT64, 1),
    ("UsbLegacyIsSupported",                  UINT64, 1),
    ("AgpIsSupported",                        UINT64, 1),
    ("I20BootIsSupported",                    UINT64, 1),
    ("Ls120BootIsSupported",                  UINT64, 1),
    ("AtapiZipDriveBootIsSupported",          UINT64, 1),
    ("Boot1394IsSupported",                   UINT64, 1),
    ("SmartBatteryIsSupported",               UINT64, 1),
    ("BiosBootSpecIsSupported",               UINT64, 1),
    ("FunctionKeyNetworkBootIsSupported",     UINT64, 1),
    ("Reserved",                              UINT64, 22)
  ]

class EFI_MISC_BIOS_CHARACTERISTICS_EXTENSION (Structure):
  _pack_   = 1
  _fields_ = [
    ("BiosReserved",    UINT64, 16),
    ("SystemReserved",  UINT64, 16),
    ("Reserved",        UINT64, 32)
  ]

class EFI_MISC_BIOS_VENDOR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("BiosVendor",                          STRING_REF),
    ("BiosVersion",                         STRING_REF),
    ("BiosReleaseDate",                     STRING_REF),
    ("BiosStartingAddress",                 EFI_PHYSICAL_ADDRESS),
    ("BiosPhysicalDeviceSize",              EFI_EXP_BASE2_DATA),
    ("BiosCharacteristics1",                EFI_MISC_BIOS_CHARACTERISTICS),
    ("BiosCharacteristics2              ",  EFI_MISC_BIOS_CHARACTERISTICS_EXTENSION),
    ("BiosMajorRelease",                    UINT8),
    ("BiosMinorRelease",                    UINT8),
    ("BiosEmbeddedFirmwareMajorRelease",    UINT8),
    ("BiosEmbeddedFirmwareMinorRelease",    UINT8)
  ]

EFI_MISC_SYSTEM_MANUFACTURER_RECORD_NUMBER    = 0x00000003

EfiSystemWakeupTypeReserved        = 0
EfiSystemWakeupTypeOther           = 1
EfiSystemWakeupTypeUnknown         = 2
EfiSystemWakeupTypeApmTimer        = 3
EfiSystemWakeupTypeModemRing       = 4
EfiSystemWakeupTypeLanRemote       = 5
EfiSystemWakeupTypePowerSwitch     = 6
EfiSystemWakeupTypePciPme          = 7
EfiSystemWakeupTypeAcPowerRestored = 8
EFI_MISC_SYSTEM_WAKEUP_TYPE        = UINTN

class EFI_MISC_SYSTEM_MANUFACTURER_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("SystemManufacturer",  STRING_REF),
    ("SystemProductName",   STRING_REF),
    ("SystemVersion",       STRING_REF),
    ("SystemSerialNumber",  STRING_REF),
    ("SystemUuid",          EFI_GUID),
    ("SystemWakeupType",    EFI_MISC_SYSTEM_WAKEUP_TYPE),
    ("SystemSKUNumber",     STRING_REF),
    ("SystemFamily",        STRING_REF)
  ]

class EFI_BASE_BOARD_FEATURE_FLAGS (Structure):
  _pack_   = 1
  _fields_ = [
    ("Motherboard",           UINT32, 1),
    ("RequiresDaughterCard",  UINT32, 1),
    ("Removable",             UINT32, 1),
    ("Replaceable",           UINT32, 1),
    ("HotSwappable",          UINT32, 1),
    ("Reserved",              UINT32, 27)
  ]

EfiBaseBoardTypeUnknown                = 1
EfiBaseBoardTypeOther                  = 2
EfiBaseBoardTypeServerBlade            = 3
EfiBaseBoardTypeConnectivitySwitch     = 4
EfiBaseBoardTypeSystemManagementModule = 5
EfiBaseBoardTypeProcessorModule        = 6
EfiBaseBoardTypeIOModule               = 7
EfiBaseBoardTypeMemoryModule           = 8
EfiBaseBoardTypeDaughterBoard          = 9
EfiBaseBoardTypeMotherBoard            = 0xA
EfiBaseBoardTypeProcessorMemoryModule  = 0xB
EfiBaseBoardTypeProcessorIOModule      = 0xC
EfiBaseBoardTypeInterconnectBoard      = 0xD
EFI_BASE_BOARD_TYPE                    = UINTN

class EFI_MISC_BASE_BOARD_MANUFACTURER_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("BaseBoardManufacturer",     STRING_REF),
    ("BaseBoardProductName",      STRING_REF),
    ("BaseBoardVersion",          STRING_REF),
    ("BaseBoardSerialNumber",     STRING_REF),
    ("BaseBoardAssetTag",         STRING_REF),
    ("BaseBoardChassisLocation",  STRING_REF),
    ("BaseBoardFeatureFlags",     EFI_BASE_BOARD_FEATURE_FLAGS),
    ("BaseBoardType",             EFI_BASE_BOARD_TYPE),
    ("BaseBoardChassisLink",      EFI_INTER_LINK_DATA),
    ("BaseBoardNumberLinks",      UINT32),
    ("LinkN",                     EFI_INTER_LINK_DATA)
  ]

EFI_MISC_CHASSIS_MANUFACTURER_RECORD_NUMBER    = 0x00000005

EfiMiscChassisTypeOther               = 0x1
EfiMiscChassisTypeUnknown             = 0x2
EfiMiscChassisTypeDeskTop             = 0x3
EfiMiscChassisTypeLowProfileDesktop   = 0x4
EfiMiscChassisTypePizzaBox            = 0x5
EfiMiscChassisTypeMiniTower           = 0x6
EfiMiscChassisTypeTower               = 0x7
EfiMiscChassisTypePortable            = 0x8
EfiMiscChassisTypeLapTop              = 0x9
EfiMiscChassisTypeNotebook            = 0xA
EfiMiscChassisTypeHandHeld            = 0xB
EfiMiscChassisTypeDockingStation      = 0xC
EfiMiscChassisTypeAllInOne            = 0xD
EfiMiscChassisTypeSubNotebook         = 0xE
EfiMiscChassisTypeSpaceSaving         = 0xF
EfiMiscChassisTypeLunchBox            = 0x10
EfiMiscChassisTypeMainServerChassis   = 0x11
EfiMiscChassisTypeExpansionChassis    = 0x12
EfiMiscChassisTypeSubChassis          = 0x13
EfiMiscChassisTypeBusExpansionChassis = 0x14
EfiMiscChassisTypePeripheralChassis   = 0x15
EfiMiscChassisTypeRaidChassis         = 0x16
EfiMiscChassisTypeRackMountChassis    = 0x17
EfiMiscChassisTypeSealedCasePc        = 0x18
EfiMiscChassisMultiSystemChassis      = 0x19
EFI_MISC_CHASSIS_TYPE                 = UINTN

class EFI_MISC_CHASSIS_STATUS (Structure):
  _pack_   = 1
  _fields_ = [
    ("ChassisType",         UINT32, 16),
    ("ChassisLockPresent",  UINT32, 1),
    ("Reserved",            UINT32, 15)
  ]

EfiChassisStateOther           = 0x01
EfiChassisStateUnknown         = 0x02
EfiChassisStateSafe            = 0x03
EfiChassisStateWarning         = 0x04
EfiChassisStateCritical        = 0x05
EfiChassisStateNonRecoverable  = 0x06
EFI_MISC_CHASSIS_STATE         = UINTN

EfiChassisSecurityStatusOther                          = 0x01
EfiChassisSecurityStatusUnknown                        = 0x02
EfiChassisSecurityStatusNone                           = 0x03
EfiChassisSecurityStatusExternalInterfaceLockedOut     = 0x04
EfiChassisSecurityStatusExternalInterfaceLockedEnabled = 0x05
EFI_MISC_CHASSIS_SECURITY_STATE                        = UINTN

class EFI_MISC_ELEMENT_TYPE (Structure):
  _pack_   = 1
  _fields_ = [
    ("RecordType",  UINT32, 1),
    ("Type",        UINT32, 7),
    ("Reserved",    UINT32, 24)
  ]

class EFI_MISC_ELEMENTS (Structure):
  _pack_   = 1
  _fields_ = [
    ("ChassisElementType",        EFI_MISC_ELEMENT_TYPE),
    ("ChassisElementStructure",   EFI_INTER_LINK_DATA),
    ("ChassisBaseBoard",          EFI_BASE_BOARD_TYPE),
    ("ChassisElementMinimum",     UINT32),
    ("ChassisElementMaximum",     UINT32)
  ]

class EFI_MISC_CHASSIS_MANUFACTURER_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ChassisManufacturer",         STRING_REF),
    ("ChassisVersion",              STRING_REF),
    ("ChassisSerialNumber",         STRING_REF),
    ("ChassisAssetTag",             STRING_REF),
    ("ChassisType",                 EFI_MISC_CHASSIS_STATUS),
    ("ChassisBootupState",          EFI_MISC_CHASSIS_STATE),
    ("ChassisPowerSupplyState",     EFI_MISC_CHASSIS_STATE),
    ("ChassisThermalState",         EFI_MISC_CHASSIS_STATE),
    ("ChassisSecurityState",        EFI_MISC_CHASSIS_SECURITY_STATE),
    ("ChassisOemDefined",           UINT32),
    ("ChassisHeight",               UINT32),
    ("ChassisNumberPowerCords",     UINT32),
    ("ChassisElementCount",         UINT32),
    ("ChassisElementRecordLength",  UINT32),
    ("ChassisElements",             EFI_MISC_ELEMENTS)
  ]

EFI_MISC_PORT_INTERNAL_CONNECTOR_DESIGNATOR_RECORD_NUMBER    = 0x00000006

EfiPortConnectorTypeNone                   = 0x00
EfiPortConnectorTypeCentronics             = 0x01
EfiPortConnectorTypeMiniCentronics         = 0x02
EfiPortConnectorTypeProprietary            = 0x03
EfiPortConnectorTypeDB25Male               = 0x04
EfiPortConnectorTypeDB25Female             = 0x05
EfiPortConnectorTypeDB15Male               = 0x06
EfiPortConnectorTypeDB15Female             = 0x07
EfiPortConnectorTypeDB9Male                = 0x08
EfiPortConnectorTypeDB9Female              = 0x09
EfiPortConnectorTypeRJ11                   = 0x0A
EfiPortConnectorTypeRJ45                   = 0x0B
EfiPortConnectorType50PinMiniScsi          = 0x0C
EfiPortConnectorTypeMiniDin                = 0x0D
EfiPortConnectorTypeMicriDin               = 0x0E
EfiPortConnectorTypePS2                    = 0x0F
EfiPortConnectorTypeInfrared               = 0x10
EfiPortConnectorTypeHpHil                  = 0x11
EfiPortConnectorTypeUsb                    = 0x12
EfiPortConnectorTypeSsaScsi                = 0x13
EfiPortConnectorTypeCircularDin8Male       = 0x14
EfiPortConnectorTypeCircularDin8Female     = 0x15
EfiPortConnectorTypeOnboardIde             = 0x16
EfiPortConnectorTypeOnboardFloppy          = 0x17
EfiPortConnectorType9PinDualInline         = 0x18
EfiPortConnectorType25PinDualInline        = 0x19
EfiPortConnectorType50PinDualInline        = 0x1A
EfiPortConnectorType68PinDualInline        = 0x1B
EfiPortConnectorTypeOnboardSoundInput      = 0x1C
EfiPortConnectorTypeMiniCentronicsType14   = 0x1D
EfiPortConnectorTypeMiniCentronicsType26   = 0x1E
EfiPortConnectorTypeHeadPhoneMiniJack      = 0x1F
EfiPortConnectorTypeBNC                    = 0x20
EfiPortConnectorType1394                   = 0x21
EfiPortConnectorTypePC98                   = 0xA0
EfiPortConnectorTypePC98Hireso             = 0xA1
EfiPortConnectorTypePCH98                  = 0xA2
EfiPortConnectorTypePC98Note               = 0xA3
EfiPortConnectorTypePC98Full               = 0xA4
EfiPortConnectorTypeOther                  = 0xFF
EFI_MISC_PORT_CONNECTOR_TYPE               = UINTN

EfiPortTypeNone                      = 0x00
EfiPortTypeParallelXtAtCompatible    = 0x01
EfiPortTypeParallelPortPs2           = 0x02
EfiPortTypeParallelPortEcp           = 0x03
EfiPortTypeParallelPortEpp           = 0x04
EfiPortTypeParallelPortEcpEpp        = 0x05
EfiPortTypeSerialXtAtCompatible      = 0x06
EfiPortTypeSerial16450Compatible     = 0x07
EfiPortTypeSerial16550Compatible     = 0x08
EfiPortTypeSerial16550ACompatible    = 0x09
EfiPortTypeScsi                      = 0x0A
EfiPortTypeMidi                      = 0x0B
EfiPortTypeJoyStick                  = 0x0C
EfiPortTypeKeyboard                  = 0x0D
EfiPortTypeMouse                     = 0x0E
EfiPortTypeSsaScsi                   = 0x0F
EfiPortTypeUsb                       = 0x10
EfiPortTypeFireWire                  = 0x11
EfiPortTypePcmciaTypeI               = 0x12
EfiPortTypePcmciaTypeII              = 0x13
EfiPortTypePcmciaTypeIII             = 0x14
EfiPortTypeCardBus                   = 0x15
EfiPortTypeAccessBusPort             = 0x16
EfiPortTypeScsiII                    = 0x17
EfiPortTypeScsiWide                  = 0x18
EfiPortTypePC98                      = 0x19
EfiPortTypePC98Hireso                = 0x1A
EfiPortTypePCH98                     = 0x1B
EfiPortTypeVideoPort                 = 0x1C
EfiPortTypeAudioPort                 = 0x1D
EfiPortTypeModemPort                 = 0x1E
EfiPortTypeNetworkPort               = 0x1F
EfiPortType8251Compatible            = 0xA0
EfiPortType8251FifoCompatible        = 0xA1
EfiPortTypeOther                     = 0xFF
EFI_MISC_PORT_TYPE                   = UINTN

class EFI_MISC_PORT_INTERNAL_CONNECTOR_DESIGNATOR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("PortInternalConnectorDesignator",   STRING_REF),
    ("PortExternalConnectorDesignator",   STRING_REF),
    ("PortInternalConnectorType",         EFI_MISC_PORT_CONNECTOR_TYPE),
    ("PortExternalConnectorType",         EFI_MISC_PORT_CONNECTOR_TYPE),
    ("PortType",                          EFI_MISC_PORT_TYPE),
    ("PortPath",                          EFI_MISC_PORT_DEVICE_PATH)
  ]

EFI_MISC_SYSTEM_SLOT_DESIGNATION_RECORD_NUMBER    = 0x00000007

EfiSlotTypeOther                        = 0x01
EfiSlotTypeUnknown                      = 0x02
EfiSlotTypeIsa                          = 0x03
EfiSlotTypeMca                          = 0x04
EfiSlotTypeEisa                         = 0x05
EfiSlotTypePci                          = 0x06
EfiSlotTypePcmcia                       = 0x07
EfiSlotTypeVlVesa                       = 0x08
EfiSlotTypeProprietary                  = 0x09
EfiSlotTypeProcessorCardSlot            = 0x0A
EfiSlotTypeProprietaryMemoryCardSlot    = 0x0B
EfiSlotTypeIORiserCardSlot              = 0x0C
EfiSlotTypeNuBus                        = 0x0D
EfiSlotTypePci66MhzCapable              = 0x0E
EfiSlotTypeAgp                          = 0x0F
EfiSlotTypeAgp2X                        = 0x10
EfiSlotTypeAgp4X                        = 0x11
EfiSlotTypePciX                         = 0x12
EfiSlotTypeAgp8x                        = 0x13
EfiSlotTypePC98C20                      = 0xA0
EfiSlotTypePC98C24                      = 0xA1
EfiSlotTypePC98E                        = 0xA2
EfiSlotTypePC98LocalBus                 = 0xA3
EfiSlotTypePC98Card                     = 0xA4
EfiSlotTypePciExpress                   = 0xA5
EfiSlotTypePciExpressX1                 = 0xA6
EfiSlotTypePciExpressX2                 = 0xA7
EfiSlotTypePciExpressX4                 = 0xA8
EfiSlotTypePciExpressX8                 = 0xA9
EfiSlotTypePciExpressX16                = 0xAA
EFI_MISC_SLOT_TYPE                      = UINTN

EfiSlotDataBusWidthOther      = 0x01
EfiSlotDataBusWidthUnknown    = 0x02
EfiSlotDataBusWidth8Bit       = 0x03
EfiSlotDataBusWidth16Bit      = 0x04
EfiSlotDataBusWidth32Bit      = 0x05
EfiSlotDataBusWidth64Bit      = 0x06
EfiSlotDataBusWidth128Bit     = 0x07
EfiSlotDataBusWidth1xOrx1     = 0x8
EfiSlotDataBusWidth2xOrx2     = 0x9
EfiSlotDataBusWidth4xOrx4     = 0xA
EfiSlotDataBusWidth8xOrx8     = 0xB
EfiSlotDataBusWidth12xOrx12   = 0xC
EfiSlotDataBusWidth16xOrx16   = 0xD
EfiSlotDataBusWidth32xOrx32   = 0xE
EFI_MISC_SLOT_DATA_BUS_WIDTH  = UINTN

EfiSlotUsageOther     = 1
EfiSlotUsageUnknown   = 2
EfiSlotUsageAvailable = 3
EfiSlotUsageInUse     = 4
EFI_MISC_SLOT_USAGE   = UINTN

EfiSlotLengthOther   = 1
EfiSlotLengthUnknown = 2
EfiSlotLengthShort   = 3
EfiSlotLengthLong    = 4
EFI_MISC_SLOT_LENGTH = UINTN
class EFI_MISC_SLOT_CHARACTERISTICS (Structure):
  _pack_   = 1
  _fields_ = [
    ("CharacteristicsUnknown",    UINT32, 1),
    ("Provides50Volts",           UINT32, 1),
    ("Provides33Volts",           UINT32, 1),
    ("SharedSlot",                UINT32, 1),
    ("PcCard16Supported",         UINT32, 1),
    ("CardBusSupported",          UINT32, 1),
    ("ZoomVideoSupported",        UINT32, 1),
    ("ModemRingResumeSupported",  UINT32, 1),
    ("PmeSignalSupported",        UINT32, 1),
    ("HotPlugDevicesSupported",   UINT32, 1),
    ("SmbusSignalSupported",      UINT32, 1),
    ("Reserved",                  UINT32, 21)
  ]

class EFI_MISC_SYSTEM_SLOT_DESIGNATION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("SlotDesignation",       STRING_REF),
    ("SlotType",              EFI_MISC_SLOT_TYPE),
    ("SlotDataBusWidth",      EFI_MISC_SLOT_DATA_BUS_WIDTH),
    ("SlotUsage",             EFI_MISC_SLOT_USAGE),
    ("SlotLength",            EFI_MISC_SLOT_LENGTH),
    ("SlotId",                UINT16),
    ("SlotCharacteristics",   EFI_MISC_SLOT_CHARACTERISTICS),
    ("SlotDevicePath",        EFI_DEVICE_PATH_PROTOCOL)
  ]

EFI_MISC_ONBOARD_DEVICE_RECORD_NUMBER    = 0x00000008

EfiOnBoardDeviceTypeOther          = 1
EfiOnBoardDeviceTypeUnknown        = 2
EfiOnBoardDeviceTypeVideo          = 3
EfiOnBoardDeviceTypeScsiController = 4
EfiOnBoardDeviceTypeEthernet       = 5
EfiOnBoardDeviceTypeTokenRing      = 6
EfiOnBoardDeviceTypeSound          = 7
EFI_MISC_ONBOARD_DEVICE_TYPE       = UINTN

class EFI_MISC_ONBOARD_DEVICE_STATUS (Structure):
  _pack_   = 1
  _fields_ = [
    ("DeviceType",    UINT32, 16),
    ("DeviceEnabled", UINT32, 1),
    ("Reserved",      UINT32, 15)
  ]

class EFI_MISC_ONBOARD_DEVICE_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("OnBoardDeviceDescription", STRING_REF),
    ("OnBoardDeviceStatus",     EFI_MISC_ONBOARD_DEVICE_STATUS),
    ("OnBoardDevicePath",       EFI_DEVICE_PATH_PROTOCOL)
  ]

EFI_MISC_OEM_STRING_RECORD_NUMBER    = 0x00000009

class EFI_MISC_OEM_STRING_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("OemStringRef", STRING_REF * 1)
  ]

class EFI_MISC_SYSTEM_OPTION_STRING_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("SystemOptionStringRef", STRING_REF * 1)
  ]

EFI_MISC_SYSTEM_OPTION_STRING_RECORD_NUMBER    = 0x0000000A

EFI_MISC_NUMBER_OF_INSTALLABLE_LANGUAGES_RECORD_NUMBER    = 0x0000000B

class EFI_MISC_LANGUAGE_FLAGS (Structure):
  _pack_   = 1
  _fields_ = [
    ("AbbreviatedLanguageFormat", UINT32, 1),
    ("Reserved",                  UINT32, 31)
  ]

class EFI_MISC_NUMBER_OF_INSTALLABLE_LANGUAGES_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("NumberOfInstallableLanguages",  UINT16),
    ("LanguageFlags",                 EFI_MISC_LANGUAGE_FLAGS),
    ("CurrentLanguageNumber",         UINT16)
  ]

EFI_MISC_SYSTEM_LANGUAGE_STRING_RECORD_NUMBER    = 0x0000000C

class EFI_MISC_SYSTEM_LANGUAGE_STRING_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("LanguageId",            UINT16),
    ("SystemLanguageString",  EFI_MISC_LANGUAGE_FLAGS)
  ]

EFI_MISC_GROUP_NAME_RECORD_NUMBER    = 0x0000000D

class EFI_MISC_GROUP_NAME_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("GroupName",         STRING_REF),
    ("NumberGroupItems",  UINT16),
    ("GroupId",           UINT16)
  ]

EFI_MISC_GROUP_ITEM_SET_RECORD_NUMBER    = 0x0000000E

class EFI_MISC_GROUP_ITEM_SET_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("SubClass",        EFI_GUID),
    ("GroupLink",       EFI_INTER_LINK_DATA),
    ("GroupId",         UINT16),
    ("GroupElementId",  UINT16)
  ]

EFI_MISC_POINTING_DEVICE_TYPE_RECORD_NUMBER    = 0x0000000F

EfiPointingDeviceTypeOther         = 0x01
EfiPointingDeviceTypeUnknown       = 0x02
EfiPointingDeviceTypeMouse         = 0x03
EfiPointingDeviceTypeTrackBall     = 0x04
EfiPointingDeviceTypeTrackPoint    = 0x05
EfiPointingDeviceTypeGlidePoint    = 0x06
EfiPointingDeviceTouchPad          = 0x07
EfiPointingDeviceTouchScreen       = 0x08
EfiPointingDeviceOpticalSensor     = 0x09
EFI_MISC_POINTING_DEVICE_TYPE      = UINTN

EfiPointingDeviceInterfaceOther              = 0x01
EfiPointingDeviceInterfaceUnknown            = 0x02
EfiPointingDeviceInterfaceSerial             = 0x03
EfiPointingDeviceInterfacePs2                = 0x04
EfiPointingDeviceInterfaceInfrared           = 0x05
EfiPointingDeviceInterfaceHpHil              = 0x06
EfiPointingDeviceInterfaceBusMouse           = 0x07
EfiPointingDeviceInterfaceADB                = 0x08
EfiPointingDeviceInterfaceBusMouseDB9        = 0xA0
EfiPointingDeviceInterfaceBusMouseMicroDin   = 0xA1
EfiPointingDeviceInterfaceUsb                = 0xA2
EFI_MISC_POINTING_DEVICE_INTERFACE           = UINTN

class EFI_MISC_POINTING_DEVICE_TYPE_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("PointingDeviceType",          EFI_MISC_POINTING_DEVICE_TYPE),
    ("PointingDeviceInterface",     EFI_MISC_POINTING_DEVICE_INTERFACE),
    ("NumberPointingDeviceButtons", UINT16),
    ("PointingDevicePath",          EFI_DEVICE_PATH_PROTOCOL)
  ]

EFI_MISC_PORTABLE_BATTERY_RECORD_NUMBER   = 0x00000010

EfiPortableBatteryDeviceChemistryOther = 1
EfiPortableBatteryDeviceChemistryUnknown = 2
EfiPortableBatteryDeviceChemistryLeadAcid = 3
EfiPortableBatteryDeviceChemistryNickelCadmium = 4
EfiPortableBatteryDeviceChemistryNickelMetalHydride = 5
EfiPortableBatteryDeviceChemistryLithiumIon = 6
EfiPortableBatteryDeviceChemistryZincAir = 7
EfiPortableBatteryDeviceChemistryLithiumPolymer = 8
EFI_MISC_PORTABLE_BATTERY_DEVICE_CHEMISTRY  = UINTN

class EFI_MISC_PORTABLE_BATTERY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Location",                  STRING_REF),
    ("Manufacturer",              STRING_REF),
    ("ManufactureDate",           STRING_REF),
    ("SerialNumber",              STRING_REF),
    ("DeviceName",                STRING_REF),
    ("DeviceChemistry",           EFI_MISC_PORTABLE_BATTERY_DEVICE_CHEMISTRY),
    ("DesignCapacity",            UINT16),
    ("DesignVoltage",             UINT16),
    ("SBDSVersionNumber",         STRING_REF),
    ("MaximumError",              UINT8),
    ("SBDSSerialNumber",          UINT16),
    ("SBDSManufactureDate",       UINT16),
    ("SBDSDeviceChemistry",       STRING_REF),
    ("DesignCapacityMultiplier",  UINT8),
    ("OEMSpecific",               UINT32),
    ("BatteryNumber",             UINT8),
    ("Valid",                     BOOLEAN)
  ]

EFI_MISC_RESET_CAPABILITIES_RECORD_NUMBER    = 0x00000011

class EFI_MISC_RESET_CAPABILITIES_TYPE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Status",                UINT32, 1),
    ("BootOption",            UINT32, 2),
    ("BootOptionOnLimit",     UINT32, 2),
    ("WatchdogTimerPresent:", UINT32, 1),
    ("Reserved",              UINT32, 26)
  ]

class EFI_MISC_RESET_CAPABILITIES (Structure):
  _pack_   = 1
  _fields_ = [
    ("ResetCapabilities",   EFI_MISC_RESET_CAPABILITIES_TYPE),
    ("ResetCount",          UINT16),
    ("ResetLimit",          UINT16),
    ("ResetTimerInterval",  UINT16),
    ("ResetTimeout",        UINT16)
  ]

class EFI_MISC_RESET_CAPABILITIES_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ResetCapabilities",   EFI_MISC_RESET_CAPABILITIES),
    ("ResetCount",          UINT16),
    ("ResetLimit",          UINT16),
    ("ResetTimerInterval",  UINT16),
    ("ResetTimeout",        UINT16)
  ]

EFI_MISC_HARDWARE_SECURITY_SETTINGS_DATA_RECORD_NUMBER    = 0x00000012

EfiHardwareSecurityStatusDisabled       = 0
EfiHardwareSecurityStatusEnabled        = 1
EfiHardwareSecurityStatusNotImplemented = 2
EfiHardwareSecurityStatusUnknown        = 3
EFI_MISC_HARDWARE_SECURITY_STATUS       = UINTN

class EFI_MISC_HARDWARE_SECURITY_SETTINGS (Structure):
  _pack_   = 1
  _fields_ = [
    ("FrontPanelResetStatus",       UINT32, 2),
    ("AdministratorPasswordStatus", UINT32, 2),
    ("KeyboardPasswordStatus",      UINT32, 2),
    ("PowerOnPasswordStatus",       UINT32, 2),
    ("Reserved",                    UINT32, 24)
  ]

class EFI_MISC_HARDWARE_SECURITY_SETTINGS_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("HardwareSecuritySettings",  EFI_MISC_HARDWARE_SECURITY_SETTINGS)
  ]

EFI_MISC_SCHEDULED_POWER_ON_MONTH_RECORD_NUMBER    = 0x00000013

class EFI_MISC_SCHEDULED_POWER_ON_MONTH_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ScheduledPoweronMonth",       UINT16),
    ("ScheduledPoweronDayOfMonth",  UINT16),
    ("ScheduledPoweronHour",        UINT16),
    ("ScheduledPoweronMinute",      UINT16),
    ("ScheduledPoweronSecond",      UINT16)
  ]

EFI_MISC_VOLTAGE_PROBE_DESCRIPTION_RECORD_NUMBER    = 0x00000014

class EFI_MISC_VOLTAGE_PROBE_LOCATION (Structure):
  _pack_   = 1
  _fields_ = [
    ("VoltageProbeSite",    UINT32, 5),
    ("VoltageProbeStatus",  UINT32, 3),
    ("Reserved",            UINT32, 24)
  ]

class EFI_MISC_VOLTAGE_PROBE_DESCRIPTION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("VoltageProbeDescription",         STRING_REF),
    ("VoltageProbeLocation",            EFI_MISC_VOLTAGE_PROBE_LOCATION),
    ("VoltageProbeMaximumValue",        EFI_EXP_BASE10_DATA),
    ("VoltageProbeMinimumValue",        EFI_EXP_BASE10_DATA),
    ("VoltageProbeResolution",          EFI_EXP_BASE10_DATA),
    ("VoltageProbeTolerance",           EFI_EXP_BASE10_DATA),
    ("VoltageProbeAccuracy",            EFI_EXP_BASE10_DATA),
    ("VoltageProbeNominalValue",        EFI_EXP_BASE10_DATA),
    ("MDLowerNoncriticalThreshold",     EFI_EXP_BASE10_DATA),
    ("MDUpperNoncriticalThreshold",     EFI_EXP_BASE10_DATA),
    ("MDLowerCriticalThreshold",        EFI_EXP_BASE10_DATA),
    ("MDUpperCriticalThreshold",        EFI_EXP_BASE10_DATA),
    ("MDLowerNonrecoverableThreshold",  EFI_EXP_BASE10_DATA),
    ("MDUpperNonrecoverableThreshold",  EFI_EXP_BASE10_DATA),
    ("VoltageProbeOemDefined",          UINT32)
  ]

EFI_MISC_COOLING_DEVICE_TEMP_LINK_RECORD_NUMBER    = 0x00000015

class EFI_MISC_COOLING_DEVICE_TYPE (Structure):
  _pack_   = 1
  _fields_ = [
    ("CoolingDevice",       UINT32, 5),
    ("CoolingDeviceStatus", UINT32, 3),
    ("Reserved",            UINT32, 24)
  ]

class EFI_MISC_COOLING_DEVICE_TEMP_LINK_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("CoolingDeviceType",             EFI_MISC_COOLING_DEVICE_TYPE),
    ("CoolingDeviceTemperatureLink",  EFI_INTER_LINK_DATA),
    ("CoolingDeviceUnitGroup",        UINT8),
    ("CoolingDeviceNominalSpeed",     UINT16),
    ("CoolingDeviceOemDefined",       UINT32)
  ]

EFI_MISC_TEMPERATURE_PROBE_DESCRIPTION_RECORD_NUMBER    = 0x00000016

class EFI_MISC_TEMPERATURE_PROBE_LOCATION (Structure):
  _pack_   = 1
  _fields_ = [
    ("TemperatureProbeSite",    UINT32, 5),
    ("TemperatureProbeStatus",  UINT32, 3),
    ("Reserved",                UINT32, 24)
  ]

class EFI_MISC_TEMPERATURE_PROBE_DESCRIPTION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("TemperatureProbeDescription",     STRING_REF),
    ("TemperatureProbeLocation",        EFI_MISC_TEMPERATURE_PROBE_LOCATION),
    ("TemperatureProbeMaximumValue",    UINT16),
    ("TemperatureProbeMinimumValue",    UINT16),
    ("TemperatureProbeResolution",      UINT16),
    ("TemperatureProbeTolerance",       UINT16),
    ("TemperatureProbeAccuracy",        UINT16),
    ("TemperatureProbeNominalValue",    UINT16),
    ("MDLowerNoncriticalThreshold",     UINT16),
    ("MDUpperNoncriticalThreshold",     UINT16),
    ("MDLowerCriticalThreshold",        UINT16),
    ("MDUpperCriticalThreshold",        UINT16),
    ("MDLowerNonrecoverableThreshold",  UINT16),
    ("MDUpperNonrecoverableThreshold",  UINT16),
    ("TemperatureProbeOemDefined",      UINT32)
  ]

EFI_MISC_ELECTRICAL_CURRENT_PROBE_DESCRIPTION_RECORD_NUMBER    = 0x00000017

class EFI_MISC_ELECTRICAL_CURRENT_PROBE_LOCATION (Structure):
  _pack_   = 1
  _fields_ = [
    ("ElectricalCurrentProbeSite",    UINT32, 5),
    ("ElectricalCurrentProbeStatus",  UINT32, 3),
    ("Reserved",                      UINT32, 24)
  ]

class EFI_MISC_ELECTRICAL_CURRENT_PROBE_DESCRIPTION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ElectricalCurrentProbeDescription",   STRING_REF),
    ("ElectricalCurrentProbeLocation",      EFI_MISC_ELECTRICAL_CURRENT_PROBE_LOCATION),
    ("ElectricalCurrentProbeMaximumValue",  EFI_EXP_BASE10_DATA),
    ("ElectricalCurrentProbeMinimumValue",  EFI_EXP_BASE10_DATA),
    ("ElectricalCurrentProbeResolution",    EFI_EXP_BASE10_DATA),
    ("ElectricalCurrentProbeTolerance",     EFI_EXP_BASE10_DATA),
    ("ElectricalCurrentProbeAccuracy",      EFI_EXP_BASE10_DATA),
    ("ElectricalCurrentProbeNominalValue",  EFI_EXP_BASE10_DATA),
    ("MDLowerNoncriticalThreshold",         EFI_EXP_BASE10_DATA),
    ("MDUpperNoncriticalThreshold",         EFI_EXP_BASE10_DATA),
    ("MDLowerCriticalThreshold",            EFI_EXP_BASE10_DATA),
    ("MDUpperCriticalThreshold",            EFI_EXP_BASE10_DATA),
    ("MDLowerNonrecoverableThreshold",      EFI_EXP_BASE10_DATA),
    ("MDUpperNonrecoverableThreshold",      EFI_EXP_BASE10_DATA),
    ("ElectricalCurrentProbeOemDefined",    UINT32)
  ]

EFI_MISC_REMOTE_ACCESS_MANUFACTURER_DESCRIPTION_RECORD_NUMBER    = 0x00000018

class EFI_MISC_REMOTE_ACCESS_CONNECTIONS (Structure):
  _pack_   = 1
  _fields_ = [
    ("InboundConnectionEnabled",  UINT32, 1),
    ("OutboundConnectionEnabled", UINT32, 1),
    ("Reserved",                  UINT32, 30)
  ]

class EFI_MISC_REMOTE_ACCESS_MANUFACTURER_DESCRIPTION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("RemoteAccessManufacturerNameDescription", STRING_REF),
    ("RemoteAccessConnections",                 EFI_MISC_REMOTE_ACCESS_CONNECTIONS)
  ]

EFI_MISC_BIS_ENTRY_POINT_RECORD_NUMBER    = 0x00000019

class EFI_MISC_BIS_ENTRY_POINT_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("BisEntryPoint", EFI_PHYSICAL_ADDRESS)
  ]

EFI_MISC_BOOT_INFORMATION_STATUS_RECORD_NUMBER    = 0x0000001A

EfiBootInformationStatusNoError                  = 0x00
EfiBootInformationStatusNoBootableMedia          = 0x01
EfiBootInformationStatusNormalOSFailedLoading    = 0x02
EfiBootInformationStatusFirmwareDetectedFailure  = 0x03
EfiBootInformationStatusOSDetectedFailure        = 0x04
EfiBootInformationStatusUserRequestedBoot        = 0x05
EfiBootInformationStatusSystemSecurityViolation  = 0x06
EfiBootInformationStatusPreviousRequestedImage   = 0x07
EfiBootInformationStatusWatchdogTimerExpired     = 0x08
EfiBootInformationStatusStartReserved            = 0x09
EfiBootInformationStatusStartOemSpecific         = 0x80
EfiBootInformationStatusStartProductSpecific     = 0xC0
EFI_MISC_BOOT_INFORMATION_STATUS_DATA_TYPE       = UINTN

class EFI_MISC_BOOT_INFORMATION_STATUS_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("BootInformationStatus", EFI_MISC_BOOT_INFORMATION_STATUS_DATA_TYPE),
    ("BootInformationData",   UINT8 * 9),
  ]

EFI_MISC_MANAGEMENT_DEVICE_DESCRIPTION_RECORD_NUMBER    = 0x0000001B

EfiManagementDeviceTypeOther      = 0x01
EfiManagementDeviceTypeUnknown    = 0x02
EfiManagementDeviceTypeLm75       = 0x03
EfiManagementDeviceTypeLm78       = 0x04
EfiManagementDeviceTypeLm79       = 0x05
EfiManagementDeviceTypeLm80       = 0x06
EfiManagementDeviceTypeLm81       = 0x07
EfiManagementDeviceTypeAdm9240    = 0x08
EfiManagementDeviceTypeDs1780     = 0x09
EfiManagementDeviceTypeMaxim1617  = 0x0A
EfiManagementDeviceTypeGl518Sm    = 0x0B
EfiManagementDeviceTypeW83781D    = 0x0C
EfiManagementDeviceTypeHt82H791   = 0x0D
EFI_MISC_MANAGEMENT_DEVICE_TYPE   = UINTN
EfiManagementDeviceAddressTypeOther   = 1
EfiManagementDeviceAddressTypeUnknown = 2
EfiManagementDeviceAddressTypeIOPort  = 3
EfiManagementDeviceAddressTypeMemory  = 4
EfiManagementDeviceAddressTypeSmbus   = 5
EFI_MISC_MANAGEMENT_DEVICE_ADDRESS_TYPE = UINTN

class EFI_MISC_MANAGEMENT_DEVICE_DESCRIPTION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ManagementDeviceDescription",   STRING_REF),
    ("ManagementDeviceType",          EFI_MISC_MANAGEMENT_DEVICE_TYPE),
    ("ManagementDeviceAddress",       UINTN),
    ("ManagementDeviceAddressType",   EFI_MISC_MANAGEMENT_DEVICE_ADDRESS_TYPE)
  ]

EFI_MISC_MANAGEMENT_DEVICE_COMPONENT_DESCRIPTION_RECORD_NUMBER    = 0x0000001C

class EFI_MISC_MANAGEMENT_DEVICE_COMPONENT_DESCRIPTION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ManagementDeviceComponentDescription",  STRING_REF),
    ("ManagementDeviceLink",                  EFI_INTER_LINK_DATA),
    ("ManagementDeviceComponentLink",         EFI_INTER_LINK_DATA),
    ("ManagementDeviceThresholdLink",         EFI_INTER_LINK_DATA),
    ("ComponentType",                         UINT8)
  ]

EfiIpmiOther = 0
EfiIpmiKcs   = 1
EfiIpmiSmic  = 2
EfiIpmiBt    = 3
EFI_MISC_IPMI_INTERFACE_TYPE  = UINTN

class EFI_MISC_IPMI_SPECIFICATION_REVISION (Structure):
  _pack_   = 1
  _fields_ = [
    ("IpmiSpecLeastSignificantDigit",   UINT16, 4),
    ("IpmiSpecMostSignificantDigit",    UINT16, 4),
    ("Reserved",                        UINT16, 8)
  ]

class EFI_MISC_IPMI_INTERFACE_TYPE_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("IpmiInterfaceType",         EFI_MISC_IPMI_INTERFACE_TYPE),
    ("IpmiSpecificationRevision", EFI_MISC_IPMI_SPECIFICATION_REVISION),
    ("IpmiI2CSlaveAddress",       UINT16),
    ("IpmiNvDeviceAddress",       UINT16),
    ("IpmiBaseAddress",           UINT64),
    ("IpmiDevicePath",            EFI_DEVICE_PATH_PROTOCOL)
  ]

EFI_MISC_IPMI_INTERFACE_TYPE_RECORD_NUMBER    = 0x0000001D

EFI_MISC_IPMI_INTERFACE_TYPE_DATA_RECORD_NUMBER = EFI_MISC_IPMI_INTERFACE_TYPE_RECORD_NUMBER

class EFI_MISC_POWER_SUPPLY_CHARACTERISTICS (Structure):
  _pack_   = 1
  _fields_ = [
    ("PowerSupplyHotReplaceable", UINT16, 1),
    ("PowerSupplyPresent",        UINT16, 1),
    ("PowerSupplyUnplugged",      UINT16, 1),
    ("InputVoltageRangeSwitch",   UINT16, 4),
    ("PowerSupplyStatus",         UINT16, 3),
    ("PowerSupplyType",           UINT16, 4),
    ("Reserved",                  UINT16, 2)
  ]

class EFI_MISC_SYSTEM_POWER_SUPPLY_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("PowerUnitGroup",                    UINT16),
    ("PowerSupplyLocation",               STRING_REF),
    ("PowerSupplyDeviceName",             STRING_REF),
    ("PowerSupplyManufacturer",           STRING_REF),
    ("PowerSupplySerialNumber",           STRING_REF),
    ("PowerSupplyAssetTagNumber",         STRING_REF),
    ("PowerSupplyModelPartNumber",        STRING_REF),
    ("PowerSupplyRevisionLevel",          STRING_REF),
    ("PowerSupplyMaxPowerCapacity",       UINT16),
    ("PowerSupplyCharacteristics",        EFI_MISC_POWER_SUPPLY_CHARACTERISTICS),
    ("PowerSupplyInputVoltageProbeLink",  EFI_INTER_LINK_DATA),
    ("PowerSupplyCoolingDeviceLink",      EFI_INTER_LINK_DATA),
    ("PowerSupplyInputCurrentProbeLink",  EFI_INTER_LINK_DATA)
  ]

EFI_MISC_SYSTEM_POWER_SUPPLY_RECORD_NUMBER    = 0x0000001E

class SMBIOS_STRUCTURE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",    UINT8),
    ("Length",  UINT8),
    ("Handle",  UINT16)
  ]

class EFI_MISC_SMBIOS_STRUCT_ENCAPSULATION_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  SMBIOS_STRUCTURE_HDR),
    ("RawData", UINT8 * 1)
  ]

EFI_MISC_SMBIOS_STRUCT_ENCAP_RECORD_NUMBER    = 0x0000001F

EFI_MISC_SYSTEM_EVENT_LOG_RECORD_NUMBER    = 0x00000020

class EFI_MISC_SYSTEM_EVENT_LOG_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("LogAreaLength",             UINT16),
    ("LogHeaderStartOffset",      UINT16),
    ("LogDataStartOffset",        UINT16),
    ("AccessMethod",              UINT8),
    ("LogStatus",                 UINT8),
    ("LogChangeToken",            UINT32),
    ("AccessMethodAddress",       UINT32),
    ("LogHeaderFormat",           UINT8),
    ("NumberOfSupportedLogType",  UINT8),
    ("LengthOfLogDescriptor",     UINT8)
  ]

ACCESS_INDEXIO_1INDEX8BIT_DATA8BIT    = 0x00
ACCESS_INDEXIO_2INDEX8BIT_DATA8BIT    = 0X01
ACCESS_INDEXIO_1INDEX16BIT_DATA8BIT   = 0X02
ACCESS_MEMORY_MAPPED                  = 0x03
ACCESS_GPNV                           = 0x04

EFI_MISC_MANAGEMENT_DEVICE_THRESHOLD_RECORD_NUMBER    = 0x00000021

class EFI_MISC_MANAGEMENT_DEVICE_THRESHOLD (Structure):
  _pack_   = 1
  _fields_ = [
    ("LowerThresNonCritical", UINT16),
    ("UpperThresNonCritical", UINT16),
    ("LowerThresCritical",    UINT16),
    ("UpperThresCritical",    UINT16),
    ("LowerThresNonRecover",  UINT16),
    ("UpperThresNonRecover",  UINT16)
  ]

class EFI_MISC_SUBCLASS_RECORDS (Union):
  _pack_   = 1
  _fields_ = [
    ("LastPciBus",                                      EFI_MISC_LAST_PCI_BUS_DATA),
    ("MiscBiosVendor",                                  EFI_MISC_BIOS_VENDOR_DATA),
    ("MiscSystemManufacturer",                          EFI_MISC_SYSTEM_MANUFACTURER_DATA),
    ("MiscBaseBoardManufacturer",                       EFI_MISC_BASE_BOARD_MANUFACTURER_DATA),
    ("MiscChassisManufacturer",                         EFI_MISC_CHASSIS_MANUFACTURER_DATA),
    ("MiscPortInternalConnectorDesignator",             EFI_MISC_PORT_INTERNAL_CONNECTOR_DESIGNATOR_DATA),
    ("MiscSystemSlotDesignation",                       EFI_MISC_SYSTEM_SLOT_DESIGNATION_DATA),
    ("MiscOnboardDevice",                               EFI_MISC_ONBOARD_DEVICE_DATA),
    ("MiscOemString",                                   EFI_MISC_OEM_STRING_DATA),
    ("MiscOptionString",                                EFI_MISC_SYSTEM_OPTION_STRING_DATA),
    ("NumberOfInstallableLanguages",                    EFI_MISC_NUMBER_OF_INSTALLABLE_LANGUAGES_DATA),
    ("MiscSystemLanguageString",                        EFI_MISC_SYSTEM_LANGUAGE_STRING_DATA),
    ("MiscSystemEventLog",                              EFI_MISC_SYSTEM_EVENT_LOG_DATA),
    ("MiscGroupNameData",                               EFI_MISC_GROUP_NAME_DATA),
    ("MiscGroupItemSetData",                            EFI_MISC_GROUP_ITEM_SET_DATA),
    ("MiscPointingDeviceTypeData",                      EFI_MISC_POINTING_DEVICE_TYPE_DATA),
    ("MiscResetCapablilitiesData",                      EFI_MISC_RESET_CAPABILITIES_DATA),
    ("MiscHardwareSecuritySettingsData",                EFI_MISC_HARDWARE_SECURITY_SETTINGS_DATA),
    ("MiscScheduledPowerOnMonthData",                   EFI_MISC_SCHEDULED_POWER_ON_MONTH_DATA),
    ("MiscVoltagePorbeDescriptionData",                 EFI_MISC_VOLTAGE_PROBE_DESCRIPTION_DATA),
    ("MiscCoolingDeviceTempLinkData",                   EFI_MISC_COOLING_DEVICE_TEMP_LINK_DATA),
    ("MiscTemperatureProbeDescriptionData",             EFI_MISC_TEMPERATURE_PROBE_DESCRIPTION_DATA),
    ("MiscElectricalCurrentProbeDescriptionData",       EFI_MISC_ELECTRICAL_CURRENT_PROBE_DESCRIPTION_DATA),
    ("MiscRemoteAccessManufacturerDescriptionData",     EFI_MISC_REMOTE_ACCESS_MANUFACTURER_DESCRIPTION_DATA),
    ("MiscBisEntryPoint",                               EFI_MISC_BIS_ENTRY_POINT_DATA),
    ("MiscBootInformationStatus",                       EFI_MISC_BOOT_INFORMATION_STATUS_DATA),
    ("MiscMangementDeviceDescriptionData",              EFI_MISC_MANAGEMENT_DEVICE_DESCRIPTION_DATA),
    ("MiscmangementDeviceComponentDescriptionData",     EFI_MISC_MANAGEMENT_DEVICE_COMPONENT_DESCRIPTION_DATA),
    ("MiscIpmiInterfaceTypeData",                       EFI_MISC_IPMI_INTERFACE_TYPE_DATA),
    ("MiscPowerSupplyInfo",                             EFI_MISC_SYSTEM_POWER_SUPPLY_DATA),
    ("MiscSmbiosStructEncapsulation",                   EFI_MISC_SMBIOS_STRUCT_ENCAPSULATION_DATA),
    ("MiscManagementDeviceThreshold",                   EFI_MISC_MANAGEMENT_DEVICE_THRESHOLD)
  ]

class EFI_MISC_SUBCLASS_DRIVER_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header", EFI_SUBCLASS_TYPE1_HEADER),
    ("Record", EFI_MISC_SUBCLASS_RECORDS)
  ]

EFI_SUBCLASS_INSTANCE_RESERVED       = 0

EFI_SUBCLASS_INSTANCE_NON_APPLICABLE = 0xFFFF

