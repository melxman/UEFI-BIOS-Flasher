# /** @file
#   Root include file for Shell Package modules that utilize the SHELL_RETURN type
# 
#   Copyright (c) 2009 - 2011, Intel Corporation. All rights reserved.<BR>
#   This program and the accompanying materials
#   are licensed and made available under the terms and conditions of the BSD License
#   which accompanies this distribution.  The full text of the license may be found at
#   http://opensource.org/licenses/bsd-license.php
# 
#   THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
#   WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
# 
# **/
# 
#
# __init__.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# __init__.py is free software: you can redistribute it and/or
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

# #ifndef _SHELL_BASE_
# #define _SHELL_BASE_
# 
# typedef VOID *SHELL_FILE_HANDLE;
SHELL_FILE_HANDLE = PVOID

# 
# #define SHELL_FREE_NON_NULL(Pointer)  \
#   do {                                \
#     if ((Pointer) != NULL) {          \
#       FreePool((Pointer));            \
#       (Pointer) = NULL;               \
#     }                                 \
#   } while(FALSE)
# 
# typedef enum {
# ///
# /// The operation completed successfully.
# ///
# SHELL_SUCCESS               = 0,
SHELL_SUCCESS               = 0
# 
# ///
# /// The image failed to load.
# ///
# SHELL_LOAD_ERROR            = 1,
SHELL_LOAD_ERROR            = 1
# 
# ///
# /// The parameter was incorrect.
# ///
# SHELL_INVALID_PARAMETER     = 2,
SHELL_INVALID_PARAMETER     = 2
# 
# ///
# /// The operation is not supported.
# ///
# SHELL_UNSUPPORTED           = 3,
SHELL_UNSUPPORTED           = 3
# 
# ///
# /// The buffer was not the proper size for the request.
# ///
# SHELL_BAD_BUFFER_SIZE       = 4,
SHELL_BAD_BUFFER_SIZE       = 4
# 
# ///
# /// The buffer was not large enough to hold the requested data.
# /// The required buffer size is returned in the appropriate
# /// parameter when this error occurs.
# ///
# SHELL_BUFFER_TOO_SMALL      = 5,
SHELL_BUFFER_TOO_SMALL      = 5
# 
# ///
# /// There is no data pending upon return.
# ///
# SHELL_NOT_READY             = 6,
SHELL_NOT_READY             = 6
# 
# ///
# /// The physical device reported an error while attempting the
# /// operation.
# ///
# SHELL_DEVICE_ERROR          = 7,
SHELL_DEVICE_ERROR          = 7
# 
# ///
# /// The device cannot be written to.
# ///
# SHELL_WRITE_PROTECTED       = 8,
SHELL_WRITE_PROTECTED       = 8
# 
# ///
# /// The resource has run out.
# ///
# SHELL_OUT_OF_RESOURCES      = 9,
SHELL_OUT_OF_RESOURCES      = 9
# 
# ///
# /// An inconsistency was detected on the file system causing the
# /// operation to fail.
# ///
# SHELL_VOLUME_CORRUPTED      = 10,
SHELL_VOLUME_CORRUPTED      = 10
# 
# ///
# /// There is no more space on the file system.
# ///
# SHELL_VOLUME_FULL           = 11,
SHELL_VOLUME_FULL           = 11
# 
# ///
# /// The device does not contain any medium to perform the
# /// operation.
# ///
# SHELL_NO_MEDIA              = 12,
SHELL_NO_MEDIA              = 12
# 
# ///
# /// The medium in the device has changed since the last
# /// access.
# ///
# SHELL_MEDIA_CHANGED         = 13,
SHELL_MEDIA_CHANGED         = 13
# 
# ///
# /// The item was not found.
# ///
# SHELL_NOT_FOUND             = 14,
SHELL_NOT_FOUND             = 14
# 
# ///
# /// Access was denied.
# ///
# SHELL_ACCESS_DENIED         = 15,
SHELL_ACCESS_DENIED         = 15
# 
# // note the skipping of 16 and 17
# 
# ///
# /// A timeout time expired.
# ///
# SHELL_TIMEOUT               = 18,
SHELL_TIMEOUT               = 18
# 
# ///
# /// The protocol has not been started.
# ///
# SHELL_NOT_STARTED           = 19,
SHELL_NOT_STARTED           = 19
# 
# ///
# /// The protocol has already been started.
# ///
# SHELL_ALREADY_STARTED       = 20,
SHELL_ALREADY_STARTED       = 20
# 
# ///
# /// The operation was aborted.
# ///
# SHELL_ABORTED               = 21,
SHELL_ABORTED               = 21
# 
# // note the skipping of 22, 23, and 24
# 
# ///
# /// A function encountered an internal version that was
# /// incompatible with a version requested by the caller.
# ///
# SHELL_INCOMPATIBLE_VERSION  = 25,
SHELL_INCOMPATIBLE_VERSION  = 25
# 
# ///
# /// The function was not performed due to a security violation.
# ///
# SHELL_SECURITY_VIOLATION    = 26,
SHELL_SECURITY_VIOLATION    = 26
# 
# ///
# /// The function was performed and resulted in an unequal
# /// comparison..
# ///
# SHELL_NOT_EQUAL             = 27
SHELL_NOT_EQUAL             = 27
# }SHELL_STATUS;
SHELL_STATUS                = ENUM

# 
# #endif //__SHELL_BASE_
