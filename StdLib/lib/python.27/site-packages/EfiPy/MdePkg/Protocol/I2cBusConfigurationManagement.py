#
# I2cBusConfigurationManagement.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# I2cBusConfigurationManagement.py is free software: you can redistribute it and/or
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

gEfiI2cBusConfigurationManagementProtocolGuid = \
  EFI_GUID (0x55b71fb5, 0x17c6, 0x410e, ( 0xb5, 0xbd, 0x5f, 0xa2, 0xe3, 0xd4, 0x46, 0x6b ))

class EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL (Structure):
  pass

EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL_ENABLE_I2C_BUS_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL), # IN *This
  UINTN,                                                  # IN I2cBusConfiguration,
  EFI_EVENT,                                              # IN Event      OPTIONAL,
  POINTER(EFI_STATUS)                                     # IN *I2cStatus OPTIONAL
  )

EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL._fields_ = [
  ("EnableI2cBusConfiguration", EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL_ENABLE_I2C_BUS_CONFIGURATION)
  ]

