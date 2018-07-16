#
# Bluetooth.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Bluetooth.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.IndustryStandard import *

class BLUETOOTH_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Address", UINT8 * 6)
    ]

class BLUETOOTH_CLASS_OF_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FormatType",        UINT8,  2),
    ("MinorDeviceClass",  UINT8,  6),
    ("MajorDeviceClass",  UINT16, 5),
    ("MajorServiceClass", UINT16, 11)
    ]

BLUETOOTH_HCI_COMMAND_LOCAL_READABLE_NAME_MAX_SIZE    = 248

BLUETOOTH_HCI_LINK_KEY_SIZE                           = 16

