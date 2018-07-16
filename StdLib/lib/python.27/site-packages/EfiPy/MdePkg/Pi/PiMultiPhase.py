#
# PiMultiPhase.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiMultiPhase.py is free software: you can redistribute it and/or
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

def DXE_ERROR(StatusCode):
  return MAX_BIT | (MAX_BIT >> 2) | StatusCode

EFI_REQUEST_UNLOAD_IMAGE  = DXE_ERROR (1)
EFI_NOT_AVAILABLE_YET     = DXE_ERROR (2)
def PI_ENCODE_WARNING(a):
  return (MAX_BIT >> 2) | a

def PI_ENCODE_ERROR(a):
  return MAX_BIT | (MAX_BIT >> 2) | a

EFI_INTERRUPT_PENDING               = PI_ENCODE_ERROR (0)
EFI_WARN_INTERRUPT_SOURCE_PENDING   = PI_ENCODE_WARNING (0)
EFI_WARN_INTERRUPT_SOURCE_QUIESCED  = PI_ENCODE_WARNING (1)

EFI_AUTH_STATUS_PLATFORM_OVERRIDE   = 0x01
EFI_AUTH_STATUS_IMAGE_SIGNED        = 0x02
EFI_AUTH_STATUS_NOT_TESTED          = 0x04
EFI_AUTH_STATUS_TEST_FAILED         = 0x08
EFI_AUTH_STATUS_ALL                 = 0x0f

EFI_SMRAM_OPEN                  = 0x00000001
EFI_SMRAM_CLOSED                = 0x00000002
EFI_SMRAM_LOCKED                = 0x00000004
EFI_CACHEABLE                   = 0x00000008
EFI_ALLOCATED                   = 0x00000010
EFI_NEEDS_TESTING               = 0x00000020
EFI_NEEDS_ECC_INITIALIZATION    = 0x00000040

class EFI_SMRAM_DESCRIPTOR (Structure):
  _fields_ = [
    ("PhysicalStart", EFI_PHYSICAL_ADDRESS),
    ("CpuStart",      EFI_PHYSICAL_ADDRESS),  
    ("PhysicalSize",  UINT64),
    ("RegionState",   UINT64)
  ]

EFI_PCD_TYPE_8    = 0
EFI_PCD_TYPE_16   = 1
EFI_PCD_TYPE_32   = 2
EFI_PCD_TYPE_64   = 3
EFI_PCD_TYPE_BOOL = 4
EFI_PCD_TYPE_PTR  = 5
EFI_PCD_TYPE      = ENUM

class EFI_PCD_INFO (Structure):
  _fields_ = [
    ("PcdType", EFI_PCD_TYPE),
    ("PcdSize", UINTN),
    ("PcdName", PCHAR8)
  ]

EFI_AP_PROCEDURE = CFUNCTYPE (
  VOID,
  PVOID # IN  OUT *Buffer
  )

