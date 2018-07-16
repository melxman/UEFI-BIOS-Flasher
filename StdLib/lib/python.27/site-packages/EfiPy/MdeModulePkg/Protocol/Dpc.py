#
# Dpc.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# Dpc.py is free software: you can redistribute it and/or
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

gEfiDpcProtocolGuid = \
  EFI_GUID (0x480f8ae9, 0xc46, 0x4aa9, (0xbc, 0x89, 0xdb, 0x9f, 0xba, 0x61, 0x98, 0x6))

class EFI_DPC_PROTOCOL (Structure):
  pass

EFI_DPC_PROCEDURE = CFUNCTYPE (
  VOID,
  PVOID,        #   IN  *DpcContext
  )

EFI_DPC_QUEUE_DPC = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DPC_PROTOCOL),  # IN *This,
  EFI_TPL,                    # IN DpcTpl,
  EFI_DPC_PROCEDURE,          # IN DpcProcedure,
  PVOID                       # IN *DpcContext    OPTIONAL
  )

EFI_DPC_DISPATCH_DPC = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DPC_PROTOCOL)   # IN *This,
  )

EFI_DPC_PROTOCOL._fields_ = [
  ("QueueDpc",    EFI_DPC_QUEUE_DPC),
  ("DispatchDpc", EFI_DPC_DISPATCH_DPC)
  ]

