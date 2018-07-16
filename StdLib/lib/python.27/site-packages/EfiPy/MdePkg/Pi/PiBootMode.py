#
# PiBootMode.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PiBootMode.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

from EfiPy import *

EFI_BOOT_MODE     = UINT32
BOOT_WITH_FULL_CONFIGURATION                  = 0x00
BOOT_WITH_MINIMAL_CONFIGURATION               = 0x01
BOOT_ASSUMING_NO_CONFIGURATION_CHANGES        = 0x02
BOOT_WITH_FULL_CONFIGURATION_PLUS_DIAGNOSTICS = 0x03
BOOT_WITH_DEFAULT_SETTINGS                    = 0x04
BOOT_ON_S4_RESUME                             = 0x05
BOOT_ON_S5_RESUME                             = 0x06
BOOT_WITH_MFG_MODE_SETTINGS                   = 0x07
BOOT_ON_S2_RESUME                             = 0x10
BOOT_ON_S3_RESUME                             = 0x11
BOOT_ON_FLASH_UPDATE                          = 0x12
BOOT_IN_RECOVERY_MODE                         = 0x20

