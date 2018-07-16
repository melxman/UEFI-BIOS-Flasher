#
# NetworkInterfaceIdentifier.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# NetworkInterfaceIdentifier.py is free software: you can redistribute it and/or
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


gEfiNetworkInterfaceIdentifierProtocolGuid    = \
  EFI_GUID (0xE18541CD, 0xF755, 0x4f73, (0x92, 0x8D, 0x64, 0x3C, 0x8A, 0x79, 0xB2, 0x29 ))

gEfiNetworkInterfaceIdentifierProtocolGuid_31 = \
  EFI_GUID (0x1ACED566, 0x76ED, 0x4218, (0xBC, 0x81, 0x76, 0x7F, 0x1F, 0x97, 0x7A, 0x89 ))

EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL_REVISION    = 0x00020000

EFI_NETWORK_INTERFACE_IDENTIFIER_INTERFACE_REVISION   = EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL_REVISION

class EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL (Structure):
  pass

EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL._fields_ = [
    ("Revision",      UINT64),
    ("Id",            UINT64),
    ("ImageAddr",     UINT64),
    ("ImageSize",     UINT32),
    ("StringId",      CHAR8 * 4),
    ("Type",          UINT8),
    ("MajorVer",      UINT8),
    ("MinorVer",      UINT8),
    ("Ipv6Supported", BOOLEAN),
    ("IfNum",         UINT16)
  ]

EfiNetworkInterfaceUndi = 1
EFI_NETWORK_INTERFACE_TYPE  = ENUM

class undiconfig_table (Structure):
  pass

class undiconfig_table_NII_entry (Structure):
  _fields_ = [
    ("NII_InterfacePointer",  PVOID),
    ("DevicePathPointer",     PVOID)
  ]

undiconfig_table._fields_ = [
    ("NumberOfInterfaces",  UINT32),
    ("reserved",            UINT32),
    ("nextlink",            POINTER(undiconfig_table)),
    ("NII_entry",           undiconfig_table_NII_entry * 1)
  ]

