#
# EapManagement2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EapManagement2.py is free software: you can redistribute it and/or
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

import EapManagement

gEfiEapManagement2ProtocolGuid    = \
  EFI_GUID (0x5e93c847, 0x456d, 0x40b3, (0xa6, 0xb4, 0x78, 0xb0, 0xc9, 0xcf, 0x7f, 0x20 ))

class EFI_EAP_MANAGEMENT2_PROTOCOL (Structure):
  pass

EFI_EAP_GET_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT2_PROTOCOL),  # IN     *This
  POINTER(UINT8),                         # IN OUT *Msk,
  POINTER(UINTN),                         # IN OUT *MskSize,
  POINTER(UINT8),                         # IN OUT *Emsk,
  POINTER(UINT8)                          # IN OUT *EmskSize
  )

EFI_EAP_MANAGEMENT2_PROTOCOL._fields_ = [
    ("GetSystemConfiguration",      EapManagement.EFI_EAP_GET_SYSTEM_CONFIGURATION),
    ("SetSystemConfiguration",      EapManagement.EFI_EAP_SET_SYSTEM_CONFIGURATION),
    ("InitializePort",              EapManagement.EFI_EAP_INITIALIZE_PORT),
    ("UserLogon",                   EapManagement.EFI_EAP_USER_LOGON),
    ("UserLogoff",                  EapManagement.EFI_EAP_USER_LOGOFF),
    ("GetSupplicantStatus",         EapManagement.EFI_EAP_GET_SUPPLICANT_STATUS),
    ("SetSupplicantConfiguration",  EapManagement.EFI_EAP_SET_SUPPLICANT_CONFIGURATION),
    ("GetSupplicantStatistics",     EapManagement.EFI_EAP_GET_SUPPLICANT_STATISTICS),
    ("GetKey",                      EFI_EAP_GET_KEY)
  ]

