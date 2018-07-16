# TpmPtp.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# TpmPtp.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard import *

# 
class PTP_FIFO_REGISTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Access",                UINT8),
    ("Reserved1",             UINT8 * 7),
    ("IntEnable",             UINT32),
    ("IntVector",             UINT8),
    ("Reserved2",             UINT8 * 3),
    ("IntSts",                UINT32),
    ("InterfaceCapability",   UINT32),
    ("Status",                UINT8),
    ("BurstCount",            UINT16),
    ("StatusEx",              UINT8),
    ("Reserved3",             UINT8 * 8),
    ("DataFifo",              UINT32),
    ("Reserved4",             UINT8 * 8),
    ("InterfaceId",           UINT32),
    ("Reserved5",             UINT8 * 0x4c),
    ("XDataFifo",             UINT32),
    ("Reserved6",             UINT8 * 0xe7c),
    ("Vid",                   UINT16),
    ("Did",                   UINT16),
    ("Rid",                   UINT8),
    ("Reserved",              UINT8 * 0xfb)
  ]

class PTP_FIFO_INTERFACE_IDENTIFIER_Structure (Structure):
  _fields_ = [
    ("InterfaceType",           UINT32, 4),
    ("InterfaceVersion",        UINT32, 4),
    ("CapLocality",             UINT32, 1),
    ("Reserved1",               UINT32, 2),
    ("CapDataXferSizeSupport",  UINT32, 2),
    ("CapFIFO",                 UINT32, 1),
    ("CapCRB",                  UINT32, 1),
    ("CapIFRes",                UINT32, 2),
    ("InterfaceSelector",       UINT32, 2),
    ("IntfSelLock",             UINT32, 1),
    ("Reserved2",               UINT32, 4),
    ("Reserved3",               UINT32, 8)
  ]

class PTP_FIFO_INTERFACE_IDENTIFIER (Union):
  _fields_ = [
    ("Bits",    PTP_FIFO_INTERFACE_IDENTIFIER_Structure),
    ("Uint32",  UINT32)
  ]

class PTP_FIFO_INTERFACE_CAPABILITY_Structure (Structure):
  _fields_ = [
    ("DataAvailIntSupport",         UINT32, 1),
    ("StsValidIntSupport",          UINT32, 1),
    ("LocalityChangeIntSupport",    UINT32, 1),
    ("InterruptLevelHigh",          UINT32, 1),
    ("InterruptLevelLow",           UINT32, 1),
    ("InterruptEdgeRising",         UINT32, 1),
    ("InterruptEdgeFalling",        UINT32, 1),
    ("CommandReadyIntSupport",      UINT32, 1),
    ("BurstCountStatic",            UINT32, 1),
    ("DataTransferSizeSupport",     UINT32, 2),
    ("Reserved",                    UINT32, 17),
    ("InterfaceVersion",            UINT32, 3),
    ("Reserved2",                   UINT32, 1)
  ]

class PTP_FIFO_INTERFACE_CAPABILITY (Union):
  _fields_ = [
    ("Bits",    PTP_FIFO_INTERFACE_CAPABILITY_Structure),
    ("Uint32",  UINT32)
  ]

INTERFACE_CAPABILITY_INTERFACE_VERSION_TIS_12  = 0x0
INTERFACE_CAPABILITY_INTERFACE_VERSION_TIS_13  = 0x2
INTERFACE_CAPABILITY_INTERFACE_VERSION_PTP     = 0x3

PTP_FIFO_VALID                = BIT7
PTP_FIFO_ACC_ACTIVE           = BIT5
PTP_FIFO_ACC_SEIZED           = BIT4
PTP_FIFO_ACC_SEIZE            = BIT3
PTP_FIFO_ACC_PENDIND          = BIT2
PTP_FIFO_ACC_RQUUSE           = BIT1
PTP_FIFO_ACC_ESTABLISH        = BIT0

PTP_FIFO_STS_VALID            = BIT7
PTP_FIFO_STS_READY            = BIT6
PTP_FIFO_STS_GO               = BIT5
PTP_FIFO_STS_DATA             = BIT4
PTP_FIFO_STS_EXPECT           = BIT3
PTP_FIFO_STS_SELFTEST_DONE    = BIT2
PTP_FIFO_STS_RETRY            = BIT1

PTP_FIFO_STS_EX_TPM_FAMILY    = (BIT2 | BIT3)
PTP_FIFO_STS_EX_TPM_FAMILY_OFFSET    = (2)
PTP_FIFO_STS_EX_TPM_FAMILY_TPM12    = (0)
PTP_FIFO_STS_EX_TPM_FAMILY_TPM20    = (BIT2)

PTP_FIFO_STS_EX_CANCEL        = BIT0

class PTP_CRB_REGISTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LocalityState",                   UINT32),
    ("Reserved1",                       UINT8  * 4),
    ("LocalityControl",                 UINT32),
    ("LocalityStatus",                  UINT32),
    ("Reserved2",                       UINT8  * 0x20),
    ("InterfaceId",                     UINT32),
    ("Vid",                             UINT16),
    ("Did",                             UINT16),
    ("CrbControlExtension",             UINT64),
    ("CrbControlRequest",               UINT32),
    ("CrbControlStatus",                UINT32),
    ("CrbControlCancel",                UINT32),
    ("CrbControlStart",                 UINT32),
    ("CrbInterruptEnable",              UINT32),
    ("CrbInterruptStatus",              UINT32),
    ("CrbControlCommandSize",           UINT32),
    ("CrbControlCommandAddressLow",     UINT32),
    ("CrbControlCommandAddressHigh",    UINT32),
    ("CrbControlResponseSize",          UINT32),
    ("CrbControlResponseAddrss",        UINT64),
    ("Reserved4",                       UINT8 * 0x10),
    ("CrbDataBuffer",                   UINT8 * 0xF80)
  ]

class PTP_CRB_INTERFACE_IDENTIFIER_Structure (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InterfaceType",           UINT32, 4),
    ("InterfaceVersion",        UINT32, 4),
    ("CapLocality",             UINT32, 1),
    ("Reserved1",               UINT32, 2),
    ("CapDataXferSizeSupport",  UINT32, 2),
    ("CapFIFO",                 UINT32, 1),
    ("CapCRB",                  UINT32, 1),
    ("CapIFRes",                UINT32, 2),
    ("InterfaceSelector",       UINT32, 2),
    ("IntfSelLock",             UINT32, 1),
    ("Reserved2",               UINT32, 4),
    ("Rid",                     UINT32, 8)
  ]

class PTP_CRB_INTERFACE_IDENTIFIER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PTP_CRB_INTERFACE_IDENTIFIER_Structure),
    ("Uint32",  UINT32)
  ]

PTP_INTERFACE_IDENTIFIER_INTERFACE_TYPE_FIFO  = 0x0
PTP_INTERFACE_IDENTIFIER_INTERFACE_TYPE_CRB   = 0x1
PTP_INTERFACE_IDENTIFIER_INTERFACE_TYPE_TIS   = 0xF

PTP_INTERFACE_IDENTIFIER_INTERFACE_VERSION_FIFO  = 0x0
PTP_INTERFACE_IDENTIFIER_INTERFACE_VERSION_CRB   = 0x1

PTP_INTERFACE_IDENTIFIER_INTERFACE_SELECTOR_FIFO  = 0x0
PTP_INTERFACE_IDENTIFIER_INTERFACE_SELECTOR_CRB   = 0x1

PTP_CRB_LOCALITY_STATE_TPM_REG_VALID_STATUS       = BIT7

PTP_CRB_LOCALITY_STATE_ACTIVE_LOCALITY_MASK       = (BIT2 | BIT3 | BIT4)
PTP_CRB_LOCALITY_STATE_ACTIVE_LOCALITY_0          = (0)
PTP_CRB_LOCALITY_STATE_ACTIVE_LOCALITY_1          = (BIT2)
PTP_CRB_LOCALITY_STATE_ACTIVE_LOCALITY_2          = (BIT3)
PTP_CRB_LOCALITY_STATE_ACTIVE_LOCALITY_3          = (BIT2 | BIT3)
PTP_CRB_LOCALITY_STATE_ACTIVE_LOCALITY_4          = (BIT4)

PTP_CRB_LOCALITY_STATE_LOCALITY_ASSIGNED          = BIT1

PTP_CRB_LOCALITY_STATE_TPM_ESTABLISHED            = BIT0

PTP_CRB_LOCALITY_CONTROL_RESET_ESTABLISHMENT_BIT  = BIT3

PTP_CRB_LOCALITY_CONTROL_SEIZE                    = BIT2

PTP_CRB_LOCALITY_CONTROL_RELINQUISH               = BIT1

PTP_CRB_LOCALITY_CONTROL_REQUEST_ACCESS           = BIT0

PTP_CRB_LOCALITY_STATUS_BEEN_SEIZED               = BIT1

PTP_CRB_LOCALITY_STATUS_GRANTED                   = BIT0

PTP_CRB_CONTROL_AREA_REQUEST_GO_IDLE              = BIT1

PTP_CRB_CONTROL_AREA_REQUEST_COMMAND_READY        = BIT0

PTP_CRB_CONTROL_AREA_STATUS_TPM_IDLE              = BIT1

PTP_CRB_CONTROL_AREA_STATUS_TPM_STATUS            = BIT0

PTP_CRB_CONTROL_CANCEL                            = BIT0

PTP_CRB_CONTROL_START                             = BIT0

PTP_TIMEOUT_A               = (750 * 1000)
PTP_TIMEOUT_B               = (2000 * 1000)
PTP_TIMEOUT_C               = (200 * 1000)
PTP_TIMEOUT_D               = (30 * 1000)

