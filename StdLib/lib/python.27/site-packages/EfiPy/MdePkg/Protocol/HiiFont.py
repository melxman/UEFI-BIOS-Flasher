#
# HiiFont.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HiiFont.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
        EFI_HII_HANDLE,     \
        EFI_HII_FONT_STYLE, \
        EFI_STRING,         \
        EFI_STRING_ID

import GraphicsOutput
import HiiImage

gEfiHiiFontProtocolGuid = \
  EFI_GUID (0xe9ca4775, 0x8657, 0x47fc, ( 0x97, 0xe7, 0x7e, 0xd6, 0x5a, 0x8, 0x43, 0x24 ))

class EFI_HII_FONT_PROTOCOL (Structure):
  pass

EFI_FONT_HANDLE   = PVOID
EFI_HII_OUT_FLAGS = UINT32
EFI_HII_OUT_FLAG_CLIP         = 0x00000001
EFI_HII_OUT_FLAG_WRAP         = 0x00000002
EFI_HII_OUT_FLAG_CLIP_CLEAN_Y = 0x00000004
EFI_HII_OUT_FLAG_CLIP_CLEAN_X = 0x00000008
EFI_HII_OUT_FLAG_TRANSPARENT  = 0x00000010
EFI_HII_IGNORE_IF_NO_GLYPH    = 0x00000020
EFI_HII_IGNORE_LINE_BREAK     = 0x00000040
EFI_HII_DIRECT_TO_SCREEN      = 0x00000080

class EFI_HII_ROW_INFO (Structure):
  _fields_ = [
    ("StartIndex",      UINTN),
    ("EndIndex",        UINTN),
    ("LineHeight",      UINTN),
    ("LineWidth",       UINTN),
    ("BaselineOffset",  UINTN)
  ]

EFI_FONT_INFO_MASK  = UINT32

EFI_FONT_INFO_SYS_FONT        = 0x00000001
EFI_FONT_INFO_SYS_SIZE        = 0x00000002
EFI_FONT_INFO_SYS_STYLE       = 0x00000004
EFI_FONT_INFO_SYS_FORE_COLOR  = 0x00000010
EFI_FONT_INFO_SYS_BACK_COLOR  = 0x00000020
EFI_FONT_INFO_RESIZE          = 0x00001000
EFI_FONT_INFO_RESTYLE         = 0x00002000
EFI_FONT_INFO_ANY_FONT        = 0x00010000
EFI_FONT_INFO_ANY_SIZE        = 0x00020000
EFI_FONT_INFO_ANY_STYLE       = 0x00040000

class EFI_FONT_INFO (Structure):
  _fields_ = [
    ("FontStyle", EFI_HII_FONT_STYLE),
    ("FontSize",  UINT16),
    ("FontName",  CHAR16 * 1)
  ]

class EFI_FONT_DISPLAY_INFO (Structure):
  _fields_ = [
    ("ForegroundColor", GraphicsOutput.EFI_GRAPHICS_OUTPUT_BLT_PIXEL),
    ("BackgroundColor", GraphicsOutput.EFI_GRAPHICS_OUTPUT_BLT_PIXEL),
    ("FontInfoMask",    EFI_FONT_INFO_MASK),
    ("FontInfo",        EFI_FONT_INFO)
  ]

EFI_HII_STRING_TO_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_FONT_PROTOCOL),               # IN CONST  *This,
  EFI_HII_OUT_FLAGS,                            # IN        Flags,
  EFI_STRING,                                   # IN CONST  String,
  POINTER(EFI_FONT_DISPLAY_INFO),               # IN CONST  *StringInfo,
  POINTER(POINTER(HiiImage.EFI_IMAGE_OUTPUT)),  # IN OUT    **Blt,
  UINTN,                                        # IN        BltX,
  UINTN,                                        # IN        BltY,
  POINTER(POINTER(EFI_HII_ROW_INFO)),           # OUT       **RowInfoArray OPTIONAL,
  POINTER(UINTN),                               # OUT       *RowInfoArraySize OPTIONAL,
  POINTER(UINTN)                                # OUT       *ColumnInfoArray OPTIONAL
  )

EFI_HII_STRING_ID_TO_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_FONT_PROTOCOL),               # IN CONST  *This,
  EFI_HII_OUT_FLAGS,                            # IN        Flags,
  EFI_HII_HANDLE,                               # IN        PackageList,
  EFI_STRING_ID,                                # IN        StringId,
  PCHAR8 ,                                      # IN CONST  *Language,
  POINTER(EFI_FONT_DISPLAY_INFO),               # IN CONST  *StringInfo       OPTIONAL,
  POINTER(POINTER(HiiImage.EFI_IMAGE_OUTPUT)),  # IN OUT    **Blt,
  UINTN,                                        # IN        BltX,
  UINTN,                                        # IN        BltY,
  POINTER(POINTER(EFI_HII_ROW_INFO)),           # OUT       **RowInfoArray    OPTIONAL,
  POINTER(UINTN),                               # OUT       *RowInfoArraySize OPTIONAL,
  POINTER(UINTN)                                # OUT       *ColumnInfoArray  OPTIONAL
  )

EFI_HII_GET_GLYPH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_FONT_PROTOCOL),               # IN CONST  *This,
  CHAR16,                                       # IN CONST  Char,
  POINTER(EFI_FONT_DISPLAY_INFO),               # IN CONST  *StringInfo,
  POINTER(POINTER(HiiImage.EFI_IMAGE_OUTPUT)),  # OUT       **Blt,
  POINTER(UINTN)                                # OUT       *Baseline OPTIONAL
  )

EFI_HII_GET_FONT_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_FONT_PROTOCOL),           # IN CONST  *This,
  POINTER(EFI_FONT_HANDLE),                 # IN OUT    *FontHandle,
  POINTER(EFI_FONT_DISPLAY_INFO),           # IN CONST  *StringInfoIn, OPTIONAL
  POINTER(POINTER(EFI_FONT_DISPLAY_INFO)),  # OUT       **StringInfoOut,
  EFI_STRING                                # IN CONST  String OPTIONAL
  )

EFI_HII_FONT_PROTOCOL._fields_ = [
    ("StringToImage",   EFI_HII_STRING_TO_IMAGE),
    ("StringIdToImage", EFI_HII_STRING_ID_TO_IMAGE),
    ("GetGlyph",        EFI_HII_GET_GLYPH),
    ("GetFontInfo",     EFI_HII_GET_FONT_INFO),
  ]

