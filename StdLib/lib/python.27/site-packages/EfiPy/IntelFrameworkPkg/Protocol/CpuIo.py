#
# CpuIo.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# CpuIo.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Protocol.CpuIo2 import EFI_CPU_IO2_PROTOCOL

gEfiCpuIoProtocolGuid = \
  EFI_GUID (0xB0732526, 0x38C8, 0x4b40, (0x88, 0x77, 0x61, 0xC7, 0xB0, 0x6A, 0xAC, 0x45))

EFI_CPU_IO_PROTOCOL = EFI_CPU_IO2_PROTOCOL

