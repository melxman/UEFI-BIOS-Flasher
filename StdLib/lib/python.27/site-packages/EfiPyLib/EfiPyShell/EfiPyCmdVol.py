#!/usr/bin/python

#
# EfiPyCmdVol.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdVol.py is free software: you can redistribute it and/or modify
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

from    EfiPy.MdePkg.Guid.FileSystemInfo  import EFI_FILE_SYSTEM_INFO, gEfiFileSystemInfoGuid

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_VOL (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays or changes information about a disk volume.'''

  name     = u"vol"

  def OutputVol (self, ws, VolInfo, VolBuffer, VolSize):

    TempStr = (VolBuffer[EFI_FILE_SYSTEM_INFO.VolumeLabel.offset : VolSize -2]).decode("utf-16")

    OutString = u"%s Volume %s " % (ws, TempStr)

    if VolInfo.ReadOnly == 1:
      OutString += "(r)\r\n"
    else:
      OutString += "(rw)\r\n"

    self.StdOut.printf(OutString)

    self.StdOut.printf(u"%d bytes total disk space\r\n" % VolInfo.VolumeSize)
    self.StdOut.printf(u"%d bytes available on disk\r\n" % VolInfo.FreeSpace)
    self.StdOut.printf(u"%d bytes in each allocation unit\r\n\r\n" % VolInfo.BlockSize)

  def Run (self):

    for ws in self.Shell.WS:

      RootFs, FilePath = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, ws)
      if RootFs == None:
        continue

      # Status, RetValue  = RootFs.GetInfo (gEfiFileSystemInfoGuid)
      # if EFI_ERROR (Status):
      #   self.StdOut.printf(u"Get Volume %s Fail (%d) r\n" %(ws, Status))

      # FsInfo = EFI_FILE_SYSTEM_INFO (RetValue[1])

      BufferSize = EfiPy.UINTN (0)
      Status = RootFs.GetInfo (
                            EfiPy.byref (RootFs),
                            gEfiFileSystemInfoGuid,
                            EfiPy.byref (BufferSize),
                            None
                            )

      if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
        continue

      # print "BufferSize.value", BufferSize.value
      # print "EfiPy.sizeof (EFI_FILE_SYSTEM_INFO)", EfiPy.sizeof (EFI_FILE_SYSTEM_INFO)

      if BufferSize.value >= EfiPy.sizeof (EFI_FILE_SYSTEM_INFO):
        TmpBuffer = bytearray (BufferSize.value)
      else:
        TmpBuffer = bytearray (EfiPy.sizeof (EFI_FILE_SYSTEM_INFO))

      FsInfo    = EFI_FILE_SYSTEM_INFO.from_buffer (TmpBuffer)

      Status = RootFs.GetInfo (
                        EfiPy.byref (RootFs),
                        gEfiFileSystemInfoGuid,
                        EfiPy.byref (BufferSize),
                        EfiPy.byref (FsInfo)
                        )

      if Status != EfiPy.EFI_SUCCESS:
        continue

      # import Utility.EfiPyUtility
      # Utility.EfiPyUtility.EfiPyHexDump (self.StdOut, 2, 0x00, TmpBuffer, True)

      self.OutputVol (ws, FsInfo, TmpBuffer, BufferSize.value)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_VOL.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_VOL (CmdSet)

  print

  Para    = EfiPyCmdObj.name + " blk1:"
  Args    = Para.split()

  EfiPyCmdObj.ParaPreBuild (Args)
  Args = EfiPyCmdObj.ParaBuild (Args)
  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
