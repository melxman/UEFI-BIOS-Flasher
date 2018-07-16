#!/usr/bin/python

#
# EfiPyCmdAttrib.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdAttrib.py is free software: you can redistribute it and/or modify
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

class EFIPY_CMD_ATTRIB (EfiPyCmdFileOp.EFIPY_CMD_FILE_OP):
  '''[INIT] Displays or changes the attributes of files or directories.'''

  name     = u"attrib"

  def ListAtttibute (self, FileSpace, FileFolder, SpaceOnly, SpaceFound):

    if SpaceFound == False:
      self.StdOut.printf(u"%s is not valide volume\r\n" % FileSpace)
      return

    if self.Shell.WS[FileSpace.upper()][WsIdxPath] == u"":
      self.StdOut.printf(u"%s is not valide volume\r\n" % FileSpace)
      return

    if SpaceOnly == True:
      FileFolder = self.Shell.WS[FileSpace.upper()][WsIdxPath]

    RootFs, FilePath = EfiPyFileOp.GetRootFsOperation (self.Shell.WS, u"%s%s" %(FileSpace, FileFolder))
    if RootFs == None:
      self.StdOut.printf(u"Volume %s cannot be opened\r\n" % FileSpace)
      return 0

    FileNode = EfiPyFileOp.GetFilesInPath (RootFs, FilePath)

    for FileItem in FileNode:

      fInfo = FileItem[1]

      AttriS = u"Attrib: "
      
      if fInfo.Attribute & EFI_FILE_DIRECTORY == EFI_FILE_DIRECTORY:
        AttriS += u"D"
      else:
        AttriS += u" "
      
      if fInfo.Attribute & EFI_FILE_ARCHIVE == EFI_FILE_ARCHIVE:
        AttriS += u"A"
      else:
        AttriS += u" "
      
      if fInfo.Attribute & EFI_FILE_SYSTEM == EFI_FILE_SYSTEM:
        AttriS += u"S"
      else:
        AttriS += u" "
      
      if fInfo.Attribute & EFI_FILE_HIDDEN == EFI_FILE_HIDDEN:
        AttriS += u"H"
      else:
        AttriS += u" "
      
      if fInfo.Attribute & EFI_FILE_READ_ONLY == EFI_FILE_READ_ONLY:
        AttriS += u"R"
      else:
        AttriS += u" "
      
      AttriS += u" %s%s\r\n" % (FileSpace, FileItem[0])
      
      self.StdOut.printf(AttriS)

    return 0

  def Run (self):

    FileSpace   = self.Shell.WorkSpace[WsIdxVol]
    FileFolder  = self.Shell.WorkSpace[WsIdxPath]

    for FilePath in self.args[1:]:
      FileSpace, FileFolder, SpaceOnly, SpaceFound = self.ParseFolder (FilePath)
      self.ListAtttibute (FileSpace, FileFolder, SpaceOnly, SpaceFound)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_ATTRIB.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_ATTRIB (CmdSet)

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
