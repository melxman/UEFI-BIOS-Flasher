#
# PaTest3.py
#
# Copyright (C) 2015 - 2018 efipy.core@gmail.com All rights reserved.
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

from pAnalyzer.Panalyzer import *

if __name__ == "__main__":

  DrvList = [u"FS0:\\EFI\\Tools\\Samples\\pAnalyzerSamples\\pAnalyzeDrv.efi"]
  AppList = [u"FS0:\\EFI\\Tools\\Samples\\pAnalyzerSamples\\pAnalyzeApp2.efi"]

  print "================================"

  dOut = dOutClass()

  dOut.section("Prepare")

  t = pAnalyzer(dOut)
  
  t.LoadEfiFiles (DrvList, AppList)

  del (t)

  dOut.terminate ()
