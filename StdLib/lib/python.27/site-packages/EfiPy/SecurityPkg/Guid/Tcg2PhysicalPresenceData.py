#
# Tcg2PhysicalPresenceData.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Tcg2PhysicalPresenceData.py is free software: you can redistribute it and/or
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

gEfiTcg2PhysicalPresenceGuid = \
  EFI_GUID (0xaeb9c5c1, 0x94f1, 0x4d02, (0xbf, 0xd9, 0x46, 0x2, 0xdb, 0x2d, 0x3c, 0x54))

TCG2_PHYSICAL_PRESENCE_VARIABLE  = u"Tcg2PhysicalPresence"


class EFI_TCG2_PHYSICAL_PRESENCE (Structure):
  _fields_ = [
  ("PPRequest",           UINT8),
  ("PPRequestParameter",  UINT32),
  ("LastPPRequest",       UINT8),
  ("PPResponse",          UINT32)
  ]

TCG2_PHYSICAL_PRESENCE_FLAGS_VARIABLE  = u"Tcg2PhysicalPresenceFlags"

class EFI_TCG2_PHYSICAL_PRESENCE_FLAGS (Structure):
  _fields_ = [
  ("PPFlags",           UINT32)
  ]

