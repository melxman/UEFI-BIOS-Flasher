#
# RuntimeCrypt.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# RuntimeCrypt.py is free software: you can redistribute it and/or
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

from EfiPy.CryptoPkg.Library.BaseCryptLib import RSA_KEY_TAG

gEfiRuntimeCryptProtocolGuid  = \
  EFI_GUID (0xe1475e0c, 0x1746, 0x4802, ( 0x86, 0x2e, 0x1, 0x1c, 0x2c, 0x2d, 0x9d, 0x86 ))

EFI_RUNTIME_CRYPT_SHA256_GET_CONTEXT_SIZE = CFUNCTYPE (
  UINTN
  )

EFI_RUNTIME_CRYPT_SHA256_INIT = CFUNCTYPE (
  BOOLEAN,
  PVOID     # IN OUT *Sha256Context
  )

EFI_RUNTIME_CRYPT_SHA256_UPDATE = CFUNCTYPE (
  BOOLEAN,
  PVOID,  # IN OUT    *Sha256Context
  PVOID,  # IN CONST  *Data,
  UINTN   # IN        DataLength
  )

EFI_RUNTIME_CRYPT_SHA256_FINAL = CFUNCTYPE (
  BOOLEAN,
  PVOID,          # IN OUT  *Sha256Context
  POINTER(UINT8)  # OUT     *HashValue
  )

EFI_RUNTIME_CRYPT_RSA_NEW = CFUNCTYPE (
  PVOID
  )

EFI_RUNTIME_CRYPT_RSA_FREE = CFUNCTYPE (
  VOID,
  PVOID   # IN *RsaContext
  )

EFI_RUNTIME_CRYPT_RSA_SET_KEY = CFUNCTYPE (
  BOOLEAN,
  PVOID,          # IN OUT       *RsaContext,
  RSA_KEY_TAG,    # IN           KeyTag,
  POINTER(UINT8), # IN     CONST *BigNumber,
  UINTN           # IN           BnLength
  )

EFI_RUNTIME_CRYPT_RSA_PKCS1_VERIFY = CFUNCTYPE (
  BOOLEAN,
  PVOID,          # IN        *RsaContext,
  POINTER(UINT8), # IN  CONST *MessageHash,
  UINTN,          # IN        HashLength,
  POINTER(UINT8), # IN  CONST *Signature,
  UINTN           # IN        SigLength
  )

class EFI_RUNTIME_CRYPT_PROTOCOL (Structure):
  _fields_ = [
    ("Sha256GetContextSize",  EFI_RUNTIME_CRYPT_SHA256_GET_CONTEXT_SIZE),
    ("Sha256Init",            EFI_RUNTIME_CRYPT_SHA256_INIT),
    ("Sha256Update",          EFI_RUNTIME_CRYPT_SHA256_UPDATE),
    ("Sha256Final",           EFI_RUNTIME_CRYPT_SHA256_FINAL),
    ("RsaNew",                EFI_RUNTIME_CRYPT_RSA_NEW),
    ("RsaFree",               EFI_RUNTIME_CRYPT_RSA_FREE),
    ("RsaSetKey",             EFI_RUNTIME_CRYPT_RSA_SET_KEY),
    ("RsaPkcs1Verify",        EFI_RUNTIME_CRYPT_RSA_PKCS1_VERIFY)
  ]

