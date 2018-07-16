#
# SuperIoControl.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# SuperIoControl.py is free software: you can redistribute it and/or
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

gEfiSioControlProtocolGuid    = \
  EFI_GUID (0xb91978df, 0x9fc1, 0x427d, ( 0xbb, 0x5, 0x4c, 0x82, 0x84, 0x55, 0xca, 0x27 ))

class EFI_SIO_CONTROL_PROTOCOL (Structure):
  pass
PEFI_SIO_CONTROL_PROTOCOL       = POINTER (EFI_SIO_CONTROL_PROTOCOL)

EFI_SIO_CONTROL_ENABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_CONTROL_PROTOCOL)     # IN      *This
  )

EFI_SIO_CONTROL_DISABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_CONTROL_PROTOCOL)     # IN      *This
  )

EFI_SIO_CONTROL_PROTOCOL._fields_ = [
    ("Version",       UINT32),
    ("EnableDevice",  EFI_SIO_CONTROL_ENABLE),
    ("DisableDevice", EFI_SIO_CONTROL_DISABLE)
  ]

