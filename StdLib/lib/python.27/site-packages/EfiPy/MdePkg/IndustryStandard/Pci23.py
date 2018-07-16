# 
# Pci23.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Pci23.py is free software: you can redistribute it and/or
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
from Pci22 import *

PCI_CLASS_MASS_STORAGE_ATA       = 0x05
PCI_IF_MASS_STORAGE_SINGLE_DMA   = 0x20
PCI_IF_MASS_STORAGE_CHAINED_DMA  = 0x30

PCI_CLASS_NETWORK_WORLDFIP              = 0x05
PCI_CLASS_NETWORK_PICMG_MULTI_COMPUTING = 0x06

PCI_CLASS_BRIDGE_SEMI_TRANSPARENT_P2P        = 0x09
PCI_IF_BRIDGE_SEMI_TRANSPARENT_P2P_PRIMARY   = 0x40
PCI_IF_BRIDGE_SEMI_TRANSPARENT_P2P_SECONDARY = 0x80
PCI_CLASS_BRIDGE_INFINIBAND_TO_PCI           = 0x0A

PCI_SUBCLASS_GPIB          = 0x04
PCI_SUBCLASS_SMART_CARD    = 0x05

PCI_IF_EHCI                      = 0x20
PCI_CLASS_SERIAL_IB              = 0x06
PCI_CLASS_SERIAL_IPMI            = 0x07
PCI_IF_IPMI_SMIC                 = 0x00
PCI_IF_IPMI_KCS                  = 0x01
PCI_IF_IPMI_BT                   = 0x02
PCI_CLASS_SERIAL_SERCOS          = 0x08
PCI_CLASS_SERIAL_CANBUS          = 0x09

PCI_SUBCLASS_BLUETOOTH    = 0x11
PCI_SUBCLASS_BROADBAND    = 0x12

PCI_SUBCLASS_PERFORMANCE_COUNTERS          = 0x01
PCI_SUBCLASS_COMMUNICATION_SYNCHRONIZATION = 0x10
PCI_SUBCLASS_MANAGEMENT_CARD               = 0x20

PCI_EXP_MAX_CONFIG_OFFSET     = 0x1000

EFI_PCI_CAPABILITY_ID_PCIX    = 0x07

class EFI_PCI_CAPABILITY_PCIX (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",         EFI_PCI_CAPABILITY_HDR),
    ("CommandReg",  UINT16),
    ("StatusReg",   UINT32)
    ]

class EFI_PCI_CAPABILITY_PCIX_BRDG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 EFI_PCI_CAPABILITY_HDR),
    ("SecStatusReg",        UINT16),
    ("StatusReg",           UINT32),
    ("SplitTransCtrlRegUp", UINT32),
    ("SplitTransCtrlRegDn", UINT32)
    ]

PCI_CODE_TYPE_EFI_IMAGE       = 0x03
