#!/usr/bin/python

#
# EfiPyCmdComp.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdComp.py is free software: you can redistribute it and/or modify
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
         EFI_FILE_READ_ONLY

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

class EFIPY_CMD_COMP (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Compares the contents of two files on a byte for byte basis.'''

  name     = u"comp"

  def Run (self):

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    if len(self.args) != 3:
      self.StdOut.printf(u"File Compare: Invalide parameter\r\n")
      self.StdOut.printf(u"comp file1 file2\r\n")
      return 0

    #
    # Compare file 1
    #

    Space1, FileFolder1, SpaceOnly, SpaceFound = self.ParseFolder (self.args[1])

    Fs1, FilePath1 = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(Space1, FileFolder1))

    if Fs1 == None:
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[1])
      return 0

    FileHandle1 = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()
    Status = Fs1.Open (
               EfiPy.byref (Fs1),
               EfiPy.byref (FileHandle1),
               FilePath1,
               EFI_FILE_MODE_READ,
               0
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[1])
      return 0

    Fs1.Close (EfiPy.byref (Fs1))


    #
    # compare file 2
    #

    Space2, FileFolder2, SpaceOnly, SpaceFound = self.ParseFolder (self.args[2])

    Fs2, FilePath2 = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(Space2, FileFolder2))
    if Fs2 == None:
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[2])
      Fs2.Close()
      return 0

    FileHandle2 = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()
    Status = Fs2.Open (
               EfiPy.byref (Fs2),
               EfiPy.byref (FileHandle2),
               FilePath2,
               EFI_FILE_MODE_READ,
               0
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[2])
      return 0

    Fs2.Close (EfiPy.byref (Fs2))

    #
    # File 1, FIle 2 compare
    #

    BufferSize = EfiPy.UINTN (0)
    Status = FileHandle1[0].GetInfo (
                              FileHandle1,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              None
                              )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      FileHandle1[0].Close (FileHandle1)
      FileHandle2[0].Close (FileHandle2)
      return 0

    TmpBuffer = bytearray (BufferSize.value)
    fInfo1    = EFI_FILE_INFO.from_buffer (TmpBuffer)
    Status = FileHandle1[0].GetInfo (
                              FileHandle1,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              EfiPy.byref (fInfo1)
                              )

    if Status != EfiPy.EFI_SUCCESS:
      FileHandle1[0].Close (FileHandle1)
      FileHandle2[0].Close (FileHandle2)
      return 0

    BufferSize = EfiPy.UINTN (0)
    Status = FileHandle2[0].GetInfo (
                              FileHandle2,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              None
                              )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      FileHandle1[0].Close (FileHandle1)
      FileHandle2[0].Close (FileHandle2)
      return 0

    TmpBuffer = bytearray (BufferSize.value)
    fInfo2    = EFI_FILE_INFO.from_buffer (TmpBuffer)
    Status = FileHandle2[0].GetInfo (
                              FileHandle2,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              EfiPy.byref (fInfo2)
                              )

    if Status != EfiPy.EFI_SUCCESS:
      FileHandle1[0].Close (FileHandle1)
      FileHandle2[0].Close (FileHandle2)
      return 0

    if fInfo1.Attribute & EFI_FILE_DIRECTORY == EFI_FILE_DIRECTORY or \
       fInfo2.Attribute & EFI_FILE_DIRECTORY == EFI_FILE_DIRECTORY:

      self.StdOut.printf(u"One of files is directory.\r\n")
      FileHandle1[0].Close (FileHandle1)
      FileHandle2[0].Close (FileHandle2)
      return 0

    if fInfo1.FileSize != fInfo2.FileSize:
      self.StdOut.printf(u"Files are different in size.\r\n")
      FileHandle1[0].Close (FileHandle1)
      FileHandle2[0].Close (FileHandle2)
      return 0

    FlagDiff = False
    while True:

      BufferSize  = EfiPy.UINT64 (0x1000)
      TmpBuffer   = (EfiPy.CHAR8 * 0x1000) ()
      Status = FileHandle1[0].Read (FileHandle1, EfiPy.byref (BufferSize) , EfiPy.byref (TmpBuffer))

      RetValue1 = (BufferSize.value, TmpBuffer)

      BufferSize  = EfiPy.UINT64 (0x1000)
      TmpBuffer   = (EfiPy.CHAR8 * 0x1000) ()
      Status = FileHandle2[0].Read (FileHandle2, EfiPy.byref (BufferSize) , EfiPy.byref (TmpBuffer))

      RetValue2 = (BufferSize.value, TmpBuffer)

      if RetValue1 [0] != RetValue2 [0] or \
         RetValue1 [1] != RetValue2 [1]:
          FlagDiff = True
          break

      if RetValue1 [0] == 0:
        break

    if FlagDiff == True:
      self.StdOut.printf(u"Files are different in conetent.\r\n")
    else:
      self.StdOut.printf(u"Files are the same.\r\n")

    FileHandle1[0].Close (FileHandle1)
    FileHandle2[0].Close (FileHandle2)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_COMP.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_COMP (CmdSet)

  print

  Para    = EfiPyCmdObj.name + " EFI\Tools\EfiPyShell2.py EFI\Tools\EfiPyShell2.py"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  print

  Para    = EfiPyCmdObj.name + " EFI\Tools\EfiPyShell2.py  EFI\Tools\EfiPyShell.py"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
