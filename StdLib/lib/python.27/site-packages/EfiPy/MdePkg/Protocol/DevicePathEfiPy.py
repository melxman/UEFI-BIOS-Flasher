#
# DevicePathEfiPy.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# DevicePathEfiPy.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
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

from EfiPy            import *
from DevicePath       import *
from DevicePathToText import *

DevToTextProtocol = None

if DevToTextProtocol == None:
  Interface = PVOID ()
  Status = gBS.LocateProtocol (byref (gEfiDevicePathToTextProtocolGuid), None, byref (Interface))
  if not EFI_ERROR (Status):
    DevToTextProtocol = cast (Interface, POINTER(EFI_DEVICE_PATH_TO_TEXT_PROTOCOL))[0]

def EfiPyDevToText (self):

  if DevToTextProtocol == None:
    return None

  return DevToTextProtocol.ConvertDevicePathToText (self, self.DisplayOnly, self.AllowShortcuts)

  return u"TestBook"

EFIPY_DEVICE_PATH_STRUCTURE.__str__ = EfiPyDevToText
EFI_DEVICE_PATH_PROTOCOL.__str__    = EfiPyDevToText
