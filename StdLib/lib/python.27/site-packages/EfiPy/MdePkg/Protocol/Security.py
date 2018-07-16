#
# Security.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Security.py is free software: you can redistribute it and/or
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

gEfiSecurityArchProtocolGuid  = \
  EFI_GUID (0xA46423E3, 0x4617, 0x49f1, (0xB9, 0xFF, 0xD1, 0xBF, 0xA9, 0x11, 0x58, 0x39 ))

class EFI_SECURITY_ARCH_PROTOCOL (Structure):
  pass

EFI_SECURITY_FILE_AUTHENTICATION_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECURITY_ARCH_PROTOCOL),    # IN        *This
  UINT32,                                 # IN        AuthenticationStatus,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)       # IN  CONST *File
  )

EFI_SECURITY_ARCH_PROTOCOL._fields_ = [
    ("FileAuthenticationState", EFI_SECURITY_FILE_AUTHENTICATION_STATE),
  ]

