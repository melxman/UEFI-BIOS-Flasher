#!/usr/bin/python

#
# EfiPyCmdDate.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdDate.py is free software: you can redistribute it and/or modify
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

class EFIPY_CMD_DATE (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays and sets the current date for the system.'''

  name     = u"date"

  #
  # Shell version working function
  #
  def Run (self):

    # print len(self.args), self.args

    TimeCurr = EfiPy.EFI_TIME ()
    Status = EfiPy.gRT.GetTime (EfiPy.byref (TimeCurr), None)

    if Status != EfiPy.EFI_SUCCESS:
      self.StdOut.printf(u"Date operation error\r\n")
      return 0

    RetStatus = EfiPy.EFI_SUCCESS

    if    len (self.args) == 1:
      self.StdOut.printf(u"%02d/%02d/%04d\r\n" % (TimeCurr.Month, TimeCurr.Day, TimeCurr.Year))

    elif  len (self.args) == 2:

      TimePara = self.args[1].split (u"/")

      if len (TimePara) != 3:
        RetStatus = EfiPy.EFI_INVALID_PARAMETER

      else:
        TimeMonth = int (TimePara[0])
        TimeDay   = int (TimePara[1])
        TimeYear  = int (TimePara[2])

        if TimeMonth > 12 or TimeMonth < 1:
          RetStatus = EfiPy.EFI_INVALID_PARAMETER

        if TimeDay > 31 or TimeDay < 1:
          RetStatus = EfiPy.EFI_INVALID_PARAMETER

      if RetStatus == EfiPy.EFI_SUCCESS:

        TimeCurr.Month, TimeCurr.Day, TimeCurr.Year = TimeMonth, TimeDay, TimeYear
        Status = EfiPy.gRT.SetTime (EfiPy.byref (TimeCurr), None)
        RetStatus = Status

    else:
      RetStatus = EfiPy.EFI_INVALID_PARAMETER

    if RetStatus == EfiPy.EFI_INVALID_PARAMETER:
      self.StdOut.printf(u"Date inccorect input parameter. [mm/dd/yyyy]\r\n")

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_DATE.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_DATE(CmdSet)

  print

  Para    = EfiPyCmdObj.name + ""
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " 07/04/2015"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  Para    = EfiPyCmdObj.name + ""
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  import sys
  sys.exit(ret)
