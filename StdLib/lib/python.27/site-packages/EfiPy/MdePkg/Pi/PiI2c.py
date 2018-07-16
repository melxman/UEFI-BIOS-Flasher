#
# PiI2c.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiI2c.py is free software: you can redistribute it and/or
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

from EfiPy import *

I2C_ADDRESSING_10_BIT     = 0x80000000

class EFI_I2C_CONTROLLER_CAPABILITIES (Structure):
  _fields_ = [
    ("StructureSizeInBytes",  UINT32),
    ("MaximumReceiveBytes",   UINT32),
    ("MaximumTransmitBytes",  UINT32),
    ("MaximumTotalBytes",     UINT32)
  ]

class EFI_I2C_DEVICE (Structure):
  _fields_ = [
    ("DeviceGuid",          POINTER(EFI_GUID)),
    ("DeviceIndex",         UINT32),
    ("HardwareRevision",    UINT32),
    ("I2cBusConfiguration", UINT32),
    ("SlaveAddressCount",   UINT32),
    ("SlaveAddressArray",   POINTER(UINT32))
  ]

I2C_FLAG_READ               = 0x00000001
I2C_FLAG_SMBUS_OPERATION    = 0x00010000
I2C_FLAG_SMBUS_BLOCK        = 0x00020000
I2C_FLAG_SMBUS_PROCESS_CALL = 0x00040000
I2C_FLAG_SMBUS_PEC          = 0x00080000

class EFI_I2C_OPERATION (Structure):
  _fields_ = [
    ("Flags",         UINT32),
    ("LengthInBytes", UINT32),
    ("Buffer",        POINTER(UINT8))
  ]

class EFI_I2C_REQUEST_PACKET (Structure):
  _fields_ = [
    ("OperationCount",  UINTN),
    ("Operation",       EFI_I2C_OPERATION * 1)
  ]

