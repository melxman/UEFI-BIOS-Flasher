#
# PxeBaseCodeCallBack.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PxeBaseCodeCallBack.py is free software: you can redistribute it and/or
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

from PxeBaseCode  import EFI_PXE_BASE_CODE_PACKET

gEfiPxeBaseCodeCallbackProtocolGuid     = \
  EFI_GUID (0x245dca21, 0xfb7b, 0x11d3, (0x8f, 0x01, 0x00, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

EFI_PXE_BASE_CODE_CALLBACK_PROTOCOL_REVISION  = 0x00010000
EFI_PXE_BASE_CODE_CALLBACK_INTERFACE_REVISION   = EFI_PXE_BASE_CODE_CALLBACK_PROTOCOL_REVISION

class EFI_PXE_BASE_CODE_CALLBACK_PROTOCOL (Structure):
  pass

EFI_PXE_BASE_CODE_FUNCTION_FIRST      = 0
EFI_PXE_BASE_CODE_FUNCTION_DHCP       = 1
EFI_PXE_BASE_CODE_FUNCTION_DISCOVER   = 2
EFI_PXE_BASE_CODE_FUNCTION_MTFTP      = 3
EFI_PXE_BASE_CODE_FUNCTION_UDP_WRITE  = 4
EFI_PXE_BASE_CODE_FUNCTION_UDP_READ   = 5
EFI_PXE_BASE_CODE_FUNCTION_ARP        = 6
EFI_PXE_BASE_CODE_FUNCTION_IGMP       = 7
EFI_PXE_BASE_CODE_PXE_FUNCTION_LAST   = 8
EFI_PXE_BASE_CODE_FUNCTION            = ENUM

EFI_PXE_BASE_CODE_CALLBACK_STATUS_FIRST     = 0
EFI_PXE_BASE_CODE_CALLBACK_STATUS_CONTINUE  = 1
EFI_PXE_BASE_CODE_CALLBACK_STATUS_ABORT     = 2
EFI_PXE_BASE_CODE_CALLBACK_STATUS_LAST      = 3
EFI_PXE_BASE_CODE_CALLBACK_STATUS           = ENUM

EFI_PXE_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_CALLBACK_PROTOCOL), # IN *This,
  EFI_PXE_BASE_CODE_FUNCTION,                   # IN Function,
  BOOLEAN,                                      # IN Received,
  UINT32,                                       # IN PacketLen,
  POINTER(EFI_PXE_BASE_CODE_PACKET)             # IN *Packet     OPTIONAL
  )

class EFI_PXE_BASE_CODE_CALLBACK_PROTOCOL (Structure):
  _fields_ = [
    ("Revision",  UINT64),
    ("Callback",  EFI_PXE_CALLBACK)
  ]

