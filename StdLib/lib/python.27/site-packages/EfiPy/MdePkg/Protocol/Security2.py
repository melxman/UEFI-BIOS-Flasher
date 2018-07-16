#
# Security2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Security2.py is free software: you can redistribute it and/or
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

gEfiSecurity2ArchProtocolGuid = \
  EFI_GUID (0x94ab2f58, 0x1438, 0x4ef1, (0x91, 0x52, 0x18, 0x94, 0x1a, 0x3a, 0x0e, 0x68 ))

class EFI_SECURITY2_ARCH_PROTOCOL (Structure):
  pass

EFI_SECURITY2_FILE_AUTHENTICATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECURITY2_ARCH_PROTOCOL), # IN        *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN  CONST *DevicePath,
  PVOID,                                # IN        *FileBuffer,
  UINTN,                                # IN        FileSize,
  BOOLEAN                               # IN        BootPolicy
  )

EFI_SECURITY2_ARCH_PROTOCOL._fields_ = [
    ("FileAuthentication", EFI_SECURITY2_FILE_AUTHENTICATION),
  ]

