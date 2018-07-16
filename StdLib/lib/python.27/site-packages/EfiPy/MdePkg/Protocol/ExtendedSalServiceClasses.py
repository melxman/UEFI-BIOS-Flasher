#
# ExtendedSalServiceClasses.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ExtendedSalServiceClasses.py is free software: you can redistribute it and/or
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

EFI_EXTENDED_SAL_BASE_IO_SERVICES_PROTOCOL_GUID_LO = 0x451531e15aea42b5L
EFI_EXTENDED_SAL_BASE_IO_SERVICES_PROTOCOL_GUID_HI = 0xa6657525d5b831bcL
EFI_EXTENDED_SAL_BASE_IO_SERVICES_PROTOCOL_GUID = \
  EFI_GUID (0x5aea42b5, 0x31e1, 0x4515, (0xbc, 0x31, 0xb8, 0xd5, 0x25, 0x75, 0x65, 0xa6 ))
IoReadFunctionId                          = 0
IoWriteFunctionId                         = 1
MemReadFunctionId                         = 2
MemWriteFunctionId                        = 3
EFI_EXTENDED_SAL_BASE_IO_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_STALL_SERVICES_PROTOCOL_GUID_LO = 0x4d8cac2753a58d06L
EFI_EXTENDED_SAL_STALL_SERVICES_PROTOCOL_GUID_HI = 0x704165808af0e9b5L
EFI_EXTENDED_SAL_STALL_SERVICES_PROTOCOL_GUID = \
  EFI_GUID (0x53a58d06, 0xac27, 0x4d8c, (0xb5, 0xe9, 0xf0, 0x8a, 0x80, 0x65, 0x41, 0x70 ))

StallFunctionId                 = 0
EFI_EXTENDED_SAL_STALL_FUNC_ID  = ENUM

EFI_EXTENDED_SAL_RTC_SERVICES_PROTOCOL_GUID_LO = 0x4d02efdb7e97a470L
EFI_EXTENDED_SAL_RTC_SERVICES_PROTOCOL_GUID_HI = 0x96a27bd29061ce8fL
EFI_EXTENDED_SAL_RTC_SERVICES_PROTOCOL_GUID = \
  EFI_GUID (0x7e97a470, 0xefdb, 0x4d02, (0x8f, 0xce, 0x61, 0x90, 0xd2, 0x7b, 0xa2, 0x96 ))

GetTimeFunctionId                     = 0
SetTimeFunctionId                     = 1
GetWakeupTimeFunctionId               = 2
SetWakeupTimeFunctionId               = 3
GetRtcFreqFunctionId                  = 4
InitializeThresholdFunctionId         = 5
BumpThresholdCountFunctionId          = 6
GetThresholdCountFunctionId           = 7
EFI_EXTENDED_SAL_RTC_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_VARIABLE_SERVICES_PROTOCOL_GUID_LO = 0x4370c6414ecb6c53L
EFI_EXTENDED_SAL_VARIABLE_SERVICES_PROTOCOL_GUID_HI = 0x78836e490e3bb28cL
EFI_EXTENDED_SAL_VARIABLE_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0x4ecb6c53, 0xc641, 0x4370, (0x8c, 0xb2, 0x3b, 0x0e, 0x49, 0x6e, 0x83, 0x78 ))

EsalGetVariableFunctionId                   = 0
EsalGetNextVariableNameFunctionId           = 1
EsalSetVariableFunctionId                   = 2
EsalQueryVariableInfoFunctionId             = 3
EFI_EXTENDED_SAL_VARIABLE_SERVICES_FUNC_ID  = ENUM

EFI_EXTENDED_SAL_MTC_SERVICES_PROTOCOL_GUID_LO = 0x408b75e8899afd18L
EFI_EXTENDED_SAL_MTC_SERVICES_PROTOCOL_GUID_HI = 0x54f4cd7e2e6e1aa4L
GetNextHighMonotonicCountFunctionId   = 0
EFI_EXTENDED_SAL_MTC_SERVICES_FUNC_ID = ENUM
EFI_EXTENDED_SAL_RESET_SERVICES_PROTOCOL_GUID_LO  = 0x46f58ce17d019990L
EFI_EXTENDED_SAL_RESET_SERVICES_PROTOCOL_GUID_HI  = 0xa06a6798513c76a7L
EFI_EXTENDED_SAL_RESET_SERVICES_PROTOCOL_GUID = \
  EFI_GUID (0x7d019990, 0x8ce1, 0x46f5, (0xa7, 0x76, 0x3c, 0x51, 0x98, 0x67, 0x6a, 0xa0 ))

ResetSystemFunctionId                   = 0
EFI_EXTENDED_SAL_RESET_SERVICES_FUNC_ID = ENUM
EFI_EXTENDED_SAL_STATUS_CODE_SERVICES_PROTOCOL_GUID_LO = 0x420f55e9dbd91dL
EFI_EXTENDED_SAL_STATUS_CODE_SERVICES_PROTOCOL_GUID_HI = 0x4fb437849f5e3996L
EFI_EXTENDED_SAL_STATUS_CODE_SERVICES_PROTOCOL_GUID = \
  EFI_GUID (0xdbd91d, 0x55e9, 0x420f, (0x96, 0x39, 0x5e, 0x9f, 0x84, 0x37, 0xb4, 0x4f ))

ReportStatusCodeServiceFunctionId             = 0
EFI_EXTENDED_SAL_STATUS_CODE_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_FV_BLOCK_SERVICES_PROTOCOL_GUID_LO = 0x4f1dbcbba2271df1L
EFI_EXTENDED_SAL_FV_BLOCK_SERVICES_PROTOCOL_GUID_HI = 0x1a072f17bc06a998L
EFI_EXTENDED_SAL_FV_BLOCK_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0xa2271df1, 0xbcbb, 0x4f1d, (0x98, 0xa9, 0x06, 0xbc, 0x17, 0x2f, 0x07, 0x1a ))
ReadFunctionId                              = 0
WriteFunctionId                             = 1
EraseBlockFunctionId                        = 2
GetVolumeAttributesFunctionId               = 3
SetVolumeAttributesFunctionId               = 4
GetPhysicalAddressFunctionId                = 5
GetBlockSizeFunctionId                      = 6
EFI_EXTENDED_SAL_FV_BLOCK_SERVICES_FUNC_ID  = ENUM

EFI_EXTENDED_SAL_MP_SERVICES_PROTOCOL_GUID_LO = 0x4dc0cf18697d81a2L
EFI_EXTENDED_SAL_MP_SERVICES_PROTOCOL_GUID_HI = 0x3f8a613b11060d9eL
EFI_EXTENDED_SAL_MP_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0x697d81a2, 0xcf18, 0x4dc0, (0x9e, 0x0d, 0x06, 0x11, 0x3b, 0x61, 0x8a, 0x3f ))
AddCpuDataFunctionId                  = 0
RemoveCpuDataFunctionId               = 1
ModifyCpuDataFunctionId               = 2
GetCpuDataByIDFunctionId              = 3
GetCpuDataByIndexFunctionId           = 4
SendIpiFunctionId                     = 5
CurrentProcInfoFunctionId             = 6
NumProcessorsFunctionId               = 7
SetMinStateFunctionId                 = 8
GetMinStateFunctionId                 = 9
EFI_EXTENDED_SAL_MP_SERVICES_FUNC_ID  = ENUM

EFI_EXTENDED_SAL_PAL_SERVICES_PROTOCOL_GUID_LO = 0x438d0fc2e1cd9d21L
EFI_EXTENDED_SAL_PAL_SERVICES_PROTOCOL_GUID_HI = 0x571e966de6040397L
EFI_EXTENDED_SAL_PAL_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0xe1cd9d21, 0x0fc2, 0x438d, (0x97, 0x03, 0x04, 0xe6, 0x6d, 0x96, 0x1e, 0x57 ))
PalProcFunctionId                     = 0
SetNewPalEntryFunctionId              = 1
GetNewPalEntryFunctionId              = 2
EsalUpdatePalFunctionId               = 3
EFI_EXTENDED_SAL_PAL_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_BASE_SERVICES_PROTOCOL_GUID_LO = 0x41c30fe0d9e9fa06L
EFI_EXTENDED_SAL_BASE_SERVICES_PROTOCOL_GUID_HI = 0xf894335a4283fb96L
EFI_EXTENDED_SAL_BASE_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0xd9e9fa06, 0x0fe0, 0x41c3, (0x96, 0xfb, 0x83, 0x42, 0x5a, 0x33, 0x94, 0xf8 ))
SalSetVectorsFunctionId                 = 0
SalMcRendezFunctionId                   = 1
SalMcSetParamsFunctionId                = 2
EsalGetVectorsFunctionId                = 3
EsalMcGetParamsFunctionId               = 4
EsalMcGetMcParamsFunctionId             = 5
EsalGetMcCheckinFlagsFunctionId         = 6
EsalGetPlatformBaseFreqFunctionId       = 7
EsalPhysicalIdInfoFunctionId            = 8
EsalRegisterPhysicalAddrFunctionId      = 9
EFI_EXTENDED_SAL_BASE_SERVICES_FUNC_ID  = ENUM

EFI_EXTENDED_SAL_MCA_SERVICES_PROTOCOL_GUID_LO = 0x42b16cc72a591128L
EFI_EXTENDED_SAL_MCA_SERVICES_PROTOCOL_GUID_HI = 0xbb2d683b9358f08aL
EFI_EXTENDED_SAL_MCA_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0x2a591128, 0x6cc7, 0x42b1, (0x8a, 0xf0, 0x58, 0x93, 0x3b, 0x68, 0x2d, 0xbb ))
McaGetStateInfoFunctionId             = 0
McaRegisterCpuFunctionId              = 1
EFI_EXTENDED_SAL_MCA_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_PCI_SERVICES_PROTOCOL_GUID_LO = 0x4905ad66a46b1a31L
EFI_EXTENDED_SAL_PCI_SERVICES_PROTOCOL_GUID_HI = 0x6330dc59462bf692L
EFI_EXTENDED_SAL_PCI_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0xa46b1a31, 0xad66, 0x4905, (0x92, 0xf6, 0x2b, 0x46, 0x59, 0xdc, 0x30, 0x63 ))
SalPciConfigReadFunctionId            = 0
SalPciConfigWriteFunctionId           = 1
EFI_EXTENDED_SAL_PCI_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_CACHE_SERVICES_PROTOCOL_GUID_LO = 0x4ba52743edc9494L
EFI_EXTENDED_SAL_CACHE_SERVICES_PROTOCOL_GUID_HI = 0x88f11352ef0a1888L
EFI_EXTENDED_SAL_CACHE_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0xedc9494, 0x2743, 0x4ba5, (0x88, 0x18, 0x0a, 0xef, 0x52, 0x13, 0xf1, 0x88 ))
SalCacheInitFunctionId                  = 0
SalCacheFlushFunctionId                 = 1
EFI_EXTENDED_SAL_CACHE_SERVICES_FUNC_ID = ENUM

EFI_EXTENDED_SAL_MCA_LOG_SERVICES_PROTOCOL_GUID_LO = 0x4c0338a3cb3fd86eL
EFI_EXTENDED_SAL_MCA_LOG_SERVICES_PROTOCOL_GUID_HI = 0x7aaba2a3cf905c9aL
EFI_EXTENDED_SAL_MCA_LOG_SERVICES_PROTOCOL_GUID  = \
  EFI_GUID (0xcb3fd86e, 0x38a3, 0x4c03, (0x9a, 0x5c, 0x90, 0xcf, 0xa3, 0xa2, 0xab, 0x7a ))
SalGetStateInfoFunctionId                 = 0
SalGetStateInfoSizeFunctionId             = 1
SalClearStateInfoFunctionId               = 2
EsalGetStateBufferFunctionId              = 3
EsalSaveStateBufferFunctionId             = 4
EFI_EXTENDED_SAL_MCA_LOG_SERVICES_FUNC_ID = ENUM

