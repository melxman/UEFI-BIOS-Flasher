#!/usr/bin/python

#
# EfiPyCmdStall.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdStall.py is free software: you can redistribute it and/or modify
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

import EfiPy
import EfiPyCmdBase

#
# EfiPy Command shell version class
#

class EFIPY_CMD_STALL (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Stalls the operation for a specified number of microseconds.'''

  name     = u"stall"

  #
  # Shell version working function
  #
  def Run (self):

    if    len (self.args) != 2:

      self.StdOut.printf(u"Stall inccorect input parameter. STALL microsecond\r\n")

      return

    Stall = int (self.args[1]) * 1000

    OriginalTpl = EfiPy.gBS.RaiseTPL (EfiPy.TPL_HIGH_LEVEL)

    Status  = EfiPy.gBS.Stall (Stall)

    EfiPy.gBS.RestoreTPL (OriginalTpl)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_STALL.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet = {}

  CmdSet  = CMD_SET ()

  EfiPyCmdObj = EFIPY_CMD_STALL(CmdSet)

  print

  Para    = EfiPyCmdObj.name + " 300"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
