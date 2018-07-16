#
# AuthenticatedVariableFormat.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# AuthenticatedVariableFormat.py is free software: you can redistribute it and/or
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

from EfiPy  import *

gEfiSecureBootEnableDisableGuid = \
  EFI_GUID (0xf0a30bc7, 0xaf08, 0x4556, (0x99, 0xc4, 0x0, 0x10, 0x9, 0xc9, 0x3a, 0x44))

gEfiCertDbGuid = \
  EFI_GUID (0xd9bee56e, 0x75dc, 0x49d9, (0xb4, 0xd7, 0xb5, 0x34, 0x21, 0xf, 0x63, 0x7a))

gEfiCustomModeEnableGuid = \
  EFI_GUID (0xc076ec0c, 0x7028, 0x4399, (0xa0, 0x72, 0x71, 0xee, 0x5c, 0x44, 0x8b, 0x9f))

gEfiVendorKeysNvGuid = \
  EFI_GUID (0x9073e4e0, 0x60ec, 0x4b6e, (0x99, 0x3, 0x4c, 0x22, 0x3c, 0x26, 0xf, 0x3c))

gEdkiiSecureBootModeGuid = \
  EFI_GUID (0xc573b77, 0xeb93, 0x4d3d, (0xaf, 0xfc, 0x5f, 0xeb, 0xca, 0xfb, 0x65, 0xb0))

EFI_SECURE_BOOT_ENABLE_NAME      = u"SecureBootEnable"
SECURE_BOOT_ENABLE               = 1
SECURE_BOOT_DISABLE              = 0

EFI_CUSTOM_MODE_NAME          = u"CustomMode"
CUSTOM_SECURE_BOOT_MODE       = 1
STANDARD_SECURE_BOOT_MODE     = 0

EFI_VENDOR_KEYS_NV_VARIABLE_NAME       = u"VendorKeysNv"
VENDOR_KEYS_VALID             = 1
VENDOR_KEYS_MODIFIED          = 0

