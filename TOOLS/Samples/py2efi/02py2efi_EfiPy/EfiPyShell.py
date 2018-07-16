#!/usr/bin/python

#
# EfiPyShell.py
#
# Copyright (C) 2014 - 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyShell.py is free software: you can redistribute it and/or modify
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

from EfiPyLib.EfiPyShell.EfiPyShell2 import EFIPY_COMMAND_SHELL

##########################################################################
# Shell program entry
##########################################################################
if __name__ == '__main__':

  ShellCmd = EFIPY_COMMAND_SHELL()

  while 1:
  
    command  = ShellCmd.CommandGet()
  
    if command == None or len(command) == 0:
      continue

    ret = ShellCmd.run(command[0], command)
    if ret == -1:
      break

  import sys
  sys.exit(0)
