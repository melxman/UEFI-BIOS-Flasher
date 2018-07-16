#!/usr/bin/python

#
# EfiPyCmdCd.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdCd.py is free software: you can redistribute it and/or modify
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

from    EfiPy.MdePkg.Guid.FileInfo  import EFI_FILE_INFO, gEfiFileInfoGuid

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_CD (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Displays or changes the current directory.'''

  name     = u"cd"

  def ChangingDir (self, FileSpace, FileFolder, SpaceOnly, SpaceFound):

    if SpaceFound == False:
      self.StdOut.printf(u"%s is not valide volume\r\n" % FileSpace)
      return

    if self.Shell.WS[FileSpace.upper()][WsIdxPath] == u"":
      self.StdOut.printf(u"%s is not valide volume\r\n" % FileSpace)
      return

    if SpaceOnly == True:
      self.StdOut.printf(u"Current volume %s working directory: %s\r\n" % (FileSpace, self.Shell.WS[FileSpace.upper()][WsIdxPath]))
      return

    RootFs, FilePath = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(FileSpace, FileFolder))
    if RootFs == None:
      self.StdOut.printf(u"Volume %s cannot be opened\r\n" % FileSpace)
      return 0

    NewFs = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()
    Status = RootFs.Open (
               EfiPy.byref (RootFs),
               EfiPy.byref (NewFs),
               FileFolder,
               EFI_FILE_MODE_READ,
               0
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"%s%s is not valid directory\r\n" % (FileSpace, FileFolder))
      return 0

    BufferSize = EfiPy.UINTN (0)
    Status = NewFs[0].GetInfo (
                        NewFs,
                        gEfiFileInfoGuid,
                        EfiPy.byref (BufferSize),
                        None
                        )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      NewFs[0].Close (NewFs)
      return

    TmpBuffer = bytearray (BufferSize.value)
    fInfo      = EFI_FILE_INFO.from_buffer (TmpBuffer)

    Status = NewFs[0].GetInfo (
                        NewFs,
                        gEfiFileInfoGuid,
                        EfiPy.byref (BufferSize),
                        EfiPy.byref (fInfo)
                        )

    if Status != EfiPy.EFI_SUCCESS:
      return

    if fInfo.Attribute & EFI_FILE_DIRECTORY == EFI_FILE_DIRECTORY:

      FileFolder = self.ParseAbsPath (NewFs[0])

      self.Shell.WS[FileSpace.upper()][WsIdxPath] = FileFolder
      self.StdOut.printf(u"Change volume %s working directory: %s\r\n" % (FileSpace, FileFolder))

    else:

      self.StdOut.printf(u"%s%s is not valid directory\r\n" % (FileSpace, FileFolder))

    NewFs[0].Close (NewFs)

  def Run (self):

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    if len (self.args[1:]) == 0:
      FileSpace, TempFolder, SpaceOnly, SpaceFound = self.ParseFolder (FileSpace)
      self.ChangingDir (FileSpace, FileFolder, SpaceOnly, SpaceFound)
      return 0

    for FilePath in self.args[1:]:
      FileSpace, FileFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)
      self.ChangingDir (FileSpace, FileFolder, SpaceOnly, SpaceFound)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_CD.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_CD (CmdSet)

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

  Para    = EfiPyCmdObj.name + " fs0:\EFI\BOOT\\"
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
