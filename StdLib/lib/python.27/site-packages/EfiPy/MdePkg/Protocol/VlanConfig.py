#
# VlanConfig.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# VlanConfig.py is free software: you can redistribute it and/or
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

gEfiVlanConfigProtocolGuid  = \
  EFI_GUID (0x9e23d768, 0xd2f3, 0x4366, (0x9f, 0xc3, 0x3a, 0x7a, 0xba, 0x86, 0x43, 0x74 ))

class EFI_VLAN_CONFIG_PROTOCOL (Structure):
  pass

class EFI_VLAN_FIND_DATA (Structure):
  _fields_ = [
    ("VlanId",    UINT16),
    ("Priority",  UINT8)
  ]

EFI_VLAN_CONFIG_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VLAN_CONFIG_PROTOCOL),  # IN  *This
  UINT16,                             # IN  VlanId
  UINT8                               # IN  Priority
  )

EFI_VLAN_CONFIG_FIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VLAN_CONFIG_PROTOCOL),  # IN    *This
  UINT16,                             # IN    VlanId  OPTIONAL,
  POINTER(UINT16),                    #   OUT *NumberOfVlan,
  POINTER(POINTER(EFI_VLAN_FIND_DATA))#   OUT **Entries
  )

EFI_VLAN_CONFIG_REMOVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VLAN_CONFIG_PROTOCOL),  # IN    *This
  UINT16                              # IN    VlanId
  )

EFI_VLAN_CONFIG_PROTOCOL._fields_ = [
    ("Set",     EFI_VLAN_CONFIG_SET),
    ("Find",    EFI_VLAN_CONFIG_FIND),
    ("Remove",  EFI_VLAN_CONFIG_REMOVE)
  ]

