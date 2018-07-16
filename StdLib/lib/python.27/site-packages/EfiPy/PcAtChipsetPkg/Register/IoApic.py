#
# IoApic.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# IoApic.py is free software: you can redistribute it and/or
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

IOAPIC_INDEX_OFFSET  = 0x00
IOAPIC_DATA_OFFSET   = 0x10

IO_APIC_IDENTIFICATION_REGISTER_INDEX  = 0x00
IO_APIC_VERSION_REGISTER_INDEX         = 0x01
IO_APIC_REDIRECTION_TABLE_ENTRY_INDEX  = 0x10

IO_APIC_DELIVERY_MODE_FIXED            = 0
IO_APIC_DELIVERY_MODE_LOWEST_PRIORITY  = 1
IO_APIC_DELIVERY_MODE_SMI              = 2
IO_APIC_DELIVERY_MODE_NMI              = 4
IO_APIC_DELIVERY_MODE_INIT             = 5
IO_APIC_DELIVERY_MODE_EXTINT           = 7

class IO_APIC_IDENTIFICATION_REGISTER_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("Reserved0",       UINT32, 24),
    ("Identification",  UINT32, 4),
    ("Reserved1",       UINT32, 4)
  ]
  
class IO_APIC_IDENTIFICATION_REGISTER (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   IO_APIC_IDENTIFICATION_REGISTER_Bits),
    ("Uint32", UINT32)
  ]

class IO_APIC_VERSION_REGISTER_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("Version",                   UINT32, 8),
    ("Reserved0",                 UINT32, 8),
    ("MaximumRedirectionEntry",   UINT32, 8),
    ("Reserved1",                 UINT32, 8)
  ]
  
class IO_APIC_VERSION_REGISTER (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   IO_APIC_VERSION_REGISTER_Bits),
    ("Uint32", UINT32)
  ]

class IO_APIC_REDIRECTION_TABLE_ENTRY_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("Vector",            UINT32, 8),
    ("DeliveryMode",      UINT32, 3),
    ("DestinationMode",   UINT32, 1),
    ("DeliveryStatus",    UINT32, 1),
    ("Polarity",          UINT32, 1),
    ("RemoteIRR",         UINT32, 1),
    ("TriggerMode",       UINT32, 1),
    ("Mask",              UINT32, 1),
    ("Reserved0",         UINT32, 15),
    ("Reserved1",         UINT32, 24),
    ("DestinationID",     UINT32, 8),
  ]

class IO_APIC_REDIRECTION_TABLE_ENTRY_Uint32 (Structure):
  _pack_ = 1
  _fields_ = [
    ("Low",   UINT32),
    ("High",  UINT32)
  ]
  
class IO_APIC_REDIRECTION_TABLE_ENTRY (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   IO_APIC_REDIRECTION_TABLE_ENTRY_Bits),
    ("Uint32", IO_APIC_REDIRECTION_TABLE_ENTRY_Uint32),
    ("Uint64", UINT64)
  ]

