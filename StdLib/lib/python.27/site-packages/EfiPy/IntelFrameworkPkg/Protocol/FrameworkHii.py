#
# FrameworkHii.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FrameworkHii.py is free software: you can redistribute it and/or
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
from EfiPy.IntelFrameworkPkg.Framework.FrameworkInternalFormRepresentation import STRING_REF
from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import EFI_KEY, EFI_STRING, EFI_FORM_ID
from EfiPy.MdePkg.Protocol.GraphicsOutput import EFI_GRAPHICS_OUTPUT_BLT_PIXEL

gEfiHiiProtocolGuid = \
  EFI_GUID (0xd7ad636e, 0xb997, 0x459b, (0xbf, 0x3f, 0x88, 0x46, 0x89, 0x79, 0x80, 0xe1))

gEfiHiiCompatibilityProtocolGuid = \
  EFI_GUID (0x5542cce1, 0xdf5c, 0x4d1b, ( 0xab, 0xca, 0x36, 0x4f, 0x77, 0xd3, 0x99, 0xfb))

RELOFST = UINT32

class EFI_HII_PROTOCOL (Structure):
  pass

FRAMEWORK_EFI_HII_HANDLE  = UINT16

EFI_HII_FONT        = 1
EFI_HII_STRING      = 2
EFI_HII_IFR         = 3
EFI_HII_KEYBOARD    = 4
EFI_HII_HANDLES     = 5
EFI_HII_VARIABLE    = 6
EFI_HII_DEVICE_PATH = 7

EFI_FORM_LABEL  = UINT16

class EFI_HII_PACK_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Length",  UINT32),
    ("Type",    UINT16)
  ]

class EFI_HII_IFR_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_PACK_HEADER)
  ]

class EFI_HII_HANDLE_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACK_HEADER),
    ("ImageHandle",       EFI_HANDLE),
    ("DeviceHandle",      EFI_HANDLE),
    ("ControllerHandle",  EFI_HANDLE),
    ("CallbackHandle",    EFI_HANDLE),
    ("COBExportHandle",   EFI_HANDLE)
  ]

class EFI_HII_VARIABLE_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_HII_PACK_HEADER),
    ("VariableGuid",        EFI_GUID),
    ("VariableNameLength",  UINT32),
    ("VariableId",          UINT16)
    # ("VariableName",        CHAR16 * N)
  ]

class EFI_HII_DEVICE_PATH_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_HII_PACK_HEADER)
    # ("DevicePath",        EFI_DEVICE_PATH * N)
  ]

class EFI_HII_DATA_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_HII_PACK_HEADER)
    # ("DevicePath",        EFI_DEVICE_PATH * N)
  ]

class EFI_HII_EXPORT_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("NumberOfHiiDataTables", UINT32),
    ("Revision",              EFI_GUID)
    # ("HiiDataTable",          POINTER(EFI_HII_DATA_TABLE))
  ]

class EFI_HII_UPDATE_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("FormSetUpdate",       BOOLEAN),
    ("FormCallbackHandle",  EFI_PHYSICAL_ADDRESS),
    ("FormUpdate",          BOOLEAN),
    ("FormValue",           UINT16),
    ("FormTitle",           STRING_REF),
    ("DataCount",           UINT16),
    ("Data",                POINTER(UINT8))
  ]

LANG_RIGHT_TO_LEFT  = 0x00000001

class EFI_HII_STRING_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                EFI_HII_PACK_HEADER),
    ("LanguageNameString",    RELOFST),
    ("PrintableLanguageName", RELOFST),
    ("NumStringPointers",     UINT32),
    ("Attributes",            UINT32)
    # ("StringPointers",        POINTER(RELOFST)),
    # ("Strings",               POINTER(EFI_STRING))
  ]

class EFI_HII_FONT_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                EFI_HII_PACK_HEADER),
    ("NumberOfNarrowGlyphs",  UINT16),
    ("NumberOfWideGlyphs",    UINT16)
    # ("NarrowGlyphs",          POINTER(EFI_NARROW_GLYPH))
    # ("WideGlyphs",            POINTER(EFI_WIDE_GLYPH))
  ]

class FRAMEWORK_EFI_KEY_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Key",                 EFI_KEY),
    ("Unicode",             CHAR16),
    ("ShiftedUnicode",      CHAR16),
    ("AltGrUnicode",        CHAR16),
    ("ShiftedAltGrUnicode", CHAR16),
    ("Modifier",            UINT16)
  ]

class EFI_HII_KEYBOARD_PACK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_PACK_HEADER),
    ("Descriptor",      POINTER(FRAMEWORK_EFI_KEY_DESCRIPTOR)),
    ("DescriptorCount", UINT8)
  ]

class EFI_HII_PACKAGES (Structure):
  _pack_   = 1
  _fields_ = [
    ("NumberOfPackages",  UINTN),
    ("GuidId",            POINTER(EFI_GUID))
    # ("HandlePack",        POINTER(EFI_HII_HANDLE_PACK)),
    # ("IfrPack",           POINTER(EFI_HII_IFR_PACK)),
    # ("FontPack",          POINTER(EFI_HII_FONT_PACK)),
    # ("StringPack",        POINTER(EFI_HII_STRING_PACK)),
    # ("KeyboardPack",      POINTER(EFI_HII_KEYBOARD_PACK))
  ]

class EFI_HII_VARIABLE_PACK_LIST (Structure):
  _pack_   = 1

EFI_HII_VARIABLE_PACK_LIST._fields_ = [
    ("NextVariablePack",  POINTER(EFI_HII_VARIABLE_PACK_LIST)),
    ("VariablePack",      POINTER(EFI_HII_VARIABLE_PACK)),
    ("Content",           EFI_HII_VARIABLE_PACK)
  ]

EFI_HII_NEW_PACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),          #   IN  *This,
  POINTER(EFI_HII_PACKAGES),          #   IN  *Packages,
  POINTER(FRAMEWORK_EFI_HII_HANDLE)   #   OUT *Handle
  )

EFI_HII_REMOVE_PACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),  #   IN  *This,
  FRAMEWORK_EFI_HII_HANDLE    #   IN  Handle
  )

EFI_HII_FIND_HANDLES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),          #   IN  *This,
  POINTER(UINT16),                    #   IN  *HandleBufferLength,
  POINTER(FRAMEWORK_EFI_HII_HANDLE)   #   OUT *Handle
  )

EFI_HII_EXPORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),          #   IN      *This,
  FRAMEWORK_EFI_HII_HANDLE,           #   IN      Handle
  POINTER(UINTN),                     #   IN OUT  *BufferSize
  PVOID                               #   OUT     *Buffer
  )

EFI_HII_RESET_STRINGS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),          #   IN      *This,
  FRAMEWORK_EFI_HII_HANDLE            #   IN      Handle
  )

EFI_HII_TEST_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),  #   IN     *This,
  POINTER(CHAR16),            #   IN     *StringToTest,
  POINTER(UINT32),            #   IN OUT *FirstMissing,
  POINTER(UINT32)             #   OUT    *GlyphBufferSize
  )

FRAMEWORK_EFI_HII_GET_GLYPH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),  #   IN     *This,
  POINTER(CHAR16),            #   IN     *Source,
  POINTER(UINT16),            #   IN OUT *Index,
  POINTER(POINTER(UINT8)),    #   OUT    **GlyphBuffer,
  POINTER(UINT16),            #   OUT    *BitWidth,
  POINTER(UINT32)             #   IN OUT *InternalStatus
  )

EFI_HII_GLYPH_TO_BLT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),              #   IN     *This,
  POINTER(UINT8),                         #   IN     *GlyphBuffer,
  EFI_GRAPHICS_OUTPUT_BLT_PIXEL,          #   IN     Foreground,
  EFI_GRAPHICS_OUTPUT_BLT_PIXEL,          #   IN     Background,
  UINTN,                                  #   IN     Count,
  UINTN,                                  #   IN     Width,
  UINTN,                                  #   IN     Height,
  POINTER(EFI_GRAPHICS_OUTPUT_BLT_PIXEL)  #   IN OUT *BltBuffer
  )

FRAMEWORK_EFI_HII_NEW_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),        #   IN     *This,
  POINTER(CHAR16),                  #   IN     *Language,
  FRAMEWORK_EFI_HII_HANDLE,         #   IN     Handle,
  POINTER(STRING_REF),              #   IN OUT *Reference,
  POINTER(CHAR16),                  #   IN     *NewString
  )

EFI_HII_GET_PRI_LANGUAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),        #   IN     *This,
  FRAMEWORK_EFI_HII_HANDLE,         #   IN     Handle,
  POINTER(EFI_STRING)               #      OUT *LanguageString
  )

EFI_HII_GET_SEC_LANGUAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),        #   IN     *This,
  FRAMEWORK_EFI_HII_HANDLE,         #   IN     Handle,
  POINTER(CHAR16),                  #   IN     *PrimaryLanguage,
  POINTER(EFI_STRING)               #      OUT *LanguageString
  )

FRAMEWORK_EFI_HII_GET_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),        #   IN     *This,
  FRAMEWORK_EFI_HII_HANDLE,         #   IN     Handle,
  STRING_REF,                       #   IN     Token,
  BOOLEAN,                          #   IN     Raw,
  POINTER(CHAR16),                  #   IN     *LanguageString,
  POINTER(UINTN),                   #   IN OUT *BufferLength,
  EFI_STRING                        #   OUT    StringBuffer
  )

EFI_HII_GET_LINE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),        #   IN     *This,
  FRAMEWORK_EFI_HII_HANDLE,         #   IN     Handle,
  STRING_REF,                       #   IN     Token,
  POINTER(UINT16),                  #   IN OUT *Index,
  UINT16,                           #   IN     LineWidth,
  POINTER(CHAR16),                  #   IN     *LanguageString,
  POINTER(UINT16),                  #   IN OUT *BufferLength,
  EFI_STRING                        #   OUT    StringBuffer
  )

EFI_HII_GET_FORMS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),        #   IN     *This,
  FRAMEWORK_EFI_HII_HANDLE,         #   IN     Handle,
  EFI_FORM_ID,                      #   IN     FormId,
  POINTER(UINTN),                   #   IN OUT *BufferLength,
  POINTER(UINT8)                    #   OUT    Buffer
  )

EFI_HII_GET_DEFAULT_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),                    #   IN     *This,
  FRAMEWORK_EFI_HII_HANDLE,                     #   IN     Handle,
  UINTN,                                        #   IN     DefaultMask,
  POINTER(POINTER(EFI_HII_VARIABLE_PACK_LIST))  #   OUT    **VariablePackList
  )

EFI_HII_UPDATE_FORM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),    #   IN *This,
  FRAMEWORK_EFI_HII_HANDLE,     #   IN Handle,
  EFI_FORM_LABEL,               #   IN Label,
  BOOLEAN,                      #   IN AddData,
  POINTER(EFI_HII_UPDATE_DATA)  #   IN *Data
  )

FRAMEWORK_EFI_HII_GET_KEYBOARD_LAYOUT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_PROTOCOL),              #   IN  *This,
  POINTER(UINT16),                        #   OUT *DescriptorCount
  POINTER(FRAMEWORK_EFI_KEY_DESCRIPTOR),  #   OUT *Descriptor
  )

EFI_HII_PROTOCOL._fields_ = [
  ("NewPack",               EFI_HII_NEW_PACK),
  ("RemovePack",            EFI_HII_REMOVE_PACK),
  ("FindHandles",           EFI_HII_FIND_HANDLES),
  ("ExportDatabase",        EFI_HII_EXPORT),
  ("TestString",            EFI_HII_TEST_STRING),
  ("GetGlyph",              FRAMEWORK_EFI_HII_GET_GLYPH),
  ("GlyphToBlt",            EFI_HII_GLYPH_TO_BLT),
  ("NewString",             FRAMEWORK_EFI_HII_NEW_STRING),
  ("GetPrimaryLanguages",   EFI_HII_GET_PRI_LANGUAGES),
  ("GetSecondaryLanguages", EFI_HII_GET_SEC_LANGUAGES),
  ("GetString",             FRAMEWORK_EFI_HII_GET_STRING),
  ("ResetStrings",          EFI_HII_RESET_STRINGS),
  ("GetLine",               EFI_HII_GET_LINE),
  ("GetForms",              EFI_HII_GET_FORMS),
  ("GetDefaultImage",       EFI_HII_GET_DEFAULT_IMAGE),
  ("UpdateForm",            EFI_HII_UPDATE_FORM),
  ("GetKeyboardLayout",     FRAMEWORK_EFI_HII_GET_KEYBOARD_LAYOUT)
  ]

