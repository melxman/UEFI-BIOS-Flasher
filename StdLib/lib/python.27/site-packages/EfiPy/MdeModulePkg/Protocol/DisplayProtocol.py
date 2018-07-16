#
# DisplayProtocol.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# DisplayProtocol.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
      EFI_STRING,           \
      EFI_IFR_TYPE_VALUE,   \
      EFI_STRING_ID,        \
      EFI_IFR_ONE_OF_OPTION,\
      EFI_IMAGE_ID,         \
      EFI_ANIMATION_ID,     \
      EFI_IFR_OP_HEADER,    \
      EFI_HII_HANDLE

from EfiPy.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY
from EfiPy.MdePkg.Protocol.FormBrowser2 import EFI_SCREEN_DESCRIPTOR

gEdkiiFormDisplayEngineProtocolGuid = \
  EFI_GUID (0x9bbe29e9, 0xfda1, 0x41ec, (0xad, 0x52, 0x45, 0x22, 0x13, 0x74, 0x2d, 0x2e))

BROWSER_ACTION_NONE         = BIT16
BROWSER_ACTION_FORM_EXIT    = BIT17
BROWSER_SUCCESS                   = 0x0
BROWSER_ERROR                     = BIT31
BROWSER_SUBMIT_FAIL               = BROWSER_ERROR | 0x01
BROWSER_NO_SUBMIT_IF              = BROWSER_ERROR | 0x02
BROWSER_FORM_NOT_FOUND            = BROWSER_ERROR | 0x03
BROWSER_FORM_SUPPRESS             = BROWSER_ERROR | 0x04
BROWSER_PROTOCOL_NOT_FOUND        = BROWSER_ERROR | 0x05
BROWSER_INCONSISTENT_IF           = BROWSER_ERROR | 0x06
BROWSER_WARNING_IF                = BROWSER_ERROR | 0x07
BROWSER_SUBMIT_FAIL_NO_SUBMIT_IF  = BROWSER_ERROR | 0x08
BROWSER_RECONNECT_REQUIRED        = BROWSER_ERROR | 0x09
BROWSER_RECONNECT_FAIL            = BROWSER_ERROR | 0x0A
BROWSER_RECONNECT_SAVE_CHANGES    = BROWSER_ERROR | 0x0B

FORM_DISPLAY_ENGINE_STATEMENT_VERSION_1  = 0x10000
FORM_DISPLAY_ENGINE_VERSION_1            = 0x10000
class EFI_HII_VALUE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Type",      UINT8),
  ("Buffer",    POINTER(UINT8)),
  ("BufferLen", UINT16),
  ("Value",     EFI_IFR_TYPE_VALUE)
  ]

DISPLAY_QUESTION_OPTION_SIGNATURE  = SIGNATURE_32 ('Q', 'O', 'P', 'T')

class DISPLAY_QUESTION_OPTION (Structure):
  _pack_   = 1
  _fields_ = [
  ("Signature",     UINTN),
  ("Link",          LIST_ENTRY),
  ("OptionOpCode",  POINTER(EFI_IFR_ONE_OF_OPTION)),
  ("ImageId",       EFI_IMAGE_ID),
  ("AnimationId",   EFI_ANIMATION_ID)
  ]

class FORM_DISPLAY_ENGINE_STATEMENT (Structure):
  pass

class FORM_DISPLAY_ENGINE_FORM (Structure):
  pass

STATEMENT_VALID             = 0x0
STATEMENT_INVALID           = BIT31

INCOSISTENT_IF_TRUE         = STATEMENT_INVALID | 0x01
WARNING_IF_TRUE             = STATEMENT_INVALID | 0x02
STRING_TOO_LONG             = STATEMENT_INVALID | 0x03
class STATEMENT_ERROR_INFO (Structure):
  _pack_   = 1
  _fields_ = [
  ("StringId",  EFI_STRING_ID),
  ("TimeOut",   UINT8)
  ]

VALIDATE_QUESTION = CFUNCTYPE (
  UINT32,
  POINTER(FORM_DISPLAY_ENGINE_FORM),      #   IN  *Form,
  POINTER(FORM_DISPLAY_ENGINE_STATEMENT), #   IN  *Statement,
  POINTER(EFI_HII_VALUE),                 #   IN  *Value, 
  POINTER(STATEMENT_ERROR_INFO)           #   OUT *ErrorInfo
  )

PASSWORD_CHECK = CFUNCTYPE (
  UINT32,
  POINTER(FORM_DISPLAY_ENGINE_FORM),      #   IN  *Form,
  POINTER(FORM_DISPLAY_ENGINE_STATEMENT), #   IN  *Statement,
  EFI_STRING                              #   IN  PasswordString  OPTIONAL
  )

FORM_DISPLAY_ENGINE_STATEMENT_SIGNATURE  = SIGNATURE_32 ('F', 'S', 'T', 'A')

HII_DISPLAY_NONE             = 0
HII_DISPLAY_GRAYOUT          = BIT0
HII_DISPLAY_LOCK             = BIT1
HII_DISPLAY_READONLY         = BIT2
HII_DISPLAY_MODAL            = BIT3
HII_DISPLAY_SUPPRESS         = BIT4

FORM_DISPLAY_ENGINE_STATEMENT._fields_ = [
  ("Signature",           UINTN),
  ("Version",             UINTN),
  ("DisplayLink",         LIST_ENTRY),
  ("OpCode",              POINTER(EFI_IFR_OP_HEADER)),
  ("CurrentValue",        EFI_HII_VALUE),
  ("SettingChangedFlag",  BOOLEAN),
  ("NestStatementList",   LIST_ENTRY),
  ("OptionListHead",      LIST_ENTRY),
  ("Attribute",           UINT32),
  ("ValidateQuestion",    VALIDATE_QUESTION),
  ("PasswordCheck",       PASSWORD_CHECK),
  ("ImageId",             EFI_IMAGE_ID),
  ("AnimationId",         EFI_ANIMATION_ID)
  ]

BROWSER_HOT_KEY_SIGNATURE  = SIGNATURE_32 ('B', 'H', 'K', 'S')

class BROWSER_HOT_KEY (Structure):
  _fields_ = [
  ("Signature",   UINTN),
  ("Link",        LIST_ENTRY),
  ("KeyData",     POINTER(EFI_INPUT_KEY)),
  ("Action",      UINT32),
  ("DefaultId",   UINT16),
  ("HelpString",  EFI_STRING)
  ]


FORM_DISPLAY_ENGINE_FORM_SIGNATURE  = SIGNATURE_32 ('F', 'F', 'R', 'M')

FORM_DISPLAY_ENGINE_FORM._fields_ = [
  ("Signature",             UINTN),
  ("Version",               UINTN),
  ("StatementListHead",     LIST_ENTRY),
  ("StatementListOSF",      LIST_ENTRY),
  ("ScreenDimensions",      POINTER(EFI_SCREEN_DESCRIPTOR)),
  ("FormSetGuid",           EFI_GUID),
  ("HiiHandle",             EFI_HII_HANDLE),
  ("FormId",                UINT16),
  ("FormTitle",             EFI_STRING_ID),
  ("Attribute",             UINT32),
  ("SettingChangedFlag",    BOOLEAN),
  ("HighLightedStatement",  POINTER(FORM_DISPLAY_ENGINE_STATEMENT)),
  ("FormRefreshEvent",      EFI_EVENT),
  ("HotKeyListHead",        LIST_ENTRY),
  ("ImageId",               EFI_IMAGE_ID),
  ("AnimationId",           EFI_ANIMATION_ID),
  ("BrowserStatus",         UINT32),
  ("ErrorString",           EFI_STRING)
  ]

class USER_INPUT (Structure):
  _fields_ = [
  ("SelectedStatement", POINTER(FORM_DISPLAY_ENGINE_STATEMENT)),
  ("InputValue",        EFI_HII_VALUE),
  ("Action",            UINT32),
  ("DefaultId",         UINT16)
  ]

FORM_DISPLAY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FORM_DISPLAY_ENGINE_FORM),  #   IN *FormData,
  POINTER(USER_INPUT)                 #   OUT *UserInputData
  )

EXIT_DISPLAY = CFUNCTYPE (
  VOID
  )

CONFIRM_DATA_CHANGE = CFUNCTYPE (
  UINTN
  )

class EDKII_FORM_DISPLAY_ENGINE_PROTOCOL (Union):
  _fields_ = [
  ("FormDisplay",       FORM_DISPLAY),
  ("ExitDisplay",       EXIT_DISPLAY),
  ("ConfirmDataChange", CONFIRM_DATA_CHANGE)
  ]

