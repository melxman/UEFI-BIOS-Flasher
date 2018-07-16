#
# OEMBadging.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# OEMBadging.py is free software: you can redistribute it and/or
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

gEfiOEMBadgingProtocolGuid = \
  EFI_GUID (0x170e13c0, 0xbf1b, 0x4218, (0x87, 0x1d, 0x2a, 0xbd, 0xc6, 0xf8, 0x87, 0xbc))

class EFI_OEM_BADGING_PROTOCOL (Structure):
  pass

EfiBadgingFormatBMP     = 0
EfiBadgingFormatJPEG    = 1
EfiBadgingFormatTIFF    = 2
EfiBadgingFormatGIF     = 3
EfiBadgingFormatUnknown = 4
EFI_BADGING_FORMAT      = UINTN

EfiBadgingDisplayAttributeLeftTop       = 0
EfiBadgingDisplayAttributeCenterTop     = 1
EfiBadgingDisplayAttributeRightTop      = 2
EfiBadgingDisplayAttributeCenterRight   = 3
EfiBadgingDisplayAttributeRightBottom   = 4
EfiBadgingDisplayAttributeCenterBottom  = 5
EfiBadgingDisplayAttributeLeftBottom    = 6
EfiBadgingDisplayAttributeCenterLeft    = 7
EfiBadgingDisplayAttributeCenter        = 8
EfiBadgingDisplayAttributeCustomized    = 9
EFI_BADGING_DISPLAY_ATTRIBUTE           = UINTN

EFI_BADGING_GET_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_OEM_BADGING_PROTOCOL),      # IN     *This
  POINTER(UINT32),                        # IN OUT *Instance,
  POINTER(EFI_BADGING_FORMAT),            #    OUT *Format,
  POINTER(UINT8),                         #    OUT **ImageData,
  POINTER(UINTN),                         #    OUT *ImageSize,
  POINTER(EFI_BADGING_DISPLAY_ATTRIBUTE), #    OUT *Attribute,
  POINTER(UINTN),                         #    OUT *CoordinateX,
  POINTER(UINTN)                          #    OUT *CoordinateY
  )

EFI_OEM_BADGING_PROTOCOL._fields_ = [
    ("GetImage",  EFI_BADGING_GET_IMAGE)
  ]

