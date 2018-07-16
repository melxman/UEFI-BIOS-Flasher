# 
# IpmiNetFnBridge.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiNetFnBridge.py is free software: you can redistribute it and/or
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
IPMI_NETFN_BRIDGE = 0x02

IPMI_BRIDGE_GET_STATE  = 0x00

IPMI_BRIDGE_SET_STATE  = 0x01

IPMI_BRIDGE_GET_ICMB_ADDRESS = 0x02

IPMI_BRIDGE_SET_ICMB_ADDRESS = 0x03

IPMI_BRIDGE_SET_PROXY_ADDRESS  = 0x04

IPMI_BRIDGE_GET_BRIDGE_STATISTICS  = 0x05

IPMI_BRIDGE_GET_ICMB_CAPABILITIES  = 0x06

IPMI_BRIDGE_CLEAR_STATISTICS = 0x08

IPMI_BRIDGE_GET_PROXY_ADDRESS  = 0x09

IPMI_BRIDGE_GET_ICMB_CONNECTOR_INFO  = 0x0A

IPMI_BRIDGE_GET_ICMB_CONNECTION_ID = 0x0B

IPMI_BRIDGE_SEND_ICMB_CONNECTION_ID  = 0x0C

IPMI_BRIDGE_PREPARE_FOR_DISCOVERY  = 0x10

IPMI_BRIDGE_GET_ADDRESSES  = 0x11

IPMI_BRIDGE_SET_DISCOVERED = 0x12

IPMI_BRIDGE_GET_CHASSIS_DEVICEID = 0x13

IPMI_BRIDGE_SET_CHASSIS_DEVICEID = 0x14

IPMI_BRIDGE_REQUEST  = 0x20

IPMI_BRIDGE_MESSAGE  = 0x21

IPMI_BRIDGE_GET_EVENT_COUNT  = 0x30

IPMI_BRIDGE_SET_EVENT_DESTINATION  = 0x31

IPMI_BRIDGE_SET_EVENT_RECEPTION_STATE  = 0x32

IPMI_BRIDGE_SET_EVENT_RECEPTION_STATE  = 0x32

IPMI_BRIDGE_SEND_ICMB_EVENT_MESSAGE  = 0x33

