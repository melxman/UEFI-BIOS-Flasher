#!/usr/bin/python

#
# EfiPyCmdGetMtc.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdGetMtc.py is free software: you can redistribute it and/or modify
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

class EFIPY_CMD_GET_MTC (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Gets the MTC from BootServices and displays it.'''

  name     = u"getmtc"

  #
  # Shell version working function
  #
  def Run (self):

    Count = EfiPy.UINT64 ()

    Status = EfiPy.gBS.GetNextMonotonicCount (EfiPy.byref (Count))
    if EfiPy.RETURN_ERROR(Status):
      return 0

    self.StdOut.printf("%016X\r\n" % Count.value)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_GET_MTC.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_GET_MTC(CmdSet)

  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
