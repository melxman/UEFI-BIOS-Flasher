#
# AcpiS3Context.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# AcpiS3Context.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Library.BaseLib import IA32_DESCRIPTOR

SMM_S3_RESUME_SMM_32 = SIGNATURE_64 ('S','M','M','S','3','_','3','2')
SMM_S3_RESUME_SMM_64 = SIGNATURE_64 ('S','M','M','S','3','_','6','4')

class SMM_S3_RESUME_STATE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Signature",             UINT64),
  ("SmmS3ResumeEntryPoint", EFI_PHYSICAL_ADDRESS),
  ("SmmS3StackBase",        EFI_PHYSICAL_ADDRESS),
  ("SmmS3StackSize",        UINT64),
  ("SmmS3Cr0",              UINT64),
  ("SmmS3Cr3",              UINT64),
  ("SmmS3Cr4",              UINT64),
  ("ReturnCs",              UINT16),
  ("ReturnEntryPoint",      EFI_PHYSICAL_ADDRESS),
  ("ReturnContext1",        EFI_PHYSICAL_ADDRESS),
  ("ReturnContext2",        EFI_PHYSICAL_ADDRESS),
  ("ReturnStackPointer",    EFI_PHYSICAL_ADDRESS),
  ("Smst",                  EFI_PHYSICAL_ADDRESS)
  ]

class SMM_S3_RESUME_STATE (Structure):
  _pack_   = 1
  _fields_ = [
  ("AcpiFacsTable",           EFI_PHYSICAL_ADDRESS),
  ("IdtrProfile",             EFI_PHYSICAL_ADDRESS),
  ("S3NvsPageTableAddress",   EFI_PHYSICAL_ADDRESS),
  ("BootScriptStackBase",     EFI_PHYSICAL_ADDRESS),
  ("BootScriptStackSize",     UINT64),
  ("S3DebugBufferAddress",    EFI_PHYSICAL_ADDRESS)
  ]

class SMM_S3_RESUME_STATE (Structure):
  _pack_   = 1
  _fields_ = [
  ("ReturnCs",            UINT16),
  ("ReturnStatus",        UINT64),
  ("ReturnEntryPoint",    EFI_PHYSICAL_ADDRESS),
  ("ReturnStackPointer",  EFI_PHYSICAL_ADDRESS),
  ("AsmTransferControl",  EFI_PHYSICAL_ADDRESS),
  ("Idtr",                IA32_DESCRIPTOR)
  ]

gEfiAcpiS3ContextGuid         = \
  EFI_GUID (0xef98d3a, 0x3e33, 0x497a, (0xa4, 0x1, 0x77, 0xbe, 0x3e, 0xb7, 0x4f, 0x38))

gEfiAcpiVariableGuid         = \
  EFI_GUID (0xAF9FFD67, 0xEC10, 0x488A, (0x9D, 0xFC, 0x6C, 0xBF, 0x5E, 0xE2, 0x2C, 0x2E ))

