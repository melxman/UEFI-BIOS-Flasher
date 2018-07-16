#!/usr/bin/python

#
# EfiPyCmdFileOp.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdFileOp.py is free software: you can redistribute it and/or modify
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

import  EfiPyCmdBase
from    Utility import EfiPyFileOp
from    EfiPy.MdePkg.Guid.FileInfo  import EFI_FILE_INFO, gEfiFileInfoGuid

from    EfiPy.MdePkg.Protocol.SimpleFileSystem import   \
          EFI_FILE_MODE_READ,                           \
          EFI_FILE_PROTOCOL,                            \
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

class EFIPY_CMD_FILE_OP (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays or changes the current directory.'''

  name     = u"fileop"

  def ParseAbsPath (self, FileHandle):

    AbsList = []

    Status = EfiPy.EFI_SUCCESS

    while Status == EfiPy.EFI_SUCCESS:

      BufferSize = EfiPy.UINTN (0)
      Status = FileHandle.GetInfo (
                            EfiPy.byref (FileHandle),
                            gEfiFileInfoGuid,
                            EfiPy.byref (BufferSize),
                            None
                            )

      TmpBuffer = bytearray (BufferSize.value)
      fInfo      = EFI_FILE_INFO.from_buffer (TmpBuffer)
      Status = FileHandle.GetInfo (
                            EfiPy.byref (FileHandle),
                            gEfiFileInfoGuid,
                            EfiPy.byref (BufferSize),
                            EfiPy.byref (fInfo)
                            )

      if Status != EfiPy.EFI_SUCCESS:
        break

      TempStr = (TmpBuffer[EFI_FILE_INFO.FileName.offset: -2]).decode("utf-16")

      if fInfo.Attribute & EFI_FILE_DIRECTORY == EFI_FILE_DIRECTORY:
        AbsList.append (TempStr + u"\\")
      else:
        AbsList.append (TempStr)

      NewFs = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()

      Status = FileHandle.Open (
                 EfiPy.byref (FileHandle),
                 EfiPy.byref (NewFs),
                 u"..",
                 EFI_FILE_MODE_READ,
                 0
                 )

      if Status != EfiPy.EFI_SUCCESS:
        break

      if len(AbsList) > 1:
        FileHandle.Close ( EfiPy.byref (FileHandle))
      FileHandle = NewFs[0]

    return "".join(v for v in AbsList[::-1])

  def ParseFolder (self, FilePath):

    FileFolder  = self.Shell.WorkFolder
    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    SpaceFound  = False
  
    WorkIdx = FilePath.find(u":")

    if WorkIdx != -1:

      FileSpace = FilePath[:WorkIdx + 1]
      FilePath  = FilePath[WorkIdx + 1:]

    for WsKey in self.Shell.WS:

      if WsKey == FileSpace.upper():
        FileSpace = WsKey
        SpaceFound = True
        break

      for alias in self.Shell.WS[WsKey][WsIdxAlias]:
        if FileSpace.upper() == alias:
          FileSpace = WsKey
          SpaceFound = True
          break

    if SpaceFound == False:
      return FileSpace, None, False, SpaceFound

    if len(FilePath) == 0:

      return FileSpace, self.Shell.WS[FileSpace.upper()][WsIdxPath], True, SpaceFound

    if FilePath[0] == u"\\":
      FileFolder = FilePath
    else:
      FileFolder = self.Shell.WS[FileSpace.upper()][WsIdxPath] + FilePath

    return FileSpace, FileFolder, False, SpaceFound

  def IsFileExist (self, FileSpace, FileFolder):

    if FileSpace == None or FileFolder == None:
      return False

    RootFs, FilePath = EfiPyFileOp.GetRootFsOperation (
                         self.Shell.WS,
                         u"%s%s" %(FileSpace, FileFolder)
                         )

    if RootFs == None:
      return False

    NewFs = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()

    Status = RootFs.Open (
               EfiPy.byref (RootFs),
               EfiPy.byref (NewFs),
               FilePath,
               EFI_FILE_MODE_READ,
               0
               )
    RetValue = True

    if EfiPy.EFI_ERROR (Status):
      RetValue = False

    Status = RootFs.Close (EfiPy.byref (RootFs))

    # if EfiPy.EFI_ERROR (Status):
    #   print "Error 1"

    if RetValue == True:
      Status = NewFs[0].Close (NewFs)
      # if EfiPy.EFI_ERROR (Status):
      #   print "Error 2"

    return RetValue

if __name__ == '__main__':

  Para    = EFIPY_CMD_FILE_OP.name + ""
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

  CmdSet  = CMD_SET ()

  #
  # Establish Volume Map database
  #

  from EfiPyCmdMap  import EFIPY_CMD_MAP
  EfiPyCmdMap = EFIPY_CMD_MAP(CmdSet)
  ret = EfiPyCmdMap.Run()

  #
  # File Operation testing program
  #

  EfiPyCmdObj = EFIPY_CMD_FILE_OP(CmdSet)

  print "IsFileExist (u\"fs0:\", u\"EFI\")", EfiPyCmdObj.IsFileExist (u"fs0:", u"EFI")
  print "IsFileExist (u\"fs0:\", u\"asd\")", EfiPyCmdObj.IsFileExist (u"fs0:", u"asd")

  print "ParseFolder:", EfiPyCmdObj.ParseFolder (u"fs0:EFI")

  import sys
  sys.exit(ret)
