
#
# PeFile.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# PeFile.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PeFile.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy import *
from EfiPy.MdePkg.Protocol.LoadedImage import EFI_LOADED_IMAGE_PROTOCOL, gEfiLoadedImageProtocolGuid
from EfiPy.MdePkg.IndustryStandard.PeImage import EFI_IMAGE_OPTIONAL_HEADER_PTR_UNION, EFI_IMAGE_OPTIONAL_HEADER_UNION, EFI_IMAGE_DOS_HEADER, EFI_IMAGE_OPTIONAL_HEADER_UNION, EFI_IMAGE_SECTION_HEADER
from EfiPyLib.EfiPyHexDump import EfiPyHexDump

TmpProtocol = PVOID ()
Status = gBS.HandleProtocol (
               gImageHandle,
               byref (gEfiLoadedImageProtocolGuid),
               byref(TmpProtocol)
               )
if (EFI_ERROR (Status)):
  print "Locate gEfiLoadedImageProtocolGuid error %X" % Status
  exit (-1)

LoadedImage       = cast (TmpProtocol, POINTER(EFI_LOADED_IMAGE_PROTOCOL))[0]

DumpBuff = cast (LoadedImage.ImageBase, POINTER(CHAR8 * 0x400))
EfiPyHexDump (0x00, 0x00, DumpBuff[0])

DosHeader           = cast (LoadedImage.ImageBase, POINTER (EFI_IMAGE_DOS_HEADER))[0]

print "Image size: 0x%08X" % LoadedImage.ImageSize
print "DosHeader at 0x%016X" % addressof (DosHeader)
print "DosHeader.e_lfanew: 0x%08X" % DosHeader.e_lfanew

class ImageClass (Structure):
  _fields_ = [
    ("PreHeader",  UINT8 * DosHeader.e_lfanew),
    ("PeHeader",   EFI_IMAGE_OPTIONAL_HEADER_UNION),
  ]

Headers           = cast (LoadedImage.ImageBase, POINTER(ImageClass))[0]
ImgHdr            = Headers.PeHeader

NumberOfSections  = ImgHdr.Pe32.FileHeader.NumberOfSections;

class ImageClass (Structure):
  _fields_ = [
    ("PreHeader",  UINT8 * DosHeader.e_lfanew),
    ("PeHeader",   EFI_IMAGE_OPTIONAL_HEADER_UNION),
    ("Sections",   EFI_IMAGE_SECTION_HEADER * NumberOfSections)
  ]

Headers           = cast (LoadedImage.ImageBase, POINTER(ImageClass))[0]
ImgHdr            = Headers.PeHeader

print "ImgHdr at 0x%016X" % addressof (ImgHdr)
print "Pe32 Signature: 0x%08X" % ImgHdr.Pe32Plus.Signature
print "Pe32 Machine: 0x%08X" % ImgHdr.Pe32Plus.FileHeader.Machine
print "NumberOfSections: %d" % ImgHdr.Pe32Plus.FileHeader.NumberOfSections
print "ImgHdr.Pe32Plus.OptionalHeader.Magic: 0x%08X" % ImgHdr.Pe32Plus.OptionalHeader.Magic
print "ImgHdr.Pe32Plus.OptionalHeader.MajorLinkerVersion: 0x%08X" % ImgHdr.Pe32Plus.OptionalHeader.MajorLinkerVersion
print "ImgHdr.Pe32Plus.OptionalHeader.SizeOfHeaders: 0x%08X" % ImgHdr.Pe32Plus.OptionalHeader.SizeOfHeaders
print "ImgHdr.Pe32Plus.OptionalHeader.NumberOfRvaAndSizes: 0x%08X" % ImgHdr.Pe32Plus.OptionalHeader.NumberOfRvaAndSizes

for Section in Headers.Sections:
  print "Section Name: %s" % bytearray (Section.Name)
  print
  print "Section VirtualAddress: 0x%08X" % Section.VirtualAddress
  print "Section PhysicalAddress: 0x%08X" % Section.Misc.PhysicalAddress

