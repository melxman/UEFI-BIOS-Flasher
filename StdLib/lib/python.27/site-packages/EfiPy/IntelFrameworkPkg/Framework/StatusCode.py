#
# StatusCode.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# StatusCode.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi.PiStatusCode import  EFI_SUBCLASS_SPECIFIC,              \
                                          EFI_SOFTWARE,                       \
                                          EFI_SW_PEI_PC_RECOVERY_BEGIN,       \
                                          EFI_SW_PEI_PC_CAPSULE_LOAD,         \
                                          EFI_SW_PEI_PC_CAPSULE_START,        \
                                          EFI_SW_PEI_PC_RECOVERY_USER,        \
                                          EFI_SW_PEI_PC_RECOVERY_AUTO,        \
                                          EFI_SW_PEI_CORE_EC_DXE_CORRUPT,     \
                                          EFI_SW_PEI_CORE_EC_DXEIPL_NOT_FOUND

from EfiPy.MdePkg.Protocol import DebugSupport

EFI_SW_DXE_BS_PC_BEGIN_CONNECTING_DRIVERS     = (EFI_SUBCLASS_SPECIFIC | 0x00000005)
EFI_SW_DXE_BS_PC_VERIFYING_PASSWORD           = (EFI_SUBCLASS_SPECIFIC | 0x00000006)

EFI_SW_DXE_RT_PC_S0 = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_DXE_RT_PC_S1 = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_SW_DXE_RT_PC_S2 = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_SW_DXE_RT_PC_S3 = (EFI_SUBCLASS_SPECIFIC | 0x00000003)
EFI_SW_DXE_RT_PC_S4 = (EFI_SUBCLASS_SPECIFIC | 0x00000004)
EFI_SW_DXE_RT_PC_S5 = (EFI_SUBCLASS_SPECIFIC | 0x00000005)

EFI_SOFTWARE_X64_EXCEPTION        = (EFI_SOFTWARE | 0x00130000)

EFI_SW_EC_X64_DIVIDE_ERROR      = DebugSupport.EXCEPT_X64_DIVIDE_ERROR
EFI_SW_EC_X64_DEBUG             = DebugSupport.EXCEPT_X64_DEBUG
EFI_SW_EC_X64_NMI               = DebugSupport.EXCEPT_X64_NMI
EFI_SW_EC_X64_BREAKPOINT        = DebugSupport.EXCEPT_X64_BREAKPOINT
EFI_SW_EC_X64_OVERFLOW          = DebugSupport.EXCEPT_X64_OVERFLOW
EFI_SW_EC_X64_BOUND             = DebugSupport.EXCEPT_X64_BOUND
EFI_SW_EC_X64_INVALID_OPCODE    = DebugSupport.EXCEPT_X64_INVALID_OPCODE
EFI_SW_EC_X64_DOUBLE_FAULT      = DebugSupport.EXCEPT_X64_DOUBLE_FAULT
EFI_SW_EC_X64_INVALID_TSS       = DebugSupport.EXCEPT_X64_INVALID_TSS
EFI_SW_EC_X64_SEG_NOT_PRESENT   = DebugSupport.EXCEPT_X64_SEG_NOT_PRESENT
EFI_SW_EC_X64_STACK_FAULT       = DebugSupport.EXCEPT_X64_STACK_FAULT
EFI_SW_EC_X64_GP_FAULT          = DebugSupport.EXCEPT_X64_GP_FAULT
EFI_SW_EC_X64_PAGE_FAULT        = DebugSupport.EXCEPT_X64_PAGE_FAULT
EFI_SW_EC_X64_FP_ERROR          = DebugSupport.EXCEPT_X64_FP_ERROR
EFI_SW_EC_X64_ALIGNMENT_CHECK   = DebugSupport.EXCEPT_X64_ALIGNMENT_CHECK
EFI_SW_EC_X64_MACHINE_CHECK     = DebugSupport.EXCEPT_X64_MACHINE_CHECK
EFI_SW_EC_X64_SIMD              = DebugSupport.EXCEPT_X64_SIMD

EFI_SW_AL_PC_ENTRY_POINT    = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_SW_AL_PC_RETURN_TO_LAST = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_SW_CSM_LEGACY_ROM_INIT                = (EFI_SUBCLASS_SPECIFIC | 0x00000000)

EFI_IOB_ATA_BUS_SMART_ENABLE          = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IOB_ATA_BUS_SMART_DISABLE         = (EFI_SUBCLASS_SPECIFIC | 0x00000001)
EFI_IOB_ATA_BUS_SMART_OVERTHRESHOLD   = (EFI_SUBCLASS_SPECIFIC | 0x00000002)
EFI_IOB_ATA_BUS_SMART_UNDERTHRESHOLD  = (EFI_SUBCLASS_SPECIFIC | 0x00000003)

EFI_IOB_ATA_BUS_SMART_NOTSUPPORTED  = (EFI_SUBCLASS_SPECIFIC | 0x00000000)
EFI_IOB_ATA_BUS_SMART_DISABLED      = (EFI_SUBCLASS_SPECIFIC | 0x00000001)

EFI_CPU_CAUSE_NOT_DISABLED              = 0x0000

EFI_SW_PEIM_PC_RECOVERY_BEGIN  = EFI_SW_PEI_PC_RECOVERY_BEGIN
EFI_SW_PEIM_PC_CAPSULE_LOAD    = EFI_SW_PEI_PC_CAPSULE_LOAD
EFI_SW_PEIM_PC_CAPSULE_START   = EFI_SW_PEI_PC_CAPSULE_START
EFI_SW_PEIM_PC_RECOVERY_USER   = EFI_SW_PEI_PC_RECOVERY_USER
EFI_SW_PEIM_PC_RECOVERY_AUTO   = EFI_SW_PEI_PC_RECOVERY_AUTO

EFI_SW_PEIM_CORE_EC_DXE_CORRUPT       = EFI_SW_PEI_CORE_EC_DXE_CORRUPT
EFI_SW_PEIM_CORE_EC_DXEIPL_NOT_FOUND  = EFI_SW_PEI_CORE_EC_DXEIPL_NOT_FOUND

