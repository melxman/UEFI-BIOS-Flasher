#
# VariableFormat.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# VariableFormat.py is free software: you can redistribute it and/or
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

gEfiVariableGuid         = \
  EFI_GUID (0xddcf3616, 0x3275, 0x4164, (0x98, 0xb6, 0xfe, 0x85, 0x70, 0x7f, 0xfe, 0x7d))

gEfiAuthenticatedVariableGuid         = \
  EFI_GUID (0xaaf32c78, 0x947b, 0x439a, (0xa1, 0x80, 0x2e, 0x14, 0x4e, 0xc3, 0x77, 0x92))

ALIGNMENT         = 1
def GET_PAD_SIZE(a):
  return 0

HEADER_ALIGNMENT  = 4

def HEADER_ALIGN(Header):
  return (Header + HEADER_ALIGNMENT - 1) & (~(HEADER_ALIGNMENT - 1))

EfiRaw      = 1
EfiValid    = 2
EfiInvalid  = 3
EfiUnknown  = 4
VARIABLE_STORE_STATUS = UINTN
VARIABLE_STORE_FORMATTED          = 0x5a
VARIABLE_STORE_HEALTHY            = 0xfe

class VARIABLE_STORE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("Signature", EFI_GUID),
  ("Size",      UINT32),
  ("Format",    UINT8),
  ("State",     UINT8),
  ("Reserved",  UINT16),
  ("Reserved1", UINT32)
  ]

VARIABLE_DATA                     = 0x55AA

VAR_IN_DELETED_TRANSITION     = 0xfe
VAR_DELETED                   = 0xfd
VAR_HEADER_VALID_ONLY         = 0x7f
VAR_ADDED                     = 0x3f

VARIABLE_ATTRIBUTE_NV_BS        = (EFI_VARIABLE_NON_VOLATILE | EFI_VARIABLE_BOOTSERVICE_ACCESS)
VARIABLE_ATTRIBUTE_BS_RT        = (EFI_VARIABLE_BOOTSERVICE_ACCESS | EFI_VARIABLE_RUNTIME_ACCESS)
VARIABLE_ATTRIBUTE_AT_AW        = (EFI_VARIABLE_TIME_BASED_AUTHENTICATED_WRITE_ACCESS | EFI_VARIABLE_AUTHENTICATED_WRITE_ACCESS)
VARIABLE_ATTRIBUTE_NV_BS_RT     = (VARIABLE_ATTRIBUTE_BS_RT | EFI_VARIABLE_NON_VOLATILE)
VARIABLE_ATTRIBUTE_NV_BS_RT_HR  = (VARIABLE_ATTRIBUTE_NV_BS_RT | EFI_VARIABLE_HARDWARE_ERROR_RECORD)
VARIABLE_ATTRIBUTE_NV_BS_RT_AT  = (VARIABLE_ATTRIBUTE_NV_BS_RT | EFI_VARIABLE_TIME_BASED_AUTHENTICATED_WRITE_ACCESS)
VARIABLE_ATTRIBUTE_NV_BS_RT_AW  = (VARIABLE_ATTRIBUTE_NV_BS_RT | EFI_VARIABLE_AUTHENTICATED_WRITE_ACCESS)
VARIABLE_ATTRIBUTE_NV_BS_RT_HR_AT_AW    = (VARIABLE_ATTRIBUTE_NV_BS_RT_HR | VARIABLE_ATTRIBUTE_AT_AW)

class VARIABLE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("StartId",     UINT16),
  ("State",       UINT8),
  ("Reserved",    UINT8),
  ("Attributes",  UINT32),
  ("NameSize",    UINT32),
  ("DataSize",    UINT32),
  ("VendorGuid",  EFI_GUID)
  ]

class AUTHENTICATED_VARIABLE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("StartId",         UINT16),
  ("State",           UINT8),
  ("Reserved",        UINT8),
  ("Attributes",      UINT32),
  ("MonotonicCount",  UINT64),
  ("TimeStamp",       EFI_TIME),
  ("PubKeyIndex",     UINT32),
  ("NameSize",        UINT32),
  ("DataSize",        UINT32),
  ("VendorGuid",      EFI_GUID)
  ]

class VARIABLE_ENTRY_CONSISTENCY (Structure):
  _pack_   = 1
  _fields_ = [
  ("Guid",         POINTER(EFI_GUID)),
  ("Name",         POINTER(CHAR16)),
  ("VariableSize", UINT8)
  ]

class VARIABLE_INFO_ENTRY (Structure):
  pass

VARIABLE_INFO_ENTRY._fields_ = [
  ("Next",        POINTER(VARIABLE_INFO_ENTRY)),
  ("VendorGuid",  EFI_GUID),
  ("Name",        POINTER(CHAR16)),
  ("Attributes",  UINT32),
  ("ReadCount",   UINT32),
  ("WriteCount",  UINT32),
  ("DeleteCount", UINT32),
  ("CacheCount",  UINT32),
  ("Volatile",    BOOLEAN)
  ]

