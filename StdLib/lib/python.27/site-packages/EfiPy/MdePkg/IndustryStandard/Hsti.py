#
# Hsti.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Hsti.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from EfiPy.MdePkg.IndustryStandard import *

gAdapterInfoPlatformSecurityGuid      = EFI_GUID(  0x6be272c7, 0x1320, 0x4ccd, ( 0x90, 0x17, 0xd4, 0x61, 0x2c, 0x01, 0x2b, 0x25 ))

PLATFORM_SECURITY_VERSION_VNEXTCS         = 0x00000003

PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE = 0x00000001
PLATFORM_SECURITY_ROLE_PLATFORM_IBV       = 0x00000002
PLATFORM_SECURITY_ROLE_IMPLEMENTOR_OEM    = 0x00000003 
PLATFORM_SECURITY_ROLE_IMPLEMENTOR_ODM    = 0x00000004  

class ADAPTER_INFO_PLATFORM_SECURITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",                     UINT32),
    ("Role",                        UINT32),
    ("ImplementationID",            CHAR16 * 256),
    ("SecurityFeaturesSize",        UINT32)
    # ("SecurityFeaturesRequired",    UINT8),
    # ("SecurityFeaturesImplemented", UINT8),
    # ("SecurityFeaturesVerified",    UINT8),
    # ("ErrorString"                  CHAR16) 
  ]

