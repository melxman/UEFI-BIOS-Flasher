#
# Pal.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Pal.py is free software: you can redistribute it and/or modify
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

PAL_SUCCESS             = 0x0

PAL_CACHE_FLUSH_INSTRUCTION_ALL   = 1
PAL_CACHE_FLUSH_DATA_ALL          = 2
PAL_CACHE_FLUSH_ALL               = 3
PAL_CACHE_FLUSH_SYNC_TO_DATA      = 4

PAL_CACHE_FLUSH_INVALIDATE_LINES     = BIT0
PAL_CACHE_FLUSH_NO_INVALIDATE_LINES  = 0
PAL_CACHE_FLUSH_POLL_INTERRUPT       = BIT1
PAL_CACHE_FLUSH_NO_INTERRUPT         = 0

PAL_CACHE_FLUSH   = 1

PAL_CACHE_ATTR_WT   = 0
PAL_CACHE_ATTR_WB   = 1

PAL_CACHE_STORE_TEMPORAL      = 0
PAL_CACHE_STORE_NONE_TEMPORAL = 3

PAL_CACHE_STORE_TEMPORAL_LVL_1        = 0
PAL_CACHE_STORE_NONE_TEMPORAL_LVL_ALL = 3

PAL_CACHE_LOAD_TEMPORAL_LVL_1         = 0
PAL_CACHE_LOAD_NONE_TEMPORAL_LVL_1    = 1
PAL_CACHE_LOAD_NONE_TEMPORAL_LVL_ALL  = 3

class PAL_CACHE_INFO_RETURN1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IsUnified",     UINT64, 1),
    ("Attributes",    UINT64, 2),
    ("Associativity", UINT64, 8),
    ("LineSize",      UINT64, 8),
    ("Stride",        UINT64, 8),
    ("StoreLatency",  UINT64, 8),
    ("StoreHint",     UINT64, 8),
    ("LoadHint",      UINT64, 8),
  ]

class PAL_CACHE_INFO_RETURN2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheSize",     UINT64, 32),
    ("AliasBoundary", UINT64, 8),
    ("TagLsBits",     UINT64, 8),
    ("TagMsBits",     UINT64, 8)
  ]

PAL_CACHE_INFO    = 2

PAL_CACHE_INIT_ALL  = 0xffffffffffffffffL

PAL_CACHE_INIT_TYPE_INSTRUCTION                 = 0x1
PAL_CACHE_INIT_TYPE_DATA                        = 0x2
PAL_CACHE_INIT_TYPE_INSTRUCTION_AND_DATA        = 0x3

PAL_CACHE_INIT_NO_RESTRICT  = 0
PAL_CACHE_INIT_RESTRICTED   = 1

PAL_CACHE_INIT    = 3

PAL_CACHE_PROTECTION_NONE_PROTECT   = 0
PAL_CACHE_PROTECTION_ODD_PROTECT    = 1
PAL_CACHE_PROTECTION_EVEN_PROTECT   = 2
PAL_CACHE_PROTECTION_ECC_PROTECT    = 3

PAL_CACHE_PROTECTION_PROTECT_DATA   = 0
PAL_CACHE_PROTECTION_PROTECT_TAG    = 1
PAL_CACHE_PROTECTION_PROTECT_TAG_ANDTHEN_DATA   = 2
PAL_CACHE_PROTECTION_PROTECT_DATA_ANDTHEN_TAG   = 3

class PAL_CACHE_PROTECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBits",    UINT32, 8),
    ("TagProtLsb",  UINT32, 6),
    ("TagProtMsb",  UINT32, 6),
    ("ProtBits",    UINT32, 6),
    ("Method",      UINT32, 4),
    ("TagOrData",   UINT32, 2)
  ]

PAL_CACHE_PROT_INFO     = 38

class PAL_PCOC_N_CACHE_INFO1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ThreadId",  UINT64, 16),
    ("Reserved1", UINT64, 16),
    ("CoreId",    UINT64, 16),
    ("Reserved2", UINT64, 16)
  ]

class PAL_PCOC_N_CACHE_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogicalAddress",  UINT64, 16),
    ("Reserved1",       UINT64, 16),
    ("Reserved2",       UINT64, 32)
  ]

PAL_CACHE_SHARED_INFO   = 43

PAL_CACHE_SUMMARY   = 4

PAL_MEMORY_ATTR_WB      = 0
PAL_MEMORY_ATTR_WC      = 6
PAL_MEMORY_ATTR_UC      = 4
PAL_MEMORY_ATTR_UCE     = 5
PAL_MEMORY_ATTR_NATPAGE = 7

PAL_MEM_ATTRIB      = 5

PAL_PREFETCH_VISIBILITY   = 41

PAL_PTCE_INFO     = 6

class PAL_TC_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberSets",          UINT64, 8),
    ("NumberWays",          UINT64, 8),
    ("NumberEntries",       UINT64, 16),
    ("PageSizeIsOptimized", UINT64, 1),
    ("TcIsUnified",         UINT64, 1),
    ("EntriesReduction",    UINT64, 1),
  ]

PAL_VM_INFO       = 7

PAL_VM_PAGE_SIZE = 34

class PAL_VM_INFO1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WalkerPresent",           UINT64, 1),
    ("WidthOfPhysicalAddress",  UINT64, 7),
    ("WidthOfKey",              UINT64, 8),
    ("MaxPkrIndex",             UINT64, 8),
    ("HashTagId",               UINT64, 8),
    ("MaxDtrIndex",             UINT64, 8),
    ("MaxItrIndex",             UINT64, 8),
    ("NumberOfUniqueTc",        UINT64, 8),
    ("NumberOfTcLevels",        UINT64, 8)
  ]

class PAL_VM_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WidthOfVirtualAddress", UINT64, 8),
    ("WidthOfRid",            UINT64, 8),
    ("MaxPurgedTlbs",         UINT64, 16),
    ("Reserved",              UINT64, 32)
  ]

PAL_VM_SUMMARY  = 8

PAL_TR_ACCESS_RIGHT_IS_VALID      = BIT0
PAL_TR_PRIVILEGE_LEVEL_IS_VALID   = BIT1
PAL_TR_DIRTY_IS_VALID             = BIT2
PAL_TR_MEMORY_ATTR_IS_VALID       = BIT3

PAL_VM_TR_READ  = 261

PAL_BUS_DISABLE_DATA_ERROR_SIGNALLING   = BIT63

PAL_BUS_DISABLE_ADDRESS_ERROR_SIGNALLING   = BIT62

PAL_BUS_DISABLE_ADDRESS_ERROR_CHECK   = BIT61

PAL_BUS_DISABLE_INITIALIZATION_EVENT_SIGNALLING   = BIT60

PAL_BUS_DISABLE_INITIALIZATION_EVENT_CHECK   = BIT59

PAL_BUS_DISABLE_ERROR_SIGNALLING   = BIT58

PAL_BUS_DISABLE__INTERNAL_ERROR_SIGNALLING   = BIT57

PAL_BUS_DISABLE_ERROR_CHECK   = BIT5

PAL_BUS_DISABLE_RSP_ERROR_CHECK   = BIT55

PAL_BUS_DISABLE_TRANSACTION_QUEUE   = BIT54

PAL_BUS_ENABLE_EXCLUSIVE_CACHE_LINE_REPLACEMENT   = BIT53

PAL_BUS_ENABLE_SHARED_CACHE_LINE_REPLACEMENT   = BIT52

PAL_BUS_ENABLE_HALF_TRANSFER   = BIT30

PAL_BUS_REQUEST_BUS_PARKING   = BIT29

PAL_BUS_GET_FEATURES = 9

PAL_BUS_SET_FEATURES = 10

PAL_DEBUG_INFO  = 11

PAL_FIXED_ADDR = 12

PAL_FREQ_BASE = 13

PAL_FREQ_RATIOS = 14

class PAL_LOGICAL_PROCESSPR_OVERVIEW (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfLogicalProcessors",   UINT64, 16),
    ("ThreadsPerCore",              UINT64, 8),
    ("Reserved1",                   UINT64, 8),
    ("CoresPerProcessor",           UINT64, 8),
    ("Reserved2",                   UINT64, 8),
    ("PhysicalProcessorPackageId",  UINT64, 8),
    ("Reserved3",                   UINT64, 8)
  ]

class PAL_LOGICAL_PROCESSORN_INFO1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ThreadId",  UINT64, 16),
    ("Reserved1", UINT64, 16),
    ("CoreId",    UINT64, 16),
    ("Reserved2", UINT64, 16)
  ]

class PAL_LOGICAL_PROCESSORN_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogicalAddress",  UINT64, 16),
    ("Reserved",        UINT64, 48)
  ]

PAL_LOGICAL_TO_PHYSICAL = 42

class PAL_PERFORMANCE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfPmcPairs",                UINT64, 8),
    ("WidthOfCounter",                  UINT64, 8),
    ("TypeOfCycleCounting",             UINT64, 8),
    ("TypeOfRetiredInstructionBundle",  UINT64, 8),
    ("Reserved",                        UINT64, 32)
  ]

PAL_PERF_MON_INFO = 15

PAL_PLATFORM_ADDR_INTERRUPT_BLOCK_TOKEN                       = 0x0
PAL_PLATFORM_ADDR_IO_BLOCK_TOKEN                              = 0x1

PAL_PLATFORM_ADDR = 16

class PAL_PROCESSOR_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",                       UINT64, 36),
    ("FaultInUndefinedIns",             UINT64, 1),
    ("NoPresentPmi",                    UINT64, 1),
    ("NoSimpleImpInUndefinedIns",       UINT64, 1),
    ("NoVariablePState",                UINT64, 1),
    ("NoVM",                            UINT64, 1),
    ("NoXipXpsrXfs",                    UINT64, 1),
    ("NoXr1ThroughXr3",                 UINT64, 1),
    ("DisableDynamicPrediction",        UINT64, 1),
    ("DisableSpontaneousDeferral",      UINT64, 1),
    ("DisableDynamicDataCachePrefetch", UINT64, 1),
    ("DisableDynamicInsCachePrefetch",  UINT64, 1),
    ("DisableBranchPrediction",         UINT64, 1),
    ("Reserved2",                       UINT64, 4),
    ("DisablePState",                   UINT64, 1),
    ("EnableMcaOnDataPoisoning",        UINT64, 1),
    ("EnableVmsw",                      UINT64, 1),
    ("EnableEnvNotification",           UINT64, 1),
    ("DisableBinitWithTimeout",         UINT64, 1),
    ("DisableDPM",                      UINT64, 1),
    ("DisableCoherency",                UINT64, 1),
    ("DisableCache",                    UINT64, 1),
    ("EnableCmciPromotion",             UINT64, 1),
    ("EnableMcaToBinitPromotion",       UINT64, 1),
    ("EnableMcaPromotion",              UINT64, 1),
    ("EnableBerrPromotion",             UINT64, 1)
  ]

PAL_PROC_GET_FEATURES = 17

PAL_PROC_SET_FEATURES = 18

PAL_APPLICATION_REGISTER_IMPLEMENTED  = 0
PAL_APPLICATION_REGISTER_READABLE     = 1
PAL_CONTROL_REGISTER_IMPLEMENTED      = 2
PAL_CONTROL_REGISTER_READABLE         = 3

PAL_REGISTER_INFO = 39

PAL_RSE_INFO = 19

class PAL_VERSION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VersionOfPalB", UINT64, 16),
    ("Reserved1",     UINT64, 8),
    ("PalVendor",     UINT64, 8),
    ("VersionOfPalA", UINT64, 16),
    ("Reserved2",     UINT64, 16)
  ]

PAL_VERSION = 20

PAL_MC_PENDING    = BIT0
PAL_INIT_PENDING  = BIT1

PAL_MC_CLEAR_LOG = 21

PAL_MC_DRAIN = 22

PAL_MC_DYNAMIC_STATE = 24

PAL_PROCESSOR_ERROR_MAP       = 0
PAL_PROCESSOR_STATE_PARAM     = 1
PAL_STRUCTURE_SPECIFIC_ERROR  = 2

class PAL_MC_ERROR_INFO_LEVEL_INDEX (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CoreId",              UINT64, 4),
    ("ThreadId",            UINT64, 4),
    ("InfoOfInsCache",      UINT64, 4),
    ("InfoOfDataCache",     UINT64, 4),
    ("InfoOfInsTlb",        UINT64, 4),
    ("InfoOfDataTlb",       UINT64, 4),
    ("InfoOfProcessorBus",  UINT64, 4),
    ("InfoOfRegisterFile",  UINT64, 4),
    ("InfoOfMicroArch",     UINT64, 4),
    ("Reserved",            UINT64, 16)
  ]

PAL_ERR_INFO_BY_LEVEL_INDEX               = 0
PAL_ERR_INFO_TARGET_ADDRESS               = 1
PAL_ERR_INFO_REQUESTER_IDENTIFIER         = 2
PAL_ERR_INFO_REPONSER_INDENTIFIER         = 3
PAL_ERR_INFO_PRECISE_INSTRUCTION_POINTER  = 4

class PAL_VERSION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Operation",               UINT64, 4),
    ("FailedCacheLevel",        UINT64, 2),
    ("Reserved1",               UINT64, 2),
    ("FailedInDataPart",        UINT64, 1),
    ("FailedInTagPart",         UINT64, 1),
    ("FailedInDataCache",       UINT64, 1),
    ("FailedInInsCache",        UINT64, 1),
    ("Mesi",                    UINT64, 3),
    ("MesiIsValid",             UINT64, 1),
    ("FailedWay",               UINT64, 5),
    ("WayIndexIsValid",         UINT64, 1),
    ("Reserved2",               UINT64, 1),
    ("MultipleBitsError",       UINT64, 1),
    ("Reserved3",               UINT64, 8),
    ("IndexOfCacheLineError",   UINT64, 20),
    ("Reserved4",               UINT64, 2),
    ("InstructionSet",          UINT64, 1),
    ("InstructionSetIsValid",   UINT64, 1),
    ("PrivilegeLevel",          UINT64, 2),
    ("PrivilegeLevelIsValide",  UINT64, 1),
    ("McCorrected",             UINT64, 1),
    ("TargetAddressIsValid",    UINT64, 1),
    ("RequesterIdentifier",     UINT64, 1),
    ("ResponserIdentifier",     UINT64, 1),
    ("PreciseInsPointer",       UINT64, 1)
  ]

class PAL_TLB_CHECK_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FailedSlot",            UINT64, 8),
    ("FailedSlotIsValid",     UINT64, 1),
    ("Reserved1",             UINT64, 1),
    ("TlbLevel",              UINT64, 2),
    ("Reserved2",             UINT64, 4),
    ("FailedInDataTr",        UINT64, 1),
    ("FailedInInsTr",         UINT64, 1),
    ("FailedInDataTc",        UINT64, 1),
    ("FailedInInsTc",         UINT64, 1),
    ("FailedOperation",       UINT64, 4),
    ("Reserved3",             UINT64, 30),
    ("InstructionSet",        UINT64, 1),
    ("InstructionSetIsValid", UINT64, 1),
    ("PrivelegeLevel",        UINT64, 2),
    ("PrivelegeLevelIsValid", UINT64, 1),
    ("McCorrected",           UINT64, 1),
    ("TargetAddressIsValid",  UINT64, 1),
    ("RequesterIdentifier",   UINT64, 1),
    ("ResponserIdentifier",   UINT64, 1),
    ("PreciseInsPointer",     UINT64, 1)
  ]

PAL_MC_ERROR_INFO = 25

PAL_MC_EXPECTED = 23

PAL_MC_REGISTER_MEM = 27

PAL_MC_RESUME = 26

PAL_HALT = 28

PAL_HALT_INFO = 257

PAL_HALT_LIGHT = 29

PAL_CACHE_LINE_INIT = 31
PAL_CACHE_READ = 259

PAL_CACHE_WRITE = 260

PAL_TEST_INFO = 37

class PAL_TEST_INFO_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BufferSize",  UINT64, 56),
    ("TestPhase",   UINT64, 8)
  ]

class PAL_SELF_TEST_CONTROL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TestControl",     UINT64, 47),
    ("ControlSupport",  UINT64, 1),
    ("Reserved",        UINT64, 16)
  ]

class PAL_TEST_CONTROL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Attributes",  UINT64, 8),
    ("Reserved",    UINT64, 8),
    ("TestControl", UINT64, 48)
  ]

PAL_TEST_PROC = 258

class PAL_PLATFORM_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfInterruptControllers",  UINT32),
    ("NumberOfProcessors",            UINT32)
  ]

PAL_COPY_INFO = 30

PAL_COPY_PAL = 256

PAL_ENTER_IA_32_ENV = 33

PAL_PMI_ENTRYPOINT = 32

PAL_BRAND_INFO_ID_REQUEST  = 0

PAL_BRAND_INFO  = 274

PAL_GET_HW_POLICY   = 48

PAL_SET_HW_POLICY_PERFORMANCE               = 0
PAL_SET_HW_POLICY_FAIRNESS                  = 1
PAL_SET_HW_POLICY_HIGH_PRIORITY             = 2
PAL_SET_HW_POLICY_EXCLUSIVE_HIGH_PRIORITY   = 3

PAL_SET_HW_POLICY   = 49

class PAL_MC_ERROR_TYPE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mode",                UINT64, 3),
    ("ErrorInjection",      UINT64, 3),
    ("ErrorSeverity",       UINT64, 2),
    ("ErrorStructure",      UINT64, 5),
    ("StructureHierarchy",  UINT64, 3),
    ("Reserved",            UINT64, 32),
    ("ImplSpec",            UINT64, 16)
  ]

class PAL_MC_ERROR_STRUCT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("StructInfoIsValid",     UINT64, 1),
    ("CacheType",             UINT64, 2),
    ("PortionOfCacheLine",    UINT64, 3),
    ("Mechanism",             UINT64, 3),
    ("DataPoisonOfCacheLine", UINT64, 1),
    ("Reserved1",             UINT64, 22),
    ("TrigerInfoIsValid",     UINT64, 1),
    ("Triger",                UINT64, 4),
    ("PrivilegeOfTriger",     UINT64, 3),
    ("Reserved2",             UINT64, 24)
  ]

class PAL_MC_ERROR_DATA_BUFFER_TLB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TrigerAddress",     UINT64),
    ("VirtualPageNumber", UINT64, 52),
    ("Reserved1",         UINT64, 8),
    ("RegionId",          UINT64, 24),
    ("Reserved2",         UINT64, 40)
  ]

PAL_MC_ERROR_INJECT = 276

PAL_GET_PSTATE_RECENT                 = 0
PAL_GET_PSTATE_AVERAGE_NEW_START      = 1
PAL_GET_PSTATE_AVERAGE                = 2
PAL_GET_PSTATE_NOW                    = 3

PAL_GET_PSTATE      = 262

class PAL_PSTATE_INFO_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PerformanceIndex",        UINT32, 7),
    ("Reserved1",               UINT32, 5),
    ("TypicalPowerDissipation", UINT32, 20),
    ("TransitionLatency1",      UINT32),
    ("TransitionLatency2",      UINT32),
    ("Reserved2",               UINT32)
  ]

PAL_PSTATE_INFO     = 44

PAL_SET_PSTATE      = 263

PAL_SHUTDOWN        = 45

class PAL_MEMORY_CONTROL_WORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Registration",    UINT64, 1),
    ("ProbeInterrupt",  UINT64, 1),
    ("Reserved",        UINT64, 62)
  ]

PAL_MEMORY_BUFFER   = 277

PAL_VP_CREATE       = 265

class PAL_VP_ENV_INFO_RETURN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1", UINT64, 8),
    ("Opcode",    UINT64, 1),
    ("Reserved",  UINT64, 53)
  ]

PAL_VP_ENV_INFO       = 266

PAL_VP_EXIT_ENV       = 267

PAL_VP_INIT_ENV       = 268

PAL_VP_REGISTER       = 269

PAL_VP_RESTORE       = 270

PAL_VP_SAVE       = 271

PAL_VP_TERMINATE       = 272

