#
# GenericMemoryTest.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# GenericMemoryTest.py is free software: you can redistribute it and/or
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

gEfiGenericMemTestProtocolGuid = \
  EFI_GUID (0xa770c357, 0xb693, 0x4e6d, (0xa6, 0xcf, 0xd2, 0x1c, 0x72, 0x8e, 0x55, 0xb))

class EFI_GENERIC_MEMORY_TEST_PROTOCOL (Structure):
  pass

IGNORE                    = 0
QUICK                     = 1
SPARSE                    = 2
EXTENSIVE                 = 3
MAXLEVEL                  = 4
EXTENDMEM_COVERAGE_LEVEL  = UINTN

EFI_MEMORY_TEST_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GENERIC_MEMORY_TEST_PROTOCOL),  # IN  *This,
  EXTENDMEM_COVERAGE_LEVEL,                   # IN  Level,
  BOOLEAN                                     # OUT *RequireSoftECCInit
  )

EFI_PERFORM_MEMORY_TEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GENERIC_MEMORY_TEST_PROTOCOL),  # IN  *This,
  POINTER(UINT64),                            # OUT *TestedMemorySize,
  POINTER(UINT64),                            # OUT *TotalMemorySize,
  POINTER(BOOLEAN),                           # OUT *ErrorOut,
  BOOLEAN                                     # IN  IfTestAbort
  )

EFI_MEMORY_TEST_FINISHED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GENERIC_MEMORY_TEST_PROTOCOL)   # IN  *This,
  )

EFI_MEMORY_TEST_COMPATIBLE_RANGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GENERIC_MEMORY_TEST_PROTOCOL),  # IN  *This,
  EFI_PHYSICAL_ADDRESS,                       # IN  StartAddress,
  UINT64                                      # IN  Length
  )

EFI_GENERIC_MEMORY_TEST_PROTOCOL._fields_ = [
  ("MemoryTestInit",      EFI_MEMORY_TEST_INIT),
  ("PerformMemoryTest",   EFI_PERFORM_MEMORY_TEST),
  ("Finished",            EFI_MEMORY_TEST_FINISHED),
  ("CompatibleRangeTest", EFI_MEMORY_TEST_COMPATIBLE_RANGE)
  ]

