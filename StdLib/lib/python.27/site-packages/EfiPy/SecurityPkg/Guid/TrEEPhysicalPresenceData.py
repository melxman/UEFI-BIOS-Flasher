#
# TrEEPhysicalPresenceData.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# TrEEPhysicalPresenceData.py is free software: you can redistribute it and/or
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

gEfiTrEEPhysicalPresenceGuid = \
  EFI_GUID (0xf24643c2, 0xc622, 0x494e, (0x8a, 0xd, 0x46, 0x32, 0x57, 0x9c, 0x2d, 0x5b))

TREE_PHYSICAL_PRESENCE_VARIABLE  = u"TrEEPhysicalPresence"

class EFI_TREE_PHYSICAL_PRESENCE (Structure):
  _fields_ = [
  ("PPRequest",     UINT8),
  ("LastPPRequest", UINT8),
  ("PPResponse",    UINT32)
  ]

TREE_FLAG_NO_PPI_CLEAR                        = BIT1
TREE_FLAG_RESET_TRACK                         = BIT3
TREE_PHYSICAL_PRESENCE_FLAGS_VARIABLE  = u"TrEEPhysicalPresenceFlags"

class EFI_TREE_PHYSICAL_PRESENCE_FLAGS (Structure):
  _fields_ = [
  ("PPFlags",     UINT8)
  ]

TREE_PHYSICAL_PRESENCE_NO_ACTION                               = 0
TREE_PHYSICAL_PRESENCE_CLEAR_CONTROL_CLEAR                     = 5
TREE_PHYSICAL_PRESENCE_CLEAR_CONTROL_CLEAR_2                   = 14
TREE_PHYSICAL_PRESENCE_SET_NO_PPI_CLEAR_FALSE                  = 17
TREE_PHYSICAL_PRESENCE_SET_NO_PPI_CLEAR_TRUE                   = 18
TREE_PHYSICAL_PRESENCE_CLEAR_CONTROL_CLEAR_3                   = 21
TREE_PHYSICAL_PRESENCE_CLEAR_CONTROL_CLEAR_4                   = 22

TREE_PHYSICAL_PRESENCE_NO_ACTION_MAX                           = 22

