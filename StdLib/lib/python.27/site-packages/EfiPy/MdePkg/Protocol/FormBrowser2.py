#
# FormBrowser2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# FormBrowser2.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiBaseType   import *
from EfiPy.MdePkg.Uefi.UefiSpec       import *

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import  \
                                    EFI_HII_HANDLE,           \
                                    EFI_STRING,               \
                                    EFI_FORM_ID

gEfiFormBrowser2ProtocolGuid  = \
  EFI_GUID (0xb9d4c360, 0xbcfb, 0x4f9b, (0x92, 0x98, 0x53, 0xc1, 0x36, 0x98, 0x22, 0x58 ))

class EFI_FORM_BROWSER2_PROTOCOL (Structure):
  pass

class EFI_SCREEN_DESCRIPTOR (Structure):
  _fields_ = [
    ("LeftColumn",  UINTN),
    ("RightColumn", UINTN),
    ("TopRow",      UINTN),
    ("BottomRow",   UINTN)
  ]

EFI_BROWSER_ACTION_REQUEST  = UINTN

EFI_BROWSER_ACTION_REQUEST_NONE   = 0
EFI_BROWSER_ACTION_REQUEST_RESET  = 1
EFI_BROWSER_ACTION_REQUEST_SUBMIT = 2
EFI_BROWSER_ACTION_REQUEST_EXIT   = 3
EFI_BROWSER_ACTION_REQUEST_FORM_SUBMIT_EXIT  = 4
EFI_BROWSER_ACTION_REQUEST_FORM_DISCARD_EXIT = 5
EFI_BROWSER_ACTION_REQUEST_FORM_APPLY        = 6
EFI_BROWSER_ACTION_REQUEST_FORM_DISCARD      = 7
EFI_BROWSER_ACTION_REQUEST_RECONNECT         = 8

EFI_SEND_FORM2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FORM_BROWSER2_PROTOCOL),  # IN CONST  *This
  POINTER(EFI_HII_HANDLE),              # IN        *Handle,
  UINTN,                                # IN        HandleCount,
  POINTER(EFI_GUID),                    # IN        *FormSetGuid, OPTIONAL
  EFI_FORM_ID,                          # IN        FormId, OPTIONAL
  POINTER(EFI_SCREEN_DESCRIPTOR),       # IN CONST  *ScreenDimensions, OPTIONAL
  POINTER(EFI_BROWSER_ACTION_REQUEST)   # OUT       *ActionRequest  OPTIONAL
  )

EFI_BROWSER_CALLBACK2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FORM_BROWSER2_PROTOCOL),  # IN CONST  *This
  POINTER(UINTN),                       # IN OUT    *ResultsDataSize,
  EFI_STRING,                           # IN OUT    ResultsData,
  BOOLEAN,                              # IN CONST  RetrieveData,
  POINTER(EFI_GUID),                    # IN CONST  *VariableGuid, OPTIONAL
  PCHAR16                               # IN CONST  *VariableName OPTIONAL
  )

EFI_FORM_BROWSER2_PROTOCOL._fields_ = [
  ("SendForm",        EFI_SEND_FORM2),
  ("BrowserCallback", EFI_BROWSER_CALLBACK2)
  ]

