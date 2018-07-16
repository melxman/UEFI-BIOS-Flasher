#
# GuidedSectionExtraction.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# GuidedSectionExtraction.py is free software: you can redistribute it and/or
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

class EFI_GUIDED_SECTION_EXTRACTION_PROTOCOL (Structure):
  pass

EFI_EXTRACT_GUIDED_SECTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUIDED_SECTION_EXTRACTION_PROTOCOL),  # IN        *This
  PVOID,                                            # IN CONST  *InputSection,
  POINTER(PVOID),                                   # OUT       **OutputBuffer,
  POINTER(UINTN),                                   # OUT       *OutputSize,
  POINTER(UINT32)                                   # OUT       *AuthenticationStatus
  )

EFI_GUIDED_SECTION_EXTRACTION_PROTOCOL._fields_ = [
  ("ExtractSection",    EFI_EXTRACT_GUIDED_SECTION),
  ]

