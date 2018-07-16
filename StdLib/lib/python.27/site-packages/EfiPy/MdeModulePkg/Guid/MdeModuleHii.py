#
# MdeModuleHii.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# MdeModuleHii.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Uefi.UefiInternalFormRepresentation import  EFI_IFR_OP_HEADER,    \
                                                              EFI_STRING_ID,        \
                                                              EFI_QUESTION_ID,      \
                                                              EFI_IFR_TYPE_VALUE

NARROW_CHAR         = 0xFFF0
WIDE_CHAR           = 0xFFF1
NON_BREAKING_CHAR   = 0xFFF2

BROWSER_STATE_VALIDATE_PASSWORD  = 0
BROWSER_STATE_SET_PASSWORD       = 1

gEfiIfrTianoGuid         = \
  EFI_GUID (0xf0b1735, 0x87a0, 0x4193, (0xb2, 0x66, 0x53, 0x8c, 0x38, 0xaf, 0x48, 0xce))

EFI_IFR_EXTEND_OP_LABEL       = 0x0
EFI_IFR_EXTEND_OP_BANNER      = 0x1
EFI_IFR_EXTEND_OP_TIMEOUT     = 0x2
EFI_IFR_EXTEND_OP_CLASS       = 0x3
EFI_IFR_EXTEND_OP_SUBCLASS    = 0x4

class EFI_IFR_GUID_LABEL (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("Number",        UINT16)
  ]

EFI_IFR_BANNER_ALIGN_LEFT     = 0
EFI_IFR_BANNER_ALIGN_CENTER   = 1
EFI_IFR_BANNER_ALIGN_RIGHT    = 2

class EFI_IFR_GUID_LABEL (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("Title",         EFI_STRING_ID),
  ("LineNumber",    UINT16),
  ("Alignment",     UINT8)
  ]

class EFI_IFR_GUID_TIMEOUT (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("TimeOut",       UINT16)
  ]

EFI_NON_DEVICE_CLASS              = 0x00
EFI_DISK_DEVICE_CLASS             = 0x01
EFI_VIDEO_DEVICE_CLASS            = 0x02
EFI_NETWORK_DEVICE_CLASS          = 0x04
EFI_INPUT_DEVICE_CLASS            = 0x08
EFI_ON_BOARD_DEVICE_CLASS         = 0x10
EFI_OTHER_DEVICE_CLASS            = 0x20

class EFI_IFR_GUID_CLASS (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("Class",         UINT16)
  ]

EFI_SETUP_APPLICATION_SUBCLASS    = 0x00
EFI_GENERAL_APPLICATION_SUBCLASS  = 0x01
EFI_FRONT_PAGE_SUBCLASS           = 0x02
EFI_SINGLE_USE_SUBCLASS           = 0x03

class EFI_IFR_GUID_SUBCLASS (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("SubClass",      UINT16)
  ]

gEfiIfrFrameworkGuid         = \
  EFI_GUID (0x31ca5d1a, 0xd511, 0x4931, (0xb7, 0x82, 0xae, 0x6b, 0x2b, 0x17, 0x8c, 0xd7))

EFI_IFR_EXTEND_OP_OPTIONKEY   = 0x0
EFI_IFR_EXTEND_OP_VAREQNAME   = 0x1

class EFI_IFR_GUID_OPTIONKEY (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("QuestionId",    EFI_QUESTION_ID),
  ("OptionValue",   EFI_IFR_TYPE_VALUE),
  ("KeyValue",      UINT16)
  ]

class EFI_IFR_GUID_VAREQNAME (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",        EFI_IFR_OP_HEADER),
  ("Guid",          EFI_GUID),
  ("ExtendOpCode",  UINT8),
  ("QuestionId",    EFI_QUESTION_ID),
  ("NameId",        UINT16)
  ]

