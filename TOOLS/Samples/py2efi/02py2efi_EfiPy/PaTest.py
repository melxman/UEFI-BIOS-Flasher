#
# PaTest.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Panalyzer.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PaTest.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy.Analyzer.Panalyzer import *

from EfiPy.MdePkg.Protocol.SimpleTextOut import gEfiSimpleTextOutProtocolGuid, EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL, EFI_TEXT_CLEAR_SCREEN
from EfiPy.MdePkg.Protocol.SimpleTextIn  import gEfiSimpleTextInProtocolGuid,  EFI_SIMPLE_TEXT_INPUT_PROTOCOL

if __name__ == "__main__":

  def _filter_func (dOut, *args):

    if args[1] != 0x00:
      dOut.msg += "Change args[1] value from 0x%X to 0x00" % args[1]
      args = (args[0], 0x00) + args[2:]

    return None, args

  print "================================"

  dOut = dOutClass()

  dOut.section("Prepare")

  t = pAnalyzer(dOut)
  
  t.Build_Capability (EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)
  t.Detect_Protocol (gEfiSimpleTextOutProtocolGuid, EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)
  
  for target, handle in t.Target:
    t.Filter.append (t.Build_Filter (target, handle))
  
  t.install("Reset")
  t.install("ABCD")
  t.install("OutputString")
  t.install("TestString")
  t.install("QueryMode")
  t.install("SetMode")
  t.install("SetAttribute")
  t.install("ClearScreen")
  t.install("SetCursorPosition")
  t.start("asd")
  t.start("QueryMode")
  t.debug_dump ()

  dOut.section("Testing_1")

  EfiPy.gST.ConOut[0].TestString (EfiPy.gST.ConOut, u"This is test\r\n")
  EfiPy.gST.ConOut[0].OutputString (EfiPy.gST.ConOut, u"This is test\r\n")
  EfiPy.gST.ConOut[0].ClearScreen (EfiPy.gST.ConOut)

  ModeNumber = EfiPy.UINTN (0)
  Columns    = EfiPy.UINTN (0)
  Rows       = EfiPy.UINTN (0)

  EfiPy.gST.ConOut[0].QueryMode (EfiPy.gST.ConOut, ModeNumber, EfiPy.byref (Columns), EfiPy.byref (Rows))

  ModeNumber = EfiPy.UINTN (1)
  Columns    = EfiPy.UINTN (0)
  Rows       = EfiPy.UINTN (0)
  EfiPy.gST.ConOut[0].QueryMode (EfiPy.gST.ConOut, ModeNumber, EfiPy.byref (Columns), EfiPy.byref (Rows))

  dOut.section("Testing_2")

  t.install("QueryMode", _filter_func)

  ModeNumber = EfiPy.UINTN (10)
  Columns    = EfiPy.UINTN (0)
  Rows       = EfiPy.UINTN (0)
  EfiPy.gST.ConOut[0].QueryMode (EfiPy.gST.ConOut, ModeNumber, EfiPy.byref (Columns), EfiPy.byref (Rows))

  del (t)

  dOut.section("Testing_3")

  p = pAnalyzer(dOut)
  
  p.Build_Capability (EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)
  p.Filter.append (p.Build_Filter (EfiPy.gST.ConOut))
  
  p.debug_dump ()
  
  p.install("Reset")
  p.install("OutputString")
  p.install("TestString")
  p.install("QueryMode")
  p.install("SetMode")
  p.install("SetAttribute")
  p.install("ClearScreen")
  p.install("SetCursorPosition")
  
  p.start()
  
  EfiPy.gST.ConOut[0].ClearScreen (EfiPy.gST.ConOut)
  EfiPy.gST.StdErr[0].ClearScreen (EfiPy.gST.StdErr)
  
  p.install ("ClearScreen")
  EfiPy.gST.ConOut[0].ClearScreen (EfiPy.gST.ConOut)
  
  p.stop()
  p.uninstall("ClearScreen")
  
  p.debug_dump ()
  p.uninstall("ClearScreen")
  
  del (p)

  dOut.terminate ()
