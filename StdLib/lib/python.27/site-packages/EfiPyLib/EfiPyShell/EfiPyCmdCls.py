#!/usr/bin/python

#
# EfiPyCmdCls.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdCls.py is free software: you can redistribute it and/or modify
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

class EFIPY_CMD_CLS (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Clears standard output and optionally changes background color.'''

  name     = u"cls"

  #
  # Clear screen working function
  #
  def Run (self):

    self.StdOut.ClearScreen()

    return 0

if __name__ == '__main__':

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.CmdSet = {}

  CmdSet = CMD_SET ()

  EfiPyCmdObj = EFIPY_CMD_CLS(CmdSet)

  Para    = EfiPyCmdObj.name + ""
  Args    = Para.split()

  print "Original Parameters:", Args
  print

  Args = EfiPyCmdObj.ParaBuild (Args)

  EfiPyCmdObj.Run ()

  EfiPyCmdObj.PostRun ()

  for item in EfiPyCmdObj.Paras :
    print item, ":", EfiPyCmdObj.Paras[item]


  import sys
  sys.exit(0)
