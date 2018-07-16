#
# FrameworkFormCallback.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FrameworkFormCallback.py is free software: you can redistribute it and/or
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

from EfiPy.IntelFrameworkPkg.Protocol.FrameworkFormBrowser import EFI_IFR_PACKET

gEfiFormCallbackProtocolGuid = \
  EFI_GUID (0xf3e4543d, 0xcf35, 0x6cef, (0x35, 0xc4, 0x4f, 0xe6, 0x34, 0x4d, 0xfc, 0x54))

class EFI_FORM_CALLBACK_PROTOCOL (Structure):
  pass

RESET_REQUIRED  = 1 
EXIT_REQUIRED   = 2
SAVE_REQUIRED   = 4
NV_CHANGED      = 8
NV_NOT_CHANGED  = 16

class EFI_IFR_DATA_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT8),
    ("Length",  UINT8),
    ("Flags",   UINT16),
    ("Data",    PVOID)
  ]

class EFI_IFR_DATA_ARRAY (Structure):
  _pack_   = 1
  _fields_ = [
    ("EntryCount",  UINT32)
    # ("Data",        EFI_IFR_DATA_ENTRY * 1)
  ]

class EFI_HII_CALLBACK_PACKET (Union):
  _pack_   = 1
  _fields_ = [
    ("DataArray",   EFI_IFR_DATA_ARRAY),
    ("DataPacket",  EFI_IFR_PACKET),
    ("String",      CHAR16 * 1)
  ]

class EFI_IFR_NV_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("QuestionId",    UINT16),
    ("StorageWidth",  UINT8)
    # ("Data",          CHAR8 * 1)
  ]

EFI_NV_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FORM_CALLBACK_PROTOCOL),    #   IN     *This,
  POINTER(CHAR16),                        #   IN     *VariableName,
  POINTER(EFI_GUID),                      #   IN     *VendorGuid,
  POINTER(UINT32),                        #   OUT    *Attributes OPTIONAL,
  POINTER(UINTN),                         #   IN OUT *DataSize,
  PVOID                                   #   OUT    *Buffer
  )

EFI_NV_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FORM_CALLBACK_PROTOCOL),    #   IN     *This,
  POINTER(CHAR16),                        #   IN     *VariableName,
  POINTER(EFI_GUID),                      #   IN     *VendorGuid,
  UINT32,                                 #   IN     Attributes,
  UINTN,                                  #   IN     DataSize,
  POINTER(VOID),                          #   IN     *Buffer,
  POINTER(BOOLEAN)                        #   OUT    *ResetRequired
  )

EFI_FORM_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FORM_CALLBACK_PROTOCOL),      #   IN     *This,
  UINT16,                                   #   IN     KeyValue,
  POINTER(EFI_IFR_DATA_ARRAY),              #   IN     *Data,
  POINTER(POINTER(EFI_HII_CALLBACK_PACKET)) #   OUT    **Packet
  )

EFI_FORM_CALLBACK_PROTOCOL._fields_ = [
    ("NvRead",    EFI_NV_READ),
    ("NvWrite",   EFI_NV_WRITE),
    ("Callback",  EFI_FORM_CALLBACK)
  ]

