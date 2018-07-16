#
# IpmiNetFnStorage.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiNetFnStorage.py is free software: you can redistribute it and/or modify
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

IPMI_NETFN_STORAGE  = 0x0A

IPMI_STORAGE_GET_FRU_INVENTORY_AREAINFO  = 0x10

IPMI_STORAGE_READ_FRU_DATA = 0x11

class IPMI_FRU_COMMON_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FruDeviceId", UINT8),
    ("FruOffset",   UINT16)
  ]

class IPMI_FRU_READ_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",  IPMI_FRU_COMMON_DATA),
    ("Count", UINT8)
  ]

IPMI_STORAGE_WRITE_FRU_DATA  = 0x12

class IPMI_FRU_WRITE_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    IPMI_FRU_COMMON_DATA),
    ("FruData", UINT8 * 16)
  ]

IPMI_STORAGE_GET_SDR_REPOSITORY_INFO = 0x20

class IPMI_GET_SDR_REPOSITORY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode;           ", UINT8),
    ("Version;                  ", UINT8),
    ("RecordCount;              ", UINT16),
    ("FreeSpace;                ", UINT16),
    ("RecentAdditionTimeStamp;  ", UINT32),
    ("RecentEraseTimeStamp;     ", UINT32),
    ("SdrRepAllocInfoCmd : 1;   ", UINT8, 1),
    ("SdrRepReserveCmd : 1;     ", UINT8, 1),
    ("PartialAddSdrCmd : 1;     ", UINT8, 1),
    ("DeleteSdrRepCmd : 1;      ", UINT8, 1),
    ("Reserved : 1;             ", UINT8, 1),
    ("SdrRepUpdateOp : 2;       ", UINT8, 2),
    ("Overflow : 1;             ", UINT8, 1)
  ]

IPMI_STORAGE_GET_SDR_REPOSITORY_ALLOCATION_INFO  = 0x21

IPMI_STORAGE_RESERVE_SDR_REPOSITORY  = 0x22

IPMI_STORAGE_GET_SDR = 0x23

class IPMI_SDR_RECORD_STRUCT_1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",                      UINT16),
    ("Version",                       UINT8),
    ("RecordType",                    UINT8),
    ("RecordLength",                  UINT8),
    ("OwnerId",                       UINT8),
    ("OwnerLun",                      UINT8),
    ("SensorNumber",                  UINT8),
    ("EntityId",                      UINT8),
    ("EntityInstance",                UINT8),
    ("EventScanningEnabled",          UINT8, 1),
    ("EventScanningDisabled",         UINT8, 1),
    ("InitSensorType",                UINT8, 1),
    ("InitHysteresis",                UINT8, 1),
    ("InitThresholds",                UINT8, 1),
    ("InitEvent",                     UINT8, 1),
    ("InitScanning",                  UINT8, 1),
    ("Reserved",                      UINT8, 1),
    ("EventMessageControl",           UINT8, 2),
    ("ThresholdAccessSupport",        UINT8, 2),
    ("HysteresisSupport",             UINT8, 2),
    ("ReArmSupport",                  UINT8, 1),
    ("IgnoreSensor",                  UINT8, 1),
    ("SensorType",                    UINT8, 1),
    ("EventType",                     UINT8, 1),
    ("Reserved1",                     UINT8 * 7),
    ("UnitType",                      UINT8),
    ("Reserved2",                     UINT8),
    ("Linearization",                 UINT8, 7),
    ("Reserved3",                     UINT8, 1),
    ("MLo",                           UINT8),
    ("Toleremce",                     UINT8, 6),
    ("MHi",                           UINT8, 2),
    ("BLo",                           UINT8),
    ("AccuracyLow",                   UINT8, 6),
    ("BHi",                           UINT8, 2),
    ("Reserved4",                     UINT8, 2),
    ("AccuracyExp",                   UINT8, 2),
    ("AccuracyHi",                    UINT8, 4),
    ("BExp",                          UINT8, 4),
    ("RExp",                          UINT8, 4),
    ("NominalReadingSpscified",       UINT8, 1),
    ("NominalMaxSpscified",           UINT8, 1),
    ("NominalMinSpscified",           UINT8, 1),
    ("Reserved5",                     UINT8, 5),
    ("NominalReading",                UINT8),
    ("Reserved6",                     UINT8 * 4),
    ("UpperNonRecoverThreshold",      UINT8),
    ("UpperCriticalThreshold",        UINT8),
    ("UpperNonCriticalThreshold",     UINT8),
    ("LowerNonRecoverThreshold",      UINT8),
    ("LowerCriticalThreshold",        UINT8),
    ("LowerNonCriticalThreshold",     UINT8),
    ("Reserved7",                     UINT8 * 5),
    ("IdStringLength",                UINT8),
    ("AsciiIdString",                 UINT8 * 16),
  ]

class IPMI_SDR_RECORD_STRUCT_2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",                  UINT16),
    ("Version",                   UINT8),
    ("RecordType",                UINT8),
    ("RecordLength",              UINT8),
    ("OwnerId",                   UINT8),
    ("OwnerLun",                  UINT8),
    ("SensorNumber",              UINT8),
    ("EntityId",                  UINT8),
    ("EntityInstance",            UINT8),
    ("SensorScanning",            UINT8, 1),
    ("EventScanning",             UINT8, 1),
    ("InitSensorType",            UINT8, 1),
    ("InitHysteresis",            UINT8, 1),
    ("InitThresholds",            UINT8, 1),
    ("InitEvent",                 UINT8, 1),
    ("InitScanning",              UINT8, 1),
    ("Reserved",                  UINT8, 1),
    ("EventMessageControl",       UINT8, 1),
    ("ThresholdAccessSupport",    UINT8, 1),
    ("HysteresisSupport",         UINT8, 1),
    ("ReArmSupport",              UINT8, 1),
    ("IgnoreSensor",              UINT8, 1),
    ("SensorType",                UINT8),
    ("EventType",                 UINT8),
    ("Reserved1",                 UINT8 * 7),
    ("UnitType",                  UINT8),
    ("Reserved2",                 UINT8 * 9),
    ("IdStringLength",            UINT8),
    ("AsciiIdString",             UINT8 * 16)
  ]

class IPMI_FRU_DATA_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",               UINT8, 1),
    ("ControllerSlaveAddress",  UINT8, 7),
    ("FruDeviceId",             UINT8),
    ("BusId",                   UINT8, 3),
    ("Lun",                     UINT8, 2),
    ("Reserved",                UINT8, 2),
    ("LogicalFruDevice",        UINT8, 1),
    ("Reserved3",               UINT8, 4),
    ("ChannelNumber",           UINT8, 4)
  ]

class IPMI_SDR_RECORD_STRUCT_11 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",              UINT16),
    ("Version",               UINT8),
    ("RecordType",            UINT8),
    ("RecordLength",          UINT8),
    ("FruDeviceData",         IPMI_FRU_DATA_INFO),
    ("Reserved1",             UINT8),
    ("DeviceType",            UINT8),
    ("DeviceTypeModifier",    UINT8),
    ("FruEntityId",           UINT8),
    ("FruEntityInstance",     UINT8),
    ("OemReserved",           UINT8),
    ("Length",                UINT8, 4),
    ("Reserved2",             UINT8, 1),
    ("StringType",            UINT8, 3),
    ("String",                UINT8 * 16)
  ]

class IPMI_SDR_RECORD_STRUCT_C0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NextRecordId",    UINT16),
    ("RecordId",        UINT16),
    ("Version",         UINT8),
    ("RecordType",      UINT8),
    ("RecordLength",    UINT8),
    ("ManufacturerId",  UINT8 * 3),
    ("StringChars",     UINT8 * 20)
  ]

class IPMI_SDR_RECORD_STRUCT_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NextRecordId",  UINT16),
    ("RecordId",      UINT16),
    ("Version",       UINT8),
    ("RecordType",    UINT8),
    ("RecordLength",  UINT8)
  ]

class IPMI_SENSOR_RECORD_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SensorType1",  IPMI_SDR_RECORD_STRUCT_1),
    ("SensorType2",  IPMI_SDR_RECORD_STRUCT_2),
    ("SensorType11", IPMI_SDR_RECORD_STRUCT_11),
    ("SensorTypeC0", IPMI_SDR_RECORD_STRUCT_C0),
    ("SensorHeader", IPMI_SDR_RECORD_STRUCT_HEADER)
  ]

class IPMI_GET_SDR_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReservationId", UINT16),
    ("RecordId",      UINT16),
    ("RecordOffset",  UINT8),
    ("BytesToRead",   UINT8)
  ]

IPMI_STORAGE_ADD_SDR = 0x24

IPMI_STORAGE_PARTIAL_ADD_SDR = 0x25

IPMI_STORAGE_DELETE_SDR  = 0x26

IPMI_STORAGE_CLEAR_SDR = 0x27

IPMI_STORAGE_GET_SDR_REPOSITORY_TIME = 0x28

IPMI_STORAGE_SET_SDR_REPOSITORY_TIME = 0x29

IPMI_STORAGE_ENTER_SDR_UPDATE_MODE = 0x2A

IPMI_STORAGE_EXIT_SDR_UPDATE_MODE  = 0x2B

IPMI_STORAGE_RUN_INIT_AGENT  = 0x2C

IPMI_STORAGE_GET_SEL_INFO  = 0x40

class IPMI_GET_SEL_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",        UINT8),
    ("Version",               UINT8),
    ("NoOfEntries",           UINT16),
    ("FreeSpace",             UINT16),
    ("RecentAddTimeStamp",    UINT32),
    ("RecentEraseTimeStamp",  UINT32),
    ("OperationSupport",      UINT8)
  ]

IPMI_STORAGE_GET_SEL_ALLOCATION_INFO = 0x41

IPMI_STORAGE_RESERVE_SEL = 0x42

IPMI_STORAGE_GET_SEL_ENTRY = 0x43

class IPMI_GET_SEL_ENTRY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReserveId",   UINT8 * 2),
    ("SelRecID",    UINT8 * 2),
    ("Offset",      UINT8),
    ("BytesToRead", UINT8)
  ]

IPMI_STORAGE_ADD_SEL_ENTRY = 0x44

IPMI_STORAGE_PARTIAL_ADD_SEL_ENTRY = 0x45

IPMI_STORAGE_DELETE_SEL_ENTRY  = 0x46

class IPMI_DELETE_SEL_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReserveId",       UINT8 * 2),
    ("RecordToDelete",  UINT8 * 2)
  ]

IPMI_STORAGE_CLEAR_SEL = 0x47

class IPMI_CLEAR_SEL_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserve", UINT8),
    ("AscC",    UINT8),
    ("AscL",    UINT8),
    ("AscR",    UINT8),
    ("Erase",   UINT8)
  ]

IPMI_STORAGE_GET_SEL_TIME  = 0x48

IPMI_STORAGE_SET_SEL_TIME  = 0x49

IPMI_STORAGE_GET_AUXILLARY_LOG_STATUS  = 0x5A

IPMI_STORAGE_SET_AUXILLARY_LOG_STATUS  = 0x5B

IPMI_COMPLETE_SEL_RECORD = 0xFF

class IPMI_SEL_EVENT_RECORD_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",      UINT16),
    ("RecordType",    UINT8),
    ("TimeStamp",     UINT32),
    ("GeneratorId",   UINT16),
    ("EvMRevision",   UINT8),
    ("SensorType",    UINT8),
    ("SensorNumber",  UINT8),
    ("EventDirType",  UINT8),
    ("OEMEvData1",    UINT8),
    ("OEMEvData2",    UINT8),
    ("OEMEvData3",    UINT8)
  ]

IPMI_SEL_SYSTEM_RECORD                     = 0x02

IPMI_EVM_REVISION                          = 0x04
IPMI_BIOS_ID                               = 0x18
IPMI_FORMAT_REV                            = 0x00
IPMI_FORMAT_REV1                           = 0x01
IPMI_SOFTWARE_ID                           = 0x01
IPMI_PLATFORM_VAL_ID                       = 0x01

def IPMI_GENERATOR_ID(i,f):
  return ((i << 1) | (f << 1) | IPMI_SOFTWARE_ID)

IPMI_SENSOR_TYPE_EVENT_CODE_DISCRETE       = 0x6F
IPMI_OEM_SPECIFIC_DATA                     = 0x02
IPMI_SENSOR_SPECIFIC_DATA                  = 0x03
