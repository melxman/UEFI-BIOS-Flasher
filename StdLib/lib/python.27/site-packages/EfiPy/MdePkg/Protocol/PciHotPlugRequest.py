#
# PciHotPlugRequest.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# PciHotPlugRequest.py is free software: you can redistribute it and/or
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

gEfiPciHotPlugRequestProtocolGuid   = \
  EFI_GUID (0x19cb87ab, 0x2cb9, 0x4665, (0x83, 0x60, 0xdd, 0xcf, 0x60, 0x54, 0xf7, 0x9d))

class EFI_PCI_HOTPLUG_REQUEST_PROTOCOL (Structure):
  pass

EfiPciHotPlugRequestAdd     = 0
EfiPciHotplugRequestRemove  = 1
EFI_PCI_HOTPLUG_OPERATION   = ENUM

EFI_PCI_HOTPLUG_REQUEST_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOTPLUG_REQUEST_PROTOCOL),  # IN  *This,
  EFI_PCI_HOTPLUG_OPERATION,                  # IN     Operation,
  EFI_HANDLE,                                 # IN     Controller,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),          # IN     *RemainingDevicePath  OPTIONAL,
  POINTER(UINT8),                             # IN OUT *NumberOfChildren,
  POINTER(EFI_HANDLE)                         # IN OUT *ChildHandleBuffer
  )

EFI_PCI_HOTPLUG_REQUEST_PROTOCOL._fields_ = [
    ("Notify",  EFI_PCI_HOTPLUG_REQUEST_NOTIFY)
  ]

