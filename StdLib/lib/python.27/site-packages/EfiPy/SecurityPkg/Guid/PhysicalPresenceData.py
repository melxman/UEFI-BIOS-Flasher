#
# PhysicalPresenceData.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# PhysicalPresenceData.py is free software: you can redistribute it and/or
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

gEfiPhysicalPresenceGuid = \
  EFI_GUID (0xf6499b1, 0xe9ad, 0x493d, ( 0xb9, 0xc2, 0x2f, 0x90, 0x81, 0x5c, 0x6c, 0xbc))

PHYSICAL_PRESENCE_VARIABLE  = u"PhysicalPresence"

class EFI_PHYSICAL_PRESENCE (Structure):
  _fields_ = [
  ("PPRequest",       UINT8),
  ("LastPPRequest",   UINT8),
  ("PPResponse",      UINT32)
  ]

PHYSICAL_PRESENCE_NO_ACTION                               = 0
PHYSICAL_PRESENCE_ENABLE                                  = 1
PHYSICAL_PRESENCE_DISABLE                                 = 2
PHYSICAL_PRESENCE_ACTIVATE                                = 3
PHYSICAL_PRESENCE_DEACTIVATE                              = 4 
PHYSICAL_PRESENCE_CLEAR                                   = 5
PHYSICAL_PRESENCE_ENABLE_ACTIVATE                         = 6
PHYSICAL_PRESENCE_DEACTIVATE_DISABLE                      = 7
PHYSICAL_PRESENCE_SET_OWNER_INSTALL_TRUE                  = 8
PHYSICAL_PRESENCE_SET_OWNER_INSTALL_FALSE                 = 9
PHYSICAL_PRESENCE_ENABLE_ACTIVATE_OWNER_TRUE              = 10
PHYSICAL_PRESENCE_DEACTIVATE_DISABLE_OWNER_FALSE          = 11
PHYSICAL_PRESENCE_DEFERRED_PP_UNOWNERED_FIELD_UPGRADE     = 12
PHYSICAL_PRESENCE_SET_OPERATOR_AUTH                       = 13
PHYSICAL_PRESENCE_CLEAR_ENABLE_ACTIVATE                   = 14
PHYSICAL_PRESENCE_SET_NO_PPI_PROVISION_FALSE              = 15
PHYSICAL_PRESENCE_SET_NO_PPI_PROVISION_TRUE               = 16
PHYSICAL_PRESENCE_SET_NO_PPI_CLEAR_FALSE                  = 17
PHYSICAL_PRESENCE_SET_NO_PPI_CLEAR_TRUE                   = 18
PHYSICAL_PRESENCE_SET_NO_PPI_MAINTENANCE_FALSE            = 19
PHYSICAL_PRESENCE_SET_NO_PPI_MAINTENANCE_TRUE             = 20
PHYSICAL_PRESENCE_ENABLE_ACTIVATE_CLEAR                   = 21
PHYSICAL_PRESENCE_ENABLE_ACTIVATE_CLEAR_ENABLE_ACTIVATE   = 22

PHYSICAL_PRESENCE_FLAGS_VARIABLE  = u"PhysicalPresenceFlags"

class EFI_PHYSICAL_PRESENCE_FLAGS (Structure):
  _fields_ = [
  ("PPFlags", UINT8)
  ]

FLAG_NO_PPI_PROVISION                    = BIT0
FLAG_NO_PPI_CLEAR                        = BIT1
FLAG_NO_PPI_MAINTENANCE                  = BIT2
FLAG_RESET_TRACK                         = BIT3

