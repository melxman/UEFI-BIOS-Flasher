#
# SectionExtraction.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# SectionExtraction.py is free software: you can redistribute it and/or
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
from EfiPy.MdePkg.Pi.PiFirmwareFile import EFI_SECTION_TYPE

gEfiSectionExtractionProtocolGuid = \
  EFI_GUID (0x448F5DA4, 0x6DD7, 0x4FE1, (0x93, 0x07, 0x69, 0x22, 0x41, 0x92, 0x21, 0x5D))

class EFI_SECTION_EXTRACTION_PROTOCOL (Structure):
  pass

EFI_OPEN_SECTION_STREAM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECTION_EXTRACTION_PROTOCOL),  # IN  *This,
  UINTN,                                     # IN  SectionStreamLength,
  PVOID,                                     # IN  *SectionStream,
  POINTER(UINTN)                             # OUT *SectionStreamHandle
  )

EFI_GET_SECTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECTION_EXTRACTION_PROTOCOL), # IN     *This,
  UINTN,                                    # IN     SectionStreamHandle,
  POINTER(EFI_SECTION_TYPE),                # IN     *SectionType,
  POINTER(EFI_GUID),                        # IN     *SectionDefinitionGuid,
  POINTER(UINTN),                           # IN     SectionInstance,
  POINTER(PVOID),                           # IN     **Buffer,
  POINTER(UINTN),                           # IN OUT *BufferSize,
  POINTER(UINT32)                           # OUT    *AuthenticationStatus
  )

EFI_CLOSE_SECTION_STREAM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECTION_EXTRACTION_PROTOCOL), # IN     *This,
  UINTN                                     # IN     SectionStreamHandle
  )

EFI_SECTION_EXTRACTION_PROTOCOL._fields_ = [
    ("OpenSectionStream",   EFI_OPEN_SECTION_STREAM),
    ("GetSection",          EFI_GET_SECTION),
    ("CloseSectionStream",  EFI_CLOSE_SECTION_STREAM)
  ]

