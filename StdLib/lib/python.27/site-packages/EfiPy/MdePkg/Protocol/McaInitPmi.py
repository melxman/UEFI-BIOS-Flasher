#
# McaInitPmi.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# McaInitPmi.py is free software: you can redistribute it and/or
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

gEfiSalMcaInitPmiProtocolGuid = \
  EFI_GUID (0xb60dc6e8, 0x3b6f, 0x11d5, (0xaf, 0x9, 0x0, 0xa0, 0xc9, 0x44, 0xa0, 0x5b))

class EFI_SAL_MCA_INIT_PMI_PROTOCOL (Structure):
  pass

class SAL_MCA_COUNT_STRUCTURE (Structure):
  _pack_   = 1
  _fields_ = [
    ("First",           UINT64, 1),
    ("Last",            UINT64, 1),
    ("EntryCount",      UINT64, 16),
    ("DispatchedCount", UINT64, 16),
    ("Reserved",        UINT64, 30)
  ]

EFI_SAL_MCA_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  PVOID,                            # IN  *ModuleGlobal,
  UINT64,                           # IN  ProcessorStateParameters,
  EFI_PHYSICAL_ADDRESS,             # IN  MinstateBase,
  UINT64,                           # IN  RendezvouseStateInformation,
  UINT64,                           # IN  CpuIndex,
  POINTER(SAL_MCA_COUNT_STRUCTURE), # IN  *McaCountStructure,
  POINTER(BOOLEAN)                  # OUT *CorrectedMachineCheck
  )

EFI_SAL_INIT_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  PVOID,                            # IN  *ModuleGlobal,
  UINT64,                           # IN  ProcessorStateParameters,
  EFI_PHYSICAL_ADDRESS,             # IN  MinstateBase,
  BOOLEAN,                          # IN  McaInProgress,
  UINT64,                           # IN  CpuIndex,
  POINTER(SAL_MCA_COUNT_STRUCTURE), # IN  *McaCountStructure,
  POINTER(BOOLEAN)                  # OUT *DumpSwitchPressed
  )

EFI_SAL_PMI_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  PVOID,                            # IN  *ModuleGlobal,
  UINT64,                           # IN  CpuIndex,
  UINT64                            # IN  PmiVector
  )

EFI_SAL_REGISTER_MCA_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SAL_MCA_INIT_PMI_PROTOCOL), # IN  *This,
  EFI_SAL_MCA_HANDLER,                    # IN  McaHandler,
  PVOID,                                  # IN  *ModuleGlobal,
  BOOLEAN,                                # IN  MakeFirst,
  BOOLEAN                                 # IN  MakeLast
  )

EFI_SAL_REGISTER_INIT_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SAL_MCA_INIT_PMI_PROTOCOL), # IN  *This,
  EFI_SAL_INIT_HANDLER,                   # IN  InitHandler,
  PVOID,                                  # IN  *ModuleGlobal,
  BOOLEAN,                                # IN  MakeFirst,
  BOOLEAN                                 # IN  MakeLast
  )

EFI_SAL_REGISTER_PMI_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SAL_MCA_INIT_PMI_PROTOCOL), # IN  *This,
  EFI_SAL_PMI_HANDLER,                    # IN  PmiHandler,
  PVOID,                                  # IN  *ModuleGlobal,
  BOOLEAN,                                # IN  MakeFirst,
  BOOLEAN                                 # IN  MakeLast
  )

EFI_SAL_MCA_INIT_PMI_PROTOCOL._fields_ = [
    ("RegisterMcaHandler",  EFI_SAL_REGISTER_MCA_HANDLER),
    ("RegisterInitHandler", EFI_SAL_REGISTER_INIT_HANDLER),
    ("RegisterPmiHandler",  EFI_SAL_REGISTER_PMI_HANDLER),
    ("McaInProgress",       BOOLEAN),
    ("InitInProgress",      BOOLEAN),
    ("PmiInProgress",       BOOLEAN)
  ]

