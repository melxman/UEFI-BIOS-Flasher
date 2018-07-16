#
# PciPlatform.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PciPlatform.py is free software: you can redistribute it and/or
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

from PciHostBridgeResourceAllocation  import        \
    EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PHASE,  \
    EFI_PCI_CONTROLLER_RESOURCE_ALLOCATION_PHASE

from PciRootBridgeIo                  import EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_PCI_ADDRESS

gEfiPciPlatformProtocolGuid = \
  EFI_GUID ()

class EFI_PCI_PLATFORM_PROTOCOL (Structure):
  pass

EFI_PCI_PLATFORM_POLICY = UINT32
EFI_RESERVE_NONE_IO_ALIAS        = 0x0000

EFI_RESERVE_ISA_IO_ALIAS         = 0x0001
EFI_RESERVE_ISA_IO_NO_ALIAS      = 0x0002
EFI_RESERVE_VGA_IO_ALIAS         = 0x0004
EFI_RESERVE_VGA_IO_NO_ALIAS      = 0x0008
BeforePciHostBridge       = 0
ChipsetEntry              = 0
AfterPciHostBridge        = 1
ChipsetExit               = 1
MaximumChipsetPhase       = 2
EFI_PCI_EXECUTION_PHASE   = ENUM

class EFI_PCI_CHIPSET_EXECUTION_PHASE (Structure):
  pass

EFI_PCI_PLATFORM_PHASE_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_PLATFORM_PROTOCOL),             # IN *This,
  EFI_HANDLE,                                     # IN HostBridge,
  EFI_PCI_HOST_BRIDGE_RESOURCE_ALLOCATION_PHASE,  # IN Phase,
  EFI_PCI_EXECUTION_PHASE                         # IN ExecPhase
  )

EFI_PCI_PLATFORM_PREPROCESS_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_PLATFORM_PROTOCOL),           # IN *This,
  EFI_HANDLE,                                   # IN HostBridge,
  EFI_HANDLE,                                   # IN RootBridge,
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_PCI_ADDRESS,  # IN PciAddress,
  EFI_PCI_CONTROLLER_RESOURCE_ALLOCATION_PHASE, # IN Phase,
  EFI_PCI_EXECUTION_PHASE                       # IN ExecPhase
  )

EFI_PCI_PLATFORM_GET_PLATFORM_POLICY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_PLATFORM_PROTOCOL), # IN  *This,
  POINTER(EFI_PCI_PLATFORM_POLICY)    # OUT *PciPolicy
  )

EFI_PCI_PLATFORM_GET_PCI_ROM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_PLATFORM_PROTOCOL), # IN  *This,
  EFI_HANDLE,                         # IN  PciHandle,
  POINTER(PVOID),                     # OUT **RomImage,
  POINTER(UINTN)                      # OUT *RomSize
  )

EFI_PCI_PLATFORM_PROTOCOL._fields_ = [
    ("PlatformNotify",          EFI_PCI_PLATFORM_PHASE_NOTIFY),
    ("PlatformPrepController",  EFI_PCI_PLATFORM_PREPROCESS_CONTROLLER),
    ("GetPlatformPolicy",       EFI_PCI_PLATFORM_GET_PLATFORM_POLICY),
    ("GetPciRom",               EFI_PCI_PLATFORM_GET_PCI_ROM)
  ]

