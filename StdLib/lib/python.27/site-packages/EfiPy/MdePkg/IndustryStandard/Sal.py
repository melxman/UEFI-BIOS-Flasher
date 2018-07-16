#
# Sal.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Sal.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from EfiPy.MdePkg.IndustryStandard import *

EFI_SAL_STATUS = INTN

EFI_SAL_SUCCESS =                       EFI_SAL_STATUS (0).value
EFI_SAL_OVERFLOW =                      EFI_SAL_STATUS (1).value
EFI_SAL_WARM_BOOT_NEEDED =              EFI_SAL_STATUS (2).value
EFI_SAL_MORE_RECORDS =                  EFI_SAL_STATUS (3).value
EFI_SAL_NOT_IMPLEMENTED =               EFI_SAL_STATUS (-1).value
EFI_SAL_INVALID_ARGUMENT =              EFI_SAL_STATUS (-2).value
EFI_SAL_ERROR =                         EFI_SAL_STATUS (-3).value
EFI_SAL_VIRTUAL_ADDRESS_ERROR =         EFI_SAL_STATUS (-4).value
EFI_SAL_NO_INFORMATION =                EFI_SAL_STATUS (-5).value
EFI_SAL_NOT_ENOUGH_SCRATCH =            EFI_SAL_STATUS (-9).value

class SAL_RETURN_REGS (Structure):
  _fields_ = [
    ("Status",  EFI_SAL_STATUS),
    ("r9",      UINTN),
    ("r10",     UINTN),
    ("r11",     UINTN)
  ]

SAL_PROC = CFUNCTYPE (
  SAL_RETURN_REGS,
  UINT64,           # IN FunctionId,
  UINT64,           # IN Arg1,
  UINT64,           # IN Arg2,
  UINT64,           # IN Arg3,
  UINT64,           # IN Arg4,
  UINT64,           # IN Arg5,
  UINT64,           # IN Arg6,
  UINT64            # IN Arg7
  )

EFI_SAL_SET_VECTORS             = 0x01000000
EFI_SAL_GET_STATE_INFO          = 0x01000001
EFI_SAL_GET_STATE_INFO_SIZE     = 0x01000002
EFI_SAL_CLEAR_STATE_INFO        = 0x01000003
EFI_SAL_MC_RENDEZ               = 0x01000004
EFI_SAL_MC_SET_PARAMS           = 0x01000005
EFI_SAL_REGISTER_PHYSICAL_ADDR  = 0x01000006
EFI_SAL_CACHE_FLUSH             = 0x01000008
EFI_SAL_CACHE_INIT              = 0x01000009
EFI_SAL_PCI_CONFIG_READ         = 0x01000010
EFI_SAL_PCI_CONFIG_WRITE        = 0x01000011
EFI_SAL_FREQ_BASE               = 0x01000012
EFI_SAL_PHYSICAL_ID_INFO        = 0x01000013
EFI_SAL_UPDATE_PAL              = 0x01000020
EFI_SAL_FUNCTION_ID_MASK        = 0x0000ffff
EFI_SAL_MAX_SAL_FUNCTION_ID     = 0x00000021

EFI_SAL_SET_MCA_VECTOR          = 0x0
EFI_SAL_SET_INIT_VECTOR         = 0x1
EFI_SAL_SET_BOOT_RENDEZ_VECTOR  = 0x2

class SAL_SET_VECTORS_CS_N (Structure):
  _fields_ = [
    ("Length",        UINT64, 32),
    ("ChecksumValid", UINT64, 1),
    ("Reserved1",     UINT64, 7),
    ("ByteChecksum",  UINT64, 8),
    ("Reserved2",     UINT64, 16)
  ]

EFI_SAL_MCA_STATE_INFO  = 0x0
EFI_SAL_INIT_STATE_INFO = 0x1
EFI_SAL_CMC_STATE_INFO  = 0x2
EFI_SAL_CP_STATE_INFO   = 0x3

EFI_SAL_MC_SET_RENDEZ_PARAM = 0x1
EFI_SAL_MC_SET_WAKEUP_PARAM = 0x2
EFI_SAL_MC_SET_CPE_PARAM    = 0x3

EFI_SAL_MC_SET_INTR_PARAM   = 0x1
EFI_SAL_MC_SET_MEM_PARAM    = 0x2

EFI_SAL_REGISTER_PAL_ADDR = 0x0

EFI_SAL_FLUSH_I_CACHE       = 0x01
EFI_SAL_FLUSH_D_CACHE       = 0x02
EFI_SAL_FLUSH_BOTH_CACHE    = 0x03
EFI_SAL_FLUSH_MAKE_COHERENT = 0x04

EFI_SAL_PCI_CONFIG_ONE_BYTE   = 0x1
EFI_SAL_PCI_CONFIG_TWO_BYTES  = 0x2
EFI_SAL_PCI_CONFIG_FOUR_BYTES = 0x4

EFI_SAL_PCI_COMPATIBLE_ADDRESS         = 0x0
EFI_SAL_PCI_EXTENDED_REGISTER_ADDRESS  = 0x1

class SAL_PCI_ADDRESS (Structure):
  _fields_ = [
    ("Register",  UINT64, 8),
    ("Function",  UINT64, 3),
    ("Device",    UINT64, 5),
    ("Bus",       UINT64, 8),
    ("Segment",   UINT64, 8),
    ("Reserved",  UINT64, 32)
  ]

class SAL_PCI_EXTENDED_REGISTER_ADDRESS (Structure):
  _fields_ = [
    ("Register",          UINT64, 8),
    ("ExtendedRegister",  UINT64, 4),
    ("Function",          UINT64, 3),
    ("Device",            UINT64, 5),
    ("Bus",               UINT64, 8),
    ("Segment",           UINT64, 16),
    ("Reserved",          UINT64, 20)
  ]

EFI_SAL_CPU_INPUT_FREQ_BASE     = 0x0
EFI_SAL_PLATFORM_IT_FREQ_BASE   = 0x1
EFI_SAL_PLATFORM_RTC_FREQ_BASE  = 0x2

EFI_SAL_UPDATE_BAD_PAL_VERSION  = UINT64( -1).value
EFI_SAL_UPDATE_PAL_AUTH_FAIL    = UINT64( -2).value
EFI_SAL_UPDATE_PAL_BAD_TYPE     = UINT64( -3).value
EFI_SAL_UPDATE_PAL_READONLY     = UINT64( -4).value
EFI_SAL_UPDATE_PAL_WRITE_FAIL   = UINT64(-10).value
EFI_SAL_UPDATE_PAL_ERASE_FAIL   = UINT64(-11).value
EFI_SAL_UPDATE_PAL_READ_FAIL    = UINT64(-12).value
EFI_SAL_UPDATE_PAL_CANT_FIT     = UINT64(-13).value

class SAL_UPDATE_PAL_DATA_BLOCK (Structure):
  _fields_ = [
    ("Size",          UINT32),
    ("MmddyyyyDate",  UINT32),
    ("Version",       UINT16),
    ("Type",          UINT8),
    ("Reserved",      UINT8 * 5),
    ("FwVendorId",    UINT64),
    ("Reserved2",     UINT8 * 40)
  ]


class SAL_UPDATE_PAL_INFO_BLOCK (Structure):
  pass

SAL_UPDATE_PAL_INFO_BLOCK._fields_ = [
    ("Next",          POINTER (SAL_UPDATE_PAL_INFO_BLOCK)),
    ("DataBlock",     POINTER (SAL_UPDATE_PAL_DATA_BLOCK)),
    ("StoreChecksum", UINT8),
    ("Reserved",      UINT8 * 15)
  ]

class SAL_SYSTEM_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",     UINT32),
    ("Length",        UINT32),
    ("SalRevision",   UINT16),
    ("EntryCount",    UINT16),
    ("CheckSum",      UINT8),
    ("Reserved",      UINT8 * 7),
    ("SalAVersion",   UINT16),
    ("SalBVersion",   UINT16),
    ("OemId",         UINT8 * 32),
    ("ProductId",     UINT8 * 32),
    ("Reserved2",     UINT8 * 8)
  ]

EFI_SAL_ST_HEADER_SIGNATURE = "SST_"
EFI_SAL_REVISION            = 0x0320

EFI_SAL_ST_ENTRY_POINT        = 0
EFI_SAL_ST_MEMORY_DESCRIPTOR  = 1
EFI_SAL_ST_PLATFORM_FEATURES  = 2
EFI_SAL_ST_TR_USAGE           = 3
EFI_SAL_ST_PTC                = 4
EFI_SAL_ST_AP_WAKEUP          = 5

EFI_SAL_ST_ENTRY_POINT_SIZE        = 48
EFI_SAL_ST_MEMORY_DESCRIPTOR_SIZE  = 32
EFI_SAL_ST_PLATFORM_FEATURES_SIZE  = 16
EFI_SAL_ST_TR_USAGE_SIZE           = 32
EFI_SAL_ST_PTC_SIZE                = 16
EFI_SAL_ST_AP_WAKEUP_SIZE          = 16

class SAL_ST_ENTRY_POINT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Reserved",              UINT8 * 7),
    ("PalProcEntry",          UINT64),
    ("SalProcEntry",          UINT64),
    ("SalGlobalDataPointer",  UINT64),
    ("Reserved2",             UINT64 * 2)
  ]

class SAL_ST_PLATFORM_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("PlatformFeatures",  UINT8),
    ("Reserved",          UINT8 * 14)
  ]

SAL_PLAT_FEAT_BUS_LOCK      = 0x01
SAL_PLAT_FEAT_PLAT_IPI_HINT = 0x02
SAL_PLAT_FEAT_PROC_IPI_HINT = 0x04

class SAL_ST_TR_DECRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("TRType",          UINT8),
    ("TRNumber",        UINT8),
    ("Reserved",        UINT8 * 5),
    ("VirtualAddress",  UINT64),
    ("EncodedPageSize", UINT64),
    ("Reserved1",       UINT64)
  ]

EFI_SAL_ST_TR_USAGE_INSTRUCTION = 00
EFI_SAL_ST_TR_USAGE_DATA        = 01

class SAL_COHERENCE_DOMAIN_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfProcessors",  UINT64),
    ("LocalIDRegister",     UINT64)
  ]

class SAL_ST_CACHE_COHERENCE_DECRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Reserved",          UINT8 * 3),
    ("NumberOfDomains",   UINT32),
    ("DomainInformation", POINTER (SAL_COHERENCE_DOMAIN_INFO))
  ]

class SAL_ST_AP_WAKEUP_DECRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                    UINT8),
    ("WakeUpType",              UINT8),
    ("Reserved",                UINT8 * 6),
    ("ExternalInterruptVector", UINT64)
  ]

class EFI_SAL_FIT_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Address",       UINT64),
    ("Size",          UINT8 * 3),
    ("Reserved",      UINT8),
    ("Revision",      UINT16),
    ("Type",          UINT8, 7),
    ("CheckSumValid", UINT8, 1),
    ("CheckSum",      UINT8),
  ]

EFI_SAL_FIT_FIT_HEADER_TYPE                = 0x00
EFI_SAL_FIT_PAL_B_TYPE                     = 0x01

EFI_SAL_FIT_PROCESSOR_SPECIFIC_PAL_A_TYPE  = 0x0E
EFI_SAL_FIT_PAL_A_TYPE                     = 0x0F

EFI_SAL_FIT_PEI_CORE_TYPE                  = 0x10
EFI_SAL_FIT_UNUSED_TYPE                    = 0x7F

EFI_SAL_FIT_ENTRY_PTR   = (0x100000000 - 32)
EFI_SAL_FIT_PALA_ENTRY  = (0x100000000 - 48)
EFI_SAL_FIT_PALB_TYPE   = 01

class SAL_TIME_STAMP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Seconds",   UINT8),
    ("Minutes",   UINT8),
    ("Hours",     UINT8),
    ("Reserved",  UINT8),
    ("Day",       UINT8),
    ("Month",     UINT8),
    ("Year",      UINT8),
    ("Century",   UINT8)
  ]

class SAL_RECORD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",        UINT64),
    ("Revision",        UINT16),
    ("ErrorSeverity",   UINT8),
    ("ValidationBits",  UINT8),
    ("RecordLength",    UINT32),
    ("TimeStamp",       SAL_TIME_STAMP),
    ("OemPlatformId",   UINT8 * 16)
  ]

class SAL_SEC_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Guid",              EFI_GUID),
    ("Revision",          UINT16),
    ("ErrorRecoveryInfo", UINT8),
    ("Reserved",          UINT8),
    ("SectionLength",     UINT32)
  ]

SAL_PROCESSOR_ERROR_RECORD_INFO = EFI_GUID (0xe429faf1, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

CHECK_INFO_VALID_BIT_MASK   = 0x1
REQUESTOR_ID_VALID_BIT_MASK = 0x2
RESPONDER_ID_VALID_BIT_MASK = 0x4
TARGER_ID_VALID_BIT_MASK    = 0x8
PRECISE_IP_VALID_BIT_MASK   = 0x10

class MOD_ERROR_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InfoValid",   UINT64, 1),
    ("ReqValid",    UINT64, 1),
    ("RespValid",   UINT64, 1),
    ("TargetValid", UINT64, 1),
    ("IpValid",     UINT64, 1),
    ("Reserved",    UINT64, 59),
    ("Info",        UINT64),
    ("Req",         UINT64),
    ("Resp",        UINT64),
    ("Target",      UINT64),
    ("Ip",          UINT64),
  ]

class CPUID_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CpuidInfo",   UINT8 * 40),
    ("Reserved",    UINT8)
  ]

class FR_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrLow",   UINT64),
    ("FrHigh",  UINT64)
  ]

MIN_STATE_VALID_BIT_MASK  = 0x1
BR_VALID_BIT_MASK         = 0x2
CR_VALID_BIT_MASK         = 0x4
AR_VALID_BIT_MASK         = 0x8
RR_VALID_BIT_MASK         = 0x10
FR_VALID_BIT_MASK         = 0x20

class PSI_STATIC_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ValidFieldBits",  UINT64),
    ("MinStateInfo",    UINT8  * 1024),
    ("Br",              UINT64 * 8),
    ("Cr",              UINT64 * 128),
    ("Ar",              UINT64 * 128),
    ("Rr",              UINT64 * 8),
    ("Fr",              FR_STRUCT * 128),
  ]

PROC_ERROR_MAP_VALID_BIT_MASK       = 0x1
PROC_STATE_PARAMETER_VALID_BIT_MASK = 0x2
PROC_CR_LID_VALID_BIT_MASK          = 0x4
PROC_STATIC_STRUCT_VALID_BIT_MASK   = 0x8
CPU_INFO_VALID_BIT_MASK             = 0x1000000

class SAL_PROCESSOR_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",       SAL_SEC_HEADER),
    ("ValidationBits",      UINT64),
    ("ProcErrorMap",        UINT64),
    ("ProcStateParameter",  UINT64),
    ("ProcCrLid",           UINT64),
    ("CacheError",          MOD_ERROR_INFO * 15),
    ("TlbError",            MOD_ERROR_INFO * 15),
    ("BusError",            MOD_ERROR_INFO * 15),
    ("RegFileCheck",        MOD_ERROR_INFO * 15),
    ("MsCheck",             MOD_ERROR_INFO * 15),
    ("CpuInfo",             CPUID_INFO),
    ("PsiValidData",        PSI_STATIC_STRUCT)
  ]

SAL_MEMORY_ERROR_RECORD_INFO = EFI_GUID (0xe429faf2, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

MEMORY_ERROR_STATUS_VALID_BIT_MASK                = 0x1
MEMORY_PHYSICAL_ADDRESS_VALID_BIT_MASK            = 0x2
MEMORY_ADDR_BIT_MASK                              = 0x4
MEMORY_NODE_VALID_BIT_MASK                        = 0x8
MEMORY_CARD_VALID_BIT_MASK                        = 0x10
MEMORY_MODULE_VALID_BIT_MASK                      = 0x20
MEMORY_BANK_VALID_BIT_MASK                        = 0x40
MEMORY_DEVICE_VALID_BIT_MASK                      = 0x80
MEMORY_ROW_VALID_BIT_MASK                         = 0x100
MEMORY_COLUMN_VALID_BIT_MASK                      = 0x200
MEMORY_BIT_POSITION_VALID_BIT_MASK                = 0x400
MEMORY_PLATFORM_REQUESTOR_ID_VALID_BIT_MASK       = 0x800
MEMORY_PLATFORM_RESPONDER_ID_VALID_BIT_MASK       = 0x1000
MEMORY_PLATFORM_TARGET_VALID_BIT_MASK             = 0x2000
MEMORY_PLATFORM_BUS_SPECIFIC_DATA_VALID_BIT_MASK  = 0x4000
MEMORY_PLATFORM_OEM_ID_VALID_BIT_MASK             = 0x8000
MEMORY_PLATFORM_OEM_DATA_STRUCT_VALID_BIT_MASK    = 0x10000

class SAL_MEMORY_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",           SAL_SEC_HEADER),
    ("ValidationBits",          UINT64),
    ("MemErrorStatus",          UINT64),
    ("MemPhysicalAddress",      UINT64),
    ("MemPhysicalAddressMask",  UINT64),
    ("MemNode",                 UINT16),
    ("MemCard",                 UINT16),
    ("MemModule",               UINT16),
    ("MemBank",                 UINT16),
    ("MemDevice",               UINT16),
    ("MemRow",                  UINT16),
    ("MemColumn",               UINT16),
    ("MemBitPosition",          UINT16),
    ("ModRequestorId",          UINT64),
    ("ModResponderId",          UINT64),
    ("ModTargetId",             UINT64),
    ("BusSpecificData",         UINT64),
    ("MemPlatformOemId",        UINT8 * 16),
  ]

SAL_PCI_BUS_ERROR_RECORD_INFO = EFI_GUID (0xe429faf4, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

PCI_BUS_ERROR_STATUS_VALID_BIT_MASK     = 0x1
PCI_BUS_ERROR_TYPE_VALID_BIT_MASK       = 0x2
PCI_BUS_ID_VALID_BIT_MASK               = 0x4
PCI_BUS_ADDRESS_VALID_BIT_MASK          = 0x8
PCI_BUS_DATA_VALID_BIT_MASK             = 0x10
PCI_BUS_CMD_VALID_BIT_MASK              = 0x20
PCI_BUS_REQUESTOR_ID_VALID_BIT_MASK     = 0x40
PCI_BUS_RESPONDER_ID_VALID_BIT_MASK     = 0x80
PCI_BUS_TARGET_VALID_BIT_MASK           = 0x100
PCI_BUS_OEM_ID_VALID_BIT_MASK           = 0x200
PCI_BUS_OEM_DATA_STRUCT_VALID_BIT_MASK  = 0x400

class PCI_BUS_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BusNumber",     UINT8),
    ("SegmentNumber", UINT8)
  ]

class SAL_PCI_BUS_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",     SAL_SEC_HEADER),
    ("ValidationBits",    UINT64),
    ("PciBusErrorStatus", UINT64),
    ("PciBusErrorType",   UINT16),
    ("PciBusId",          PCI_BUS_ID),
    ("Reserved",          UINT32),
    ("PciBusAddress",     UINT64),
    ("PciBusData",        UINT64),
    ("PciBusCommand",     UINT64),
    ("PciBusRequestorId", UINT64),
    ("PciBusResponderId", UINT64),
    ("PciBusTargetId",    UINT64),
    ("PciBusOemId",       UINT8 * 16),
  ]

SAL_PCI_COMP_ERROR_RECORD_INFO = EFI_GUID (0xe429faf6, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

PCI_COMP_ERROR_STATUS_VALID_BIT_MASK    = 0x1
PCI_COMP_INFO_VALID_BIT_MASK            = 0x2
PCI_COMP_MEM_NUM_VALID_BIT_MASK         = 0x4
PCI_COMP_IO_NUM_VALID_BIT_MASK          = 0x8
PCI_COMP_REG_DATA_PAIR_VALID_BIT_MASK   = 0x10
PCI_COMP_OEM_DATA_STRUCT_VALID_BIT_MASK = 0x20

class PCI_COMP_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VendorId",        UINT16),
    ("DeviceId",        UINT16),
    ("ClassCode",       UINT8* 3),
    ("FunctionNumber",  UINT8),
    ("DeviceNumber",    UINT8),
    ("BusNumber",       UINT8),
    ("SegmentNumber",   UINT8),
    ("Reserved",        UINT8 * 5),
  ]

class SAL_PCI_COMPONENT_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",           SAL_SEC_HEADER),
    ("ValidationBits",          UINT64),
    ("PciComponentErrorStatus", UINT64),
    ("PciComponentInfo",        PCI_COMP_INFO),
    ("PciComponentMemNum",      UINT32),
    ("PciComponentIoNum",       UINT32),
    ("PciBusOemId",             UINT8 * 16)
  ]

SAL_SEL_DEVICE_ERROR_RECORD_INFO = EFI_GUID (0xe429faf3, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

SEL_RECORD_ID_VALID_BIT_MASK      = 0x1
SEL_RECORD_TYPE_VALID_BIT_MASK    = 0x2
SEL_GENERATOR_ID_VALID_BIT_MASK   = 0x4
SEL_EVM_REV_VALID_BIT_MASK        = 0x8
SEL_SENSOR_TYPE_VALID_BIT_MASK    = 0x10
SEL_SENSOR_NUM_VALID_BIT_MASK     = 0x20
SEL_EVENT_DIR_TYPE_VALID_BIT_MASK = 0x40
SEL_EVENT_DATA1_VALID_BIT_MASK    = 0x80
SEL_EVENT_DATA2_VALID_BIT_MASK    = 0x100
SEL_EVENT_DATA3_VALID_BIT_MASK    = 0x200

class SAL_SEL_DEVICE_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",   SAL_SEC_HEADER),
    ("ValidationBits",  UINT64),
    ("SelRecordId",     UINT16),
    ("SelRecordType",   UINT8),
    ("TimeStamp",       UINT32),
    ("GeneratorId",     UINT16),
    ("EvmRevision",     UINT8),
    ("SensorType",      UINT8),
    ("SensorNum",       UINT8),
    ("EventDirType",    UINT8),
    ("Data1",           UINT8),
    ("Data2",           UINT8),
    ("Data3",           UINT8),
  ]

SAL_SMBIOS_ERROR_RECORD_INFO = EFI_GUID (0xe429faf5, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

SMBIOS_EVENT_TYPE_VALID_BIT_MASK  = 0x1
SMBIOS_LENGTH_VALID_BIT_MASK      = 0x2
SMBIOS_TIME_STAMP_VALID_BIT_MASK  = 0x4
SMBIOS_DATA_VALID_BIT_MASK        = 0x8

class SAL_SMBIOS_DEVICE_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",       SAL_SEC_HEADER),
    ("ValidationBits",      UINT64),
    ("SmbiosEventType",     UINT8),
    ("SmbiosLength",        UINT8),
    ("SmbiosBcdTimeStamp",  UINT8 * 6),
  ]

SAL_PLATFORM_ERROR_RECORD_INFO = EFI_GUID (0xe429faf7, 0x3cb7, 0x11d4, (0xbc, 0xa7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

PLATFORM_ERROR_STATUS_VALID_BIT_MASK    = 0x1
PLATFORM_REQUESTOR_ID_VALID_BIT_MASK    = 0x2
PLATFORM_RESPONDER_ID_VALID_BIT_MASK    = 0x4
PLATFORM_TARGET_VALID_BIT_MASK          = 0x8
PLATFORM_SPECIFIC_DATA_VALID_BIT_MASK   = 0x10
PLATFORM_OEM_ID_VALID_BIT_MASK          = 0x20
PLATFORM_OEM_DATA_STRUCT_VALID_BIT_MASK = 0x40
PLATFORM_OEM_DEVICE_PATH_VALID_BIT_MASK = 0x80

class SAL_PLATFORM_SPECIFIC_ERROR_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionHeader",           SAL_SEC_HEADER),
    ("ValidationBits",          UINT64),
    ("PlatformErrorStatus",     UINT64),
    ("PlatformRequestorId",     UINT64),
    ("PlatformResponderId",     UINT64),
    ("PlatformTargetId",        UINT64),
    ("PlatformBusSpecificData", UINT64),
    ("OemComponentId",          UINT8 * 16)
  ]

class SAL_ERROR_RECORDS_POINTERS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("RecordHeader",          POINTER (SAL_RECORD_HEADER)),
    ("SalProcessorRecord",    POINTER (SAL_PROCESSOR_ERROR_RECORD)),
    ("SalPciBusRecord",       POINTER (SAL_PCI_BUS_ERROR_RECORD)),
    ("SalPciComponentRecord", POINTER (SAL_PCI_COMPONENT_ERROR_RECORD)),
    ("ImpiRecord",            POINTER (SAL_SEL_DEVICE_ERROR_RECORD)),
    ("SmbiosRecord",          POINTER (SAL_SMBIOS_DEVICE_ERROR_RECORD)),
    ("PlatformRecord",        POINTER (SAL_PLATFORM_SPECIFIC_ERROR_RECORD)),
    ("MemoryRecord",          POINTER (SAL_MEMORY_ERROR_RECORD)),
    ("Raw",                   POINTER (UINT8))
  ]

