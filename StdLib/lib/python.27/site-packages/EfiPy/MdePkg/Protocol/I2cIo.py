#
# I2cIo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# I2cIo.py is free software: you can redistribute it and/or
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

gEfiI2cIoProtocolGuid = \
  EFI_GUID (0xb60a3e6b, 0x18c4, 0x46e5, ( 0xa2, 0x9a, 0xc9, 0xa1, 0x06, 0x65, 0xa2, 0x8e ))

class EFI_I2C_IO_PROTOCOL (Structure):
  pass

EFI_I2C_IO_PROTOCOL_QUEUE_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_IO_PROTOCOL),           # IN CONST  *This
  UINTN,                                  # IN  SlaveAddressIndex,
  EFI_EVENT,                              # IN  Event      OPTIONAL,
  POINTER(PiI2c.EFI_I2C_REQUEST_PACKET),  # IN  *RequestPacket,
  POINTER(EFI_STATUS)                     # OUT *I2cStatus OPTIONAL
  )

EFI_I2C_IO_PROTOCOL._fields_ = [
    ("QueueRequest",              EFI_I2C_IO_PROTOCOL_QUEUE_REQUEST),
    ("DeviceGuid",                POINTER(EFI_GUID)),
    ("DeviceIndex",               UINT32),
    ("HardwareRevision",          UINT32),
    ("I2cControllerCapabilities", POINTER(PiI2c.EFI_I2C_CONTROLLER_CAPABILITIES))
  ]

