#
# WatchdogTimer.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# WatchdogTimer.py is free software: you can redistribute it and/or
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

gEfiWatchdogTimerArchProtocolGuid = \
  EFI_GUID (0x665E3FF5, 0x46CC, 0x11d4, (0x9A, 0x38, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_WATCHDOG_TIMER_ARCH_PROTOCOL (Structure):
  pass

EFI_WATCHDOG_TIMER_NOTIFY = CFUNCTYPE (
  VOID,
  UINT64  # IN  Time
  )

EFI_WATCHDOG_TIMER_REGISTER_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WATCHDOG_TIMER_ARCH_PROTOCOL),  # IN  *This
  POINTER(EFI_WATCHDOG_TIMER_NOTIFY)          # IN  NotifyFunction
  )

EFI_WATCHDOG_TIMER_SET_TIMER_PERIOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WATCHDOG_TIMER_ARCH_PROTOCOL),  # IN  *This
  UINT64                                      # IN  TimerPeriod
  )

EFI_WATCHDOG_TIMER_GET_TIMER_PERIOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WATCHDOG_TIMER_ARCH_PROTOCOL),  # IN  *This,
  POINTER(UINT64)                             # OUT 8TimerPeriod
  )

EFI_WATCHDOG_TIMER_ARCH_PROTOCOL._fields_ = [
    ("RegisterHandler", EFI_WATCHDOG_TIMER_REGISTER_HANDLER),
    ("SetTimerPeriod",  EFI_WATCHDOG_TIMER_SET_TIMER_PERIOD),
    ("GetTimerPeriod",  EFI_WATCHDOG_TIMER_GET_TIMER_PERIOD)
  ]

