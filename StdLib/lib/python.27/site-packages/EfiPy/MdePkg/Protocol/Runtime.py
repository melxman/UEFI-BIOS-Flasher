#
# Runtime.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Runtime.py is free software: you can redistribute it and/or
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

gEfiRuntimeArchProtocolGuid             = \
  EFI_GUID (0xb7dfb4e1, 0x52f, 0x449f, (0x87, 0xbe, 0x98, 0x18, 0xfc, 0x91, 0xb7, 0x33 ))

class EFI_RUNTIME_ARCH_PROTOCOL (Structure):
  pass

EFI_LIST_ENTRY  = LIST_ENTRY

class EFI_RUNTIME_IMAGE_ENTRY (Structure):
  _fields_ = [
    ("ImageBase",       PVOID),
    ("ImageSize",       UINT64),
    ("RelocationData",  PVOID),
    ("Handle",          EFI_HANDLE),
    ("Link",            EFI_LIST_ENTRY)
  ]

class EFI_RUNTIME_EVENT_ENTRY (Structure):
  _fields_ = [
    ("Type",            UINT32),
    ("NotifyTpl",       EFI_TPL),
    ("NotifyFunction",  EFI_EVENT_NOTIFY),
    ("NotifyContext",   PVOID),
    ("Event",           POINTER(EFI_EVENT)),
    ("Link",            EFI_LIST_ENTRY)
  ]

EFI_RUNTIME_ARCH_PROTOCOL._fields_ = [
    ("ImageHead",               EFI_LIST_ENTRY),
    ("EventHead",               EFI_LIST_ENTRY),
    ("MemoryDescriptorSize",    UINTN),
    ("MemoryDesciptorVersion",  UINT32),
    ("MemoryMapSize",           UINTN),
    ("MemoryMapPhysical",       POINTER(EFI_MEMORY_DESCRIPTOR)),
    ("MemoryMapVirtual",        POINTER(EFI_MEMORY_DESCRIPTOR)),
    ("VirtualMode",             BOOLEAN),
    ("AtRuntime",               BOOLEAN)
  ]

