# 
# IpmiNetFnChassis.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiNetFnChassis.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard import *

IPMI_NETFN_CHASSIS  = 0x00

IPMI_CHASSIS_GET_CAPABILITIES  = 0x00

IPMI_CHASSIS_GET_STATUS  = 0x01

IPMI_CHASSIS_CONTROL = 0x02

IPMI_CHASSIS_RESET = 0x03

IPMI_CHASSIS_IDENTIFY  = 0x04

IPMI_CHASSIS_SET_CAPABILITIES  = 0x05

IPMI_CHASSIS_SET_POWER_RESTORE_POLICY  = 0x06

IPMI_CHASSIS_GET_SYSTEM_RESTART_CAUSE  = 0x07

Unknown                     =  0
ChassisControlCommand       =  1
ResetViaPushButton          =  2
PowerupViaPowerButton       =  3
WatchdogExpiration          =  4
Oem                         =  5
AutoPowerOnAlwaysRestore    =  6
AutoPowerOnRestorePrevious  =  7
ResetViaPef                 =  8
PowerCycleViaPef            =  9
SoftReset                   = 10
PowerUpViaRtc               = 11
IPMISYSTEM_RESTART_CAUSE    = UINTN

class IPMI_GET_SYSTEM_RESTART_CAUSE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Cause",           UINT8, 4),
    ("Reserved",        UINT8, 4),
    ("ChannelNumber",   UINT8)
  ]

IPMI_CHASSIS_SET_SYSTEM_BOOT_OPTIONS = 0x08

class IPMI_SET_BOOT_OPTIONS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",     UINT8, 7),
    ("MarkParameterInvalid",  UINT8, 1),
    ("ParameterData",         UINT8 * 1)
  ]

IPMI_CHASSIS_GET_SYSTEM_BOOT_OPTIONS = 0x09

class IPMI_GET_BOOT_OPTIONS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector", UINT8, 7),
    ("Reserved",          UINT8, 1),
    ("SetSelector",       UINT8),
    ("BlockSelector",     UINT8)
  ]

class IPMI_GET_THE_SYSTEM_BOOT_OPTIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Parameter", UINT8),
    ("Valid",     UINT8),
    ("Data1",     UINT8),
    ("Data2",     UINT8),
    ("Data3",     UINT8),
    ("Data4",     UINT8),
    ("Data5",     UINT8)
  ]

class IPMI_BOOT_INITIATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterVersion",UINT8),
    ("ParameterValid",  UINT8),
    ("ChannelNumber",   UINT8),
    ("SessionId",       UINT8),
    ("TimeStamp",       UINT8),
    ("Reserved",        UINT8 * 3)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetInProgress", UINT8, 2),
    ("Reserved",      UINT8, 6)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ServicePartitionSelector", UINT8)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ServicePartitionDiscovered",  UINT8, 1),
    ("ServicePartitionScanRequest", UINT8, 1),
    ("Reserved",                    UINT8, 5)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BmcBootFlagValid",  UINT8, 5),
    ("Reserved",          UINT8, 3)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WriteMask",                     UINT8),
    ("BootInitiatorAcknowledgeData",  UINT8)
  ]

BOOT_OPTION_HANDLED_BY_BIOS = 0x01

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved0",                 UINT8, 6),
    ("PersistentOptions",         UINT8, 1),
    ("BootFlagValid",             UINT8, 1),
    ("LockReset",                 UINT8, 1),
    ("ScreenBlank",               UINT8, 1),
    ("BootDeviceSelector",        UINT8, 4),
    ("LockKeyboard",              UINT8, 1),
    ("CmosClear",                 UINT8, 1),
    ("ConsoleRedirection",        UINT8, 2),
    ("LockSleep",                 UINT8, 1),
    ("UserPasswordBypass",        UINT8, 1),
    ("ForceProgressEventTrap",    UINT8, 1),
    ("BiosVerbosity",             UINT8, 2),
    ("LockPower",                 UINT8, 1),
    ("BiosMuxControlOverride",    UINT8, 2),
    ("BiosSharedModeOverride",    UINT8, 1),
    ("Reserved1",                 UINT8, 4)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",     UINT8, 4),
    ("Reserved",          UINT8, 4),
    ("SessionId",         UINT8 * 4),
    ("BootInfoTimeStamp", UINT8 * 4)
  ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetSelector", UINT8),
    ("BlockData",   UINT8 * 16)
  ]

class IPMI_BOOT_OPTIONS_PARAMETERS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Parm0", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0),
    ("Parm1", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1),
    ("Parm2", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2),
    ("Parm3", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3),
    ("Parm4", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4),
    ("Parm5", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5),
    ("Parm6", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6),
    ("Parm7", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7)
  ]

class IPMI_GET_BOOT_OPTIONS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",    UINT8),
    ("ParameterVersion",  UINT8, 4),
    ("Reserved",          UINT8, 4),
    ("ParameterSelector", UINT8, 7),
    ("ParameterValid",    UINT8, 1),
    ("ParameterData",     UINT8 * 1)
  ]

IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES = 0x0A

class IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DisablePoweroffButton",             UINT8, 1),
    ("DisableResetButton",                UINT8, 1),
    ("DisableDiagnosticInterruptButton",  UINT8, 1),
    ("DisableStandbyButton",              UINT8, 1),
    ("Reserved",                          UINT8, 4)
  ]

IPMI_CHASSIS_SET_POWER_CYCLE_INTERVALS = 0x0B

IPMI_CHASSIS_GET_POH_COUNTER = 0x0F

# 
