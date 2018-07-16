#
# Ip4Config.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Ip4Config.py is free software: you can redistribute it and/or
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

gEfiIp4ConfigProtocolGuid = \
  EFI_GUID (0x3b95aa31, 0x3793, 0x434b, (0x86, 0x67, 0xc8, 0x07, 0x08, 0x92, 0xe0, 0x5e ))

class EFI_IP4_CONFIG_PROTOCOL (Structure):
  pass

IP4_CONFIG_VARIABLE_ATTRIBUTES  = \
         (EFI_VARIABLE_NON_VOLATILE | EFI_VARIABLE_BOOTSERVICE_ACCESS)

class EFI_IP4_IPCONFIG_DATA (Structure):
  _fields_ = [
    ("StationAddress",  EFI_IPv4_ADDRESS),
    ("SubnetMask",      EFI_IPv4_ADDRESS),
    ("RouteTableSize",  UINT32),
    ("RouteTable",      POINTER(Ip4.EFI_IP4_ROUTE_TABLE))
  ]

EFI_IP4_CONFIG_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG_PROTOCOL),   # IN *This
  EFI_EVENT,                          # IN DoneEvent,
  EFI_EVENT,                          # IN ReconfigEvent
  )

EFI_IP4_CONFIG_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG_PROTOCOL)  # IN *This
  )

EFI_IP4_CONFIG_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_CONFIG_PROTOCOL), # IN      *This
  POINTER(UINTN),                   # IN OUT  *IpConfigDataSize,
  POINTER(EFI_IP4_IPCONFIG_DATA)    # OUT     *IpConfigData    OPTIONAL
  )

EFI_IP4_CONFIG_PROTOCOL._fields_ = [
    ("Start",   EFI_IP4_CONFIG_START),
    ("Stop",    EFI_IP4_CONFIG_STOP),
    ("GetData", EFI_IP4_CONFIG_GET_DATA)
  ]

