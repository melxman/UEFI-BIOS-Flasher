#
# IncompatiblePciDeviceSupport.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# IncompatiblePciDeviceSupport.py is free software: you can redistribute it and/or
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

gEfiIncompatiblePciDeviceSupportProtocolGuid  = \
  EFI_GUID (0xeb23f55a, 0x7863, 0x4ac2, (0x8d, 0x3d, 0x95, 0x65, 0x35, 0xde, 0x03, 0x75))

class EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_PROTOCOL (Structure):
  pass

EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_CHECK_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_PROTOCOL),  # IN  *This
  UINTN,                                                  # IN  VendorId,
  UINTN,                                                  # IN  DeviceId,
  UINTN,                                                  # IN  RevisionId,
  UINTN,                                                  # IN  SubsystemVendorId,
  UINTN,                                                  # IN  SubsystemDeviceId,
  POINTER(PVOID)                                          # OUT **Configuration
  )

EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_PROTOCOL._fields_ = [
    ("CheckDevice", EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_CHECK_DEVICE)
  ]

