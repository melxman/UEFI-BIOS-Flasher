#
# ReportStatusCodeHandler.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ReportStatusCodeHandler.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiStatusCode  import \
            EFI_STATUS_CODE_TYPE,         \
            EFI_STATUS_CODE_VALUE,        \
            EFI_STATUS_CODE_DATA

gEfiRscHandlerProtocolGuid  = \
  EFI_GUID (0x86212936, 0xe76, 0x41c8, (0xa0, 0x3a, 0x2a, 0xf2, 0xfc, 0x1c, 0x39, 0xe2))

EFI_RSC_HANDLER_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_STATUS_CODE_TYPE),        # IN *This
  EFI_STATUS_CODE_VALUE,                # IN Value,
  UINT32,                               # IN Instance,
  POINTER(EFI_GUID),                    # IN *CallerId,
  POINTER(EFI_STATUS_CODE_DATA)         # IN *Data
  )

EFI_RSC_HANDLER_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_RSC_HANDLER_CALLBACK, # IN Callback
  EFI_TPL                   # IN Tpl
  )

EFI_RSC_HANDLER_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_RSC_HANDLER_CALLBACK  # IN Callback
  )

class EFI_RSC_HANDLER_PROTOCOL (Structure):
  _fields_ = [
    ("Register",    EFI_RSC_HANDLER_REGISTER),
    ("Unregister",  EFI_RSC_HANDLER_UNREGISTER)
  ]

