#!/usr/bin/python

#
# EfiPyCmdType.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdType.py is free software: you can redistribute it and/or modify
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

class EFIPY_CMD_TYPE (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Sends the contents of a file to the standard output device.'''

  name     = u"type"

  #
  # Before Run function is called
  #
  def ParaPreBuild(self, args):

    self.Paras.update ({u"address": ["-addr", False, 1, (), []]})
    self.Paras.update ({u"length":  ["-len",  False, 1, (), []]})

  def Run (self):

    if len (self.args) == 1:
      self.StdOut.printf("Invalide parameter %s\r\n" % str(self.args))
      return 0

    FilePath  = self.args[1]
    Address   = 0x00L
    Length    = -1L

    if self.Paras[u"address"][EfiPyCmdBase.ParaIdxSet] == True:
      print "Address is set"
      pass

    if self.Paras[u"length"][EfiPyCmdBase.ParaIdxSet] == True:
      print "length is set"
      pass

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    FileSpace, TempFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)

    Fs1, FilePath1 = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(FileSpace, TempFolder))

    if Fs1 == None:
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[1])
      return 0

    Handle1 = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()
    Status = Fs1.Open (
               EfiPy.byref (Fs1),
               EfiPy.byref (Handle1),
               FilePath1,
               EFI_FILE_MODE_READ,
               0
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"File %s cannot be opened\r\n" % self.args[1])
      return 0

    Fs1.Close (EfiPy.byref (Fs1))

    BufferSize = EfiPy.UINTN (0)
    Status = Handle1[0].GetInfo (
                              Handle1,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              None
                              )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      Handle1[0].Close()
      return 0

    TmpBuffer = bytearray (BufferSize.value)
    fInfo1    = EFI_FILE_INFO.from_buffer (TmpBuffer)
    Status = Handle1[0].GetInfo (
                              Handle1,
                              gEfiFileInfoGuid,
                              EfiPy.byref (BufferSize),
                              EfiPy.byref (fInfo1)
                              )

    if Status != EfiPy.EFI_SUCCESS:
      Handle1[0].Close(Handle1)
      return 0

    if fInfo1.Attribute & EFI_FILE_ARCHIVE != EFI_FILE_ARCHIVE:
      self.StdOut.printf(u"Cannot dump none archive file %s%s\r\n" %(FileSpace, TempFolder))
      Handle1[0].Close(Handle1)
      return 0

    if Length == -1:
      Length = fInfo1.FileSize

    if Address >= fInfo1.FileSize:
      self.StdOut.printf(u"Dump Start point more than file size 0x%08X.\r\n" % fInfo1.FileSize)
      Handle1[0].Close(Handle1)
      return 0

    Status = Handle1[0].SetPosition (Handle1, EfiPy.UINT64 (Address))

    TotalSize = 0
    while True:

      BufferSize  = EfiPy.UINT64 (0x1000)
      TmpBuffer   = (EfiPy.CHAR8 * 0x1000) ()
      Status = Handle1[0].Read (Handle1, EfiPy.byref (BufferSize) , EfiPy.byref (TmpBuffer))

      RetValue1 = (BufferSize.value, TmpBuffer)

      if RetValue1 [0] == 0:
        break

      if Length >= len (RetValue1[1]):
        DumpBuff = RetValue1[1]
      else:
        DumpBuff = RetValue1[1][0:Length]

      for char in DumpBuff:
        if ord(char) >= 0x20 and ord(char) <= 0x7E:
          self.StdOut.printf("%s" % char)
        elif ord(char) == 0x0D or ord(char) == 0x0A:
          self.StdOut.printf("%s" % char)
        else:
          self.StdOut.printf(".")

      Length -= RetValue1 [0]

      TotalSize += RetValue1 [0]

      if Length <= 0:
        break

    Handle1[0].Close (Handle1)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_TYPE.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_TYPE (CmdSet)

  print

  Para    = EfiPyCmdObj.name + " EFI\Tools\EfiPyShell2.py"
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

  import sys
  sys.exit(ret)
