#
# IpmiProtocol.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IpmiProtocol.py is free software: you can redistribute it and/or
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

from EfiPy  import *

class IPMI_PROTOCOL (Structure):
  pass

gIpmiProtocolGuid = \
  EFI_GUID (0xdbc6381f, 0x5554, 0x4d14, (0x8f, 0xfd, 0x76, 0xd7, 0x87, 0xb8, 0xac, 0xbf))

gSmmIpmiProtocolGuid = \
  EFI_GUID (0x5169af60, 0x8c5a, 0x4243, (0xb3, 0xe9, 0x56, 0xc5, 0x6d, 0x18, 0xee, 0x26))

IPMI_SUBMIT_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(IPMI_PROTOCOL),  # IN     *This,
  UINT8,                   # IN     NetFunction,
  UINT8,                   # IN     Command,
  UINT8,                   # IN     *RequestData,
  UINT32,                  # IN     RequestDataSize,
  UINT8,                   #    OUT *ResponseData,
  UINT32                   # IN OUT *ResponseDataSize
  )

IPMI_PROTOCOL._fields_ = [
  ("IpmiSubmitCommand", IPMI_SUBMIT_COMMAND)
  ]

