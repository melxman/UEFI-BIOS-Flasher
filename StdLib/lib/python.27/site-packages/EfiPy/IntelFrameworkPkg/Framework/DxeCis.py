#
# DxeCis.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# DxeCis.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.StatusCode import EFI_REPORT_STATUS_CODE
FRAMEWORK_EFI_AP_PROCEDURE = CFUNCTYPE (
  VOID,
  PVOID   # IN *Buffer
  )

class FRAMEWORK_EFI_RUNTIME_SERVICES (Structure):
  _fields_ = [
  ("Hdr",                       EFI_TABLE_HEADER),
  ("GetTime",                   EFI_GET_TIME),
  ("SetTime",                   EFI_SET_TIME),
  ("GetWakeupTime",             EFI_GET_WAKEUP_TIME),
  ("SetWakeupTime",             EFI_SET_WAKEUP_TIME),
  ("SetVirtualAddressMap",      EFI_SET_VIRTUAL_ADDRESS_MAP),
  ("ConvertPointer",            EFI_CONVERT_POINTER),
  ("GetVariable",               EFI_GET_VARIABLE),
  ("GetNextVariableName",       EFI_GET_NEXT_VARIABLE_NAME),
  ("SetVariable",               EFI_SET_VARIABLE),
  ("GetNextHighMonotonicCount", EFI_GET_NEXT_HIGH_MONO_COUNT),
  ("ResetSystem",               EFI_RESET_SYSTEM),
  ("ReportStatusCode",          EFI_REPORT_STATUS_CODE)
  ]

class FRAMEWORK_EFI_BOOT_SERVICES (Structure):
  _fields_ = [
  ("Hdr",                                   EFI_TABLE_HEADER),
  ("RaiseTPL",                              EFI_RAISE_TPL),
  ("RestoreTPL",                            EFI_RESTORE_TPL),
  ("AllocatePages",                         EFI_ALLOCATE_PAGES),
  ("FreePages",                             EFI_FREE_PAGES),
  ("GetMemoryMap",                          EFI_GET_MEMORY_MAP),
  ("AllocatePool",                          EFI_ALLOCATE_POOL),
  ("FreePool",                              EFI_FREE_POOL),
  ("CreateEvent",                           EFI_CREATE_EVENT),
  ("SetTimer",                              EFI_SET_TIMER),
  ("WaitForEvent",                          EFI_WAIT_FOR_EVENT),
  ("SignalEvent",                           EFI_SIGNAL_EVENT),
  ("CloseEvent",                            EFI_CLOSE_EVENT),
  ("CheckEvent",                            EFI_CHECK_EVENT),
  ("InstallProtocolInterface",              EFI_INSTALL_PROTOCOL_INTERFACE),
  ("ReinstallProtocolInterface",            EFI_REINSTALL_PROTOCOL_INTERFACE),
  ("UninstallProtocolInterface",            EFI_UNINSTALL_PROTOCOL_INTERFACE),
  ("HandleProtocol",                        EFI_HANDLE_PROTOCOL),
  ("PcHandleProtocol",                      EFI_HANDLE_PROTOCOL),
  ("RegisterProtocolNotify",                EFI_REGISTER_PROTOCOL_NOTIFY),
  ("LocateHandle",                          EFI_LOCATE_HANDLE),
  ("LocateDevicePath",                      EFI_LOCATE_DEVICE_PATH),
  ("InstallConfigurationTable",             EFI_INSTALL_CONFIGURATION_TABLE),
  ("LoadImage",                             EFI_IMAGE_LOAD),
  ("StartImage",                            EFI_IMAGE_START),
  ("Exit",                                  EFI_EXIT),
  ("UnloadImage",                           EFI_IMAGE_UNLOAD),
  ("ExitBootServices",                      EFI_EXIT_BOOT_SERVICES),
  ("GetNextMonotonicCount",                 EFI_GET_NEXT_MONOTONIC_COUNT),
  ("Stall",                                 EFI_STALL),
  ("SetWatchdogTimer",                      EFI_SET_WATCHDOG_TIMER),
  ("ConnectController",                     EFI_CONNECT_CONTROLLER),
  ("DisconnectController",                  EFI_DISCONNECT_CONTROLLER),
  ("OpenProtocol",                          EFI_OPEN_PROTOCOL),
  ("CloseProtocol",                         EFI_CLOSE_PROTOCOL),
  ("OpenProtocolInformation",               EFI_OPEN_PROTOCOL_INFORMATION),
  ("ProtocolsPerHandle",                    EFI_PROTOCOLS_PER_HANDLE),
  ("LocateHandleBuffer",                    EFI_LOCATE_HANDLE_BUFFER),
  ("LocateProtocol",                        EFI_LOCATE_PROTOCOL),
  ("InstallMultipleProtocolInterfaces",     EFI_INSTALL_MULTIPLE_PROTOCOL_INTERFACES  ),
  ("UninstallMultipleProtocolInterfaces",   EFI_UNINSTALL_MULTIPLE_PROTOCOL_INTERFACES),
  ("CalculateCrc32",                        EFI_CALCULATE_CRC32),
  ("CopyMem",                               EFI_COPY_MEM),
  ("SetMem",                                EFI_SET_MEM)
  ]

EFI_EVENT_RUNTIME_CONTEXT       = 0x20000000
EFI_EVENT_NOTIFY_SIGNAL_ALL     = 0x00000400
EFI_EVENT_SIGNAL_READY_TO_BOOT  = 0x00000203
EFI_EVENT_SIGNAL_LEGACY_BOOT    = 0x00000204

