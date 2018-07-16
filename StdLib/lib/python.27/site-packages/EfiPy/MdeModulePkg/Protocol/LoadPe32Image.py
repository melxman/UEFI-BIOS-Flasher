#
# LoadPe32Image.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# LoadPe32Image.py is free software: you can redistribute it and/or
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

gEfiLoadPeImageProtocolGuid = \
  EFI_GUID (0x5cb5c776,0x60d5,0x45ee,(0x88,0x3c,0x45,0x27,0x8,0xcd,0x74,0x3f))

EFI_LOAD_PE_IMAGE_ATTRIBUTE_NONE                                 = 0x00
EFI_LOAD_PE_IMAGE_ATTRIBUTE_RUNTIME_REGISTRATION                 = 0x01
EFI_LOAD_PE_IMAGE_ATTRIBUTE_DEBUG_IMAGE_INFO_TABLE_REGISTRATION  = 0x02

class EFI_PE32_IMAGE_PROTOCOL (Structure):
  pass

LOAD_PE_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PE32_IMAGE_PROTOCOL),   # IN      *This,
  EFI_HANDLE,                         # IN      ParentImageHandle,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),  # IN      *FilePath,
  PVOID,                              # IN      *SourceBuffer       OPTIONAL,
  UINTN,                              # IN      SourceSize,
  EFI_PHYSICAL_ADDRESS,               # IN      DstBuffer           OPTIONAL,
  POINTER(UINTN),                     # IN OUT  *NumberOfPages      OPTIONAL,
  POINTER(EFI_HANDLE),                # OUT     *ImageHandle,
  POINTER(EFI_PHYSICAL_ADDRESS),      # OUT     *EntryPoint         OPTIONAL,
  UINT32                              # IN      Attribute
  )

UNLOAD_PE_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PE32_IMAGE_PROTOCOL),   # IN      *This,
  EFI_HANDLE                          # IN      ImageHandle,
  )

EFI_PE32_IMAGE_PROTOCOL._fields_ = [
  ("LoadPeImage",   LOAD_PE_IMAGE),
  ("UnLoadPeImage", UNLOAD_PE_IMAGE)
  ]

