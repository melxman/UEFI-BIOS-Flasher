#
# Pkcs7Verify.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Pkcs7Verify.py is free software: you can redistribute it and/or
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

from EfiPy.MdePkg.Guid import ImageAuthentication

gEfiPkcs7VerifyProtocolGuid = \
  EFI_GUID (0x47889fb2, 0xd671, 0x4fab, (0xa0, 0xca, 0xdf, 0x0e, 0x44, 0xdf, 0x70, 0xd6 ))

class EFI_PKCS7_VERIFY_PROTOCOL (Structure):
  pass

EFI_PKCS7_VERIFY_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PKCS7_VERIFY_PROTOCOL),                       # IN      *This
  PVOID,                                                    # IN      *SignedData,
  UINTN,                                                    # IN      SignedDataSize,
  PVOID,                                                    # IN      *InData          OPTIONAL,
  UINTN,                                                    # IN      InDataSize,
  POINTER(POINTER(ImageAuthentication.EFI_SIGNATURE_LIST)), # IN      **AllowedDb,
  POINTER(POINTER(ImageAuthentication.EFI_SIGNATURE_LIST)), # IN      **RevokedDb      OPTIONAL,
  POINTER(POINTER(ImageAuthentication.EFI_SIGNATURE_LIST)), # IN      **TimeStampDb    OPTIONAL,
  PVOID,                                                    # OUT     *Content         OPTIONAL,
  POINTER(UINTN)                                            # IN OUT  *ContentSize
  )

EFI_PKCS7_VERIFY_SIGNATURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PKCS7_VERIFY_PROTOCOL),                       # IN *This
  PVOID,                                                    # IN *Signature,
  UINTN,                                                    # IN SignatureSize,
  PVOID,                                                    # IN *InHash,
  UINTN,                                                    # IN InHashSize,
  POINTER(POINTER(ImageAuthentication.EFI_SIGNATURE_LIST)), # IN **AllowedDb,
  POINTER(POINTER(ImageAuthentication.EFI_SIGNATURE_LIST)), # IN **RevokedDb       OPTIONAL,
  POINTER(POINTER(ImageAuthentication.EFI_SIGNATURE_LIST))  # IN **TimeStampDb     OPTIONAL
  )

EFI_PKCS7_VERIFY_PROTOCOL._fields_ = [
  ("VerifyBuffer",    EFI_PKCS7_VERIFY_BUFFER),
  ("VerifySignature", EFI_PKCS7_VERIFY_SIGNATURE)
  ]

