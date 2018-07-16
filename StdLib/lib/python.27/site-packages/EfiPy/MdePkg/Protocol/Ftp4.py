#
# Ftp4.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Ftp4.py is free software: you can redistribute it and/or
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

gEfiFtp4ServiceBindingProtocolGuid  = \
  EFI_GUID (0xfaaecb1, 0x226e, 0x4782, (0xaa, 0xce, 0x7d, 0xb9, 0xbc, 0xbf, 0x4d, 0xaf ))

gEfiFtp4ProtocolGuid                = \
  EFI_GUID (0xeb338826, 0x681b, 0x4295, (0xb3, 0x56, 0x2b, 0x36, 0x4c, 0x75, 0x7b, 0x9 ))

class EFI_FTP4_PROTOCOL (Structure):
  pass

class EFI_FTP4_CONNECTION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS)
  ]

class EFI_FTP4_CONFIG_DATA (Structure):
  _fields_ = [
    ("Username",          POINTER(UINT8)),
    ("Password",          POINTER(UINT8)),
    ("Active",            BOOLEAN),
    ("UseDefaultSetting", BOOLEAN),
    ("StationIp",         EFI_IPv4_ADDRESS),
    ("SubnetMask",        EFI_IPv4_ADDRESS),
    ("GatewayIp",         EFI_IPv4_ADDRESS),
    ("ServerIp",          EFI_IPv4_ADDRESS),
    ("ServerPort",        UINT16),
    ("AltDataPort",       UINT16),
    ("RepType",           UINT8),
    ("FileStruct",        UINT8),
    ("TransMode",         UINT8)
  ]

class EFI_FTP4_COMMAND_TOKEN (Structure):
  pass

EFI_FTP4_DATA_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),     # IN *This
  POINTER(EFI_FTP4_COMMAND_TOKEN) # IN *Token
  )

EFI_FTP4_COMMAND_TOKEN._fields_ = [
    ("Event",           EFI_EVENT),
    ("Pathname",        POINTER(UINT8)),
    ("DataBufferSize",  UINT64),       
    ("DataBuffer",      PVOID),
    ("DataCallback",    POINTER(EFI_FTP4_DATA_CALLBACK)),
    ("Context",         PVOID),
    ("Status",          EFI_STATUS)
  ]

EFI_FTP4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),     # IN  *This
  POINTER(EFI_FTP4_CONFIG_DATA)   # OUT *ModeData
  )

EFI_FTP4_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),         # IN  *This
  POINTER(EFI_FTP4_CONNECTION_TOKEN)  # IN  *Token
  )

EFI_FTP4_CLOSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),         # IN  *This
  POINTER(EFI_FTP4_CONNECTION_TOKEN)  # IN  *Token
  )

EFI_FTP4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),   # IN  *This
  POINTER(EFI_FTP4_CONFIG_DATA) # IN  *FtpConfigData OPTIONAL
  )

EFI_FTP4_READ_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),     # IN  *This
  POINTER(EFI_FTP4_COMMAND_TOKEN) # IN  *Token
  )

EFI_FTP4_WRITE_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),     # IN  *This
  POINTER(EFI_FTP4_COMMAND_TOKEN) # IN  *Token
  )

EFI_FTP4_READ_DIRECTORY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL),     # IN  *This
  POINTER(EFI_FTP4_COMMAND_TOKEN) # IN  *Token
  )

EFI_FTP4_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_FTP4_PROTOCOL)  # IN  *This
  )

EFI_FTP4_PROTOCOL._fields_ = [
    ("GetModeData",   EFI_FTP4_GET_MODE_DATA),
    ("Connect",       EFI_FTP4_CONNECT),
    ("Close",         EFI_FTP4_CLOSE),
    ("Configure",     EFI_FTP4_CONFIGURE),
    ("ReadFile",      EFI_FTP4_READ_FILE),
    ("WriteFile",     EFI_FTP4_WRITE_FILE),
    ("ReadDirectory", EFI_FTP4_READ_DIRECTORY),
    ("Poll",          EFI_FTP4_POLL)
  ]

