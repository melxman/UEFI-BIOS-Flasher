#!/usr/bin/python

#
# EfiPyShellIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyShellIo.py is free software: you can redistribute it and/or modify
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

import copy

from EfiPy import *
from EfiPy.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY, SCAN_NULL, CHAR_CARRIAGE_RETURN

#
# EfiPy Shell Standard Input class
#
class SHELL_INPUT:

  def __init__ (self, ConIn):
    self.ConIn      = ConIn

  def Reset (self, This, ExtendedVerification):
    return 0

  def ReadKeyStroke (self, This, Key):
    return 0

#
# EfiPy Shell Output class
#
class SHELL_OUTPUT:

  def __init__ (self, ConOut, ConIn = None):

    self.ModeDefault = None
    self.ModeCurrent = None

    self.OutBreakEnable = False
    self.OutBreakCount  = 0
    self.OutBreakLimit  = 25
    self.ColumnsLimit   = 0
    self.ColumnsCount   = 0

    self.OutFontToggle  = True

    self.ConOut   = ConOut
    self.ConIn    = ConIn
    self.Mode     = None

  #
  # Output break by page functions
  #
  def ConOutBreakSet(self, BreakEnable):

    self.OutBreakCount = 0

    if type(BreakEnable) != bool:
      return

    Columns = UINTN ()
    Rows    = UINTN ()
    Status = self.ConOut[0].QueryMode (
                              self.ConOut,
                              self.ModeCurrent.Mode,
                              byref (Columns),
                              byref (Rows)
                              )

    if Status == EFI_SUCCESS:
      self.OutBreakLimit = Rows.value
      self.ColumnsLimit  = Columns.value

    self.OutBreakEnable = BreakEnable

  def ConOutBreakCheck(self):

    if self.OutBreakEnable == False:
      return

    # self.OutBreakCount += 1

    if self.OutBreakCount >= self.OutBreakLimit - 1:

      self.ConOut[0].OutputString(self.ConOut, u"\r\nPress ENTER to continue or \'Q\' to break:")

      Status      = EFI_NOT_READY
      EventIndex  = UINTN()
      InputKey    = EFI_INPUT_KEY ()

      while RETURN_ERROR (Status):

        Status = gBS.WaitForEvent (1, byref(EFI_EVENT(self.ConIn[0].WaitForKey)), byref(EventIndex))
        Status = self.ConIn[0].ReadKeyStroke (gST.ConIn, byref (InputKey))

        if InputKey.ScanCode != SCAN_NULL:
          Status = EFI_NOT_READY
          continue

        elif  ord(InputKey.UnicodeChar) == CHAR_CARRIAGE_RETURN:
          self.OutBreakCount = 0
          self.ConOut[0].OutputString(self.ConOut, u"\r\n")
          break

        elif  InputKey.UnicodeChar == u"Q" or InputKey.UnicodeChar == u"q":
          self.OutBreakCount = 0
          self.ConOut[0].OutputString(self.ConOut, u"\r\n")
          raise NameError(u"EFIPY_CON_IO.ConOutBreakCheck")
          break

        else:
          Status = EFI_NOT_READY

  #
  # Output Mode settings
  # (mode, FontFg, FontBg, Toggle)
  #
  def ConOutModeDefault(self, Mode=None):

    # use current system setting
    if Mode == None:
      self.ModeDefault = copy.copy(self.ConOut[0].Mode[0])
    else:
      self.ModeDefault = Mode

    self.ModeCurrent = copy.copy(self.ModeDefault)
    self.ConOutBreakSet(False)

  #
  # Restore to ModeInit value
  #
  def ConOutModeRestore(self):

    self.ModeCurrent = copy.copy(self.ModeDefault)

    if self.ModeDefault == None:
      return

    self.ConOut[0].SetAttribute(self.ConOut, self.ModeDefault.Attribute)  
    self.ConOut[0].EnableCursor(self.ConOut, self.ModeDefault.CursorVisible)  

    self.ConOutBreakSet(False)

  #
  # Cursor settings
  #
  def ConOutCursorSet(self, pos=None, Visible=None, Toggle=None):

    if pos != None:
      self.ConOut[0].SetCursorPosition (self.ConOut, pos[0], pos[1])
      self.ConOutBreakSet(False)

    if Visible != None:
      self.ConOut[0].EnableCursor (self.ConOut,Visible)
      self.ModeCurrent.CursorVisible = Visible

    if Toggle != None and type(Toggle) is bool:
      self.OutFontToggle = Toggle

  #
  # output functions
  #
  def _print(self, pList):

    #
    # Cursor setting
    #
    if pList[2] != None:
      self.ConOut[0].EnableCursor(self.ConOut, pList[2])
      self.ModeCurrent.CursorVisible = pList[2]

    #
    # Font fg/bg setting
    #
    if pList[1] != None:
      self.ConOut[0].SetAttribute(self.ConOut, pList[1])
      self.ModeCurrent.Attribute = pList[1]
      
    if pList[0] != None:
      
      for char in pList[0]:

        if    ord(char) == 0x0D:
          self.OutBreakCount += 1
        elif  ord(char) == 0x08 and self.ColumnsCount > 0:
          self.ColumnsCount  -= 1
        elif  ord(char) == 0x0A:
          self.ColumnsCount   = 0
        elif  ord(char) == 0x09:
          self.ColumnsCount  += 4
        elif  self.ColumnsCount < self.ColumnsLimit:
          self.ColumnsCount  += 1
        else:
          self.OutBreakCount += 1
          self.ColumnsCount   = 0

        self.ConOut[0].OutputString(self.ConOut, char)
        self.ConOutBreakCheck()
      
      # self.ConOut[0].OutputString(self.ConOut, pList[0])
      # self.ConOutBreakCheck()

    if self.OutFontToggle == True:
      self.ConOut[0].SetAttribute(self.ConOut, self.ModeDefault.Attribute)

  def printf(self, args):

    #           [Str,  Attr, Cursor]
    TmpOutStr = [None, None, None]

    if type(args) is unicode:
      TmpOutStr[0] = args

    elif type(args) is str:
      TmpOutStr[0] = unicode(args)

    elif type(args) is not list:
      return

    else:

      if len(args) == 3:
        TmpOutStr[2] = args[2]  # Cursor

      if len(args) >= 2:
        TmpOutStr[1] = args[1]  # Attr

      if  len(args) >= 1:

        if type(args[0]) is str:
          TmpOutStr[0] = unicode(args[0])     # String
        elif type(args[0]) is unicode:
          TmpOutStr[0] = args[0]              # String

    self._print (TmpOutStr)

  def ClearScreen (self):

    if self.ConOut is None:
      return -1L

    Status = self.ConOut[0].ClearScreen (self.ConOut)
    return Status

if __name__ == '__main__':

  from EfiPy.MdePkg.Protocol.SimpleTextOut import EFI_BACKGROUND_CYAN, EFI_LIGHTBLUE

  # EfiPyConIn = SHELL_INPUT (gST.ConIn)
  EfiPyConIO = SHELL_OUTPUT(gST.ConOut, gST.ConIn)

  EfiPyConIO.ConOutModeDefault()
  EfiPyConIO.printf(None)
  EfiPyConIO.printf(u"11111\r\n")
  EfiPyConIO.printf("8888\r\n")
  EfiPyConIO.printf(["2222\r\n"])
  EfiPyConIO.printf([u"3333\r\n"])
  EfiPyConIO.printf([u"4444\r\n", EFI_BACKGROUND_CYAN | EFI_LIGHTBLUE])
  EfiPyConIO.ConOutModeRestore()

  EfiPyConIO.ConOutModeDefault()
  EfiPyConIO.ConOutBreakSet(True)

  try:
    EfiPyConIO.printf("==>001\r\n")
    EfiPyConIO.printf("==>002\r\n")
    EfiPyConIO.printf("==>003\r\n")
    EfiPyConIO.printf("==>004\r\n")
    EfiPyConIO.printf("==>005\r\n")
    EfiPyConIO.printf("==>006\r\n")
    EfiPyConIO.printf("==>007\r\n")
    EfiPyConIO.printf("==>008\r\n")
    EfiPyConIO.printf("==>009\r\n")
    EfiPyConIO.printf("==>010\r\n")
    EfiPyConIO.printf("==>011\r\n")
    EfiPyConIO.printf("==>012\r\n")
    EfiPyConIO.printf("==>013\r\n")
    EfiPyConIO.printf("==>014\r\n")
    EfiPyConIO.printf("==>015\r\n")
    EfiPyConIO.printf("==>016\r\n")
    EfiPyConIO.printf("==>017\r\n")
    EfiPyConIO.printf("==>018\r\n")
    EfiPyConIO.printf("==>019\r\n")
    EfiPyConIO.printf("==>020\r\n")
    EfiPyConIO.printf("==>021\r\n")
    EfiPyConIO.printf("==>022\r\n")
    EfiPyConIO.printf("==>023\r\n")
    EfiPyConIO.printf("==>024\r\n")
    EfiPyConIO.printf("==>025\r\n")
    EfiPyConIO.printf("==>026\r\n")
    EfiPyConIO.printf("==>027\r\n")
    EfiPyConIO.printf("==>028\r\n")
    EfiPyConIO.printf("==>029\r\n")
    EfiPyConIO.printf("==>030\r\n")
    EfiPyConIO.printf("==>031\r\n")
    EfiPyConIO.printf("==>032\r\n")
    EfiPyConIO.printf("==>033\r\n")
    EfiPyConIO.printf("==>034\r\n")
    EfiPyConIO.printf("==>035\r\n")
    EfiPyConIO.printf("==>036\r\n")
    EfiPyConIO.printf("==>037\r\n")
    EfiPyConIO.printf("==>038\r\n")
    EfiPyConIO.printf("==>039\r\n")
    EfiPyConIO.printf("==>040\r\n")
    EfiPyConIO.printf("==>041\r\n")
    EfiPyConIO.printf("==>042\r\n")
    EfiPyConIO.printf("==>043\r\n")
    EfiPyConIO.printf("==>044\r\n")
    EfiPyConIO.printf("==>045\r\n")
    EfiPyConIO.printf("==>046\r\n")
    EfiPyConIO.printf("==>047\r\n")
    EfiPyConIO.printf("==>048\r\n")
    EfiPyConIO.printf("==>049\r\n")
    EfiPyConIO.printf("==>050\r\n")
    EfiPyConIO.printf("==>051\r\n")
    EfiPyConIO.printf("==>052\r\n")
    EfiPyConIO.printf("==>053\r\n")
    EfiPyConIO.printf("==>054\r\n")
    EfiPyConIO.printf("==>055\r\n")
    EfiPyConIO.printf("==>056\r\n")
    EfiPyConIO.printf("==>057\r\n")
    EfiPyConIO.printf("==>058\r\n")
    EfiPyConIO.printf("==>059\r\n")
    EfiPyConIO.printf("==>060\r\n")
    EfiPyConIO.printf("==>061\r\n")
    EfiPyConIO.printf("==>062\r\n")
    EfiPyConIO.printf("==>063\r\n")
    EfiPyConIO.printf("==>064\r\n")
    EfiPyConIO.printf("==>065\r\n")
    EfiPyConIO.printf("==>066\r\n")
    EfiPyConIO.printf("==>067\r\n")
    EfiPyConIO.printf("==>068\r\n")
    EfiPyConIO.printf("==>069\r\n")
    EfiPyConIO.printf("==>070\r\n")
    EfiPyConIO.printf("==>071\r\n")
    EfiPyConIO.printf("==>072\r\n")
    EfiPyConIO.printf("==>073\r\n")
    EfiPyConIO.printf("==>074\r\n")
    EfiPyConIO.printf("==>075\r\n")
    EfiPyConIO.printf("==>076\r\n")
    EfiPyConIO.printf("==>077\r\n")
    EfiPyConIO.printf("==>078\r\n")
    EfiPyConIO.printf("==>079\r\n")
    EfiPyConIO.printf("==>080\r\n")
    EfiPyConIO.printf("==>081\r\n")
    EfiPyConIO.printf("==>082\r\n")
    EfiPyConIO.printf("==>083\r\n")
    EfiPyConIO.printf("==>084\r\n")
    EfiPyConIO.printf("==>085\r\n")
    EfiPyConIO.printf("==>086\r\n")
    EfiPyConIO.printf("==>087\r\n")
    EfiPyConIO.printf("==>088\r\n")
    EfiPyConIO.printf("==>089\r\n")
    EfiPyConIO.printf("==>090\r\n")
    EfiPyConIO.printf("==>091\r\n")
    EfiPyConIO.printf("==>092\r\n")
    EfiPyConIO.printf("==>093\r\n")
    EfiPyConIO.printf("==>094\r\n")
    EfiPyConIO.printf("==>095\r\n")
    EfiPyConIO.printf("==>096\r\n")
    EfiPyConIO.printf("==>097\r\n")
    EfiPyConIO.printf("==>098\r\n")
    EfiPyConIO.printf("==>099\r\n")
    EfiPyConIO.printf("==>100\r\n")
    EfiPyConIO.printf("==>101\r\n")
    EfiPyConIO.printf("==>102\r\n")
    EfiPyConIO.printf("==>103\r\n")
    EfiPyConIO.printf("==>104\r\n")
    EfiPyConIO.printf("==>105\r\n")
    EfiPyConIO.printf("==>106\r\n")
    EfiPyConIO.printf("==>107\r\n")
    EfiPyConIO.printf("==>108\r\n")
    EfiPyConIO.printf("==>109\r\n")
    EfiPyConIO.printf("==>110\r\n")
    EfiPyConIO.printf("==>111\r\n")
    EfiPyConIO.printf("==>112\r\n")
    EfiPyConIO.printf("==>113\r\n")
    EfiPyConIO.printf("==>114\r\n")
    EfiPyConIO.printf("==>115\r\n")
    EfiPyConIO.printf("==>116\r\n")
    EfiPyConIO.printf("==>117\r\n")
    EfiPyConIO.printf("==>118\r\n")
    EfiPyConIO.printf("==>119\r\n")
    EfiPyConIO.printf("==>120\r\n")
    EfiPyConIO.printf("==>121\r\n")
    EfiPyConIO.printf("==>122\r\n")
    EfiPyConIO.printf("==>123\r\n")
    EfiPyConIO.printf("==>124\r\n")
    EfiPyConIO.printf("==>125\r\n")
    EfiPyConIO.printf("==>126\r\n")
    EfiPyConIO.printf("==>127\r\n")
    EfiPyConIO.printf("==>128\r\n")
    EfiPyConIO.printf("==>129\r\n")
    EfiPyConIO.printf("==>130\r\n")
    EfiPyConIO.printf("==>131\r\n")
    EfiPyConIO.printf("==>132\r\n")
    EfiPyConIO.printf("==>133\r\n")
    EfiPyConIO.printf("==>134\r\n")
    EfiPyConIO.printf("==>135\r\n")
    EfiPyConIO.printf("==>136\r\n")
    EfiPyConIO.printf("==>137\r\n")
    EfiPyConIO.printf("==>138\r\n")
    EfiPyConIO.printf("==>139\r\n")
    EfiPyConIO.printf("==>140\r\n")
    EfiPyConIO.printf("==>141\r\n")
    EfiPyConIO.printf("==>142\r\n")
    EfiPyConIO.printf("==>143\r\n")
    EfiPyConIO.printf("==>144\r\n")
    EfiPyConIO.printf("==>145\r\n")
    EfiPyConIO.printf("==>146\r\n")
    EfiPyConIO.printf("==>147\r\n")
    EfiPyConIO.printf("==>148\r\n")
    EfiPyConIO.printf("==>149\r\n")
    EfiPyConIO.printf("==>150\r\n")
    EfiPyConIO.printf("==>151\r\n")
    EfiPyConIO.printf("==>152\r\n")
    EfiPyConIO.printf("==>153\r\n")
    EfiPyConIO.printf("==>154\r\n")
    EfiPyConIO.printf("==>155\r\n")
    EfiPyConIO.printf("==>156\r\n")
    EfiPyConIO.printf("==>157\r\n")
    EfiPyConIO.printf("==>158\r\n")
    EfiPyConIO.printf("==>159\r\n")
    EfiPyConIO.printf("==>160\r\n")
    EfiPyConIO.printf("==>161\r\n")
    EfiPyConIO.printf("==>162\r\n")
    EfiPyConIO.printf("==>163\r\n")
    EfiPyConIO.printf("==>164\r\n")
    EfiPyConIO.printf("==>165\r\n")
    EfiPyConIO.printf("==>166\r\n")
    EfiPyConIO.printf("==>167\r\n")
    EfiPyConIO.printf("==>168\r\n")
    EfiPyConIO.printf("==>169\r\n")
    EfiPyConIO.printf("==>170\r\n")
    EfiPyConIO.printf("==>171\r\n")
    EfiPyConIO.printf("==>172\r\n")
    EfiPyConIO.printf("==>173\r\n")
    EfiPyConIO.printf("==>174\r\n")
    EfiPyConIO.printf("==>175\r\n")
    EfiPyConIO.printf("==>176\r\n")
    EfiPyConIO.printf("==>177\r\n")
    EfiPyConIO.printf("==>178\r\n")
    EfiPyConIO.printf("==>179\r\n")
    EfiPyConIO.printf("==>180\r\n")
    EfiPyConIO.printf("==>181\r\n")
    EfiPyConIO.printf("==>182\r\n")
    EfiPyConIO.printf("==>183\r\n")
    EfiPyConIO.printf("==>184\r\n")
    EfiPyConIO.printf("==>185\r\n")
    EfiPyConIO.printf("==>186\r\n")
    EfiPyConIO.printf("==>187\r\n")
    EfiPyConIO.printf("==>188\r\n")
    EfiPyConIO.printf("==>189\r\n")
    EfiPyConIO.printf("==>190\r\n")
    EfiPyConIO.printf("==>191\r\n")
    EfiPyConIO.printf("==>192\r\n")
    EfiPyConIO.printf("==>193\r\n")
    EfiPyConIO.printf("==>194\r\n")
    EfiPyConIO.printf("==>195\r\n")
    EfiPyConIO.printf("==>196\r\n")
    EfiPyConIO.printf("==>197\r\n")
    EfiPyConIO.printf("==>198\r\n")
    EfiPyConIO.printf("==>199\r\n")
    EfiPyConIO.printf("==>200\r\n")
    EfiPyConIO.printf("==>201\r\n")
    EfiPyConIO.printf("==>202\r\n")
    EfiPyConIO.printf("==>203\r\n")
    EfiPyConIO.printf("==>204\r\n")
    EfiPyConIO.printf("==>205\r\n")
    EfiPyConIO.printf("==>206\r\n")
    EfiPyConIO.printf("==>207\r\n")
    EfiPyConIO.printf("==>208\r\n")
    EfiPyConIO.printf("==>209\r\n")
    EfiPyConIO.printf("==>210\r\n")
    EfiPyConIO.printf("==>211\r\n")
    EfiPyConIO.printf("==>212\r\n")
    EfiPyConIO.printf("==>213\r\n")
    EfiPyConIO.printf("==>214\r\n")
    EfiPyConIO.printf("==>215\r\n")
    EfiPyConIO.printf("==>216\r\n")
    EfiPyConIO.printf("==>217\r\n")
    EfiPyConIO.printf("==>218\r\n")
    EfiPyConIO.printf("==>219\r\n")
    EfiPyConIO.printf("==>220\r\n")
    EfiPyConIO.printf("==>221\r\n")
    EfiPyConIO.printf("==>222\r\n")
    EfiPyConIO.printf("==>223\r\n")
    EfiPyConIO.printf("==>224\r\n")
    EfiPyConIO.printf("==>225\r\n")
    EfiPyConIO.printf("==>226\r\n")
    EfiPyConIO.printf("==>227\r\n")
    EfiPyConIO.printf("==>228\r\n")
    EfiPyConIO.printf("==>229\r\n")
    EfiPyConIO.printf("==>230\r\n")
    EfiPyConIO.printf("==>231\r\n")
    EfiPyConIO.printf("==>232\r\n")
    EfiPyConIO.printf("==>233\r\n")
    EfiPyConIO.printf("==>234\r\n")
    EfiPyConIO.printf("==>235\r\n")
    EfiPyConIO.printf("==>236\r\n")
    EfiPyConIO.printf("==>237\r\n")
    EfiPyConIO.printf("==>238\r\n")
    EfiPyConIO.printf("==>239\r\n")
    EfiPyConIO.printf("==>240\r\n")
    EfiPyConIO.printf("==>241\r\n")
    EfiPyConIO.printf("==>242\r\n")
    EfiPyConIO.printf("==>243\r\n")
    EfiPyConIO.printf("==>244\r\n")
    EfiPyConIO.printf("==>245\r\n")
    EfiPyConIO.printf("==>246\r\n")
    EfiPyConIO.printf("==>247\r\n")
    EfiPyConIO.printf("==>248\r\n")
    EfiPyConIO.printf("==>249\r\n")
    EfiPyConIO.printf("==>250\r\n")
    EfiPyConIO.printf("==>251\r\n")
    EfiPyConIO.printf("==>252\r\n")
    EfiPyConIO.printf("==>253\r\n")
    EfiPyConIO.printf("==>254\r\n")
    EfiPyConIO.printf("==>255\r\n")
    EfiPyConIO.printf("==>256\r\n")
    EfiPyConIO.printf("==>257\r\n")
    EfiPyConIO.printf("==>258\r\n")
    EfiPyConIO.printf("==>259\r\n")
    EfiPyConIO.printf("==>260\r\n")
    EfiPyConIO.printf("==>261\r\n")
    EfiPyConIO.printf("==>262\r\n")
    EfiPyConIO.printf("==>263\r\n")
    EfiPyConIO.printf("==>264\r\n")
    EfiPyConIO.printf("==>265\r\n")
    EfiPyConIO.printf("==>266\r\n")
    EfiPyConIO.printf("==>267\r\n")
    EfiPyConIO.printf("==>268\r\n")
    EfiPyConIO.printf("==>269\r\n")
    EfiPyConIO.printf("==>270\r\n")
    EfiPyConIO.printf("==>271\r\n")
    EfiPyConIO.printf("==>272\r\n")
    EfiPyConIO.printf("==>273\r\n")

  except Exception as inst:
    print "DEBUG==>Exit", inst

  print "EXIT...."

  EfiPyConIO.printf([u"4444\r\n", EFI_BACKGROUND_CYAN | EFI_LIGHTBLUE])

  import sys

  sys.exit(0)
