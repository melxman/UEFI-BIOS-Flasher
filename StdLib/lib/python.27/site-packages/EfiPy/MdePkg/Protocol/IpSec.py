#
# IpSec.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# IpSec.py is free software: you can redistribute it and/or
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

import IpSecConfig

gEfiIpSecProtocolGuid  = \
  EFI_GUID (0xdfb386f7, 0xe100, 0x43ad, (0x9c, 0x9a, 0xed, 0x90, 0xd0, 0x8a, 0x5e, 0x12 ))

gEfiIpSec2ProtocolGuid = \
  EFI_GUID (0xa3979e64, 0xace8, 0x4ddc, (0xbc, 0x7, 0x4d, 0x66, 0xb8, 0xfd, 0x9, 0x77 ))

class EFI_IPSEC_PROTOCOL (Structure):
  pass

class EFI_IPSEC2_PROTOCOL (Structure):
  pass

class EFI_IPSEC_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

EFI_IPSEC_PROCESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IPSEC_PROTOCOL),                # IN     *This,
  EFI_HANDLE,                                 # IN     NicHandle,
  UINT8,                                      # IN     IpVer,
  PVOID,                                      # IN OUT *IpHead,
  POINTER(UINT8),                             # IN     *LastHead,
  PVOID,                                      # IN     *OptionsBuffer,
  UINT32,                                     # IN     OptionsLength,
  POINTER(POINTER(EFI_IPSEC_FRAGMENT_DATA)),  # IN OUT **FragmentTable,
  POINTER(UINT32),                            # IN     *FragmentCount,
  IpSecConfig.EFI_IPSEC_TRAFFIC_DIR,          # IN     TrafficDirection,
  POINTER(EFI_EVENT)                          #    OUT *RecycleSignal
  )

EFI_IPSEC_PROTOCOL._fields_ = [
    ("Process",       EFI_IPSEC_PROCESS),
    ("DisabledEvent", EFI_EVENT),
    ("DisabledFlag",  BOOLEAN)
  ]

EFI_IPSEC_PROCESSEXT = CFUNCTYPE (
    POINTER(EFI_IPSEC2_PROTOCOL),               # IN     *This, 
    EFI_HANDLE,                                 # IN     NicHandle, 
    UINT8,                                      # IN     IpVer, 
    PVOID,                                      # IN OUT *IpHead, 
    POINTER(UINT8),                             # IN OUT *LastHead, 
    POINTER(PVOID),                             # IN OUT **OptionsBuffer, 
    POINTER(UINT32),                            # IN OUT *OptionsLength, 
    POINTER(POINTER(EFI_IPSEC_FRAGMENT_DATA)),  # IN OUT **FragmentTable, 
    POINTER(UINT32),                            # IN OUT *FragmentCount, 
    IpSecConfig.EFI_IPSEC_TRAFFIC_DIR,          # IN     TrafficDirection, 
    POINTER(EFI_EVENT)                          #    OUT *RecycleSignal
  )

EFI_IPSEC2_PROTOCOL._fields_ = [
    ("ProcessExt",    EFI_IPSEC_PROCESSEXT),
    ("DisabledEvent", EFI_EVENT),
    ("DisabledFlag",  BOOLEAN)
  ]

