#!/usr/bin/python

#
# EfiPyCmdDir.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdDir.py is free software: you can redistribute it and/or modify
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
         EFI_FILE_MODE_READ,                            \
         EFI_FILE_PROTOCOL,                             \
         EFI_FILE_DIRECTORY

from EfiPyCmdMap import             \
                   WsIdxVol,        \
                   WsIdxAlias,      \
                   WsIdxHandle,     \
                   WsIdxDevPath,    \
                   WsIdxFont,       \
                   WsIdxBackGround, \
                   WsIdxPath

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_DIR (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Lists a directory\'s contents or file information.'''

  name     = u"dir"

  def OutputFile (self, fName, fInfo):

    OutString = u"%02d/%02d/%04d  %02d:%02d " % (fInfo.ModificationTime.Month,
                                                 fInfo.ModificationTime.Day,
                                                 fInfo.ModificationTime.Year,
                                                 fInfo.ModificationTime.Hour,
                                                 fInfo.ModificationTime.Minute)
    if fInfo.Attribute & EFI_FILE_DIRECTORY == EFI_FILE_DIRECTORY:
      OutString += u"<DIR>"
    else:
      OutString += u"     "

    OutString += u"%14d  %s\r\n" % (fInfo.FileSize, fName)

    self.StdOut.printf(OutString)

  def ListDir (self, TargetSpace, TargetFolder, SpaceOnly, SpaceFound):

    RootFs, FilePath = EfiPyFileOp.GetRootFsOperation (
                         self.Shell.WS, u"%s%s" %(TargetSpace, TargetFolder)
                         )
    if RootFs == None:
      self.StdOut.printf(u"File %s%s not found\r\n" % (TargetSpace, TargetFolder))
      return 0

    NewFs = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()

    Status = RootFs.Open (
               EfiPy.byref (RootFs),
               EfiPy.byref (NewFs),
               TargetFolder,
               EFI_FILE_MODE_READ,
               0
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"File %s%s not found\r\n" % (TargetSpace, TargetFolder))
      return 0

    FileFolder = self.ParseAbsPath (NewFs[0])
    self.StdOut.printf(u"Directory of: %s%s\r\n" % (TargetSpace, FileFolder))

    NewFs[0].Close (NewFs)

    FileNode = EfiPyFileOp.GetFilesInPath (RootFs, FilePath)

    for FileItem in FileNode:

      self.OutputFile (FileItem[2], FileItem[1])

  def Run (self):

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    if len (self.args[1:]) == 0:

      FileSpace, TempFolder, SpaceOnly, SpaceFound = self.ParseFolder (FileSpace)
      self.ListDir (FileSpace, FileFolder, SpaceOnly, SpaceFound)

    for FilePath in self.args[1:]:
      FileSpace, FileFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)
      self.ListDir (FileSpace, FileFolder, SpaceOnly, SpaceFound)
      self.StdOut.printf(u"\r\n")

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_DIR.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_DIR (CmdSet)

  print

  Para    = EfiPyCmdObj.name + " blk1:"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " fs1:"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " fs1:\EFI\BOOT"
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

  Para    = EfiPyCmdObj.name + " \EFI\BOOT\\"
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

  Para    = EfiPyCmdObj.name + " BOOT"
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

  Para    = EfiPyCmdObj.name + " blk2:"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " bbk:"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  import sys
  sys.exit(ret)
