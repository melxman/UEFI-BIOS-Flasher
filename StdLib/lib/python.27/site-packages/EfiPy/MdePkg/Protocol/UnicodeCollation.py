#
# UnicodeCollation.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UnicodeCollation.py is free software: you can redistribute it and/or
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


gEfiUnicodeCollationProtocolGuid  = \
  EFI_GUID (0x1d85cd7f, 0xf43d, 0x11d2, (0x9a, 0xc, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

gEfiUnicodeCollation2ProtocolGuid = \
  EFI_GUID (0xa4c751fc, 0x23ae, 0x4c3e, (0x92, 0xe9, 0x49, 0x64, 0xcf, 0x63, 0xf3, 0x49 ))

class EFI_UNICODE_COLLATION_PROTOCOL (Structure):
  pass

EFI_UNICODE_BYTE_ORDER_MARK = 0xfeff
EFI_UNICODE_COLLATION_STRICOLL = CFUNCTYPE (
  INTN,
  POINTER(EFI_UNICODE_COLLATION_PROTOCOL),  # IN  *This,
  PCHAR16,                                  # IN  *Str1,
  PCHAR16                                   # IN  *Str2
  )

EFI_UNICODE_COLLATION_METAIMATCH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UNICODE_COLLATION_PROTOCOL),  # IN  *This,
  PCHAR16,                                  # IN  *String,
  PCHAR16                                   # IN  *Pattern
  )

EFI_UNICODE_COLLATION_STRLWR = CFUNCTYPE (
  VOID,
  POINTER(EFI_UNICODE_COLLATION_PROTOCOL),  # IN      *This,
  PCHAR16                                   # IN  OUT *Str
  )

EFI_UNICODE_COLLATION_STRUPR = CFUNCTYPE (
  VOID,
  POINTER(EFI_UNICODE_COLLATION_PROTOCOL),  # IN      *This,
  PCHAR16                                   # IN  OUT *Str
  )

EFI_UNICODE_COLLATION_FATTOSTR = CFUNCTYPE (
  VOID,
  POINTER(EFI_UNICODE_COLLATION_PROTOCOL),  # IN      *This,
  UINTN,                                    # IN      FatSize,
  PCHAR8,                                   # IN      *Fat,
  PCHAR16                                   #     OUT *String
  )

EFI_UNICODE_COLLATION_STRTOFAT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UNICODE_COLLATION_PROTOCOL),  # IN      *This,
  PCHAR16,                                  # IN      *String
  UINTN,                                    # IN      FatSize,
  PCHAR8                                    #     OUT *Fat,
  )

EFI_UNICODE_COLLATION_PROTOCOL._fields_ = [
    ("StriColl",            EFI_UNICODE_COLLATION_STRICOLL),
    ("MetaiMatch",          EFI_UNICODE_COLLATION_METAIMATCH),
    ("StrLwr",              EFI_UNICODE_COLLATION_STRLWR),
    ("StrUpr",              EFI_UNICODE_COLLATION_STRUPR),
    ("FatToStr",            EFI_UNICODE_COLLATION_FATTOSTR),
    ("StrToFat",            EFI_UNICODE_COLLATION_STRTOFAT),
    ("SupportedLanguages",  PCHAR8)
  ]

