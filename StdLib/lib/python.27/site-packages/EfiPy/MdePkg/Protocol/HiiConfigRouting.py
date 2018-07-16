#
# HiiConfigRouting.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# HiiConfigRouting.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import \
      EFI_STRING

gEfiHiiConfigRoutingProtocolGuid  = \
  EFI_GUID (0x587e72d7, 0xcc50, 0x4f79, ( 0x82, 0x09, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0x0f ))

class EFI_HII_CONFIG_ROUTING_PROTOCOL (Structure):
  pass

EFI_HII_EXTRACT_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  EFI_STRING,                               # IN CONST Request,
  POINTER(EFI_STRING),                      # OUT      *Progress,
  POINTER(EFI_STRING)                       # OUT      *Results
  )

EFI_HII_EXPORT_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  POINTER(EFI_STRING)                       # OUT      *Results
  )

EFI_HII_ROUTE_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  EFI_STRING,                               # IN CONST Configuration,
  POINTER(EFI_STRING)                       # OUT      *Progress
  )

EFI_HII_BLOCK_TO_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  POINTER(EFI_STRING),                      # IN CONST ConfigRequest,
  POINTER(UINT8),                           # IN CONST *Block,
  UINTN,                                    # IN CONST BlockSize,
  POINTER(EFI_STRING),                      # OUT      *Config,
  POINTER(EFI_STRING)                       # OUT      *Progress
  )

EFI_HII_CONFIG_TO_BLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN        *This
  EFI_STRING,                               # IN CONST  ConfigResp,
  POINTER(UINT8),                           # IN OUT    *Block,
  POINTER(UINTN),                           # IN OUT    *BlockSize,
  POINTER(EFI_STRING)                       # OUT       *Progress
  )

EFI_HII_GET_ALT_CFG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN        *This
  EFI_STRING,                               # IN  CONST ConfigResp, 
  POINTER(EFI_GUID),                        # IN  CONST *Guid, 
  EFI_STRING,                               # IN  CONST Name, 
  POINTER(EFI_DEVICE_PATH_PROTOCOL),        # IN  CONST *DevicePath,  
  POINTER(UINT16),                          # IN  CONST *AltCfgId,
  POINTER(EFI_STRING)                       # OUT       *AltCfgResp 
  )

EFI_HII_CONFIG_ROUTING_PROTOCOL._fields_ = [
    ("ExtractConfig", EFI_HII_EXTRACT_CONFIG),
    ("ExportConfig",  EFI_HII_EXPORT_CONFIG),
    ("RouteConfig",   EFI_HII_ROUTE_CONFIG),
    ("BlockToConfig", EFI_HII_BLOCK_TO_CONFIG),
    ("ConfigToBlock", EFI_HII_CONFIG_TO_BLOCK),
    ("GetAltConfig",  EFI_HII_GET_ALT_CFG)
  ]

