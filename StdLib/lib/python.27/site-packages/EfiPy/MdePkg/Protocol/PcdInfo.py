#
# PcdInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PcdInfo.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiMultiPhase import EFI_PCD_INFO

gGetPcdInfoProtocolGuid = \
  EFI_GUID (0x5be40f57, 0xfa68, 0x4610, ( 0xbb, 0xbf, 0xe9, 0xc5, 0xfc, 0xda, 0xd3, 0x65 ))

class GET_PCD_INFO_PROTOCOL (Structure):
  pass

GET_PCD_INFO_PROTOCOL_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                # IN  TokenNumber,
  POINTER(EFI_PCD_INFO) # OUT *PcdInfo
  )

GET_PCD_INFO_PROTOCOL_GET_INFO_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),    # IN CONST  *Guid,
  UINTN,                # IN  TokenNumber,
  POINTER(EFI_PCD_INFO) # OUT *PcdInfo
  )

GET_PCD_INFO_PROTOCOL_GET_SKU = CFUNCTYPE (
  UINTN
  )

GET_PCD_INFO_PROTOCOL._fields_ = [
    ("GetInfo",   GET_PCD_INFO_PROTOCOL_GET_INFO),
    ("GetInfoEx", GET_PCD_INFO_PROTOCOL_GET_INFO_EX),
    ("GetSku",    GET_PCD_INFO_PROTOCOL_GET_SKU)
  ]
