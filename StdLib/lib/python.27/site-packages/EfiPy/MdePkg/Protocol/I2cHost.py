#
# I2cHost.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# I2cHost.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Pi import PiI2c

gEfiI2cHostProtocolGuid =   \
  EFI_GUID (0xa5aab9e3, 0xc727, 0x48cd, ( 0x8b, 0xbf, 0x42, 0x72, 0x33, 0x85, 0x49, 0x48 ))

class EFI_I2C_HOST_PROTOCOL (Structure):
  pass

EFI_I2C_HOST_PROTOCOL_QUEUE_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_HOST_PROTOCOL),         # IN CONST  *This
  UINTN,                                  # IN        I2cBusConfiguration,
  UINTN,                                  # IN        SlaveAddress,
  EFI_EVENT,                              # IN        Event      OPTIONAL,
  POINTER(PiI2c.EFI_I2C_REQUEST_PACKET),  # IN        *RequestPacket,
  POINTER(EFI_STATUS)                     # OUT       *I2cStatus OPTIONAL
  )

EFI_I2C_HOST_PROTOCOL._fields_ = [
    ("QueueRequest",              EFI_I2C_HOST_PROTOCOL_QUEUE_REQUEST),
    ("I2cControllerCapabilities", POINTER(PiI2c.EFI_I2C_CONTROLLER_CAPABILITIES))
  ]

