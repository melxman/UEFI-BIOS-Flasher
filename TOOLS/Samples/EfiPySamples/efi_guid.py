#
# efi_guid.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# efi_guid.py is free software: you can redistribute it and/or modify
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

from EfiPy import *
TestGuid1 = EFI_GUID  \
     (0x8D59D32B, 0xC655, 0x4AE9, \
     (0x9B, 0x15, 0xF2, 0x59, 0x04, 0x99, 0x2A, 0x43))
TestGuid2 = EFI_GUID  \
     (0x8D59D32B, 0xC655, 0x4AE9, \
     (0x9B, 0x15, 0xF2, 0x59, 0x04, 0x99, 0x2A, 0x44))

print "TestGuid1 == TestGuid2 :", TestGuid1 == TestGuid2
print "%s" % TestGuid1
