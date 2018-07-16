#
# SmBus.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SmBus.py is free software: you can redistribute it and/or modify
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

from EfiPy.MdePkg.IndustryStandard import *

class EFI_SMBUS_UDID (Structure):
  _fields_ = [
    ("VendorSpecificId",    UINT32),
    ("SubsystemDeviceId",   UINT16),
    ("SubsystemVendorId",   UINT16),
    ("Interface",           UINT16),
    ("DeviceId",            UINT16),
    ("VendorId",            UINT16),
    ("VendorRevision",      UINT8),
    ("DeviceCapabilities",  UINT8),
  ]

class EFI_SMBUS_DEVICE_ADDRESS (Structure):
  _fields_ = [
    ("SmbusDeviceAddress",    UINTN, 7)
  ]

class EFI_SMBUS_DEVICE_MAP (Structure):
  _fields_ = [
    ("SmbusDeviceAddress",  EFI_SMBUS_DEVICE_ADDRESS),
    ("SmbusDeviceUdid",     EFI_SMBUS_UDID)
  ]

EfiSmbusQuickRead       =  0
EfiSmbusQuickWrite      =  1
EfiSmbusReceiveByte     =  2
EfiSmbusSendByte        =  3
EfiSmbusReadByte        =  4
EfiSmbusWriteByte       =  5
EfiSmbusReadWord        =  6
EfiSmbusWriteWord       =  7
EfiSmbusReadBlock       =  8
EfiSmbusWriteBlock      =  9
EfiSmbusProcessCall     = 10
EfiSmbusBWBRProcessCall = 11
EFI_SMBUS_OPERATION = ENUM

EFI_SMBUS_DEVICE_COMMAND = UINTN

