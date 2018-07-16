#!/usr/bin/python

#
# EfiPyCmdTouch.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdTouch.py is free software: you can redistribute it and/or modify
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
         EFI_FILE_DIRECTORY,                            \
         EFI_FILE_ARCHIVE,                            \
         EFI_FILE_SYSTEM,                            \
         EFI_FILE_HIDDEN,                            \
         EFI_FILE_READ_ONLY,                        \
         EFI_FILE_MODE_WRITE,                       \
         EFI_FILE_MODE_CREATE

from EfiPyCmdMap import             \
                   WsIdxVol,        \
                   WsIdxAlias,      \
                   WsIdxHandle,     \
                   WsIdxDevPath,    \
                   WsIdxFont,       \
                   WsIdxBackGround, \
                   WsIdxPath

from  EfiPy.MdePkg.Guid.FileInfo  import EFI_FILE_INFO, gEfiFileInfoGuid
from  Utility.EfiPyUtility        import EfiPyHexDump

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_TOUCH (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Updates the filename timestamp with the current system date and time.'''

  name     = u"touch"

  def ListTouch (self, FileSpace, FileFolder, EfiPyTime):

    if self.Shell.WS[FileSpace.upper()][WsIdxPath] == u"":
      self.StdOut.printf(u"%s is not valide volume\r\n" % FileSpace)
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
               EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE,
               0
               )

    if Status == EfiPy.EFI_NOT_FOUND:
      Status = RootFs.Open (
                 EfiPy.byref (RootFs),
                 EfiPy.byref (NewFs),
                 FileFolder,
                 EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE | EFI_FILE_MODE_CREATE,
                 0
                 )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"File %s%s cannot be opened 0x%016X\r\n" % (FileSpace, FileFolder, Status))
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
      return 0

    TmpBuffer = bytearray (BufferSize.value)
    fInfo     = EFI_FILE_INFO.from_buffer (TmpBuffer)
    Status = NewFs[0].GetInfo (
                              NewFs,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              EfiPy.byref (fInfo)
                              )

    if Status != EfiPy.EFI_SUCCESS:
      NewFs[0].Close (NewFs)
      return 0

    fInfo.LastAccessTime    = EfiPyTime
    fInfo.ModificationTime  = EfiPyTime

    Status = NewFs[0].SetInfo (
               NewFs,
               gEfiFileInfoGuid,
               BufferSize,
               EfiPy.byref (fInfo)
               )

    self.StdOut.printf(u"Touch %s%s, Status: 0x%016X\r\n" % (FileSpace, FileFolder, Status))

    NewFs[0].Close (NewFs)

    return 0

  def Run (self):

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    EfiPyTime = EfiPy.EFI_TIME ()
    CapTime   = EfiPy.EFI_TIME_CAPABILITIES ()
    Status = EfiPy.gRT.GetTime (EfiPy.byref (EfiPyTime), EfiPy.byref (CapTime))

    if EfiPy.EFI_ERROR (Status):
      return

    # EfiPyTime = EFI_TIME (RetTime)

    for FilePath in self.args[1:]:

      FileSpace, FileFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)

      if SpaceFound == False:
        self.StdOut.printf(u"%s is not valide volume\r\n" % FileSpace)
        continue

      if SpaceOnly == True:
        self.StdOut.printf(u"%s Only volume identified\r\n" % FileSpace)
        continue

      self.ListTouch (FileSpace, FileFolder, EfiPyTime)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_TOUCH.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_TOUCH (CmdSet)

  print

  Para    = EfiPyCmdObj.name + " \\aa.txt"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " fs1:\\bb.txt"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
