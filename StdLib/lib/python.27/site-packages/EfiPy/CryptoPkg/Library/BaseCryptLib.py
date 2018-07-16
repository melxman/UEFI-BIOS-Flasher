#
# BaseCryptLib.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# BaseCryptLib.py is free software: you can redistribute it and/or
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

MD4_DIGEST_SIZE     = 16
MD5_DIGEST_SIZE     = 16
SHA1_DIGEST_SIZE    = 20
SHA256_DIGEST_SIZE  = 32
SHA384_DIGEST_SIZE  = 48
SHA512_DIGEST_SIZE  = 64
TDES_BLOCK_SIZE     = 8
AES_BLOCK_SIZE      = 16

RsaKeyN       = 0
RsaKeyE       = 1
RsaKeyD       = 2
RsaKeyP       = 3
RsaKeyQ       = 4
RsaKeyDp      = 5
RsaKeyDq      = 6
RsaKeyQInv    = 7
RSA_KEY_TAG   = UINTN

