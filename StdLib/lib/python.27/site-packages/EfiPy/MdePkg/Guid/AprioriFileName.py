#
# AprioriFileName.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# AprioriFileName.py is free software: you can redistribute it and/or
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

gPeiAprioriFileNameGuid = \
  EFI_GUID (0x1b45cc0a, 0x156a, 0x428a, ( 0x62, 0XAF, 0x49, 0x86, 0x4d, 0xa0, 0xe6, 0xe6 ))

class PEI_APRIORI_FILE_CONTENTS (Structure):
  _fields_ = [
    ("FileNamesWithinVolume",  EFI_GUID * 1)
  ]

