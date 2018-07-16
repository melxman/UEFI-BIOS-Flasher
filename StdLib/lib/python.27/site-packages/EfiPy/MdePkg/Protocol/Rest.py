#
# Rest.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Rest.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.Http import EFI_HTTP_MESSAGE
gEfiRestProtocolGuid           = \
  EFI_GUID (0x0db48a36, 0x4e54, 0xea9c, (0x9b, 0x09, 0x1e, 0xa5, 0xbe, 0x3a, 0x66, 0x0b ))

class EFI_REST_PROTOCOL (Structure):
  pass

EFI_REST_SEND_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_PROTOCOL),        # IN  *This,
  POINTER(EFI_HTTP_MESSAGE),         # IN  *RequestMessage,
  POINTER(EFI_HTTP_MESSAGE)          # OUT *ResponseMessage
  )

EFI_REST_GET_TIME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_PROTOCOL),        # IN  *This,
  POINTER(EFI_TIME)                  # OUT *Time
  )

EFI_REST_PROTOCOL._fields_ = [
    ("SendReceive",         EFI_REST_SEND_RECEIVE),
    ("GetServiceTime",      EFI_REST_GET_TIME)
  ]

