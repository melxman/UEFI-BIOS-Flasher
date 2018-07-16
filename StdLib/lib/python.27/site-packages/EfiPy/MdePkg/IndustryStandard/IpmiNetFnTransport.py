#
# IpmiNetFnTransport.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiNetFnTransport.py is free software: you can redistribute it and/or modify
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

IPMI_NETFN_TRANSPORT  = 0x0C

IPMI_TRANSPORT_SET_LAN_CONFIG_PARAMETERS = 0x01

IpmiLanReserved1              =  0
IpmiLanReserved2              =  1
IpmiLanAuthType               =  2
IpmiLanIpAddress              =  3
IpmiLanIpAddressSource        =  4
IpmiLanMacAddress             =  5
IpmiLanSubnetMask             =  6
IpmiLanIpv4HeaderParam        =  7
IpmiLanPrimaryRcmpPort        =  8
IpmiLanSecondaryRcmpPort      =  9
IpmiLanBmcGeneratedArpCtrl    = 10
IpmiLanArpInterval            = 11
IpmiLanDefaultGateway         = 12
IpmiLanDefaultGatewayMac      = 13
IpmiLanBackupGateway          = 14
IpmiLanBackupGatewayMac       = 15
IpmiLanCommunityString        = 16
IpmiLanReserved3              = 17
IpmiLanDestinationType        = 18
IpmiLanDestinationAddress     = 19
IPMI_LAN_OPTION_TYPE          = UINTN

IpmiUnspecified               = 0
IpmiStaticAddrsss             = 1
IpmiDynamicAddressBmcDhcp     = 2
IpmiDynamicAddressBiosDhcp    = 3
IpmiDynamicAddressBmcNonDhcp  = 4
IPMI_IP_ADDRESS_SRC           = UINTN

IpmiPetTrapDestination          = 0
IpmiDirectedEventDestination    = 1
IpmiReserved1                   = 2
IpmiReserved2                   = 3
IpmiReserved3                   = 4
IpmiReserved4                   = 5
IpmiReserved5                   = 6
IpmiOem1                        = 7
IpmiOem2                        = 8
IPMI_LAN_DEST_TYPE_DEST_TYPE    = UINTN

class IPMI_LAN_AUTH_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NoAuth",        UINT8, 1),
    ("MD2Auth",       UINT8, 1),
    ("MD5Auth",       UINT8, 1),
    ("Reserved1",     UINT8, 1),
    ("StraightPswd",  UINT8, 1),
    ("OemType",       UINT8, 1),
    ("Reserved2",     UINT8, 2)
  ]

class IPMI_LAN_IP_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddress", UINT8 * 4)
  ]

class IPMI_LAN_IP_ADDRESS_SRC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressSrc",  UINT8, 4),
    ("Reserved",    UINT8, 4)
  ]

class IPMI_LAN_MAC_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MacAddress",  UINT8 * 6)
  ]

class IPMI_LAN_SUBNET_MASK (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddress",  UINT8 * 4)
  ]

class IPMI_LAN_IPV4_HDR_PARAM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimeToLive",  UINT8),
    ("IpFlag",      UINT8, 3),
    ("Reserved1",   UINT8, 5),
    ("Precedence",  UINT8, 3),
    ("Reserved2",   UINT8, 1),
    ("ServiceType", UINT8, 4)
  ]

class IPMI_LAN_RCMP_PORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RcmpPortMsb",  UINT8),
    ("RcmpPortLsb",  UINT8)
  ]

class IPMI_LAN_BMC_GENERATED_ARP_CONTROL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EnableBmcArpResponse",    UINT8, 1),
    ("EnableBmcGratuitousArp",  UINT8, 1),
    ("Reserved",                UINT8, 6)
  ]

class IPMI_LAN_ARP_INTERVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ArpInterval",    UINT8)
  ]

class IPMI_LAN_COMMUNITY_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    UINT8 * 18)
  ]

class IPMI_LAN_DEST_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector",   UINT8, 4),
    ("Reserved2",             UINT8, 4),
    ("DestinationType",       UINT8, 3),
    ("Reserved1",             UINT8, 4),
    ("AlertAcknowledged",     UINT8, 1)
  ]

class IPMI_LAN_DEST_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector",         UINT8, 4),
    ("Reserved1",                   UINT8, 4),
    ("AlertingIpAddressSelector",   UINT8, 4),
    ("AddressFormat",               UINT8, 4),
    ("UseDefaultGateway",           UINT8, 1),
    ("Reserved2",                   UINT8, 7),
    ("AlertingIpAddress",           IPMI_LAN_IP_ADDRESS),
    ("AlertingMacAddress",          IPMI_LAN_MAC_ADDRESS)
  ]

class IPMI_LAN_OPTIONS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("IpmiLanAuthType",         IPMI_LAN_AUTH_TYPE),
    ("IpmiLanIpAddress",        IPMI_LAN_IP_ADDRESS),
    ("IpmiLanIpAddressSrc",     IPMI_LAN_IP_ADDRESS_SRC),
    ("IpmiLanMacAddress",       IPMI_LAN_MAC_ADDRESS),
    ("IpmiLanSubnetMask",       IPMI_LAN_SUBNET_MASK),
    ("IpmiLanIpv4HdrParam",     IPMI_LAN_IPV4_HDR_PARAM),
    ("IpmiLanPrimaryRcmpPort",  IPMI_LAN_RCMP_PORT),
    ("IpmiLanArpControl",       IPMI_LAN_BMC_GENERATED_ARP_CONTROL),
    ("IpmiLanArpInterval",      IPMI_LAN_ARP_INTERVAL),
    ("IpmiLanCommunityString",  IPMI_LAN_COMMUNITY_STRING),
    ("IpmiLanDestType",         IPMI_LAN_DEST_TYPE),
    ("IpmiLanDestAddress",      IPMI_LAN_DEST_ADDRESS)
  ]

IPMI_TRANSPORT_GET_LAN_CONFIG_PARAMETERS = 0x02

IPMI_TRANSPORT_SUSPEND_BMC_ARPS  = 0x03

IPMI_TRANSPORT_GET_PACKET_STATISTICS = 0x04

IPMI_TRANSPORT_SET_SERIAL_CONFIGURATION  = 0x10

class IPMI_EMP_AUTH_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NoAuthentication",  UINT8, 1),
    ("MD2Authentication", UINT8, 1),
    ("MD5Authentication", UINT8, 1),
    ("Reserved1",         UINT8, 1),
    ("StraightPassword",  UINT8, 1),
    ("OemProprietary",    UINT8, 1),
    ("Reservd2",          UINT8, 2)
  ]

class IPMI_EMP_CONNECTION_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EnableBasicMode",       UINT8, 1),
    ("EnablePPPMode",         UINT8, 1),
    ("EnableTerminalMode",    UINT8, 1),
    ("Reserved1",             UINT8, 2),
    ("SnoopOsPPPNegotiation", UINT8, 1),
    ("Reserved2",             UINT8, 1),
    ("DirectConnect",         UINT8, 1)
  ]

class IPMI_EMP_INACTIVITY_TIMEOUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InactivityTimeout", UINT8, 4),
    ("Reserved",          UINT8, 4)
  ]

class IPMI_EMP_CHANNEL_CALLBACK_CONTROL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpmiCallback",                  UINT8, 1),
    ("CBCPCallback",                  UINT8, 1),
    ("Reserved1",                     UINT8, 6),
    ("CbcpEnableNoCallback",          UINT8, 1),
    ("CbcpEnablePreSpecifiedNumber",  UINT8, 1),
    ("CbcpEnableUserSpecifiedNumber", UINT8, 1),
    ("CbcpEnableCallbackFromList",    UINT8, 1),
    ("Reserved",                      UINT8, 4),
    ("CallbackDestination1",          UINT8),
    ("CallbackDestination2",          UINT8),
    ("CallbackDestination3",          UINT8)
  ]

class IPMI_EMP_SESSION_TERMINATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CloseSessionOnDCDLoss",           UINT8, 1),
    ("EnableSessionInactivityTimeout",  UINT8, 1),
    ("Reserved",                        UINT8, 6)
  ]

class IPMI_EMP_MESSAGING_COM_SETTING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",       UINT8, 5),
    ("EnableDtrHangup", UINT8, 1),
    ("FlowControl",     UINT8, 2),
    ("BitRate",         UINT8, 4),
    ("Reserved2",       UINT8, 4),
    ("SaveSetting",     UINT8, 1),
    ("SetComPort",      UINT8, 1),
    ("Reserved3",       UINT8, 6)
  ]

class IPMI_EMP_MODEM_RING_TIME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RingDurationInterval",  UINT8, 6),
    ("Reserved1",             UINT8, 2),
    ("RingDeadTime",          UINT8, 4),
    ("Reserved",              UINT8, 4)
  ]

class IPMI_EMP_MODEM_INIT_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8),
    ("InitString",  UINT8 * 48)
  ]

class IPMI_EMP_MODEM_ESC_SEQUENCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EscapeSequence",  UINT8 * 5)
  ]

class IPMI_EMP_MODEM_HANGUP_SEQUENCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HangupSequence",  UINT8 * 8)
  ]

class IPMI_MODEM_DIALUP_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModelDialCommend",  UINT8 * 8)
  ]

class IPMI_PAGE_BLACKOUT_INTERVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PageBlackoutInterval",  UINT8)
  ]

class IPMI_EMP_COMMUNITY_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommunityString",  UINT8 * 18)
  ]

class IPMI_DIAL_PAGE_DESTINATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved5",           UINT8, 4),
    ("DialStringSelector",  UINT8, 4)
  ]

class IPMI_TAP_PAGE_DESTINATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapAccountSelector",  UINT8, 4),
    ("Reserved",            UINT8, 4)
  ]

class IPMI_PPP_ALERT_DESTINATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PPPAccountSetSelector",  UINT8),
    ("DialStringSelector",     UINT8)
  ]

class IPMI_DEST_TYPE_SPECIFIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("DialPageDestination", IPMI_DIAL_PAGE_DESTINATION),
    ("TapPageDestination",  IPMI_TAP_PAGE_DESTINATION),
    ("PppAlertDestination", IPMI_PPP_ALERT_DESTINATION)
  ]

class IPMI_EMP_DESTINATION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector",     UINT8, 4),
    ("Reserved1",               UINT8, 4),
    ("DestinationType",         UINT8, 4),
    ("Reserved2",               UINT8, 3),
    ("AlertAckRequired",        UINT8, 1),
    ("AlertAckTimeoutSeconds",  UINT8),
    ("NumRetriesCall",          UINT8, 3),
    ("Reserved3",               UINT8, 1),
    ("NumRetryAlert",           UINT8, 3),
    ("Reserved4",               UINT8, 1),
    ("DestinationTypeSpecific", IPMI_DEST_TYPE_SPECIFIC)
  ]

class IPMI_EMP_DESTINATION_COM_SETTING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector",   UINT8, 4),
    ("Reserved1",             UINT8, 4),
    ("Parity",                UINT8, 4),
    ("CharacterSize",         UINT8, 4),
    ("StopBit",               UINT8, 4),
    ("DtrHangup",             UINT8, 4),
    ("FlowControl",           UINT8, 4),
    ("BitRate",               UINT8, 4),
    ("Reserved2",             UINT8, 4),
    ("SaveSetting",           UINT8, 4),
    ("SetComPort",            UINT8, 4),
    ("Reserved3",             UINT8, 4)
  ]

class IPMI_DESTINATION_DIAL_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DialStringSelector",  UINT8, 4),
    ("Reserved1",           UINT8, 4),
    ("Reserved2",           UINT8),
    ("DialString",          UINT8 * 48)
  ]

class IPMI_PPP_IP_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("IpAddressLong", UINT32),
    ("IpAddress",     UINT8 * 4)
  ]

class IPMI_DESTINATION_IP_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddressSelector", UINT8, 4),
    ("Reserved1",         UINT8, 4),
    ("PppIpAddress",      IPMI_PPP_IP_ADDRESS)
  ]

class IPMI_DESTINATION_TAP_ACCOUNT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapSelector",           UINT8),
    ("TapServiceSelector",    UINT8, 4),
    ("TapDialStringSelector", UINT8, 4)
  ]

class IPMI_TAP_PAGER_ID_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapSelector",   UINT8),
    ("PagerIdString", UINT8 * 16)
  ]

class IPMI_EMP_OPTIONS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("OptionData",                      UINT8),
    ("EmpAuthType",                     IPMI_EMP_AUTH_TYPE),
    ("EmpConnectionType",               IPMI_EMP_CONNECTION_TYPE),
    ("EmpInactivityTimeout",            IPMI_EMP_INACTIVITY_TIMEOUT),
    ("EmpCallbackControl",              IPMI_EMP_CHANNEL_CALLBACK_CONTROL),
    ("EmpSessionTermination",           IPMI_EMP_SESSION_TERMINATION),
    ("EmpMessagingComSetting",          IPMI_EMP_MESSAGING_COM_SETTING),
    ("EmpModemRingTime",                IPMI_EMP_MODEM_RING_TIME),
    ("EmpModemInitString",              IPMI_EMP_MODEM_INIT_STRING),
    ("EmpModemEscSequence",             IPMI_EMP_MODEM_ESC_SEQUENCE),
    ("EmpModemHangupSequence",          IPMI_EMP_MODEM_HANGUP_SEQUENCE),
    ("EmpModemDialupCommand",           IPMI_MODEM_DIALUP_COMMAND),
    ("EmpPageBlackoutInterval",         IPMI_PAGE_BLACKOUT_INTERVAL),
    ("EmpCommunityString",              IPMI_EMP_COMMUNITY_STRING),
    ("EmpDestinationInfo",              IPMI_EMP_DESTINATION_INFO),
    ("EmpDestinationComSetting",        IPMI_EMP_DESTINATION_COM_SETTING),
    ("CallRetryBusySignalInterval",     UINT8),
    ("DestinationDialString",           IPMI_DESTINATION_DIAL_STRING),
    ("DestinationIpAddress",            IPMI_DESTINATION_IP_ADDRESS),
    ("DestinationTapAccount",           IPMI_DESTINATION_TAP_ACCOUNT),
    ("TapPagerIdString",                IPMI_TAP_PAGER_ID_STRING)
  ]

IPMI_TRANSPORT_GET_SERIAL_CONFIGURATION  = 0x11

IPMI_TRANSPORT_SET_SERIAL_MUX  = 0x12

class IPMI_SET_SERIAL_MODEM_MUX_COMMAND_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved1",   UINT8, 4),
    ("MuxSetting",  UINT8, 4),
    ("Reserved2",   UINT8, 4)
  ]

class IPMI_SET_SERIAL_MODEM_MUX_COMMAND_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MuxSetToBmc",               UINT8, 1),
    ("CommandStatus",             UINT8, 1),
    ("MessagingSessionActive",    UINT8, 1),
    ("AlertInProgress",           UINT8, 1),
    ("Reserved2",                 UINT8, 2),
    ("MuxToBmcAllowed",           UINT8, 1),
    ("MuxToSystemBlocked",        UINT8, 1)
  ]

IPMI_TRANSPORT_GET_TAP_RESPONSE_CODE = 0x13

IPMI_TRANSPORT_SET_PPP_UDP_PROXY_TXDATA  = 0x14

IPMI_TRANSPORT_GET_PPP_UDP_PROXY_TXDATA  = 0x15

IPMI_TRANSPORT_SEND_PPP_UDP_PROXY_PACKET = 0x16

IPMI_TRANSPORT_GET_PPP_UDP_PROXY_RX  = 0x17

IPMI_TRANSPORT_SERIAL_CONNECTION_ACTIVE  = 0x18

IPMI_TRANSPORT_CALLBACK  = 0x19

IPMI_TRANSPORT_SET_USER_CALLBACK_OPTIONS = 0x1A

IPMI_TRANSPORT_GET_USER_CALLBACK_OPTIONS = 0x1B

IPMI_TRANSPORT_SOL_ACTIVATING  = 0x20

IPMI_TRANSPORT_SET_SOL_CONFIG_PARAM  = 0x21

IPMI_TRANSPORT_GET_SOL_CONFIG_PARAM  = 0x22

