#
# FrameworkInternalFormRepresentation.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# FrameworkInternalFormRepresentation.py is free software: you can redistribute it and/or
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

STRING_REF  = UINT16

FRAMEWORK_EFI_IFR_FORM_OP                 = 0x01
FRAMEWORK_EFI_IFR_SUBTITLE_OP             = 0x02
FRAMEWORK_EFI_IFR_TEXT_OP                 = 0x03
EFI_IFR_GRAPHIC_OP                        = 0x04
FRAMEWORK_EFI_IFR_ONE_OF_OP               = 0x05
FRAMEWORK_EFI_IFR_CHECKBOX_OP             = 0x06
FRAMEWORK_EFI_IFR_NUMERIC_OP              = 0x07
FRAMEWORK_EFI_IFR_PASSWORD_OP             = 0x08
FRAMEWORK_EFI_IFR_ONE_OF_OPTION_OP        = 0x09
FRAMEWORK_EFI_IFR_SUPPRESS_IF_OP          = 0x0A
EFI_IFR_END_FORM_OP                       = 0x0B
EFI_IFR_HIDDEN_OP                         = 0x0C
EFI_IFR_END_FORM_SET_OP                   = 0x0D
FRAMEWORK_EFI_IFR_FORM_SET_OP             = 0x0E
FRAMEWORK_EFI_IFR_REF_OP                  = 0x0F
EFI_IFR_END_ONE_OF_OP                     = 0x10
FRAMEWORK_EFI_IFR_END_OP                  = EFI_IFR_END_ONE_OF_OP
FRAMEWORK_EFI_IFR_INCONSISTENT_IF_OP      = 0x11
FRAMEWORK_EFI_IFR_EQ_ID_VAL_OP            = 0x12
FRAMEWORK_EFI_IFR_EQ_ID_ID_OP             = 0x13
FRAMEWORK_EFI_IFR_EQ_ID_LIST_OP           = 0x14
FRAMEWORK_EFI_IFR_AND_OP                  = 0x15
FRAMEWORK_EFI_IFR_OR_OP                   = 0x16
FRAMEWORK_EFI_IFR_NOT_OP                  = 0x17
EFI_IFR_END_IF_OP                         = 0x18
EFI_IFR_GRAYOUT_IF_OP                     = 0x19
FRAMEWORK_EFI_IFR_DATE_OP                 = 0x1A
FRAMEWORK_EFI_IFR_TIME_OP                 = 0x1B
FRAMEWORK_EFI_IFR_STRING_OP               = 0x1C
EFI_IFR_LABEL_OP                          = 0x1D
EFI_IFR_SAVE_DEFAULTS_OP                  = 0x1E
EFI_IFR_RESTORE_DEFAULTS_OP               = 0x1F
EFI_IFR_BANNER_OP                         = 0x20
EFI_IFR_INVENTORY_OP                      = 0x21
EFI_IFR_EQ_VAR_VAL_OP                     = 0x22
FRAMEWORK_EFI_IFR_ORDERED_LIST_OP         = 0x23
FRAMEWORK_EFI_IFR_VARSTORE_OP             = 0x24
EFI_IFR_VARSTORE_SELECT_OP                = 0x25
EFI_IFR_VARSTORE_SELECT_PAIR_OP           = 0x26
EFI_IFR_LAST_OPCODE                       = EFI_IFR_VARSTORE_SELECT_PAIR_OP
EFI_IFR_OEM_OP                            = 0xFE
EFI_IFR_NV_ACCESS_COMMAND                 = 0xFF

EFI_IFR_FLAG_DEFAULT            = 0x01
EFI_IFR_FLAG_MANUFACTURING      = 0x02
EFI_IFR_FLAG_INTERACTIVE        = 0x04
EFI_IFR_FLAG_NV_ACCESS          = 0x08
EFI_IFR_FLAG_RESET_REQUIRED     = 0x10
EFI_IFR_FLAG_LATE_CHECK         = 0x20

EFI_NON_DEVICE_CLASS              = 0x00
EFI_DISK_DEVICE_CLASS             = 0x01
EFI_VIDEO_DEVICE_CLASS            = 0x02
EFI_NETWORK_DEVICE_CLASS          = 0x04
EFI_INPUT_DEVICE_CLASS            = 0x08
EFI_ON_BOARD_DEVICE_CLASS         = 0x10
EFI_OTHER_DEVICE_CLASS            = 0x20

EFI_SETUP_APPLICATION_SUBCLASS    = 0x00
EFI_GENERAL_APPLICATION_SUBCLASS  = 0x01
EFI_FRONT_PAGE_SUBCLASS           = 0x02
EFI_SINGLE_USE_SUBCLASS           = 0x03

EFI_IFR_FLAG_CREATED  = 128
class FRAMEWORK_EFI_IFR_OP_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("OpCode", UINT8),
  ("Length", UINT8)
  ]

class FRAMEWORK_EFI_IFR_OP_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",          FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Guid",            EFI_GUID),
  ("FormSetTitle",    STRING_REF),
  ("Help",            STRING_REF),
  ("CallbackHandle",  EFI_PHYSICAL_ADDRESS),
  ("Class",           UINT16),
  ("SubClass",        UINT16),
  ("NvDataSize",      UINT16)
  ]

class FRAMEWORK_EFI_IFR_FORM (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",    FRAMEWORK_EFI_IFR_OP_HEADER),
  ("FormId",    UINT16),
  ("FormTitle", STRING_REF)
  ]

class EFI_IFR_LABEL (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("LabelId", UINT16)
  ]

class FRAMEWORK_EFI_IFR_SUBTITLE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",    FRAMEWORK_EFI_IFR_OP_HEADER),
  ("SubTitle",  STRING_REF)
  ]

class FRAMEWORK_EFI_IFR_TEXT (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Help",    STRING_REF),
  ("Text",    STRING_REF),
  ("TextTwo", STRING_REF),
  ("Flags",   UINT8),
  ("Key",     UINT16)
  ]

class FRAMEWORK_EFI_IFR_REF (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("FormId",  UINT16),
  ("Prompt",  STRING_REF),
  ("Help",    STRING_REF),
  ("Flags",   UINT8),
  ("Key",     UINT16)
  ]

class EFI_IFR_END_FORM (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_END_FORM_SET (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

class FRAMEWORK_EFI_IFR_ONE_OF (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("Prompt",      STRING_REF),
  ("Help",        STRING_REF)      
  ]

class FRAMEWORK_EFI_IFR_ORDERED_LIST (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("MaxEntries",  UINT8),
  ("Prompt",      STRING_REF),
  ("Help",        STRING_REF)
  ]

class FRAMEWORK_EFI_IFR_CHECKBOX (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("Prompt",      STRING_REF),
  ("Help",        STRING_REF),
  ("Flags",       UINT8),
  ("Key",         UINT16)
  ]

EFI_IFR_CHECK_BOX = FRAMEWORK_EFI_IFR_CHECKBOX

class FRAMEWORK_EFI_IFR_ONE_OF_OPTION (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Option",  STRING_REF),
  ("Value",   UINT16),
  ("Flags",   UINT8),
  ("Key",     UINT16)
  ]

class FRAMEWORK_EFI_IFR_NUMERIC (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("Prompt",      STRING_REF),
  ("Help",        STRING_REF),
  ("Flags",       UINT8),
  ("Key",         UINT16),
  ("Minimum",     UINT16),
  ("Maximum",     UINT16),
  ("Step",        UINT16),
  ("Default",     UINT16)
  ]

class FRAMEWORK_EFI_IFR_TIME (Structure):
  _pack_   = 1
  _fields_ = [
  ("Hour",    FRAMEWORK_EFI_IFR_NUMERIC),
  ("Minute",  FRAMEWORK_EFI_IFR_NUMERIC),
  ("Second",  FRAMEWORK_EFI_IFR_NUMERIC)
  ]

class FRAMEWORK_EFI_IFR_DATE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Year",  FRAMEWORK_EFI_IFR_NUMERIC),
  ("Month", FRAMEWORK_EFI_IFR_NUMERIC),
  ("Day",   FRAMEWORK_EFI_IFR_NUMERIC)
  ]

class FRAMEWORK_EFI_IFR_PASSWORD (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("Prompt",      STRING_REF),
  ("Help",        STRING_REF),
  ("Flags",       UINT8),
  ("Key",         UINT16),
  ("MinSize",     UINT8),
  ("MaxSize",     UINT8),
  ("Encoding",    UINT16)
  ]

class FRAMEWORK_EFI_IFR_STRING (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("Prompt",      STRING_REF),
  ("Help",        STRING_REF),
  ("Flags",       UINT8),
  ("Key",         UINT16),
  ("MinSize",     UINT8),
  ("MaxSize",     UINT8)
  ]

class EFI_IFR_END_ONE_OF (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_HIDDEN (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Value",   UINT16),
  ("Key",     UINT16)
  ]

class EFI_IFR_SUPPRESS (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Flags",   UINT8)
  ]

class EFI_IFR_GRAY_OUT (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Flags",   UINT8)
  ]

class EFI_IFR_INCONSISTENT (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Popup",   STRING_REF),
  ("Flags",   UINT8)
  ]

class FRAMEWORK_EFI_IFR_EQ_ID_VAL (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("Value",       UINT16)
  ]

class FRAMEWORK_EFI_IFR_EQ_ID_LIST (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("ListLength",  UINT16),
  ("ValueList",   UINT16 * 1)
  ]

class FRAMEWORK_EFI_IFR_EQ_ID_ID (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("QuestionId",  UINT16),
  ("Width",       UINT8),
  ("QuestionId2", UINT16)
  ]

class EFI_IFR_EQ_VAR_VAL (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("VariableId",  UINT16),
  ("Value",       UINT16)
  ]

class FRAMEWORK_EFI_IFR_AND (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

class FRAMEWORK_EFI_IFR_OR (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

class FRAMEWORK_EFI_IFR_NOT (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_END_EXPR (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER)
  ]

EFI_IFR_END_IF  = EFI_IFR_END_EXPR

class EFI_IFR_SAVE_DEFAULTS (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("FormId",  UINT16),
  ("Prompt",  STRING_REF),
  ("Help",    STRING_REF),
  ("Flags;",  UINT8),
  ("Key",     UINT16)
  ]

class EFI_IFR_INVENTORY (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Help",    STRING_REF),
  ("Text",    STRING_REF),
  ("TextTwo", STRING_REF)
  ]

class FRAMEWORK_EFI_IFR_VARSTORE (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Guid;",   EFI_GUID),
  ("VarId",   UINT16),
  ("Size",    UINT16)
  ]

class EFI_IFR_VARSTORE_SELECT (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",  FRAMEWORK_EFI_IFR_OP_HEADER),
  ("VarId",   UINT16)
  ]

class EFI_IFR_VARSTORE_SELECT_PAIR (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",          FRAMEWORK_EFI_IFR_OP_HEADER),
  ("VarId",           UINT16),
  ("SecondaryVarId",  UINT16),
  ]

EFI_IFR_RESTORE_DEFAULTS  = EFI_IFR_SAVE_DEFAULTS

class EFI_IFR_BANNER (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",      FRAMEWORK_EFI_IFR_OP_HEADER),
  ("Title",       STRING_REF),
  ("LineNumber",  UINT16),
  ("Alignment",   UINT8)
  ]

EFI_IFR_BANNER_ALIGN_LEFT   = 0
EFI_IFR_BANNER_ALIGN_CENTER = 1
EFI_IFR_BANNER_ALIGN_RIGHT  = 2
EFI_IFR_BANNER_TIMEOUT      = 0xFF

