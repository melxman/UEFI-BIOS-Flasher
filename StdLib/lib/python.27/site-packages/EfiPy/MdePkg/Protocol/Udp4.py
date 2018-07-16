#
# Udp4.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Udp4.py is free software: you can redistribute it and/or
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

from EfiPy import *

import Ip4
import ManagedNetwork
import SimpleNetwork

gEfiUdp4ServiceBindingProtocolGuid  = \
  EFI_GUID (0x83f01464, 0x99bd, 0x45e5, (0xb3, 0x83, 0xaf, 0x63, 0x05, 0xd8, 0xe9, 0xe6 ))

gEfiUdp4ProtocolGuid                  = \
  EFI_GUID (0x3ad9df29, 0x4501, 0x478d, (0xb1, 0xf8, 0x7f, 0x7f, 0xe7, 0x0e, 0x50, 0xf3 ))

class EFI_UDP4_PROTOCOL (Structure):
  pass

class EFI_UDP4_SERVICE_POINT (Structure):
  _fields_ = [
    ("InstanceHandle",EFI_HANDLE),
    ("LocalAddress",  EFI_IPv4_ADDRESS),
    ("LocalPort",     UINT16),
    ("RemoteAddress", EFI_IPv4_ADDRESS),
    ("RemotePort",    UINT16)
  ]

class EFI_UDP4_VARIABLE_DATA (Structure):
  _fields_ = [
    ("DriverHandle",  EFI_HANDLE),
    ("ServiceCount",  UINT32),
    ("Services",      EFI_UDP4_SERVICE_POINT * 1)
  ]

class EFI_UDP4_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_UDP4_SESSION_DATA (Structure):
  _fields_ = [
    ("SourceAddress",       EFI_IPv4_ADDRESS),
    ("SourcePort",          UINT16),
    ("DestinationAddress",  EFI_IPv4_ADDRESS),
    ("DestinationPort",     UINT16)
  ]

class EFI_UDP4_CONFIG_DATA (Structure):
  _fields_ = [
    ("AcceptBroadcast",     BOOLEAN),
    ("AcceptPromiscuous",   BOOLEAN),
    ("AcceptAnyPort",       BOOLEAN),
    ("AllowDuplicatePort",  BOOLEAN),
    ("TypeOfService",       UINT8),
    ("TimeToLive",          UINT8),
    ("DoNotFragment",       BOOLEAN),
    ("ReceiveTimeout",      UINT32),
    ("TransmitTimeout",     UINT32),
    ("UseDefaultAddress",   BOOLEAN),
    ("StationAddress",      EFI_IPv4_ADDRESS),
    ("SubnetMask",          EFI_IPv4_ADDRESS),
    ("StationPort",         UINT16),
    ("RemoteAddress",       EFI_IPv4_ADDRESS),
    ("RemotePort",          UINT16)
  ]

class EFI_UDP4_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("UdpSessionData",  POINTER(EFI_UDP4_SESSION_DATA)),
    ("GatewayAddress",  POINTER(EFI_IPv4_ADDRESS)),
    ("DataLength",      UINT32),
    ("FragmentCount",   UINT32),
    ("FragmentTable",   EFI_UDP4_FRAGMENT_DATA * 1)
  ]

class EFI_UDP4_RECEIVE_DATA (Structure):
  _fields_ = [
    ("TimeStamp",     EFI_TIME),
    ("RecycleSignal", EFI_EVENT),
    ("UdpSession",    EFI_UDP4_SESSION_DATA),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_UDP4_FRAGMENT_DATA * 1)
  ]

class EFI_UDP4_COMPLETION_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData", POINTER(EFI_UDP4_RECEIVE_DATA)),
    ("TxData", POINTER(EFI_UDP4_TRANSMIT_DATA))
  ]

class EFI_UDP4_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS),
    ("Packet",  EFI_UDP4_COMPLETION_TOKEN_Packet)
  ]

EFI_UDP4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),                               # IN  *This
  POINTER(EFI_UDP4_CONFIG_DATA),                            # OUT *Udp4ConfigData OPTIONAL,
  POINTER(Ip4.EFI_IP4_MODE_DATA),                           # OUT *Ip4ModeData    OPTIONAL,
  POINTER(ManagedNetwork.EFI_MANAGED_NETWORK_CONFIG_DATA),  # OUT *MnpConfigData  OPTIONAL,
  POINTER(SimpleNetwork.EFI_SIMPLE_NETWORK_MODE)            # OUT *SnpModeData    OPTIONAL
  )

EFI_UDP4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),   # IN  *This
  POINTER(EFI_UDP4_CONFIG_DATA) # IN  *UdpConfigData  OPTIONAL
  )

EFI_UDP4_GROUPS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),   # IN  *This
  BOOLEAN,                      # IN  JoinFlag
  POINTER(EFI_IPv4_ADDRESS)     # IN  *MulticastAddress  OPTIONAL
  )

EFI_UDP4_ROUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),   # IN  *This
  BOOLEAN,                      # IN  DeleteRoute
  POINTER(EFI_IPv4_ADDRESS),    # IN  *SubnetAddress  OPTIONAL
  POINTER(EFI_IPv4_ADDRESS),    # IN  *SubnetMask     OPTIONAL
  POINTER(EFI_IPv4_ADDRESS)     # IN  *GatewayAddress OPTIONAL
  )

EFI_UDP4_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL)    # IN  *This
  )

EFI_UDP4_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),         # IN  *This
  POINTER(EFI_UDP4_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_UDP4_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),         # IN  *This
  POINTER(EFI_UDP4_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_UDP4_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP4_PROTOCOL),         # IN  *This
  POINTER(EFI_UDP4_COMPLETION_TOKEN)  # IN  *Token  OPTIONAL
  )

EFI_UDP4_PROTOCOL._fields_ = [
    ("GetModeData", EFI_UDP4_GET_MODE_DATA),
    ("Configure",   EFI_UDP4_CONFIGURE),
    ("Groups",      EFI_UDP4_GROUPS),
    ("Routes",      EFI_UDP4_ROUTES),
    ("Transmit",    EFI_UDP4_TRANSMIT),
    ("Receive",     EFI_UDP4_RECEIVE),
    ("Cancel",      EFI_UDP4_CANCEL),
    ("Poll",        EFI_UDP4_POLL)
  ]

