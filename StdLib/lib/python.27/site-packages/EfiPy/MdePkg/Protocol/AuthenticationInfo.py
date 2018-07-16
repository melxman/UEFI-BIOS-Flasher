#
# AuthenticationInfo.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# AuthenticationInfo.py is free software: you can redistribute it and/or
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

gEfiAuthenticationInfoProtocolGuid  = \
  EFI_GUID (0x7671d9d0, 0x53db, 0x4173, (0xaa, 0x69, 0x23, 0x27, 0xf2, 0x1f, 0x0b, 0xc7 ))

gEfiAuthenticationChapRadiusGuid    = \
  EFI_GUID (0xd6062b50, 0x15ca, 0x11da, (0x92, 0x19, 0x00, 0x10, 0x83, 0xff, 0xca, 0x4d ))

gEfiAuthenticationChapLocalGuid     = \
  EFI_GUID (0xc280c73e, 0x15ca, 0x11da, (0xb0, 0xca, 0x00, 0x10, 0x83, 0xff, 0xca, 0x4d ))

class EFI_AUTHENTICATION_INFO_PROTOCOL (Structure):
  pass

class AUTH_NODE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Guid",    EFI_GUID),
    ("Length",  UINT16)
  ]

class CHAP_RADIUS_AUTH_NODE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                    AUTH_NODE_HEADER),
    ("RadiusIpAddr",              UINT8 * 16),
    ("Reserved",                  UINT16),
    ("NasIpAddr",                 UINT8 * 16),
    ("NasSecretLength",           UINT16),
    ("NasSecret",                 UINT8 * 1)
    # ("ChapSecretLength",        UINT16),
    # ("ChapSecret",              UINT8 * N),
    # ("ChapNameLength",          UINT16),
    # ("ChapName",                UINT8 * N),
    # ("ReverseChapNameLength",   UINT16),
    # ("ReverseChapName",         UINT8 * N),
    # ("ReverseChapSecretLength", UINT16),
    # ("ReverseChapSecret",       UINT8 * N)
  ]

class CHAP_LOCAL_AUTH_NODE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                    AUTH_NODE_HEADER),
    ("Reserved",                  UINT16),
    ("UserSecretLength",          UINT16),
    ("UserSecret",                UINT8 * 1)
    # ("UserNameLength",          UINT16),
    # ("UserName",                UINT8 * N),
    # ("ChapSecretLength",        UINT16),
    # ("ChapSecret",              UINT8 * N),
    # ("ChapNameLength",          UINT16),
    # ("ChapName",                UINT8 * N),
    # ("ReverseChapNameLength",   UINT16),
    # ("ReverseChapName",         UINT8 * N),
    # ("ReverseChapSecretLength", UINT16),
    # ("ReverseChapSecret",       UINT8 * N)
  ]

EFI_AUTHENTICATION_INFO_PROTOCOL_GET = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_AUTHENTICATION_INFO_PROTOCOL), # IN  *This
  EFI_HANDLE,                                 # IN  ControllerHandle,
  POINTER (PVOID)                             # OUT **Buffer
  )

EFI_AUTHENTICATION_INFO_PROTOCOL_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_AUTHENTICATION_INFO_PROTOCOL), # IN  *This
  EFI_HANDLE,                                 # IN  ControllerHandle,
  PVOID                                       # IN  *Buffer
  )

EFI_AUTHENTICATION_INFO_PROTOCOL._fields_ = [
    ("Get", EFI_AUTHENTICATION_INFO_PROTOCOL_GET),
    ("Set", EFI_AUTHENTICATION_INFO_PROTOCOL_SET)
  ]

