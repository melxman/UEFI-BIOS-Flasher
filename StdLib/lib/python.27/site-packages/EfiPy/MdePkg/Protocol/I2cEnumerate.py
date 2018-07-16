#
# I2cEnumerate.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# I2cEnumerate.py is free software: you can redistribute it and/or
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


from EfiPy.MdePkg.Pi.PiI2c import EFI_I2C_DEVICE

gEfiI2cEnumerateProtocolGuid  = \
  EFI_GUID (0xda8cd7c4, 0x1c00, 0x49e2, ( 0x80, 0x3e, 0x52, 0x14, 0xe7, 0x01, 0x89, 0x4c ))

class EFI_I2C_ENUMERATE_PROTOCOL (Structure):
  pass

EFI_I2C_ENUMERATE_PROTOCOL_ENUMERATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_ENUMERATE_PROTOCOL),  # IN CONST  *This
  POINTER(POINTER(EFI_I2C_DEVICE))      # IN OUT    **Device
  )

EFI_I2C_ENUMERATE_PROTOCOL_GET_BUS_FREQUENCY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_ENUMERATE_PROTOCOL),  # IN CONST  *This
  UINTN,                                # IN        I2cBusConfiguration
  POINTER(UINTN)                        #    OUT    *BusClockHertz
  )

EFI_I2C_ENUMERATE_PROTOCOL._fields_ = [
  ("Enumerate",       EFI_I2C_ENUMERATE_PROTOCOL_ENUMERATE),
  ("GetBusFrequency", EFI_I2C_ENUMERATE_PROTOCOL_GET_BUS_FREQUENCY)
  ]

