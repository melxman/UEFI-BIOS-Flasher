#
# DataHub.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# DataHub.py is free software: you can redistribute it and/or
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

gEfiDataHubProtocolGuid = \
  EFI_GUID (0xae80d021, 0x618e, 0x11d4, (0xbc, 0xd7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81))

EFI_DATA_RECORD_HEADER_VERSION  = 0x0100

class EFI_DATA_RECORD_HEADER (Structure):
  _fields_ = [
    ("Version",             UINT16),
    ("HeaderSize",          UINT16),
    ("RecordSize",          UINT32),
    ("DataRecordGuid",      EFI_GUID),
    ("ProducerName",        EFI_GUID),
    ("DataRecordClass",     UINT64),
    ("LogTime",             EFI_TIME),
    ("LogMonotonicCount",   UINT64)
  ]

EFI_DATA_RECORD_CLASS_DEBUG         = 0x0000000000000001
EFI_DATA_RECORD_CLASS_ERROR         = 0x0000000000000002
EFI_DATA_RECORD_CLASS_DATA          = 0x0000000000000004
EFI_DATA_RECORD_CLASS_PROGRESS_CODE = 0x0000000000000008

class EFI_DATA_HUB_PROTOCOL (Structure):
  pass

EFI_DATA_HUB_LOG_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DATA_HUB_PROTOCOL),   # IN  *This
  POINTER(EFI_GUID),                # IN  *DataRecordGuid,
  POINTER(EFI_GUID),                # IN  *ProducerName,
  UINT64,                           # IN  DataRecordClass,
  PVOID,                            # IN  *RawData,
  UINT32                            # IN  RawDataSize
  )

EFI_DATA_HUB_GET_NEXT_RECORD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DATA_HUB_PROTOCOL),           # IN      *This
  POINTER(UINT64),                          # IN OUT  *MonotonicCount,
  POINTER(EFI_EVENT),                       # IN      *FilterDriver OPTIONAL,
  POINTER(POINTER(EFI_DATA_RECORD_HEADER))  # OUT     **Record
  )

EFI_DATA_HUB_REGISTER_FILTER_DRIVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DATA_HUB_PROTOCOL),   # IN *This
  EFI_EVENT,                        # IN FilterEvent,
  EFI_TPL,                          # IN FilterTpl,
  UINT64,                           # IN FilterClass,
  POINTER(EFI_GUID)                 # IN *FilterDataRecordGuid OPTIONAL
  )

EFI_DATA_HUB_UNREGISTER_FILTER_DRIVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DATA_HUB_PROTOCOL),   # IN *This
  EFI_EVENT                         # IN FilterEvent
  )

EFI_DATA_HUB_PROTOCOL._fields_ = [
    ("LogData",                 EFI_DATA_HUB_LOG_DATA),
    ("GetNextRecord",           EFI_DATA_HUB_GET_NEXT_RECORD),
    ("RegisterFilterDriver",    EFI_DATA_HUB_REGISTER_FILTER_DRIVER),
    ("UnregisterFilterDriver",  EFI_DATA_HUB_UNREGISTER_FILTER_DRIVER)
  ]

