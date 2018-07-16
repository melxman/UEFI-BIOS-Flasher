#
# FormBrowserEx2.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FormBrowserEx2.py is free software: you can redistribute it and/or
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
      EFI_HII_HANDLE,   \
      EFI_QUESTION_ID,  \
      EFI_FORM_ID
from EfiPy.MdeModulePkg.Protocol.FormBrowserEx import \
      SET_SCOPE,        \
      REGISTER_HOT_KEY, \
      REGISTER_EXIT_HANDLER

gEdkiiFormBrowserEx2ProtocolGuid = \
  EFI_GUID (0xa770c357, 0xb693, 0x4e6d, (0xa6, 0xcf, 0xd2, 0x1c, 0x72, 0x8e, 0x55, 0xb))

class EDKII_FORM_BROWSER_EXTENSION2_PROTOCOL (Structure):
  pass

BROWSER_EXTENSION2_VERSION_1    = 0x10000
BROWSER_EXTENSION2_VERSION_1_1  = 0x10001

IS_BROWSER_DATA_MODIFIED = CFUNCTYPE (
  BOOLEAN
  )

EXECUTE_ACTION = CFUNCTYPE (
  EFI_STATUS,
  UINT32,        # IN Action,
  UINT16         # IN DefaultId
  )

IS_RESET_REQUIRED = CFUNCTYPE (
  BOOLEAN
  )

FORM_ENTRY_INFO_SIGNATURE    = SIGNATURE_32 ('f', 'e', 'i', 's')

class FORM_ENTRY_INFO (Structure):
  _fields_ = [
  ("Signature",   UINTN),
  ("Link",        LIST_ENTRY),
  ("HiiHandle",   EFI_HII_HANDLE),
  ("FormSetGuid", EFI_GUID),
  ("FormId",      EFI_FORM_ID),
  ("QuestionId",  EFI_QUESTION_ID)
  ]

FORM_QUESTION_ATTRIBUTE_OVERRIDE_SIGNATURE    = SIGNATURE_32 ('f', 'q', 'o', 's')

class QUESTION_ATTRIBUTE_OVERRIDE (Structure):
  _fields_ = [
  ("Signature",   UINTN),
  ("Link",        LIST_ENTRY),
  ("QuestionId",  EFI_QUESTION_ID),
  ("FormId",      EFI_FORM_ID),
  ("FormSetGuid", EFI_GUID),
  ("HiiHandle",   EFI_HII_HANDLE),
  ("Attribute",   UINT32)
  ]

EDKII_FORM_BROWSER_EXTENSION2_PROTOCOL._fields_ = [
  ("Version",               UINT32),
  ("SetScope",              SET_SCOPE),
  ("RegisterHotKey",        REGISTER_HOT_KEY),
  ("RegiserExitHandler",    REGISTER_EXIT_HANDLER),
  ("IsBrowserDataModified", IS_BROWSER_DATA_MODIFIED),
  ("ExecuteAction",         EXECUTE_ACTION),
  ("FormViewHistoryHead",   LIST_ENTRY),
  ("OverrideQestListHead",  LIST_ENTRY),
  ("IsResetRequired",       IS_RESET_REQUIRED)
  ]

