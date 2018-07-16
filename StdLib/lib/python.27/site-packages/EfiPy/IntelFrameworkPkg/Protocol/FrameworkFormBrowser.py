#
# FrameworkFormBrowser.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FrameworkFormBrowser.py is free software: you can redistribute it and/or
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

from EfiPy.IntelFrameworkPkg.Protocol.FrameworkHii  import  EFI_HII_IFR_PACK,     \
                                                            EFI_HII_STRING_PACK,  \
                                                            EFI_HII_STRING_PACK,  \
                                                            FRAMEWORK_EFI_HII_HANDLE
from EfiPy.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY


gEfiFormBrowserProtocolGuid              = \
  EFI_GUID (0xe5a1333e, 0xe1b4, 0x4d55, (0xce, 0xeb, 0x35, 0xc3, 0xef, 0x13, 0x34, 0x43 ))

gEfiFormBrowserCompatibilityProtocolGuid = \
  EFI_GUID (0xfb7c852, 0xadca, 0x4853, ( 0x8d, 0xf, 0xfb, 0xa7, 0x1b, 0x1c, 0xe1, 0x1a ))

class EFI_FORM_BROWSER_PROTOCOL (Structure):
  pass

class EFI_HII_PACKET (Structure):
  _fields_ = [
    ("Length",  UINT32),
    ("Type",    UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_IFR_PACKET (Structure):
  _fields_ = [
    ("IfrData",     POINTER(EFI_HII_IFR_PACK)),
    ("StringData",  POINTER(EFI_HII_STRING_PACK))
  ]

class FRAMEWORK_EFI_SCREEN_DESCRIPTOR (Structure):
  _fields_ = [
    ("LeftColumn",  UINTN),
    ("RightColumn", UINTN),
    ("TopRow",      UINTN),
    ("BottomRow",   UINTN)
  ]

EFI_SEND_FORM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FORM_BROWSER_PROTOCOL),       #   IN  *This,
  BOOLEAN,                                  #   IN  UseDatabase,
  POINTER(FRAMEWORK_EFI_HII_HANDLE),        #   IN  *Handle,
  UINTN,                                    #   IN  HandleCount,
  POINTER(EFI_IFR_PACKET),                  #   IN  *Packet, OPTIONAL
  EFI_HANDLE,                               #   IN  CallbackHandle, OPTIONAL
  POINTER(UINT8),                           #   IN  *NvMapOverride, OPTIONAL
  POINTER(FRAMEWORK_EFI_SCREEN_DESCRIPTOR), #   IN  *ScreenDimensions, OPTIONAL
  POINTER(BOOLEAN)                          #   OUT *ResetRequired OPTIONAL
  )

EFI_CREATE_POP_UP = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                   #   IN  NumberOfLines,
  BOOLEAN,                 #   IN  HotKey,
  UINTN,                   #   IN  MaximumStringSize,
  POINTER(CHAR16),         #   OUT *StringBuffer,
  POINTER(EFI_INPUT_KEY),  #   OUT *KeyValue,
  POINTER(CHAR16)          #   IN  *String,
  )

EFI_FORM_BROWSER_PROTOCOL._fields_ = [
    ("SendForm",         EFI_SEND_FORM),
    ("CreatePopUp",      EFI_CREATE_POP_UP)
  ]

