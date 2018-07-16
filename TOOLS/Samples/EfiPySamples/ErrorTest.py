#
# ErrorTest.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# ErrorTest.py is free software: you can redistribute it and/or modify
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

import traceback
import EfiPy

from EfiPy.MdePkg.Protocol.SimpleTextOut import     \
                    gEfiSimpleTextOutProtocolGuid,  \
                    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL

try:
  Status = EfiPy.gBS.LocateProtocol (
             EfiPy.byref (gEfiSimpleTextOutProtocolGuid),
             None,
             EfiPy.byref (Interface)
             )

except:
  print "Exception Test"
  print traceback.format_exc()
