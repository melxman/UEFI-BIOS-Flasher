#
# LegacyBiosMpTable.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# LegacyBiosMpTable.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

from EfiPy.MdePkg.IndustryStandard import *

EFI_LEGACY_MP_TABLE_REV_1_4 = 0x04

EFI_LEGACY_MP_TABLE_FLOATING_POINTER_SIGNATURE  = SIGNATURE_32 ('_', 'M', 'P', '_')
class FEATUREBYTE2_5 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT32, 6),
    ("MutipleClk",  UINT32, 1),
    ("Imcr",        UINT32, 1),
    ("Reserved2",   UINT32, 24)
  ]

class EFI_LEGACY_MP_TABLE_FLOATING_POINTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("PhysicalAddress", UINT32),
    ("Length",          UINT8),
    ("SpecRev",         UINT8),
    ("Checksum",        UINT8),
    ("FeatureByte1",    UINT8),
    ("FeatureByte2_5",  FEATUREBYTE2_5)
  ]

EFI_LEGACY_MP_TABLE_HEADER_SIGNATURE  = SIGNATURE_32 ('P', 'C', 'M', 'P')

class EFI_LEGACY_MP_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",           UINT32),
    ("BaseTableLength",     UINT16),
    ("SpecRev",             UINT8),
    ("Checksum",            UINT8),
    ("OemId",               CHAR8 * 8),
    ("OemProductId",        CHAR8 * 12),
    ("OemTablePointer",     UINT32),
    ("OemTableSize",        UINT16),
    ("EntryCount",          UINT16),
    ("LocalApicAddress",    UINT32),
    ("ExtendedTableLength", UINT16),
    ("ExtendedChecksum",    UINT8),
    ("Reserved",            UINT8)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8)
  ]

EFI_LEGACY_MP_TABLE_ENTRY_TYPE_PROCESSOR  = 0x00
class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Enabled",   UINT8, 1),
    ("Bsp",       UINT8, 1),
    ("Reserved",  UINT8, 6)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_SIGNATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Stepping",  UINT32, 4),
    ("Model",     UINT32, 4),
    ("Family",    UINT32, 4),
    ("Reserved",  UINT32, 20)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fpu",       UINT32, 1),
    ("Reserved1", UINT32, 6),
    ("Mce",       UINT32, 1),
    ("Cx8",       UINT32, 1),
    ("Apic",      UINT32, 1),
    ("Reserved2", UINT32, 22)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8),
    ("Id",        UINT8),
    ("Ver",       UINT8),
    ("Flags",     EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FLAGS),
    ("Signature", EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_SIGNATURE),
    ("Features",  EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FEATURES),
    ("Reserved1", UINT32),
    ("Reserved2", UINT32)
  ]

EFI_LEGACY_MP_TABLE_ENTRY_TYPE_BUS  = 0x01

class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",   UINT8),
    ("Id",          UINT8),
    ("TypeString",  UINT8 * 6)
  ]

EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_CBUS   = "CBUS  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_CBUSII = "CBUSII"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_EISA   = "EISA  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_FUTURE = "FUTURE"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_INTERN = "INTERN"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_ISA    = "ISA   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MBI    = "MBI   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MBII   = "MBII  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MCA    = "MCA   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MPI    = "MPI   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MPSA   = "MPSA  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_NUBUS  = "NUBUS "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_PCI    = "PCI   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_PCMCIA = "PCMCIA"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_TC     = "TC    "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_VL     = "VL    "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_VME    = "VME   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_XPRESS = "XPRESS"

EFI_LEGACY_MP_TABLE_ENTRY_TYPE_IOAPIC = 0x02

class EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Enabled",   UINT8, 1),
    ("Reserved",  UINT8, 7)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8),
    ("Id",        UINT8),
    ("Ver",       UINT8),
    ("Flags",     EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC_FLAGS),
    ("Address",   UINT32)
  ]

EFI_LEGACY_MP_TABLE_ENTRY_TYPE_IO_INT = 0x03

class EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Polarity",  UINT16, 2),
    ("Trigger",   UINT16, 2),
    ("Reserved",  UINT16, 12)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_INT_FIELDS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IntNo",     UINT16, 2),
    ("Dev",       UINT16, 5),
    ("Reserved",  UINT16, 1)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("fields",  EFI_LEGACY_MP_TABLE_ENTRY_INT_FIELDS),
    ("byte",    UINT8)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_IO_INT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",     UINT8),
    ("IntType",       UINT8),
    ("Flags",         EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS),
    ("SourceBusId",   UINT8),
    ("SourceBusIrq",  UINT8),
    ("DestApicId",    EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ),
    ("DestApicIntIn", UINT8)
  ]

EfiLegacyMpTableEntryIoIntTypeInt   = 0
EfiLegacyMpTableEntryIoIntTypeNmi   = 1
EfiLegacyMpTableEntryIoIntTypeSmi   = 2
EfiLegacyMpTableEntryIoIntTypeExtInt= 3
EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_TYPE = ENUM

EfiLegacyMpTableEntryIoIntFlagsPolaritySpec       = 0x0
EfiLegacyMpTableEntryIoIntFlagsPolarityActiveHigh = 0x1
EfiLegacyMpTableEntryIoIntFlagsPolarityReserved   = 0x2
EfiLegacyMpTableEntryIoIntFlagsPolarityActiveLow  = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_FLAGS_POLARITY = ENUM

EfiLegacyMpTableEntryIoIntFlagsTriggerSpec        = 0x0
EfiLegacyMpTableEntryIoIntFlagsTriggerEdge        = 0x1
EfiLegacyMpTableEntryIoIntFlagsTriggerReserved    = 0x2
EfiLegacyMpTableEntryIoIntFlagsTriggerLevel       = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_FLAGS_TRIGGER = ENUM

EFI_LEGACY_MP_TABLE_ENTRY_TYPE_LOCAL_INT  = 0x04

class EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",     UINT8),
    ("IntType",       UINT8),
    ("Flags",         EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS),
    ("SourceBusId",   UINT8),
    ("SourceBusIrq",  EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ ),
    ("DestApicId",    UINT8),
    ("DestApicIntIn", UINT8)
  ]

EfiLegacyMpTableEntryLocalIntTypeInt              = 0
EfiLegacyMpTableEntryLocalIntTypeNmi              = 1
EfiLegacyMpTableEntryLocalIntTypeSmi              = 2
EfiLegacyMpTableEntryLocalIntTypeExtInt           = 3
EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_TYPE = ENUM

EfiLegacyMpTableEntryLocalIntFlagsPolaritySpec      = 0x0
EfiLegacyMpTableEntryLocalIntFlagsPolarityActiveHigh= 0x1
EfiLegacyMpTableEntryLocalIntFlagsPolarityReserved  = 0x2
EfiLegacyMpTableEntryLocalIntFlagsPolarityActiveLow = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_FLAGS_POLARITY = ENUM

EfiLegacyMpTableEntryLocalIntFlagsTriggerSpec       = 0x0
EfiLegacyMpTableEntryLocalIntFlagsTriggerEdge       = 0x1
EfiLegacyMpTableEntryLocalIntFlagsTriggerReserved   = 0x2
EfiLegacyMpTableEntryLocalIntFlagsTriggerLevel      = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_FLAGS_TRIGGER = ENUM

EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_SYS_ADDR_SPACE_MAPPING = 0x80

class EFI_LEGACY_MP_TABLE_ENTRY_EXT_SYS_ADDR_SPACE_MAPPING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",     UINT8),
    ("Length",        UINT8),
    ("BusId",         UINT8),
    ("AddressType",   UINT8),
    ("AddressBase",   UINT64),
    ("AddressLength", UINT64)
  ]

EfiLegacyMpTableEntryExtSysAddrSpaceMappingIo       = 0
EfiLegacyMpTableEntryExtSysAddrSpaceMappingMemory   = 1
EfiLegacyMpTableEntryExtSysAddrSpaceMappingPrefetch = 2
EFI_LEGACY_MP_TABLE_ENTRY_EXT_SYS_ADDR_SPACE_MAPPING_TYPE = ENUM

EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_BUS_HIERARCHY  = 0x81

class EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY_BUSINFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SubtractiveDecode", UINT8, 1),
    ("Reserved",          UINT8, 7)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8),
    ("Length",    UINT8),
    ("BusId",     UINT8),
    ("BusInfo",   EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY_BUSINFO),
    ("ParentBus", UINT8),
    ("Reserved1", UINT8),
    ("Reserved2", UINT8),
    ("Reserved3", UINT8)
  ]

EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_COMPAT_BUS_ADDR_SPACE_MODIFIER = 0x82

class EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER_ADDR_MODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RangeMode", UINT8, 1),
    ("Reserved",  UINT8, 7)
  ]

class EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",           UINT8),
    ("Length",              UINT8),
    ("BusId",               UINT8),
    ("AddrMode",            EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER_ADDR_MODE),
    ("PredefinedRangeList", UINT32)
  ]

