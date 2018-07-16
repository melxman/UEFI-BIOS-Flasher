#!/usr/bin/python

#
# DmpStore.py
#
# Copyright (C) 2015 - 2018 efipy.core@gmail.com All rights reserved.
#
# DmpStore.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from EfiPy                      import EFI_GUID
from EfiPyLib.EfiPyVariableDump import DmpVariable, DumpAllVariable

if __name__ == '__main__':

  DumpAllVariable ()

  print "================================================================="
  name = u"BootOrder"
  # guid = EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, ( 0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C ))
  from EfiPy.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid as guid
  DmpVariable (name, guid)