#
# IpmiNetFnSensorEvent.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiNetFnSensorEvent.py is free software: you can redistribute it and/or modify
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

IPMI_NETFN_SENSOR_EVENT = 0x04

IPMI_SENSOR_PLATFORM_EVENT_MESSAGE   = 0x02

class IPMI_PLATFORM_EVENT_MESSAGE_DATA_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("GeneratorId",  UINT8),
    ("EvMRevision",  UINT8),
    ("SensorType",   UINT8),
    ("SensorNumber", UINT8),
    ("EventDirType", UINT8),
    ("OEMEvData1",   UINT8),
    ("OEMEvData2",   UINT8),
    ("OEMEvData3",   UINT8)
  ]

