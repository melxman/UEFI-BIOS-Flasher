#
# PiPcdInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiPcdInfo.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi import PiMultiPhase

gEfiGetPcdInfoProtocolGuid  = \
  EFI_GUID (0xfd0f4478,  0xefd, 0x461d, ( 0xba, 0x2d, 0xe5, 0x8c, 0x45, 0xfd, 0x5f, 0x5e ))

class EFI_GET_PCD_INFO_PROTOCOL (Structure):
  pass

EFI_GET_PCD_INFO_PROTOCOL_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),                  # IN CONST  *Guid,
  UINTN,                              # IN        TokenNumber,
  POINTER(PiMultiPhase.EFI_PCD_INFO)  # OUT       *PcdInfo
  )

EFI_GET_PCD_INFO_PROTOCOL_GET_SKU = CFUNCTYPE (
  UINTN
  )

EFI_GET_PCD_INFO_PROTOCOL._fields_ = [
    ("GetInfo", EFI_GET_PCD_INFO_PROTOCOL_GET_INFO),
    ("GetSku",  EFI_GET_PCD_INFO_PROTOCOL_GET_SKU)
  ]

