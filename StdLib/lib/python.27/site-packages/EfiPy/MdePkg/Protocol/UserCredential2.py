#
# UserCredential2.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UserCredential2.py is free software: you can redistribute it and/or
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

import UserManager

from EfiPy.MdePkg.Uefi  import UefiInternalFormRepresentation

gEfiUserCredential2ProtocolGuid = \
  EFI_GUID (0xe98adb03, 0xb8b9, 0x4af8, ( 0xba, 0x20, 0x26, 0xe9, 0x11, 0x4c, 0xbc, 0xe5 ))

class EFI_USER_CREDENTIAL2_PROTOCOL (Structure):
  pass

EFI_CREDENTIAL2_ENROLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL), # IN  CONST *This
  UserManager.EFI_USER_PROFILE_HANDLE     # IN         User
  )

EFI_CREDENTIAL2_FORM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),                 # IN  CONST *This
  POINTER(UefiInternalFormRepresentation.EFI_HII_HANDLE), #     OUT   *Hii,
  POINTER(EFI_GUID),                                      #     OUT   *FormSetId,
  POINTER(UefiInternalFormRepresentation.EFI_FORM_ID)     #     OUT   *FormId
  )

EFI_CREDENTIAL2_TILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),                 # IN CONST *This,
  POINTER(UINTN),                                         # IN OUT   *Width,
  POINTER(UINTN),                                         # IN OUT   *Height,
  POINTER(UefiInternalFormRepresentation.EFI_HII_HANDLE), # OUT      *Hii,
  POINTER(UefiInternalFormRepresentation.EFI_IMAGE_ID)    # OUT      *Image
  )

EFI_CREDENTIAL2_TITLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),                 # IN CONST *This,
  POINTER(UefiInternalFormRepresentation.EFI_HII_HANDLE), # OUT      *Hii,
  POINTER(UefiInternalFormRepresentation.EFI_STRING_ID)   # OUT      *String
  )

EFI_CREDENTIAL2_USER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),               # IN CONST *This,
  UserManager.EFI_USER_PROFILE_HANDLE,                  # IN       User,
  POINTER(UserManager.EFI_USER_INFO_IDENTIFIER)         # OUT      *Identifier
  )

EFI_CREDENTIAL2_SELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),               # IN CONST *This,
  POINTER(UserManager.EFI_CREDENTIAL_LOGON_FLAGS)       # OUT      *AutoLogon
  )

EFI_CREDENTIAL2_DESELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL)  # IN CONST *This,
  )

EFI_CREDENTIAL2_DEFAULT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),         # IN CONST  *This,
  POINTER(UserManager.EFI_CREDENTIAL_LOGON_FLAGS) # OUT       *AutoLogon
  )

EFI_CREDENTIAL2_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL), # IN CONST  *This,
  UserManager.EFI_USER_INFO_HANDLE,       # IN        UserInfo,
  POINTER(UserManager.EFI_USER_INFO),     # OUT       *Info,
  POINTER(UINTN)                          # IN OUT    *InfoSize
  )

EFI_CREDENTIAL2_GET_NEXT_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST  *This,
  POINTER(UserManager.EFI_USER_INFO_HANDLE) # IN OUT    *UserInfo
  )

EFI_CREDENTIAL2_DELETE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),       # IN CONST  *This,
  POINTER(UserManager.EFI_USER_PROFILE_HANDLE)  # IN        User
  )

EFI_USER_CREDENTIAL2_PROTOCOL._fields_ = [
    ("Identifier",    EFI_GUID),
    ("Type",          EFI_GUID),
    ("Enroll",        EFI_CREDENTIAL2_ENROLL),
    ("Form",          EFI_CREDENTIAL2_FORM),
    ("Tile",          EFI_CREDENTIAL2_TILE),
    ("Title",         EFI_CREDENTIAL2_TITLE),
    ("User",          EFI_CREDENTIAL2_USER),
    ("Select",        EFI_CREDENTIAL2_SELECT),
    ("Deselect",      EFI_CREDENTIAL2_DESELECT),
    ("Default",       EFI_CREDENTIAL2_DEFAULT),
    ("GetInfo",       EFI_CREDENTIAL2_GET_INFO),
    ("GetNextInfo",   EFI_CREDENTIAL2_GET_NEXT_INFO),
    ("Capabilities",  UserManager.EFI_CREDENTIAL_CAPABILITIES),
    ("Delete",        EFI_CREDENTIAL2_DELETE)
  ]
