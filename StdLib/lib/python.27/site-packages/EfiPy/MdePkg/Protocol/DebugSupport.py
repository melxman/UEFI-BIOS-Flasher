#
# DebugSupport.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DebugSupport.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard  import PeImage

class EFI_DEBUG_SUPPORT_PROTOCOL (Structure):
  pass

gEfiDebugSupportProtocolGuid            = \
  EFI_GUID (0x2755590C, 0x6F3C, 0x42FA, (0x9E, 0xA4, 0xA3, 0xBA, 0x54, 0x3C, 0xDA, 0x25 ))

EFI_EXCEPTION_TYPE  = INTN

EXCEPT_IA32_DIVIDE_ERROR    = 0
EXCEPT_IA32_DEBUG           = 1
EXCEPT_IA32_NMI             = 2
EXCEPT_IA32_BREAKPOINT      = 3
EXCEPT_IA32_OVERFLOW        = 4
EXCEPT_IA32_BOUND           = 5
EXCEPT_IA32_INVALID_OPCODE  = 6
EXCEPT_IA32_DOUBLE_FAULT    = 8
EXCEPT_IA32_INVALID_TSS     = 10
EXCEPT_IA32_SEG_NOT_PRESENT = 11
EXCEPT_IA32_STACK_FAULT     = 12
EXCEPT_IA32_GP_FAULT        = 13
EXCEPT_IA32_PAGE_FAULT      = 14
EXCEPT_IA32_FP_ERROR        = 16
EXCEPT_IA32_ALIGNMENT_CHECK = 17
EXCEPT_IA32_MACHINE_CHECK   = 18
EXCEPT_IA32_SIMD            = 19

class EFI_FX_SAVE_STATE_IA32 (Structure):
  _fields_ = [
    ("Fcw",         UINT16),
    ("Fsw",         UINT16),
    ("Ftw",         UINT16),
    ("Opcode",      UINT16),
    ("Eip",         UINT32),
    ("Cs",          UINT16),
    ("Reserved1",   UINT16),
    ("DataOffset",  UINT32),
    ("Ds",          UINT16),
    ("Reserved2",   UINT8 * 10),
    ("St0Mm0",      UINT8 * 10),
    ("Reserved3",   UINT8 * 6),
    ("St1Mm1",      UINT8 * 10),
    ("Reserved4",   UINT8 * 6),
    ("St2Mm2",      UINT8 * 10),
    ("Reserved5",   UINT8 * 6),
    ("St3Mm3",      UINT8 * 10),
    ("Reserved6",   UINT8 * 6),
    ("St4Mm4",      UINT8 * 10),
    ("Reserved7",   UINT8 * 6),
    ("St5Mm5",      UINT8 * 10),
    ("Reserved8",   UINT8 * 6),
    ("St6Mm6",      UINT8 * 10),
    ("Reserved9",   UINT8 * 6),
    ("St7Mm7",      UINT8 * 10),
    ("Reserved10",  UINT8 * 6),
    ("Xmm0",        UINT8 * 16),
    ("Xmm1",        UINT8 * 16),
    ("Xmm2",        UINT8 * 16),
    ("Xmm3",        UINT8 * 16),
    ("Xmm4",        UINT8 * 16),
    ("Xmm5",        UINT8 * 16),
    ("Xmm6",        UINT8 * 16),
    ("Xmm7",        UINT8 * 16),
    ("Reserved11",  UINT8 * (14 * 16))
  ]

class EFI_SYSTEM_CONTEXT_IA32 (Structure):
  _fields_ = [
    ("ExceptionData", UINT32),
    ("FxSaveState",   EFI_FX_SAVE_STATE_IA32),
    ("Dr0",           UINT32),
    ("Dr1",           UINT32),
    ("Dr2",           UINT32),
    ("Dr3",           UINT32),
    ("Dr6",           UINT32),
    ("Dr7",           UINT32),
    ("Cr0",           UINT32),
    ("Cr1",           UINT32),
    ("Cr2",           UINT32),
    ("Cr3",           UINT32),
    ("Cr4",           UINT32),
    ("Eflags",        UINT32),
    ("Ldtr",          UINT32),
    ("Tr",            UINT32),
    ("Gdtr",          UINT32 * 2),
    ("Idtr",          UINT32 * 2),
    ("Eip",           UINT32),
    ("Gs",            UINT32),
    ("Fs",            UINT32),
    ("Es",            UINT32),
    ("Ds",            UINT32),
    ("Cs",            UINT32),
    ("Ss",            UINT32),
    ("Edi",           UINT32),
    ("Esi",           UINT32),
    ("Ebp",           UINT32),
    ("Esp",           UINT32),
    ("Ebx",           UINT32),
    ("Edx",           UINT32),
    ("Ecx",           UINT32),
    ("Eax",           UINT32)
  ]           

EXCEPT_X64_DIVIDE_ERROR    = 0
EXCEPT_X64_DEBUG           = 1
EXCEPT_X64_NMI             = 2
EXCEPT_X64_BREAKPOINT      = 3
EXCEPT_X64_OVERFLOW        = 4
EXCEPT_X64_BOUND           = 5
EXCEPT_X64_INVALID_OPCODE  = 6
EXCEPT_X64_DOUBLE_FAULT    = 8
EXCEPT_X64_INVALID_TSS     = 10
EXCEPT_X64_SEG_NOT_PRESENT = 11
EXCEPT_X64_STACK_FAULT     = 12
EXCEPT_X64_GP_FAULT        = 13
EXCEPT_X64_PAGE_FAULT      = 14
EXCEPT_X64_FP_ERROR        = 16
EXCEPT_X64_ALIGNMENT_CHECK = 17
EXCEPT_X64_MACHINE_CHECK   = 18
EXCEPT_X64_SIMD            = 19

class EFI_FX_SAVE_STATE_X64 (Structure):
  _fields_ = [
    ("Fcw",         UINT16),
    ("Fsw",         UINT16),
    ("Ftw",         UINT16),
    ("Opcode",      UINT16),
    ("Rip",         UINT64),
    ("DataOffset",  UINT64),
    ("Reserved1",   UINT8 *  8),
    ("St0Mm0",      UINT8 * 10),
    ("Reserved2",   UINT8 *  6),
    ("St1Mm1",      UINT8 * 10),
    ("Reserved3",   UINT8 *  6),
    ("St2Mm2",      UINT8 * 10),
    ("Reserved4",   UINT8 *  6),
    ("St3Mm3",      UINT8 * 10),
    ("Reserved5",   UINT8 *  6),
    ("St4Mm4",      UINT8 * 10),
    ("Reserved6",   UINT8 *  6),
    ("St5Mm5",      UINT8 * 10),
    ("Reserved7",   UINT8 *  6),
    ("St6Mm6",      UINT8 * 10),
    ("Reserved8",   UINT8 *  6),
    ("St7Mm7",      UINT8 * 10),
    ("Reserved9",   UINT8 *  6),
    ("Xmm0",        UINT8 * 16),
    ("Xmm1",        UINT8 * 16),
    ("Xmm2",        UINT8 * 16),
    ("Xmm3",        UINT8 * 16),
    ("Xmm4",        UINT8 * 16),
    ("Xmm5",        UINT8 * 16),
    ("Xmm6",        UINT8 * 16),
    ("Xmm7",        UINT8 * 16),
    ("Reserved11",  UINT8 * (14 * 16))
  ]

class EFI_SYSTEM_CONTEXT_X64 (Structure):
  _fields_ = [
    ("ExceptionData", UINT64),
    ("FxSaveState",   EFI_FX_SAVE_STATE_X64),
    ("Dr0",           UINT64),
    ("Dr1",           UINT64),
    ("Dr2",           UINT64),
    ("Dr3",           UINT64),
    ("Dr6",           UINT64),
    ("Dr7",           UINT64),
    ("Cr0",           UINT64),
    ("Cr1",           UINT64),
    ("Cr2",           UINT64),
    ("Cr3",           UINT64),
    ("Cr4",           UINT64),
    ("Cr8",           UINT64),
    ("Rflags",        UINT64),
    ("Ldtr",          UINT64),
    ("Tr",            UINT64),
    ("Gdtr",          UINT64 * 2),
    ("Idtr",          UINT64 * 2),
    ("Rip",           UINT64),
    ("Gs",            UINT64),
    ("Fs",            UINT64),
    ("Es",            UINT64),
    ("Ds",            UINT64),
    ("Cs",            UINT64),
    ("Ss",            UINT64),
    ("Rdi",           UINT64),
    ("Rsi",           UINT64),
    ("Rbp",           UINT64),
    ("Rsp",           UINT64),
    ("Rbx",           UINT64),
    ("Rdx",           UINT64),
    ("Rcx",           UINT64),
    ("Rax",           UINT64),
    ("R8",            UINT64),
    ("R9",            UINT64),
    ("R10",           UINT64),
    ("R11",           UINT64),
    ("R12",           UINT64),
    ("R13",           UINT64),
    ("R14",           UINT64),
    ("R15",           UINT64)
  ]
EXCEPT_IPF_VHTP_TRANSLATION       = 0
EXCEPT_IPF_INSTRUCTION_TLB        = 1
EXCEPT_IPF_DATA_TLB               = 2
EXCEPT_IPF_ALT_INSTRUCTION_TLB    = 3
EXCEPT_IPF_ALT_DATA_TLB           = 4
EXCEPT_IPF_DATA_NESTED_TLB        = 5
EXCEPT_IPF_INSTRUCTION_KEY_MISSED = 6
EXCEPT_IPF_DATA_KEY_MISSED        = 7
EXCEPT_IPF_DIRTY_BIT              = 8
EXCEPT_IPF_INSTRUCTION_ACCESS_BIT = 9
EXCEPT_IPF_DATA_ACCESS_BIT        = 10
EXCEPT_IPF_BREAKPOINT             = 11
EXCEPT_IPF_EXTERNAL_INTERRUPT     = 12

EXCEPT_IPF_PAGE_NOT_PRESENT           = 20
EXCEPT_IPF_KEY_PERMISSION             = 21
EXCEPT_IPF_INSTRUCTION_ACCESS_RIGHTS  = 22
EXCEPT_IPF_DATA_ACCESS_RIGHTS         = 23
EXCEPT_IPF_GENERAL_EXCEPTION          = 24
EXCEPT_IPF_DISABLED_FP_REGISTER       = 25
EXCEPT_IPF_NAT_CONSUMPTION            = 26
EXCEPT_IPF_SPECULATION                = 27

EXCEPT_IPF_DEBUG                          = 29
EXCEPT_IPF_UNALIGNED_REFERENCE            = 30
EXCEPT_IPF_UNSUPPORTED_DATA_REFERENCE     = 31
EXCEPT_IPF_FP_FAULT                       = 32
EXCEPT_IPF_FP_TRAP                        = 33
EXCEPT_IPF_LOWER_PRIVILEGE_TRANSFER_TRAP  = 34
EXCEPT_IPF_TAKEN_BRANCH                   = 35
EXCEPT_IPF_SINGLE_STEP                    = 36

EXCEPT_IPF_IA32_EXCEPTION = 45
EXCEPT_IPF_IA32_INTERCEPT = 46
EXCEPT_IPF_IA32_INTERRUPT = 47

class EFI_SYSTEM_CONTEXT_IPF (Structure):
  _fields_ = [
    ("Reserved",    UINT64),
    ("R1",          UINT64),
    ("R2",          UINT64),
    ("R3",          UINT64),
    ("R4",          UINT64),
    ("R5",          UINT64),
    ("R6",          UINT64),
    ("R7",          UINT64),
    ("R8",          UINT64),
    ("R9",          UINT64),
    ("R10",         UINT64),
    ("R11",         UINT64),
    ("R12",         UINT64),
    ("R13",         UINT64),
    ("R14",         UINT64),
    ("R15",         UINT64),
    ("R16",         UINT64),
    ("R17",         UINT64),
    ("R18",         UINT64),
    ("R19",         UINT64),
    ("R20",         UINT64),
    ("R21",         UINT64),
    ("R22",         UINT64),
    ("R23",         UINT64),
    ("R24",         UINT64),
    ("R25",         UINT64),
    ("R26",         UINT64),
    ("R27",         UINT64),
    ("R28",         UINT64),
    ("R29",         UINT64),
    ("R30",         UINT64),
    ("R31",         UINT64),
    ("F2",          UINT64 * 2),
    ("F3",          UINT64 * 2),
    ("F4",          UINT64 * 2),
    ("F5",          UINT64 * 2),
    ("F6",          UINT64 * 2),
    ("F7",          UINT64 * 2),
    ("F8",          UINT64 * 2),
    ("F9",          UINT64 * 2),
    ("F10",         UINT64 * 2),
    ("F11",         UINT64 * 2),
    ("F12",         UINT64 * 2),
    ("F13",         UINT64 * 2),
    ("F14",         UINT64 * 2),
    ("F15",         UINT64 * 2),
    ("F16",         UINT64 * 2),
    ("F17",         UINT64 * 2),
    ("F18",         UINT64 * 2),
    ("F19",         UINT64 * 2),
    ("F20",         UINT64 * 2),
    ("F21",         UINT64 * 2),
    ("F22",         UINT64 * 2),
    ("F23",         UINT64 * 2),
    ("F24",         UINT64 * 2),
    ("F25",         UINT64 * 2),
    ("F26",         UINT64 * 2),
    ("F27",         UINT64 * 2),
    ("F28",         UINT64 * 2),
    ("F29",         UINT64 * 2),
    ("F30",         UINT64 * 2),
    ("F31",         UINT64 * 2),
    ("Pr",          UINT64),
    ("B0",          UINT64),
    ("B1",          UINT64),
    ("B2",          UINT64),
    ("B3",          UINT64),
    ("B4",          UINT64),
    ("B5",          UINT64),
    ("B6",          UINT64),
    ("B7",          UINT64),
    ("ArRsc",       UINT64),
    ("ArBsp",       UINT64),
    ("ArBspstore",  UINT64),
    ("ArRnat",      UINT64),
    ("ArFcr",       UINT64),
    ("ArEflag",     UINT64),
    ("ArCsd",       UINT64),
    ("ArSsd",       UINT64),
    ("ArCflg",      UINT64),
    ("ArFsr",       UINT64),
    ("ArFir",       UINT64),
    ("ArFdr",       UINT64),
    ("ArCcv",       UINT64),
    ("ArUnat",      UINT64),
    ("ArFpsr",      UINT64),
    ("ArPfs",       UINT64),
    ("ArLc",        UINT64),
    ("ArEc",        UINT64),
    ("CrDcr",       UINT64),
    ("CrItm",       UINT64),
    ("CrIva",       UINT64),
    ("CrPta",       UINT64),
    ("CrIpsr",      UINT64),
    ("CrIsr",       UINT64),
    ("CrIip",       UINT64),
    ("CrIfa",       UINT64),
    ("CrItir",      UINT64),
    ("CrIipa",      UINT64),
    ("CrIfs",       UINT64),
    ("CrIim",       UINT64),
    ("CrIha",       UINT64),
    ("Dbr0",        UINT64),
    ("Dbr1",        UINT64),
    ("Dbr2",        UINT64),
    ("Dbr3",        UINT64),
    ("Dbr4",        UINT64),
    ("Dbr5",        UINT64),
    ("Dbr6",        UINT64),
    ("Dbr7",        UINT64),
    ("Ibr0",        UINT64),
    ("Ibr1",        UINT64),
    ("Ibr2",        UINT64),
    ("Ibr3",        UINT64),
    ("Ibr4",        UINT64),
    ("Ibr5",        UINT64),
    ("Ibr6",        UINT64),
    ("Ibr7",        UINT64),
    ("IntNat",      UINT64)
  ]

EXCEPT_EBC_UNDEFINED            = 0
EXCEPT_EBC_DIVIDE_ERROR          = 1
EXCEPT_EBC_DEBUG                 = 2
EXCEPT_EBC_BREAKPOINT            = 3
EXCEPT_EBC_OVERFLOW              = 4
EXCEPT_EBC_INVALID_OPCODE        = 5
EXCEPT_EBC_STACK_FAULT           = 6
EXCEPT_EBC_ALIGNMENT_CHECK       = 7
EXCEPT_EBC_INSTRUCTION_ENCODING  = 8
EXCEPT_EBC_BAD_BREAK             = 9
EXCEPT_EBC_STEP                  = 10

MAX_EBC_EXCEPTION = EXCEPT_EBC_STEP

class EFI_SYSTEM_CONTEXT_EBC (Structure):
  _fields_ = [
    ("R0",            UINT64),
    ("R1",            UINT64),
    ("R2",            UINT64),
    ("R3",            UINT64),
    ("R4",            UINT64),
    ("R5",            UINT64),
    ("R6",            UINT64),
    ("R7",            UINT64),
    ("Flags",         UINT64),
    ("ControlFlags",  UINT64),
    ("Ip",            UINT64)
  ]

EXCEPT_ARM_RESET                    = 0
EXCEPT_ARM_UNDEFINED_INSTRUCTION    = 1
EXCEPT_ARM_SOFTWARE_INTERRUPT       = 2
EXCEPT_ARM_PREFETCH_ABORT           = 3
EXCEPT_ARM_DATA_ABORT               = 4
EXCEPT_ARM_RESERVED                 = 5
EXCEPT_ARM_IRQ                      = 6
EXCEPT_ARM_FIQ                      = 7

MAX_ARM_EXCEPTION = EXCEPT_ARM_FIQ
class EFI_SYSTEM_CONTEXT_ARM (Structure):
  _fields_ = [
    ("R0",    UINT32),
    ("R1",    UINT32),
    ("R2",    UINT32),
    ("R3",    UINT32),
    ("R4",    UINT32),
    ("R5",    UINT32),
    ("R6",    UINT32),
    ("R7",    UINT32),
    ("R8",    UINT32),
    ("R9",    UINT32),
    ("R10",   UINT32),
    ("R11",   UINT32),
    ("R12",   UINT32),
    ("SP",    UINT32),
    ("LR",    UINT32),
    ("PC",    UINT32),
    ("CPSR",  UINT32),
    ("DFSR",  UINT32),
    ("DFAR",  UINT32),
    ("IFSR",  UINT32),
    ("IFAR",  UINT32)
  ]

EXCEPT_AARCH64_SYNCHRONOUS_EXCEPTIONS    = 0
EXCEPT_AARCH64_IRQ                       = 1
EXCEPT_AARCH64_FIQ                       = 2
EXCEPT_AARCH64_SERROR                    = 3

MAX_AARCH64_EXCEPTION = EXCEPT_AARCH64_SERROR
class EFI_SYSTEM_CONTEXT_AARCH64 (Structure):
  _fields_ = [
    ("X0",    UINT64),
    ("X1",    UINT64),
    ("X2",    UINT64),
    ("X3",    UINT64),
    ("X4",    UINT64),
    ("X5",    UINT64),
    ("X6",    UINT64),
    ("X7",    UINT64),
    ("X8",    UINT64),
    ("X9",    UINT64),
    ("X10",   UINT64),
    ("X11",   UINT64),
    ("X12",   UINT64),
    ("X13",   UINT64),
    ("X14",   UINT64),
    ("X15",   UINT64),
    ("X16",   UINT64),
    ("X17",   UINT64),
    ("X18",   UINT64),
    ("X19",   UINT64),
    ("X20",   UINT64),
    ("X21",   UINT64),
    ("X22",   UINT64),
    ("X23",   UINT64),
    ("X24",   UINT64),
    ("X25",   UINT64),
    ("X26",   UINT64),
    ("X27",   UINT64),
    ("X28",   UINT64),
    ("FP",    UINT64),
    ("LR",    UINT64),
    ("SP",    UINT64),
    ("V0",    UINT64 * 2),
    ("V1",    UINT64 * 2),
    ("V2",    UINT64 * 2),
    ("V3",    UINT64 * 2),
    ("V4",    UINT64 * 2),
    ("V5",    UINT64 * 2),
    ("V6",    UINT64 * 2),
    ("V7",    UINT64 * 2),
    ("V8",    UINT64 * 2),
    ("V9",    UINT64 * 2),
    ("V10",   UINT64 * 2),
    ("V11",   UINT64 * 2),
    ("V12",   UINT64 * 2),
    ("V13",   UINT64 * 2),
    ("V14",   UINT64 * 2),
    ("V15",   UINT64 * 2),
    ("V16",   UINT64 * 2),
    ("V17",   UINT64 * 2),
    ("V18",   UINT64 * 2),
    ("V19",   UINT64 * 2),
    ("V20",   UINT64 * 2),
    ("V21",   UINT64 * 2),
    ("V22",   UINT64 * 2),
    ("V23",   UINT64 * 2),
    ("V24",   UINT64 * 2),
    ("V25",   UINT64 * 2),
    ("V26",   UINT64 * 2),
    ("V27",   UINT64 * 2),
    ("V28",   UINT64 * 2),
    ("V29",   UINT64 * 2),
    ("V30",   UINT64 * 2),
    ("V31",   UINT64 * 2),
    ("ELR",   UINT64),
    ("SPSR",  UINT64),
    ("FPSR",  UINT64),
    ("ESR",   UINT64),
    ("FAR",   UINT64)
  ]

class EFI_SYSTEM_CONTEXT (Union):
  _fields_ = [
    ("SystemContextEbc",      POINTER (EFI_SYSTEM_CONTEXT_EBC)),
    ("SystemContextIa32",     POINTER (EFI_SYSTEM_CONTEXT_IA32)),
    ("SystemContextX64",      POINTER (EFI_SYSTEM_CONTEXT_X64)),
    ("SystemContextIpf",      POINTER (EFI_SYSTEM_CONTEXT_IPF)),
    ("SystemContextArm",      POINTER (EFI_SYSTEM_CONTEXT_ARM)),
    ("SystemContextAArch64",  POINTER (EFI_SYSTEM_CONTEXT_AARCH64))
  ]

EFI_EXCEPTION_CALLBACK = CFUNCTYPE (
  VOID,
  EFI_EXCEPTION_TYPE, # IN     ExceptionType,              
  EFI_SYSTEM_CONTEXT  # IN OUT SystemContext         
  )

EFI_PERIODIC_CALLBACK = CFUNCTYPE (
  VOID,
  EFI_SYSTEM_CONTEXT  # IN OUT SystemContext         
  )

IsaIa32 = PeImage.IMAGE_FILE_MACHINE_I386
IsaX64  = PeImage.IMAGE_FILE_MACHINE_X64
IsaIpf  = PeImage.IMAGE_FILE_MACHINE_IA64
IsaEbc  = PeImage.IMAGE_FILE_MACHINE_EBC
IsaArm  = PeImage.IMAGE_FILE_MACHINE_ARMTHUMB_MIXED
IsaAArch64  = PeImage.IMAGE_FILE_MACHINE_ARM64
EFI_INSTRUCTION_SET_ARCHITECTURE  = ENUM

EFI_GET_MAXIMUM_PROCESSOR_INDEX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN     *This
  POINTER (UINTN)                       #    OUT *MaxProcessorIndex
  )

EFI_REGISTER_PERIODIC_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN    *This
  UINTN,                                # IN    MaxProcessorIndex
  EFI_PERIODIC_CALLBACK                 # IN    PeriodicCallback
  )

EFI_REGISTER_EXCEPTION_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN    *This
  UINTN,                                # IN    MaxProcessorIndex
  EFI_EXCEPTION_CALLBACK,               # IN    ExceptionCallback
  EFI_EXCEPTION_TYPE                    # IN    ExceptionType
  )

EFI_INVALIDATE_INSTRUCTION_CACHE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN    *This
  UINTN,                                # IN    MaxProcessorIndex
  PVOID,                                # IN    *Start
  UINT64                                # IN    Length
  )

EFI_DEBUG_SUPPORT_PROTOCOL._fields_ = [
    ("Isa",                         EFI_INSTRUCTION_SET_ARCHITECTURE),
    ("GetMaximumProcessorIndex",    EFI_GET_MAXIMUM_PROCESSOR_INDEX),
    ("RegisterPeriodicCallback",    EFI_REGISTER_PERIODIC_CALLBACK),
    ("RegisterExceptionCallback",   EFI_REGISTER_EXCEPTION_CALLBACK),
    ("InvalidateInstructionCache",  EFI_INVALIDATE_INSTRUCTION_CACHE)
  ]
