#!/usr/bin/python

#
# EfiPyCmdBase.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdBase.py is free software: you can redistribute it and/or modify
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

# import EfiPy

ParaIdxAlias  = 0
ParaIdxSet    = 1
ParaIdxNum    = 2
ParaIdxType   = 3
ParaIdxValue  = 4

#
# EfiPy Command utility base class
#

class EFIPY_CMD_BASE:
  '''[TEMPLATE] EfiPy Command utility base class'''

  Paras = {
  # Key:          [ParaIdxAlias,ParaIdxSet,     ParaNum,  ParaType, ParaIdxValue]
    u"-b":        ["--break",   False,          0,        (),       []],   # Output pose per page
    u"-v":        ["--verbose", False,          0,        (),       []],   # Verbose output
  # u"-t":        ["--test",    False,          2,        (),       []],   # Parameter testing
    u"-?":        ["--help",    False,          0,        (),       []]    # Help string
  }

  name      = u"EfiPy Command Base Class"

  def __init__ (self, Shell):

    self.Shell   = Shell
    self.args    = []
    self.Shell.CmdSet.update ({self.__class__.name: self})

    self.StdIn  = Shell.StdIn
    self.StdOut = Shell.StdOut
    self.StdErr = Shell.StdErr

  #
  # EfiPy Command base utility output string
  #
  def __str__ (self):

    return self.output

  #
  # Before Run function is called
  #
  def ParaPreBuild(self, args):

    pass

  #
  # filter shell standard command parameter
  #
  def ParaBuild(self, args):

    if type (args) is not list:
       return args

    import copy

    TempArg = copy.copy(args)

    for key in args:

      if key in self.Paras.keys():

        #
        # processing command parameters with "-" or "--" leading
        #

        # print "==", key, TempArg.index(key)

        self.Paras[key][ParaIdxSet] = True

        for item in range(self.Paras[key][ParaIdxNum]):

          # print key, item, TempArg.index(key), TempArg

          self.Paras[key][ParaIdxValue].append(TempArg[TempArg.index(key) + 1])
          del TempArg[TempArg.index(key) + 1]

        TempArg.remove(key)

      else:

        #
        # processing command parameters without special leading
        #

        pass

    self.args = TempArg

    # self.StdOut.OutBreakEnable = self.Paras[u"-b"][ParaIdxSet]
    self.StdOut.ConOutBreakSet(self.Paras[u"-b"][ParaIdxSet])

    return TempArg

  #
  # Get parameter from list to command specific function
  #
  def ParaGet(self):

    pass

  #
  # EfiPy Command base utility working function
  #
  def Run (self):

    pass

  #
  # EfiPy Command base utility working function
  #
  def PostRun (self):

    for item in self.Paras :
      self.Paras[item][ParaIdxSet]    = False
      self.Paras[item][ParaIdxValue]  = []

    self.StdOut.ConOutModeRestore()

    self.args = []

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

  EfiPyCmdObj = EFIPY_CMD_BASE(CmdSet)

  EfiPyCmdObj.Paras.update ({u"-t": ["--test", False, 2, (), []]})

  print "Help: ", EfiPyCmdObj.__doc__
  print

  args = "--help -b -r -t sda sdf fd".split()

  print "Original Parameters:", args
  print

  EfiPyCmdObj.ParaPreBuild (args)

  args = EfiPyCmdObj.ParaBuild (args)

  for item in EfiPyCmdObj.Paras :
    print item, ":", EfiPyCmdObj.Paras[item]
  print
  print "Processed Parameters:", args
  print

  EfiPyCmdObj.Run ()

  EfiPyCmdObj.PostRun ()

  for item in EfiPyCmdObj.Paras :
    print item, ":", EfiPyCmdObj.Paras[item]
