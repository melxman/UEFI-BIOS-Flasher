#!/usr/bin/python

#
# EfiPyCmdMkDir.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdMkDir.py is free software: you can redistribute it and/or modify
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
import EfiPyCmdFileOp

from   Utility import EfiPyFileOp
from   EfiPy.MdePkg.Protocol.SimpleFileSystem import    \
         EFI_FILE_PROTOCOL,                             \
         EFI_FILE_DIRECTORY,                            \
         EFI_FILE_MODE_READ,                            \
         EFI_FILE_MODE_WRITE,                           \
         EFI_FILE_MODE_CREATE

from EfiPyCmdMap import             \
                   WsIdxVol,        \
                   WsIdxAlias,      \
                   WsIdxHandle,     \
                   WsIdxDevPath,    \
                   WsIdxFont,       \
                   WsIdxBackGround, \
                   WsIdxPath

from    EfiPy.MdePkg.Guid.FileInfo  import EFI_FILE_INFO, gEfiFileInfoGuid

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_MKDIR (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Creates one or more new directories.'''

  name     = u"mkdir"

  #
  # Before Run function is called
  #
  def ParaPreBuild(self, args):

    self.Paras.update ({u"-p": ["--test", False, 0, (), []]})

  def Run (self):

    if len (self.args) == 1:
      self.StdOut.printf("Invalide parameter %s\r\n" % str(self.args))
      return 0

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    FilePaths = self.args[1:]
    for FilePath in FilePaths:
      FileSpace, ArgFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)

      if ArgFolder == None:
        self.StdOut.printf(u"Cannot create folder %s%s\r\n" % (FileSpace, FilePath))

      if self.IsFileExist (FileSpace, ArgFolder):
        self.StdOut.printf(u"Target file %s exist\r\n" % FilePath)
        continue

      RootFs, FilePath = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(FileSpace, ArgFolder))
      if RootFs == None:
        self.StdOut.printf(u"Cannot create folder %s%s\r\n" % (FileSpace, FilePath))
        continue

      # print "Try to create folder", FilePath

      NewFs = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()
      Status = RootFs.Open (
                 EfiPy.byref (RootFs),
                 EfiPy.byref (NewFs),
                 FilePath,
                 EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE | EFI_FILE_MODE_CREATE, EFI_FILE_DIRECTORY,
                 0
                 )
      RootFs.Close (EfiPy.byref (RootFs))

      if EfiPy.EFI_ERROR (Status):

        # print "-p:", self.Paras[u"-p"][EfiPyCmdBase.ParaIdxSet]
        if self.Paras[u"-p"][EfiPyCmdBase.ParaIdxSet] == False:

          self.StdOut.printf(u"Cannot create folder %s%s\r\n" % (FileSpace, FilePath))

        else:

          #
          # TO-DO for recursive create folder
          #
          self.StdOut.printf(u"TO-DO for recursive create folder %s%s\r\n" % (FileSpace, FilePath))

        continue

      # TargetFs = EFI_FILE_PROTOCOL (NewHandle)
      # TargetFs.Close()
      NewFs[0].Close (NewFs)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_MKDIR.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet     = {}
      self.WS         = {}
      self.WorkFolder = u"EFI"
      self.WorkSpace  = None

  CmdSet  = CMD_SET ()

  #
  # Establish Volume Map database
  #

  from EfiPyCmdMap  import EFIPY_CMD_MAP
  EfiPyCmdMap = EFIPY_CMD_MAP (CmdSet)
  ret = EfiPyCmdMap.Run()

  # for WorkSpace in EfiPyCmdMap.WS:
  #   print WorkSpace, ":", EfiPyCmdMap.WS[WorkSpace]

  CmdSet.WorkSpace = EfiPyCmdMap.WS[u"FS0:"]

  EfiPyCmdObj = EFIPY_CMD_MKDIR (CmdSet)
  EfiPyCmdObj.ParaPreBuild (Args)

  print

  Para    = EfiPyCmdObj.name + " fs1:\EFI\BOOT\ABCD"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " \EFI\BOOT"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " fs0:\EFI\BOOT\ABCD"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " \EFI\BOOT\BootX64.efi"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " ABCD"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " -p fs0:\EFI\BOOT\AA\BB\CC"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  print

  import sys
  sys.exit(ret)
