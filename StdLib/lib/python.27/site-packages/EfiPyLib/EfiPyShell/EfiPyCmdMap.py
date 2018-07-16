#!/usr/bin/python

#
# EfiPyCmdMap.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdBase.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.Protocol.SimpleFileSystem import gEfiSimpleFileSystemProtocolGuid
from EfiPy.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL, gEfiDevicePathProtocolGuid
from EfiPy.MdePkg.Protocol.BlockIo          import gEfiBlockIoProtocolGuid
from EfiPy.MdePkg.Protocol.SimpleTextOut    import *

WsIdxVol        = 0
WsIdxAlias      = 1
WsIdxHandle     = 2
WsIdxDevPath    = 3
WsIdxFont       = 4
WsIdxBackGround = 5
WsIdxPath       = 6

#
# EfiPy Command utility FS Mapping utility class
#

class EFIPY_CMD_MAP (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Displays or defines mappings.'''

  name     = u"map"

  def __init__ (self, shell):

    EfiPyCmdBase.EFIPY_CMD_BASE.__init__(self, shell)
    self.WS = shell.WS

    #
    # Get Device Path from gEfiSimpleFileSystemProtocolGuid
    #

    BufferSize = EfiPy.UINTN (0)
    Status = EfiPy.gBS.LocateHandle (
               EfiPy.ByProtocol,
               EfiPy.byref (gEfiSimpleFileSystemProtocolGuid),
               None,
               EfiPy.byref(BufferSize),
               None
               )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      return

    HandleArrayType = EfiPy.EFI_HANDLE * (BufferSize.value / EfiPy.sizeof (EfiPy.EFI_HANDLE))
    HandleArray     = HandleArrayType ()

    Status = EfiPy.gBS.LocateHandle(
               EfiPy.ByProtocol,
               EfiPy.byref(gEfiSimpleFileSystemProtocolGuid),
               None,
               EfiPy.byref(BufferSize),
               HandleArray
               )

    if Status != EfiPy.EFI_SUCCESS:
      return

    MappingIndex = 0

    if not EfiPy.RETURN_ERROR (Status):

      for Handle in HandleArray:
        Volume = u"FS%d:" % MappingIndex

        TmpDevPath = EfiPy.PVOID ()

        Status = EfiPy.gBS.HandleProtocol (
                   Handle,
                   EfiPy.byref (gEfiDevicePathProtocolGuid),
                   EfiPy.byref (TmpDevPath)
                   )
        if EfiPy.EFI_ERROR (Status):
          continue

        DevicePath = (EfiPy.cast (TmpDevPath, EfiPy.POINTER(EFI_DEVICE_PATH_PROTOCOL)))[0]

        DevicePath.DisplayOnly    = True
        DevicePath.AllowShortcuts = False

        # print "(0x%02X, 0x%02X) %s" % (DevicePath.Type, DevicePath.SubType, DevicePath)

                       # Key:       [Volumn, Alias, Handle, DevicePath, BgColor, FgColor]
        self.WS.update( {Volume:    [Volume, [],    Handle, DevicePath, EFI_YELLOW | EFI_BACKGROUND_BLACK, EFI_LIGHTGRAY | EFI_BACKGROUND_BLACK, u"\\"]})

        MappingIndex += 1

    # print "===="

    #
    # Get Device Path from gEfiBlockIoProtocolGuid
    #

    BufferSize = EfiPy.UINTN (0)
    Status = EfiPy.gBS.LocateHandle (
               EfiPy.ByProtocol,
               EfiPy.byref (gEfiBlockIoProtocolGuid),
               None,
               EfiPy.byref(BufferSize),
               None
               )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      return

    HandleArrayType = EfiPy.EFI_HANDLE * (BufferSize.value / EfiPy.sizeof (EfiPy.EFI_HANDLE))
    HandleArray     = HandleArrayType ()

    Status = EfiPy.gBS.LocateHandle(
               EfiPy.ByProtocol,
               EfiPy.byref(gEfiBlockIoProtocolGuid),
               None,
               EfiPy.byref(BufferSize),
               HandleArray
               )

    if Status != EfiPy.EFI_SUCCESS:
      return

    MappingIndex = 0

    if not EfiPy.RETURN_ERROR (Status):

      for Handle in HandleArray:
        Volume = u"BLK%d:" % MappingIndex

        TmpDevPath = EfiPy.PVOID ()

        Status = EfiPy.gBS.HandleProtocol (
                   Handle,
                   EfiPy.byref (gEfiDevicePathProtocolGuid),
                   EfiPy.byref (TmpDevPath)
                   )
        if EfiPy.EFI_ERROR (Status):
          continue

        DevicePath = (EfiPy.cast (TmpDevPath, EfiPy.POINTER(EFI_DEVICE_PATH_PROTOCOL)))[0]

        DevicePath.DisplayOnly    = True
        DevicePath.AllowShortcuts = False
        # print "(0x%02X, 0x%02X) %s" % (DevicePath.Type, DevicePath.SubType, DevicePath)

        VolumeFound = False
        for Volumn in self.WS:
          if self.WS[Volumn][WsIdxDevPath] != None and Handle == self.WS[Volumn][WsIdxHandle]:
            self.WS[Volumn][WsIdxAlias].append(u"BLK%d:" % MappingIndex)
            VolumeFound = True
            break

        if VolumeFound == False:
          self.WS.update( {Volume:    [Volume, [],    Handle, DevicePath, EFI_RED | EFI_BACKGROUND_BLACK, EFI_LIGHTGRAY | EFI_BACKGROUND_BLACK, u""]})

        MappingIndex += 1

  #
  # Clear screen working function
  #
  def Run (self):

    self.StdOut.printf(u"Mapping table\r\n")

    for Volumn in self.WS:

      if Volumn.upper() == u"SHELL:":
        continue

      self.StdOut.printf(u"%10s  Alias(s):" % self.WS[Volumn][WsIdxVol])

      for Alias in self.WS[Volumn][WsIdxAlias]:
        self.StdOut.printf(u"%s" % Alias)

      print

      if self.WS[Volumn][WsIdxDevPath] != None:
        self.StdOut.printf("          %s\r\n" % str(self.WS[Volumn][WsIdxDevPath]))

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_MAP.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet = {}
      self.WS     = {}

  CmdSet  = CMD_SET ()

  EfiPyCmdObj = EFIPY_CMD_MAP(CmdSet)
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)

  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
