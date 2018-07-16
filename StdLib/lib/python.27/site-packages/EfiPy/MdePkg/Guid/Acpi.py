# 
# Acpi.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Acpi.py is free software: you can redistribute it and/or
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

gEfiAcpi10TableGuid      = EFI_GUID(  0xeb9d2d30, 0x2d88, 0x11d3, (0x9a, 0x16, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))
gEfiAcpi20TableGuid       = EFI_GUID( 0x8868e871, 0xe4f1, 0x11d3, (0xbc, 0x22, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))
gEfiAcpiTableGuid         = gEfiAcpi20TableGuid
