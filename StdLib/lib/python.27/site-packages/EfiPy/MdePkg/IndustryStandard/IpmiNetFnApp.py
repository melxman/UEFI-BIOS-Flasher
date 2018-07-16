#
# IpmiNetFnApp.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiNetFnApp.py is free software: you can redistribute it and/or modify
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

IPMI_NETFN_APP  = 0x06

IPMI_APP_GET_DEVICE_ID = 0x1

class IPMI_GET_DEVICE_ID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",          UINT8),
    ("DeviceId",                UINT8),
    ("DeviceRevision",          UINT8, 4),
    ("Reserved",                UINT8, 3),
    ("DeviceSdr",               UINT8, 1),
    ("MajorFirmwareRev",        UINT8, 7),
    ("UpdateMode",              UINT8, 1),
    ("MinorFirmwareRev",        UINT8),
    ("SpecificationVersion",    UINT8),
    ("SensorDeviceSupport",     UINT8, 1),
    ("SdrRepositorySupport",    UINT8, 1),
    ("SelDeviceSupport",        UINT8, 1),
    ("FruInventorySupport",     UINT8, 1),
    ("IpmbMessageReceiver",     UINT8, 1),
    ("IpmbMessageGenerator",    UINT8, 1),
    ("BridgeSupport",           UINT8, 1),
    ("ChassisSupport",          UINT8, 1),
    ("ManufacturerId",          UINT8 * 4),
    ("ProductId",               UINT16),
    ("AuxFirmwareRevInfo",      UINT32)
  ]

IPMI_APP_COLD_RESET  = 0x2

IPMI_APP_WARM_RESET  = 0x3

IPMI_APP_GET_SELFTEST_RESULTS  = 0x4

class IPMI_SELF_TEST_RESULT_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Result",          UINT8),
    ("Param",           UINT8)
  ]

IPMI_APP_SELFTEST_NO_ERROR             = 0x55
IPMI_APP_SELFTEST_NOT_IMPLEMENTED      = 0x56
IPMI_APP_SELFTEST_ERROR                = 0x57
IPMI_APP_SELFTEST_FATAL_HW_ERROR       = 0x58
IPMI_APP_SELFTEST_INACCESSIBLE_SEL     = 0x80
IPMI_APP_SELFTEST_INACCESSIBLE_SDR     = 0x40
IPMI_APP_SELFTEST_INACCESSIBLE_FRU     = 0x20
IPMI_APP_SELFTEST_IPMB_SIGNAL_FAIL     = 0x10
IPMI_APP_SELFTEST_SDR_REPOSITORY_EMPTY = 0x08
IPMI_APP_SELFTEST_FRU_CORRUPT          = 0x04
IPMI_APP_SELFTEST_FW_BOOTBLOCK_CORRUPT = 0x02
IPMI_APP_SELFTEST_FW_CORRUPT           = 0x01

IPMI_APP_MANUFACTURING_TEST_ON = 0x5

IPMI_APP_SET_ACPI_POWERSTATE = 0x6

class IPMI_SET_ACPI_POWER_STATE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AcpiSystemPowerState",  UINT8, 7),
    ("AcpiSystemStateChange", UINT8, 1),
    ("AcpiDevicePowerState",  UINT8, 7),
    ("AcpiDeviceStateChange", UINT8, 1)
  ]

IPMI_APP_GET_ACPI_POWERSTATE = 0x7

IPMI_APP_GET_DEVICE_GUID = 0x8

class IPMI_GET_DEVICE_GUID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Guid",            UINT8 * 16)
  ]

IPMI_APP_RESET_WATCHDOG_TIMER  = 0x22

class IPMI_WATCHDOG_TIMER_USE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimerUse",                  UINT8, 3),
    ("Reserved",                  UINT8, 3),
    ("TimerRunning",              UINT8, 1),
    ("TimerUseExpirationFlagLog", UINT8, 1)
  ]

IPMI_APP_SET_WATCHDOG_TIMER  = 0x24

class IPMI_SET_WATCHDOG_TIMER_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimerUse",                      IPMI_WATCHDOG_TIMER_USE),
    ("TimerActions",                  UINT8),
    ("PretimeoutInterval",            UINT8),
    ("TimerUseExpirationFlagsClear",  UINT8),
    ("InitialCountdownValue",         UINT16)
  ]

IPMI_APP_GET_WATCHDOG_TIMER  = 0x25

class IPMI_GET_WATCHDOG_TIMER_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",              UINT8),
    ("TimerUse",                    IPMI_WATCHDOG_TIMER_USE),
    ("TimerActions",                UINT8),
    ("PretimeoutInterval",          UINT8),
    ("TimerUseExpirationFlagsClear",UINT8),
    ("InitialCountdownValue",       UINT16),
    ("PresentCountdownValue",       UINT16)
  ]

IPMI_APP_SET_BMC_GLOBAL_ENABLES  = 0x2E

IPMI_APP_GET_BMC_GLOBAL_ENABLES  = 0x2F

IPMI_APP_CLEAR_MESSAGE_FLAGS = 0x30

IPMI_APP_GET_MESSAGE_FLAGS = 0x31

IPMI_APP_ENABLE_MESSAGE_CHANNEL_RECEIVE  = 0x32

IPMI_APP_GET_MESSAGE = 0x33

IPMI_APP_SEND_MESSAGE  = 0x34

IPMI_APP_READ_EVENT_MSG_BUFFER = 0x35

IPMI_APP_GET_BT_INTERFACE_CAPABILITY = 0x36

IPMI_APP_GET_SYSTEM_GUID = 0x37

IPMI_APP_GET_CHANNEL_AUTHENTICATION_CAPABILITIES = 0x38

IPMI_APP_GET_SESSION_CHALLENGE = 0x39

IPMI_APP_ACTIVATE_SESSION  = 0x3A

IPMI_APP_SET_SESSION_PRIVELEGE_LEVEL = 0x3B

IPMI_APP_CLOSE_SESSION = 0x3C

IPMI_APP_GET_SESSION_INFO  = 0x3D

IPMI_APP_GET_AUTHCODE  = 0x3F

IPMI_APP_SET_CHANNEL_ACCESS  = 0x40

IPMI_APP_GET_CHANNEL_ACCESS  = 0x41

class IPMI_GET_CHANNEL_ACCESS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",  UINT8, 4),
    ("Reserve1",   UINT8, 4),
    ("Reserve2",   UINT8, 6),
    ("MemoryType", UINT8, 2)
  ]

class IPMI_GET_CHANNEL_ACCESS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",          UINT8, 1),
    ("AccessMode",              UINT8, 3),
    ("UserLevelAuthEnabled",    UINT8, 1),
    ("MessageAuthEnable",       UINT8, 1),
    ("Alert",                   UINT8, 1),
    ("Reserve1",                UINT8, 2),
    ("ChannelPriviledgeLimit",  UINT8, 4),
    ("Reserve2",                UINT8, 4)
  ]

IPMI_APP_GET_CHANNEL_INFO  = 0x42

class IPMI_GET_CHANNEL_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8),
    ("ChannelNo",           UINT8, 4),
    ("Reserve1",            UINT8, 4),
    ("ChannelMediumType",   UINT8, 7),
    ("Reserve2",            UINT8, 1),
    ("ChannelProtocolType", UINT8, 5),
    ("Reserve3",            UINT8, 3),
    ("ActiveSessionCount",  UINT8, 6),
    ("SessionSupport",      UINT8, 2),
    ("VendorId",            UINT8 * 3),
    ("AuxChannelInfo",      UINT16)
  ]

IPMI_APP_GET_CHANNEL_INFO  = 0x42

IPMI_APP_SET_USER_ACCESS = 0x43

IPMI_APP_GET_USER_ACCESS = 0x44

IPMI_APP_SET_USER_NAME = 0x45

IPMI_APP_GET_USER_NAME = 0x46

IPMI_APP_SET_USER_PASSWORD = 0x47

IPMI_APP_ACTIVATE_PAYLOAD  = 0x48

IPMI_APP_DEACTIVATE_PAYLOAD  = 0x49

IPMI_APP_GET_PAYLOAD_ACTIVATION_STATUS = 0x4a

IPMI_APP_GET_PAYLOAD_INSTANCE_INFO = 0x4b

IPMI_APP_SET_USER_PAYLOAD_ACCESS = 0x4C

IPMI_APP_GET_USER_PAYLOAD_ACCESS = 0x4D

IPMI_APP_GET_CHANNEL_PAYLOAD_SUPPORT = 0x4E

IPMI_APP_GET_CHANNEL_PAYLOAD_VERSION = 0x4F

IPMI_APP_GET_CHANNEL_OEM_PAYLOAD_INFO  = 0x50

IPMI_APP_MASTER_WRITE_READ = 0x52

IPMI_APP_GET_CHANNEL_CIPHER_SUITES = 0x54

IPMI_APP_SUSPEND_RESUME_PAYLOAD_ENCRYPTION = 0x55

IPMI_APP_SET_CHANNEL_SECURITY_KEYS = 0x56

IPMI_APP_GET_SYSTEM_INTERFACE_CAPABILITIES = 0x57

