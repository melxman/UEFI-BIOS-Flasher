#
# UgaDraw.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# UgaDraw.py is free software: you can redistribute it and/or
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

gEfiUgaDrawProtocolGuid   = \
  EFI_GUID (0x982c298b, 0xf4fa, 0x41cb, (0xb8, 0x38, 0x77, 0xaa, 0x68, 0x8f, 0xb8, 0x39 ))

class EFI_UGA_DRAW_PROTOCOL (Structure):
  pass

EFI_UGA_DRAW_PROTOCOL_GET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_DRAW_PROTOCOL), # IN      *This
  POINTER(UINT32),                #     OUT *HorizontalResolution,
  POINTER(UINT32),                #     OUT *VerticalResolution,
  POINTER(UINT32),                #     OUT *ColorDepth,
  POINTER(UINT32)                 #     OUT *RefreshRate
  )

EFI_UGA_DRAW_PROTOCOL_SET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_DRAW_PROTOCOL), # IN  *This
  UINT32,                         # IN  HorizontalResolution,
  UINT32,                         # IN  VerticalResolution,
  UINT32,                         # IN  ColorDepth,
  UINT32                          # IN  RefreshRate
  )

class EFI_UGA_PIXEL (Structure):
  _fields_ = [
    ("Blue",      UINT8),
    ("Green",     UINT8),
    ("Red",       UINT8),
    ("Reserved",  UINT8)
  ]

class EFI_UGA_PIXEL_UNION (Union):
  _fields_ = [
    ("Pixel", EFI_UGA_PIXEL),
    ("Raw",   UINT32)
  ]

EfiUgaVideoFill         = 0
EfiUgaVideoToBltBuffer  = 1
EfiUgaBltBufferToVideo  = 2
EfiUgaVideoToVideo      = 3
EfiUgaBltMax            = 4
EFI_UGA_BLT_OPERATION   = ENUM

EFI_UGA_DRAW_PROTOCOL_BLT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_DRAW_PROTOCOL), # IN  *This
  POINTER(EFI_UGA_PIXEL),         # IN  * BltBuffer, OPTIONAL
  EFI_UGA_BLT_OPERATION,          # IN  BltOperation,
  UINTN,                          # IN  SourceX,
  UINTN,                          # IN  SourceY,
  UINTN,                          # IN  DestinationX,
  UINTN,                          # IN  DestinationY,
  UINTN,                          # IN  Width,
  UINTN,                          # IN  Height,
  UINTN                           # IN  Delta         OPTIONAL
  )

EFI_UGA_DRAW_PROTOCOL._fields_ = [
    ("GetMode", EFI_UGA_DRAW_PROTOCOL_GET_MODE),
    ("SetMode", EFI_UGA_DRAW_PROTOCOL_SET_MODE),
    ("Blt",     EFI_UGA_DRAW_PROTOCOL_BLT)
  ]

