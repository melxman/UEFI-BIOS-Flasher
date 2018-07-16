#
# FrameworkMpService.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FrameworkMpService.py is free software: you can redistribute it and/or
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

from EfiPy.IntelFrameworkPkg.Framework.DxeCis import FRAMEWORK_EFI_AP_PROCEDURE

gFrameworkEfiMpServiceProtocolGuid = \
  EFI_GUID (0xf33261e7, 0x23cb, 0x11d5, (0xbd, 0x5c, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81))

class FRAMEWORK_EFI_MP_SERVICES_PROTOCOL (Structure):
  pass

DELIVERY_MODE_FIXED           = 0x0
DELIVERY_MODE_LOWEST_PRIORITY = 0x1
DELIVERY_MODE_SMI             = 0x2
DELIVERY_MODE_REMOTE_READ     = 0x3
DELIVERY_MODE_NMI             = 0x4
DELIVERY_MODE_INIT            = 0x5
DELIVERY_MODE_SIPI            = 0x6
DELIVERY_MODE_MAX             = 0x7
EFI_MP_HEALTH_FLAGS_STATUS_HEALTHY                  = 0x0
EFI_MP_HEALTH_FLAGS_STATUS_PERFORMANCE_RESTRICTED   = 0x1
EFI_MP_HEALTH_FLAGS_STATUS_FUNCTIONALLY_RESTRICTED  = 0x2
class EFI_MP_HEALTH_FLAGS_Bits (Structure):
  _fields_ = [
    ("Status",                      UINT32, 2),
    ("Tested",                      UINT32, 1),
    ("Reserved1",                   UINT32, 13),
    ("VirtualMemoryUnavailable",    UINT32, 1),
    ("Ia32ExecutionUnavailable",    UINT32, 1),
    ("FloatingPointUnavailable",    UINT32, 1),
    ("MiscFeaturesUnavailable",     UINT32, 1),
    ("Reserved2",                   UINT32, 12)
  ]

class EFI_MP_HEALTH_FLAGS (Union):
  _fields_ = [
    ("Bits",    EFI_MP_HEALTH_FLAGS_Bits),
    ("Uint32",  UINT32)
  ]

class EFI_MP_HEALTH (Structure):
  _fields_ = [
    ("Flags",       EFI_MP_HEALTH_FLAGS),
    ("TestStatus",  UINT32)
  ]

EfiCpuAP                  = 0
EfiCpuBSP                 = 1
EfiCpuDesignationMaximum  = 2
EFI_CPU_DESIGNATION       = UINTN

class EFI_MP_PROC_CONTEXT (Structure):
  _fields_ = [
    ("ApicID",                          UINT32),
    ("Enabled",                         BOOLEAN),
    ("Designation",                     EFI_CPU_DESIGNATION),
    ("Health",                          EFI_MP_HEALTH),
    ("PackageNumber",                   UINTN),
    ("NumberOfCores",                   UINTN),
    ("NumberOfThreads",                 UINTN),
    ("ProcessorPALCompatibilityFlags",  UINT64),
    ("ProcessorTestMask",               UINT64)
  ]

EFI_MP_SERVICES_GET_GENERAL_MP_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  # IN  *This,
  POINTER(UINTN),                               # OUT *NumberOfCPUs          OPTIONAL,
  POINTER(UINTN),                               # OUT *MaximumNumberOfCPUs   OPTIONAL,
  POINTER(UINTN),                               # OUT *NumberOfEnabledCPUs   OPTIONAL,
  POINTER(UINTN),                               # OUT *RendezvousIntNumber   OPTIONAL,
  POINTER(UINTN)                                # OUT *RendezvousProcLength  OPTIONAL
  )

EFI_MP_SERVICES_GET_PROCESSOR_CONTEXT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  UINTN,                                        #   IN     ProcessorNumber,
  POINTER(UINTN),                               #   IN OUT *BufferLength,
  POINTER(EFI_MP_PROC_CONTEXT)                  #   OUT    *ProcessorContextBuffer
  )

FRAMEWORK_EFI_MP_SERVICES_STARTUP_ALL_APS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  FRAMEWORK_EFI_AP_PROCEDURE,                   #   IN  Procedure,
  BOOLEAN,                                      #   IN  SingleThread,
  EFI_EVENT,                                    #   IN  WaitEvent           OPTIONAL,
  UINTN,                                        #   IN  TimeoutInMicroSecs,  
  PVOID,                                        #   IN  *ProcArguments      OPTIONAL,
  POINTER(UINTN)                                #   OUT *FailedCPUList      OPTIONAL
  )

FRAMEWORK_EFI_MP_SERVICES_STARTUP_THIS_AP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  FRAMEWORK_EFI_AP_PROCEDURE,                   #   IN  Procedure,
  UINTN,                                        #   IN  ProcessorNumber,
  EFI_EVENT,                                    #   IN  WaitEvent           OPTIONAL,
  UINTN,                                        #   IN  TimeoutInMicroSecs,  
  PVOID,                                        #   IN  *ProcArguments      OPTIONAL,
  )

FRAMEWORK_EFI_MP_SERVICES_SWITCH_BSP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  UINTN,                                        #   IN  ProcessorNumber,
  BOOLEAN                                       #   IN  EnableOldBSP  
  )

EFI_MP_SERVICES_SEND_IPI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  UINTN,                                        #   IN  ProcessorNumber,
  UINTN,                                        #   IN  VectorNumber,
  UINTN                                         #   IN  DeliveryMode  
  )

FRAMEWORK_EFI_MP_SERVICES_ENABLEDISABLEAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  UINTN,                                        #   IN  ProcessorNumber,
  BOOLEAN,                                      #   IN NewAPState,
  POINTER(EFI_MP_HEALTH)                        #   IN *HealthState  OPTIONAL
  )

FRAMEWORK_EFI_MP_SERVICES_WHOAMI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(FRAMEWORK_EFI_MP_SERVICES_PROTOCOL),  #   IN  *This,
  POINTER(UINTN)                                #   OUT *ProcessorNumber
  )

FRAMEWORK_EFI_MP_SERVICES_PROTOCOL._fields_ = [
    ("GetGeneralMPInfo",      EFI_MP_SERVICES_GET_GENERAL_MP_INFO),
    ("GetProcessorContext",   EFI_MP_SERVICES_GET_PROCESSOR_CONTEXT),
    ("StartupAllAPs",         FRAMEWORK_EFI_MP_SERVICES_STARTUP_ALL_APS),
    ("StartupThisAP",         FRAMEWORK_EFI_MP_SERVICES_STARTUP_THIS_AP),
    ("SwitchBSP",             FRAMEWORK_EFI_MP_SERVICES_SWITCH_BSP),
    ("SendIPI",               EFI_MP_SERVICES_SEND_IPI),
    ("EnableDisableAP",       FRAMEWORK_EFI_MP_SERVICES_ENABLEDISABLEAP),
    ("WhoAmI",                FRAMEWORK_EFI_MP_SERVICES_WHOAMI)
  ]

