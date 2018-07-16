#
# BootScriptExecutorVariable.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# BootScriptExecutorVariable.py is free software: you can redistribute it and/or
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

class BOOT_SCRIPT_EXECUTOR_VARIABLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("BootScriptExecutorEntrypoint",  EFI_PHYSICAL_ADDRESS)
  ]

BOOT_SCRIPT_EXECUTOR_VARIABLE_NAME  = u"BootScriptExecutorVariable"
gEfiBootScriptExecutorVariableGuid         = \
  EFI_GUID (0x3079818c, 0x46d4, 0x4a73, (0xae, 0xf3, 0xe3, 0xe4, 0x6c, 0xf1, 0xee, 0xdb))

gEfiBootScriptExecutorContextGuid         = \
  EFI_GUID (0x79cb58c4, 0xac51, 0x442f, (0xaf, 0xd7, 0x98, 0xe4, 0x7d, 0x2e, 0x99, 0x8))

