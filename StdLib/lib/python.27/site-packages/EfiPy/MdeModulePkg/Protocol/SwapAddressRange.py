#
# SwapAddressRange.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# SwapAddressRange.py is free software: you can redistribute it and/or
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

gEfiSwapAddressRangeProtocolGuid = \
  EFI_GUID (0x1259f60d, 0xb754, 0x468e, (0xa7, 0x89, 0x4d, 0xb8, 0x5d, 0x55, 0xe8, 0x7e))

class EFI_SWAP_ADDRESS_RANGE_PROTOCOL (Structure):
  pass

EFI_UNSUPPORT_LOCK  = 0
EFI_SOFTWARE_LOCK   = 1
EFI_HARDWARE_LOCK   = 2

EFI_SWAP_LOCK_CAPABILITY = UINT8

EFI_GET_RANGE_LOCATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SWAP_ADDRESS_RANGE_PROTOCOL), # IN  *This,
  POINTER(EFI_PHYSICAL_ADDRESS),            # OUT *BootBlockBase,
  POINTER(UINTN),                           # OUT *BootBlockSize,
  POINTER(EFI_PHYSICAL_ADDRESS),            # OUT *BackupBlockBase,
  POINTER(UINTN)                            # OUT *BackupBlockSize
  )

EFI_GET_SWAP_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SWAP_ADDRESS_RANGE_PROTOCOL), # IN  *This,
  POINTER(BOOLEAN)                          # OUT *SwapState
  )

EFI_SET_SWAP_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SWAP_ADDRESS_RANGE_PROTOCOL), # IN  *This,
  BOOLEAN                                   # IN  NewSwapState
  )

EFI_GET_RTC_POWER_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SWAP_ADDRESS_RANGE_PROTOCOL), # IN  *This,
  POINTER(BOOLEAN)                          # OUT *RtcPowerFailed
  )

EFI_GET_SWAP_LOCK_CAPABILITY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SWAP_ADDRESS_RANGE_PROTOCOL), # IN  *This,
  POINTER(EFI_SWAP_LOCK_CAPABILITY)         # OUT *LockCapability
  )

EFI_SET_SWAP_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SWAP_ADDRESS_RANGE_PROTOCOL), # IN  *This,
  EFI_SWAP_LOCK_CAPABILITY,                 # IN  LockCapability,
  BOOLEAN,                                  # IN  NewLockState
  )

EFI_SWAP_ADDRESS_RANGE_PROTOCOL._fields_ = [
  ("GetRangeLocation",      EFI_GET_RANGE_LOCATION),
  ("GetSwapState",          EFI_GET_SWAP_STATE),
  ("SetSwapState",          EFI_SET_SWAP_STATE),
  ("GetRtcPowerStatus",     EFI_GET_RTC_POWER_STATUS),
  ("GetSwapLockCapability", EFI_GET_SWAP_LOCK_CAPABILITY),
  ("SetSwapLock",           EFI_SET_SWAP_LOCK)
  ]

