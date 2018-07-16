#
# HiiString.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HiiString.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
    EFI_HII_HANDLE, \
    EFI_STRING_ID,  \
    EFI_STRING

import HiiFont

gEfiHiiStringProtocolGuid = \
  EFI_GUID (0xfd96974, 0x23aa, 0x4cdc, ( 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a ))

class EFI_HII_STRING_PROTOCOL (Structure):
  pass

EFI_HII_NEW_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL),   # IN CONST  *This,
  EFI_HII_HANDLE,                     # IN        PackageList,
  POINTER(EFI_STRING_ID),             # OUT       *StringId,
  PCHAR8,                             # IN CONST  *Language,
  PCHAR16,                            # IN  CONST *LanguageName, OPTIONAL  
  EFI_STRING,                         # IN CONST  String,
  POINTER(HiiFont.EFI_FONT_INFO)      # IN CONST  *StringFontInfo OPTIONAL
  )

EFI_HII_GET_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL),       # IN CONST  *This,
  PCHAR8,                                 # IN CONST  *Language,
  EFI_HII_HANDLE,                         # IN        PackageList,
  EFI_STRING_ID,                          # IN        StringId,
  EFI_STRING,                             # OUT       String,
  POINTER(UINTN),                         # IN OUT    *StringSize,
  POINTER(POINTER(HiiFont.EFI_FONT_INFO)) # OUT       **StringFontInfo OPTIONAL
  )

EFI_HII_SET_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                   # IN        PackageList,
  EFI_STRING_ID,                    # IN        StringId,
  PCHAR8,                           # IN CONST  *Language,
  EFI_STRING,                       # IN        String,
  POINTER(HiiFont.EFI_FONT_INFO)    # IN CONST  *StringFontInfo OPTIONAL
  )

EFI_HII_GET_LANGUAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                   # IN        PackageList,
  PCHAR8,                           # IN OUT    *Languages,
  POINTER(UINTN)                    # IN OUT    *LanguagesSize
  )

EFI_HII_GET_2ND_LANGUAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                   # IN        PackageList,
  PCHAR8,                           # IN CONST  *PrimaryLanguage,
  PCHAR8,                           # IN OUT    *SecondaryLanguages,
  POINTER(UINTN)                    # IN OUT    *SecondaryLanguagesSize
  )

EFI_HII_STRING_PROTOCOL._fields_ = [
    ("NewString",             EFI_HII_NEW_STRING),
    ("GetString",             EFI_HII_GET_STRING),
    ("SetString",             EFI_HII_SET_STRING),
    ("GetLanguages",          EFI_HII_GET_LANGUAGES),
    ("GetSecondaryLanguages", EFI_HII_GET_2ND_LANGUAGES)
  ]

