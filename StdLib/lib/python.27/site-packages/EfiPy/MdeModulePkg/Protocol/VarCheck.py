#
# VarCheck.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# VarCheck.py is free software: you can redistribute it and/or
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

class EDKII_VAR_CHECK_PROTOCOL (Structure):
  pass

gEdkiiVarCheckProtocolGuid = \
  EFI_GUID (0xaf23b340, 0x97b4, 0x4685, (0x8d, 0x4f, 0xa3, 0xf2, 0x81, 0x69, 0xb2, 0x1d))

VAR_CHECK_SET_VARIABLE_CHECK_HANDLER  = EFI_SET_VARIABLE

EDKII_VAR_CHECK_REGISTER_SET_VARIABLE_CHECK_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  VAR_CHECK_SET_VARIABLE_CHECK_HANDLER, # IN  Handler
  )

VAR_CHECK_VARIABLE_PROPERTY_REVISION  = 0x0001

VAR_CHECK_VARIABLE_PROPERTY_READ_ONLY = BIT0

class VAR_CHECK_VARIABLE_PROPERTY (Structure):
  _fields_ = [
  ("Revision",    UINT16),
  ("Property",    UINT16),
  ("Attributes",  UINT32),
  ("MinSize",     UINTN),
  ("MaxSize",     UINTN)
  ]

class VARIABLE_ENTRY_PROPERTY (Structure):
  _fields_ = [
  ("Guid",              POINTER(EFI_GUID)),
  ("Name",              POINTER(CHAR16)),
  ("VariableProperty",  VAR_CHECK_VARIABLE_PROPERTY)
  ]

EDKII_VAR_CHECK_VARIABLE_PROPERTY_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),                      # IN *Name,
  POINTER(EFI_GUID),                    # IN *Guid,
  POINTER(VAR_CHECK_VARIABLE_PROPERTY)  # IN *VariableProperty
  )

EDKII_VAR_CHECK_VARIABLE_PROPERTY_GET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),                      # IN  *Name,
  POINTER(EFI_GUID),                    # IN  *Guid,
  POINTER(VAR_CHECK_VARIABLE_PROPERTY)  # OUT *VariableProperty
  )

EDKII_VAR_CHECK_PROTOCOL._fields_ = [
  ("RegisterSetVariableCheckHandler",   EDKII_VAR_CHECK_REGISTER_SET_VARIABLE_CHECK_HANDLER),
  ("VariablePropertySet",               EDKII_VAR_CHECK_VARIABLE_PROPERTY_SET),
  ("VariablePropertyGet",               EDKII_VAR_CHECK_VARIABLE_PROPERTY_GET)
  ]

