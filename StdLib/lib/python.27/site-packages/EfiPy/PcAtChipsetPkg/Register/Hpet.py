#
# Hpet.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Hpet.py is free software: you can redistribute it and/or
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

HPET_GENERAL_CAPABILITIES_ID_OFFSET   = 0x000
HPET_GENERAL_CONFIGURATION_OFFSET     = 0x010
HPET_GENERAL_INTERRUPT_STATUS_OFFSET  = 0x020

HPET_MAIN_COUNTER_OFFSET              = 0x0F0
HPET_TIMER_CONFIGURATION_OFFSET       = 0x100
HPET_TIMER_COMPARATOR_OFFSET          = 0x108
HPET_TIMER_MSI_ROUTE_OFFSET           = 0x110

HPET_TIMER_STRIDE         = 0x20

class HPET_GENERAL_CAPABILITIES_ID_REGISTER_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("Revision",            UINT32, 8),
    ("NumberOfTimers",      UINT32, 5),
    ("CounterSize",         UINT32, 1),
    ("Reserved0",           UINT32, 1),
    ("LegacyRoute",         UINT32, 1),
    ("VendorId",            UINT32, 16),
    ("CounterClockPeriod",  UINT32, 32)
  ]
  
class HPET_GENERAL_CAPABILITIES_ID_REGISTER (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   HPET_GENERAL_CAPABILITIES_ID_REGISTER_Bits),
    ("Uint64", UINT64)
  ]

class HPET_GENERAL_CONFIGURATION_REGISTER_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("MainCounterEnable", UINT32, 1),
    ("LegacyRouteEnable", UINT32, 1),
    ("Reserved0",         UINT32, 30),
    ("Reserved1",         UINT32, 32)
  ]
  
class HPET_GENERAL_CONFIGURATION_REGISTER (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   HPET_GENERAL_CONFIGURATION_REGISTER_Bits),
    ("Uint64", UINT64)
  ]

class HPET_TIMER_CONFIGURATION_REGISTER_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("Reserved0",                   UINT32, 1),
    ("LevelTriggeredInterrupt",     UINT32, 1),
    ("InterruptEnable",             UINT32, 1),
    ("PeriodicInterruptEnable",     UINT32, 1),
    ("PeriodicInterruptCapablity",  UINT32, 1),
    ("CounterSizeCapablity",        UINT32, 1),
    ("ValueSetEnable",              UINT32, 1),
    ("Reserved1",                   UINT32, 1),
    ("CounterSizeEnable",           UINT32, 1),
    ("InterruptRoute",              UINT32, 5),
    ("MsiInterruptEnable",          UINT32, 1),
    ("MsiInterruptCapablity",       UINT32, 1),
    ("Reserved2",                   UINT32, 16),
    ("InterruptRouteCapability",    UINT32)
  ]
  
class HPET_TIMER_CONFIGURATION_REGISTER (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   HPET_TIMER_CONFIGURATION_REGISTER_Bits),
    ("Uint64", UINT64)
  ]

class HPET_TIMER_MSI_ROUTE_REGISTER_Bits (Structure):
  _pack_ = 1
  _fields_ = [
    ("Value",   UINT32, 32),
    ("Address", UINT32, 32)
  ]
  
class HPET_TIMER_MSI_ROUTE_REGISTER (Union):
  _pack_ = 1
  _fields_ = [
    ("Bits",   HPET_TIMER_MSI_ROUTE_REGISTER_Bits),
    ("Uint64", UINT64)
  ]

