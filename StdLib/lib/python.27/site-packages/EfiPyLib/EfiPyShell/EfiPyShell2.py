#!/usr/bin/python

#
# EfiPyShell.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyShell.py is free software: you can redistribute it and/or modify
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

import sys, os, traceback
import EfiPyShellIo

from EfiPy import *

from Utility                              import EfiPyFileOp

from EfiPy.MdePkg.Protocol.SimpleTextOut  import *
from EfiPy.MdePkg.Protocol.SimpleTextIn   import  EFI_INPUT_KEY,        \
                                                  SCAN_NULL,            \
                                                  CHAR_NULL,            \
                                                  CHAR_CARRIAGE_RETURN, \
                                                  CHAR_BACKSPACE,       \
                                                  CHAR_LINEFEED,        \
                                                  CHAR_TAB

from EfiPyCmdCls      import EFIPY_CMD_CLS
from EfiPyCmdExit     import EFIPY_CMD_EXIT
from EfiPyCmdHelp     import EFIPY_CMD_HELP
from EfiPyCmdVer      import EFIPY_CMD_VER
from EfiPyCmdGetMtc   import EFIPY_CMD_GET_MTC
from EfiPyCmdMem      import EFIPY_CMD_MEM
from EfiPyCmdDmpStore import EFIPY_CMD_DMP_STORE
from EfiPyCmdDmpBoot  import EFIPY_CMD_DMP_BOOT
from EfiPyCmdMap      import EFIPY_CMD_MAP
from EfiPyCmdDir      import EFIPY_CMD_DIR
from EfiPyCmdCd       import EFIPY_CMD_CD
from EfiPyCmdMkDir    import EFIPY_CMD_MKDIR
from EfiPyCmdVol      import EFIPY_CMD_VOL
from EfiPyCmdAttrib   import EFIPY_CMD_ATTRIB
from EfiPyCmdType     import EFIPY_CMD_TYPE
from EfiPyCmdComp     import EFIPY_CMD_COMP
from EfiPyCmdHexDump  import EFIPY_CMD_HEXDUMP
from EfiPyCmdTouch    import EFIPY_CMD_TOUCH
from EfiPyCmdSetSize  import EFIPY_CMD_SET_SIZE
from EfiPyCmdDate     import EFIPY_CMD_DATE
from EfiPyCmdTime     import EFIPY_CMD_TIME
from EfiPyCmdStall    import EFIPY_CMD_STALL
from EfiPyCmdMemMap   import EFIPY_CMD_MEMMAP
from EfiPyCmdMm       import EFIPY_CMD_MM
from EfiPyCmdPci      import EFIPY_CMD_PCI
from EfiPyCmdRun      import EFIPY_CMD_RUN

WsIdxVol        = 0
WsIdxAlias      = 1
WsIdxHandle     = 2
WsIdxDevPath    = 3
WsIdxFont       = 4
WsIdxBackGround = 5
WsIdxPath       = 6

class EFIPY_COMMAND_SHELL:

  def __init__ (self):

    import EfiPy
    self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
    self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut, EfiPy.gST.ConIn)
    self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

    self.StdOut.ConOutModeDefault ()
    self.StdOut.ConOutCursorSet(Toggle=True)

    #
    # EfiPy Shell default variable
    #
    self.CmdHistory   = []
    self.CmdSet       = {}
    self.EfiPyCmdMap  = None

    self.WS = {
      u"SHELL:":   [                          # Key
        u"EfiPyShell:",                       # Volumn      WsIdxVol        = 0
        [],                                   # Alias       WsIdxAlias      = 1
        None,                                 # handle      WsIdxHandle     = 2
        None,                                 # DevicePath  WsIdxDevPath    = 3
        EFI_GREEN | EFI_BACKGROUND_BLACK,     # BgColor     WsIdxFont       = 4
        EFI_LIGHTGRAY | EFI_BACKGROUND_BLACK, # FgColor     WsIdxBackGround = 5
        u""                                   # Path        WsIdxPath       = 6
        ]
    }

    #
    # EfiPy Shell command initilize
    #
    self.EfiPyCmdCls      = EFIPY_CMD_CLS       (self)
    self.EfiPyCmdExit     = EFIPY_CMD_EXIT      (self)
    self.EfiPyCmdHelp     = EFIPY_CMD_HELP      (self)
    self.EfiPyCmdVer      = EFIPY_CMD_VER       (self)
    self.EfiPyCmdGetMtc   = EFIPY_CMD_GET_MTC   (self)
    self.EfiPyCmdMem      = EFIPY_CMD_MEM       (self)
    self.EfiPyCmdDmpStore = EFIPY_CMD_DMP_STORE (self)
    self.EfiPyCmdDmpBoot  = EFIPY_CMD_DMP_BOOT  (self)
    self.EfiPyCmdMap      = EFIPY_CMD_MAP       (self)
    self.EfiPyCmdDir      = EFIPY_CMD_DIR       (self)
    self.EfiPyCmdCd       = EFIPY_CMD_CD        (self)
    self.EfiPyCmdMkDir    = EFIPY_CMD_MKDIR     (self)
    self.EfiPyCmdVol      = EFIPY_CMD_VOL       (self)
    self.EfiPyCmdAttrib   = EFIPY_CMD_ATTRIB    (self)
    self.EfiPyCmdType     = EFIPY_CMD_TYPE      (self)
    self.EfiPyCmdComp     = EFIPY_CMD_COMP      (self)
    self.EfiPyCmdHexDump  = EFIPY_CMD_HEXDUMP   (self)
    self.EfiPyCmdTouch    = EFIPY_CMD_TOUCH     (self)
    self.EfiPyCmdSetSize  = EFIPY_CMD_SET_SIZE  (self)
    self.EfiPyCmdDate     = EFIPY_CMD_DATE      (self)
    self.EfiPyCmdTime     = EFIPY_CMD_TIME      (self)
    self.EfiPyCmdStall    = EFIPY_CMD_STALL     (self)
    self.EfiPyCmdMemMap   = EFIPY_CMD_MEMMAP    (self)
    self.EfiPyCmdMm       = EFIPY_CMD_MM        (self)
    self.EfiPyCmdPci      = EFIPY_CMD_PCI       (self)
    self.EfiPyCmdRun      = EFIPY_CMD_RUN       (self)

    #
    # EfiPy Shell variable initilize
    #
    self.WS             = self.EfiPyCmdMap.WS
    self.WorkSpace      = self.WS[u"SHELL:"]
    # self.WorkFolder     = self.WorkSpace[WsIdxPath]
    self.WorkFolder     = self.WorkSpace[6]         # Using hard coding for w/o Map command
    self.CommandList    = sorted(self.CmdSet.keys())
    self.ParameterList  = []

    self.EfiPyCmdMap.Run()

  def PromptChange(self, label):

    if label.upper() in self.WS.keys():

      self.WorkSpace      = self.WS[label.upper()]
      return 0

    else:

      for ws in self.WS:

        alias = self.WS[ws][WsIdxAlias]
        if label.upper() in alias:
          self.WorkSpace      = self.WS[ws]
          # self.WorkSpace      = label.upper()
          return 0

    self.StdOut.printf(u"\'%s\' is not a correct mapping.\r\n" % label)

    return -1

  #
  # Show Shell prompt by shell current status
  #
  def PromptShow(self):

    if len(self.WorkSpace[WsIdxAlias]) != 0:
      # _prompt = self.WorkSpace[WsIdxVol] + self.WorkSpace[WsIdxAlias] + u"> "
      _prompt = self.WorkSpace[WsIdxVol] + self.WorkSpace[WsIdxPath] + u"> "
    else:
      _prompt = self.WorkSpace[WsIdxVol] + self.WorkSpace[WsIdxPath] + u"> "

    self.StdOut.printf([_prompt, self.WorkSpace[WsIdxFont]])
    # self.StdOut.printf(_prompt)

  def _StringCandidateSearch (self, StringPre, StringFullList):

    StringCandidate = []

    for StringItem in StringFullList:
      if StringItem.lower().startswith(StringPre.lower()):
        StringCandidate.append(StringItem)

    return StringCandidate

  def CommandGet(self):

    self.PromptShow()

    StringIn  = u""
    Command   = u""
    Parameter = u""

    #
    # used by TAB key
    #

    CmdSearch           = True

    StringCandidatePre  = u""
    StringCandidateList = self._StringCandidateSearch(StringCandidatePre, self.CommandList)

    while True:

      Status      = EFI_NOT_READY
      EventIndex  = UINTN()
      InputKey    = EFI_INPUT_KEY ()

      while RETURN_ERROR (Status):
        Status = gBS.WaitForEvent (1, byref(EFI_EVENT(gST.ConIn[0].WaitForKey)), byref(EventIndex))
        Status = gST.ConIn[0].ReadKeyStroke (gST.ConIn, byref (InputKey))

      #
      # ScanCode is inpute
      #
      if InputKey.ScanCode == SCAN_NULL:

        if   ord(InputKey.UnicodeChar) == CHAR_NULL:
          pass

        elif ord(InputKey.UnicodeChar) == CHAR_BACKSPACE:

          if StringIn != u"":
            StringIn = StringIn[:-1]
            self.StdOut.printf(InputKey.UnicodeChar)

          TmpStr = StringIn.split()
          if len(TmpStr) == 1:
            StringCandidatePre  = TmpStr[0]
            StringCandidateList = self._StringCandidateSearch(TmpStr[0], self.CommandList)
          elif len(TmpStr) > 1:
            StringCandidatePre  = TmpStr[-1]
            StringCandidateList = self._StringCandidateSearch(TmpStr[-1], self.ParameterList)

        elif ord(InputKey.UnicodeChar) == CHAR_TAB:

          for TmpString in StringCandidateList:

            if StringCandidatePre.lower() in TmpString.lower():
              self.StdOut.printf(unichr(CHAR_BACKSPACE) * len(StringIn))
              StringIn = TmpString
              self.StdOut.printf(StringIn)
              StringCandidateList.remove(TmpString)
              break

          if len(StringCandidateList) == 0:
            if CmdSearch == True:
              StringCandidateList = self._StringCandidateSearch(StringCandidatePre, self.CommandList)
            else:
              StringCandidateList = self._StringCandidateSearch(StringCandidatePre, self.ParameterList)

        elif ord(InputKey.UnicodeChar) == CHAR_LINEFEED:
          pass

        elif ord(InputKey.UnicodeChar) == CHAR_CARRIAGE_RETURN:
          self.StdOut.printf(u"\n\r")
          self.CmdHistory.append (StringIn)
          break

        elif ord(InputKey.UnicodeChar) == u" ":
          StringIn += chr(KeyIn[1])
          self.StdOut.printf(u"%c" % KeyIn[1])

          TmpStr = StringIn.split()
          if len(TmpStr) >= 1:
            CmdSearch = False
            Command   = TmpStr[0]
            
          if len(TmpStr) == 1:
            StringCandidatePre  = TmpStr[0]
            StringCandidateList = self._StringCandidateSearch(TmpStr[0], self.CommandList)
          elif len(TmpStr) > 1:
            StringCandidatePre  = TmpStr[-1]
            StringCandidateList = self._StringCandidateSearch(TmpStr[0], self.ParameterList)

        else:
          StringIn    += InputKey.UnicodeChar
          CmdCandidate = StringIn
          self.StdOut.printf(InputKey.UnicodeChar)

          TmpStr = StringIn.split()
          if len(TmpStr) == 1:
            StringCandidatePre  = TmpStr[0]
            StringCandidateList = self._StringCandidateSearch(TmpStr[0], self.CommandList)
          elif len(TmpStr) > 1:
            StringCandidatePre  = TmpStr[-1]
            StringCandidateList = self._StringCandidateSearch(TmpStr[0], self.ParameterList)

      #
      # Unicode is inpute
      #
      else:
        pass

    return StringIn.split()

  def _ExecFile (self, Space, Folder, args):

    if Space == None:
      wSpace = self.WorkSpace
    elif Space.upper() in self.WS:
      wSpace = self.WS[Space.upper()]
    else:
      wSpace = None

    if wSpace == None or wSpace[WsIdxDevPath] == None:
      self.StdOut.printf(u"Can not execute command without space\r\n")
      return

    # print wSpace, Folder
    # self.StdOut.printf(u"Try to exec command %s (1)\r\n" % str(args))
    self.EfiPyCmdRun.ParaPreBuild (args)
    Args  = self.EfiPyCmdRun.ParaBuild (args)
    ret   = self.EfiPyCmdRun.Run()

  def run(self, Command, args):


    if Command.lower() not in self.CommandList:

      try:
        TempSpace, TempFolder = EfiPyFileOp.GetVolumePathName (args[0])

        if len(args) == 1:

          if TempFolder == None and TempSpace != None:
            self.PromptChange (TempSpace)
            return 0
          else:
            self._ExecFile (TempSpace, TempFolder, args)
            return 0
        else:
          self._ExecFile (TempSpace, TempFolder, args)
          return 0
      except:
        self.StdOut.printf(u"Try to exec command %s (3)\r\n" % args[0])
        print traceback.format_exc()
        return 0
    else:

      try:
        self.CmdSet[Command.lower()].ParaPreBuild(args)
        self.CmdSet[Command.lower()].ParaBuild(args)
        self.CmdSet[Command.lower()].ParaGet()
        ret  = self.CmdSet[Command.lower()].Run()
      except NameError as inst:
        ret = 0
        if inst.args[0].startswith(u"EFIPY_"):
          pass
        else:
          print traceback.format_exc()
      except Exception, err:
        print traceback.format_exc()
        ret = 0

      self.CmdSet[Command.lower()].PostRun()

    return ret

##########################################################################
# Shell program entry
##########################################################################
if __name__ == '__main__':

  ShellCmd = EFIPY_COMMAND_SHELL()

  while 1:
  
    command  = ShellCmd.CommandGet()
  
    if command == None or len(command) == 0:
      continue

    ret = ShellCmd.run(command[0], command)
    if ret == -1:
      break

  sys.exit(0)
