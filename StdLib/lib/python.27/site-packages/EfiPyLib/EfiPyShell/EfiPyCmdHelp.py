#!/usr/bin/python

#
# EfiPyCmdHelp.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdHelp.py is free software: you can redistribute it and/or modify
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

import EfiPyCmdBase

#
# EfiPy Command Clear screen class
#

class EFIPY_CMD_HELP (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays the UEFI Shell command list or verbose command help.'''

  name     = u"help"

  #
  # Help command working function
  #
  def Run (self):

    self.StdOut.printf(u"Supported EfiPyShell internal command...\r\n")

    for CmdLine in sorted(self.Shell.CmdSet.keys()):
      self.StdOut.printf(CmdLine + ":\r\n")

      if self.Shell.CmdSet[CmdLine] != None:
        self.StdOut.printf("  " + self.Shell.CmdSet[CmdLine].__doc__ + "\r\n")
      else:
        self.StdOut.printf("  No Document\r\n")

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_HELP.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet = {}

  CmdSet  = CMD_SET ()

  CmdHelp = EFIPY_CMD_HELP (CmdSet)

  import EfiPyCmdCls
  CmdCls  = EfiPyCmdCls.EFIPY_CMD_CLS  (CmdSet)

  CmdHelp.Run ()

  import sys
  sys.exit(0)
