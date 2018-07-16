#!/usr/bin/python

#
# EfiPyFileOp.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyFileOp.py is free software: you can redistribute it and/or modify
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

import re

import EfiPy

from EfiPy.MdePkg.Guid.FileInfo  import EFI_FILE_INFO, gEfiFileInfoGuid
from EfiPy.MdePkg.Protocol.SimpleFileSystem import    \
       gEfiSimpleFileSystemProtocolGuid,              \
       EFI_SIMPLE_FILE_SYSTEM_PROTOCOL,               \
       EFI_FILE_PROTOCOL,                             \
       EFI_FILE_MODE_READ,                            \
       EFI_FILE_DIRECTORY

WsIdxVol        = 0
WsIdxAlias      = 1
WsIdxHandle     = 2
WsIdxDevPath    = 3
WsIdxFont       = 4
WsIdxBackGround = 5
WsIdxPath       = 6

def GetVolumePathName (Fname = None):

  if Fname == None:

    return None

  WorkIdx = Fname.find(u":")

  if WorkIdx == -1:
    return None, Fname

  if WorkIdx + 1 == len(Fname):
    return Fname, None

  return Fname[:WorkIdx + 1], Fname[WorkIdx + 1:]

def _GetVolumeHandle (WS = None, Fname = None):

  if WS == None:
    return None, None

  vol, FilePath = GetVolumePathName (Fname)

  if vol == None:
    return None, FilePath

  for ws in WS:

    if WS[ws][WsIdxVol].upper() == vol.upper():
      return WS[ws][WsIdxHandle], FilePath

    else:

      for alias in WS[ws][WsIdxAlias]:
        if vol.upper() == alias.upper():
          return WS[ws][WsIdxHandle], FilePath

  return None, FilePath

def _GetSimpleFsProtocol (WS = None, Fname = None):

  Handle, FilePath = _GetVolumeHandle (WS, Fname)

  if Handle == None:
    return None, FilePath

  TmpProtocol = EfiPy.PVOID ()

  Status = EfiPy.gBS.HandleProtocol (
             Handle,
             EfiPy.byref (gEfiSimpleFileSystemProtocolGuid),
             EfiPy.byref (TmpProtocol)
             )

  if EfiPy.RETURN_ERROR (Status):
    return None, FilePath

  FsProtocol = (EfiPy.cast (TmpProtocol, EfiPy.POINTER(EFI_SIMPLE_FILE_SYSTEM_PROTOCOL)))[0]

  return FsProtocol, FilePath

def GetRootFsOperation (WS = None, Fname = None):

  FsProtocol, FilePath = _GetSimpleFsProtocol (WS, Fname)

  if FsProtocol == None:
    return None, FilePath

  RootFsOp = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()

  Status = FsProtocol.OpenVolume (
             EfiPy.byref (FsProtocol),
             EfiPy.byref (RootFsOp)
             )

  if EfiPy.RETURN_ERROR (Status):
    return None, FilePath

  return RootFsOp[0], FilePath

def ParseAbsPath (FileHandle):

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

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      continue

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

def GetFilesInPath (RootFs, FilePath, Sensitive=False):

  RetFile = []

  Pattern = ".*"
  DeepList = False

  FileNodes = FilePath.split(u"\\")
  if u"*" in FileNodes[-1] or u"?" in FileNodes[-1]:

    Pattern   = FileNodes[-1].replace(".", "\\.").replace("?", ".?").replace("*", ".*")
    FileNodes = (v + u"\\" for v in FileNodes[:-1])
    FilePath  = "".join(v for v in FileNodes)
    DeepList  = True

  elif FilePath[-1] == "\\":
    DeepList  = True

  NewFs = EfiPy.POINTER(EFI_FILE_PROTOCOL) ()

  Status = RootFs.Open (
             EfiPy.byref (RootFs),
             EfiPy.byref (NewFs),
             FilePath,
             EFI_FILE_MODE_READ,
             0
             )

  if EfiPy.EFI_ERROR (Status):
    return RetFile

  AbsPath = ParseAbsPath (NewFs[0])

  BufferSize = EfiPy.UINTN (0)
  Status = NewFs[0].GetInfo (
             NewFs,
             gEfiFileInfoGuid,
             EfiPy.byref (BufferSize),
             None
             )

  TmpBuffer = bytearray (BufferSize.value)
  fInfo      = EFI_FILE_INFO.from_buffer (TmpBuffer)

  Status = NewFs[0].GetInfo (
                   NewFs,
                   gEfiFileInfoGuid,
                   EfiPy.byref (BufferSize),
                   EfiPy.byref (fInfo)
                   )

  TempStr = (TmpBuffer[EFI_FILE_INFO.FileName.offset: -2]).decode("utf-16")

  flag = re.I
  if Sensitive == True:
    flag = 0

  if DeepList == False:

    if re.match(Pattern, TempStr, flag):
      RetFile.append((AbsPath, fInfo, TempStr))

    NewFs[0].Close (NewFs)

    return RetFile

  if fInfo.Attribute & EFI_FILE_DIRECTORY != EFI_FILE_DIRECTORY:

    if re.match(Pattern, TempStr, flag):

      RetFile.append((AbsPath + TempStr, fInfo, TempStr))

    NewFs[0].Close (NewFs)

    return RetFile

  while True:

    BufferSize = EfiPy.UINTN ()
    Status = NewFs[0].Read (
               NewFs,
               EfiPy.byref (BufferSize),
               None)

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      break

    TmpBuffer = bytearray (BufferSize.value)
    fInfo      = EFI_FILE_INFO.from_buffer (TmpBuffer)


    Status = NewFs[0].Read (
               NewFs,
               EfiPy.byref (BufferSize),
               EfiPy.cast (
                 EfiPy.byref (fInfo),
                 EfiPy.PVOID
                 )
               )

    if EfiPy.EFI_ERROR (Status):
      self.StdOut.printf(u"Error: Status: 0x%016X\r\n" % Status)
      break

    TempStr = (TmpBuffer[EFI_FILE_INFO.FileName.offset: -2]).decode("utf-16")

    if re.match(Pattern, TempStr, flag):
      RetFile.append((AbsPath + TempStr, fInfo, TempStr))

  NewFs[0].Close (NewFs)

  return RetFile

if __name__ == '__main__':

  from Uefi.EfiPyPkg.Ext.EfiPyConIO      import EFIPY_CON_IO
  from Uefi.EfiPyPkg.Cmd.EfiPyCmdMap     import EFIPY_CMD_MAP

  print GetVolumePathName (u"blk1:")
  print GetVolumePathName (u"fs1:\EFI\BOOT")
  print GetVolumePathName (u"\EFI\BOOT")

  EfiPyIo     = EFIPY_CON_IO()
  EfiPyIo.ConOutModeDefault()

  EfiPyCmdMap = EFIPY_CMD_MAP(EfiPyIo)
  WS          = EfiPyCmdMap.WS

  print "GetRootFsOperation"
  print GetRootFsOperation (WS, u"blk1:")
  print GetRootFsOperation (WS, u"fs1:\EFI\BOOT")
  print GetRootFsOperation (WS, u"\EFI\BOOT")
