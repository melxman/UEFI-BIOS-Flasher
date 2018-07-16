#
# PciSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# PciSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PciSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import  EfiPyLib.PciEmulate as PciEmulate
from    EfiPyLib.PciStructure import PciDeviceS, PciBridgeS, PciCardBusS
from    EfiPyLib.PciIo import PciIo8, PciIo16, PciIo32, PciMmioConfigOffset

PciList = PciEmulate.PciEmulate ()
print "==" * 10
print "PciList:", PciList

#
# 1. List all pci device vendor id, device id, device type and if miltifunction
# 2. update PCI structure by device type
#
print "==== Sample 1. Simple dump VID, PID and Multifunction"
for pcid in PciList:
  print "Pci" + str(pcid) + ": VID: 0x%04X, PID: 0x%04X" % (PciIo16(*pcid)[0x00], PciIo16(*pcid)[0x02])
  print "Pci" + str(pcid) + ": VIDPID: 0x%08X" % (PciIo32(*pcid)[0x00])
  print "Pci" + str(pcid) + ": VIDPID: 0x%08X" % (PciIo32(*pcid)[0x00][0:15])
  _HeaderType = PciIo32(*pcid)[0x0C][16:23]
  print "         (1) DeviceType: 0x%02X, Multifunction: 0x%02X" % (PciIo32(*pcid).DeviceType, PciIo32(*pcid).Multifunction)
  print "         (2) DeviceType: 0x%02X, Multifunction: 0x%02X" % (PciIo32(*pcid)[0x0C][16:21], PciIo32(*pcid)[0x0C][23])
  print "         (3) DeviceType: 0x%02X, Multifunction: 0x%02X" % (_HeaderType[0:6], _HeaderType[7])
  if PciIo32(*pcid).DeviceType == 0x00:
    PciIo32(*pcid).DictKey.update (PciDeviceS)
  elif PciIo32(*pcid).DeviceType == 0x01:
    PciIo32(*pcid).DictKey.update (PciBridgeS)
  elif PciIo32(*pcid).DeviceType == 0x02:
    PciIo32(*pcid).DictKey.update (PciCardBusS)

print
print "==== Sample 2. Dump each VID and PID"
for pcid in PciList:
  print "Pci" + str(pcid) + ": VID: 0x%04X, PID: 0x%04X" % (PciIo16(*pcid)[0x00], PciIo16(*pcid)[0x02])

print
for pcid in PciList:
  print "Pci" + str(pcid) + ": VIDPID: 0x%08X" % (PciIo32(*pcid)[0x00])


print
print "==== Sample 3. Dump each DWORD using PciIo16 and PciIo32"
for pcid in PciList:
  print "=== PCI %s" % str(pcid)
  PciReg8  = PciIo8(*pcid)
  PciReg32 = PciIo32(*pcid)
  PciReg16 = PciIo16(*pcid)
  print "PciReg16[0x00]:",          PciIo16(*pcid)[0x00]
  print "PciReg16[0x02]:",          PciIo16(*pcid)[0x02]
  print "PciReg32[0x00]:",          PciIo32(*pcid)[0x00]
  print "PciReg32[0x04]:",          PciIo32(*pcid)[0x04]
  print "PciReg32[0x08]:",          PciIo32(*pcid)[0x08]
  print "PciReg32[0x0C]:",          PciIo32(*pcid)[0x0C]
  print "PciReg32[0x10]:",          PciIo32(*pcid)[0x10]
  print "PciReg32[0x14]:",          PciIo32(*pcid)[0x14]
  print "PciReg32[0x18]:",          PciIo32(*pcid)[0x18]
  print "PciReg32[0x1C]:",          PciIo32(*pcid)[0x1C]
  print "PciReg32[0x20]:",          PciIo32(*pcid)[0x20]
  print "PciReg32[0x24]:",          PciIo32(*pcid)[0x24]
  print "PciReg32[0x28]:",          PciIo32(*pcid)[0x28]
  print "PciReg32[0x2C]:",          PciIo32(*pcid)[0x2C]
  print "PciReg32[0x30]:",          PciIo32(*pcid)[0x30]
  print "PciReg32[0x34]:",          PciIo32(*pcid)[0x34]
  print "PciReg32[0x38]:",          PciIo32(*pcid)[0x38]
  print "PciReg32[0x3C]:",          PciIo32(*pcid)[0x3C]

print
print "==== Sample 4. Dump each field PciIo32"
for pcid in PciList:
  PciReg32 = PciIo32(*pcid)
  print
  print "=== PCI %s" % str(pcid)
  print 'PCI%s.VendorId                  : 0x%X' % (pcid, PciReg32.VendorId      )
  print 'PCI%s.DeviceId                  : 0x%X' % (pcid, PciReg32.DeviceId      )
  print 'PCI%s.Command                   : 0x%X' % (pcid, PciReg32.Command       )
  print 'PCI%s.Status                    : 0x%X' % (pcid, PciReg32.Status        )
  print 'PCI%s.RevisionID                : 0x%X' % (pcid, PciReg32.RevisionID    )
  print 'PCI%s.ClassCode                 : 0x%X' % (pcid, PciReg32.ClassCode     )
  print 'PCI%s.CacheLineSize             : 0x%X' % (pcid, PciReg32.CacheLineSize )
  print 'PCI%s.LatencyTimer              : 0x%X' % (pcid, PciReg32.LatencyTimer  )
  print 'PCI%s.HeaderType                : 0x%X' % (pcid, PciReg32.HeaderType    )
  print 'PCI%s.BIST                      : 0x%X' % (pcid, PciReg32.BIST          )
  if PciReg32.DeviceType == 0x00:
    print 'PCI%s.BAR0                      : 0x%X' % (pcid, PciReg32.BAR0              )
    print 'PCI%s.BAR1                      : 0x%X' % (pcid, PciReg32.BAR1              )
    print 'PCI%s.BAR2                      : 0x%X' % (pcid, PciReg32.BAR2              )
    print 'PCI%s.BAR3                      : 0x%X' % (pcid, PciReg32.BAR3              )
    print 'PCI%s.BAR4                      : 0x%X' % (pcid, PciReg32.BAR4              )
    print 'PCI%s.BAR5                      : 0x%X' % (pcid, PciReg32.BAR5              )
    print 'PCI%s.CISPtr                    : 0x%X' % (pcid, PciReg32.CISPtr            )
    print 'PCI%s.SubsystemVendorID         : 0x%X' % (pcid, PciReg32.SubsystemVendorID )
    print 'PCI%s.SubsystemID               : 0x%X' % (pcid, PciReg32.SubsystemID       )
    print 'PCI%s.ExpansionRomBar           : 0x%X' % (pcid, PciReg32.ExpansionRomBar   )
    print 'PCI%s.CapabilityPtr             : 0x%X' % (pcid, PciReg32.CapabilityPtr     )
    print 'PCI%s.InterruptLine             : 0x%X' % (pcid, PciReg32.InterruptLine     )
    print 'PCI%s.InterruptPin              : 0x%X' % (pcid, PciReg32.InterruptPin      )
    print 'PCI%s.MinGnt                    : 0x%X' % (pcid, PciReg32.MinGnt            )
    print 'PCI%s.MaxLat                    : 0x%X' % (pcid, PciReg32.MaxLat            )
  elif PciReg32.DeviceType == 0x01:
    print 'PCI%s.BAR0                      : 0x%X' % (pcid, PciReg32.BAR0                     )
    print 'PCI%s.BAR1                      : 0x%X' % (pcid, PciReg32.BAR1                     )
    print 'PCI%s.PrimaryBus                : 0x%X' % (pcid, PciReg32.PrimaryBus               )
    print 'PCI%s.SecondaryBus              : 0x%X' % (pcid, PciReg32.SecondaryBus             )
    print 'PCI%s.SubordinateBus            : 0x%X' % (pcid, PciReg32.SubordinateBus           )
    print 'PCI%s.SecondaryLatencyTimer     : 0x%X' % (pcid, PciReg32.SecondaryLatencyTimer    )
    print 'PCI%s.IoBase                    : 0x%X' % (pcid, PciReg32.IoBase                   )
    print 'PCI%s.IoLimit                   : 0x%X' % (pcid, PciReg32.IoLimit                  )
    print 'PCI%s.SecondaryStatus           : 0x%X' % (pcid, PciReg32.SecondaryStatus          )
    print 'PCI%s.MemoryBase                : 0x%X' % (pcid, PciReg32.MemoryBase               )
    print 'PCI%s.MemoryLimit               : 0x%X' % (pcid, PciReg32.MemoryLimit              )
    print 'PCI%s.PrefetchableMemoryBase    : 0x%X' % (pcid, PciReg32.PrefetchableMemoryBase   )
    print 'PCI%s.PrefetchableMemoryLimit   : 0x%X' % (pcid, PciReg32.PrefetchableMemoryLimit  )
    print 'PCI%s.PrefetchableBaseUpper32   : 0x%X' % (pcid, PciReg32.PrefetchableBaseUpper32  )
    print 'PCI%s.PrefetchableLimitUpper32  : 0x%X' % (pcid, PciReg32.PrefetchableLimitUpper32 )
    print 'PCI%s.IoBaseUpper16             : 0x%X' % (pcid, PciReg32.IoBaseUpper16            )
    print 'PCI%s.IoLimitUpper16            : 0x%X' % (pcid, PciReg32.IoLimitUpper16           )
    print 'PCI%s.CapabilityPtr             : 0x%X' % (pcid, PciReg32.CapabilityPtr            )
    print 'PCI%s.ExpansionRomBAR           : 0x%X' % (pcid, PciReg32.ExpansionRomBAR          )
    print 'PCI%s.InterruptLine             : 0x%X' % (pcid, PciReg32.InterruptLine            )
    print 'PCI%s.InterruptPin              : 0x%X' % (pcid, PciReg32.InterruptPin             )
    print 'PCI%s.BridgeControl             : 0x%X' % (pcid, PciReg32.BridgeControl            )
  elif PciReg32.DeviceType == 0x02:
    print 'PCI%s.CardBusSocketReg          : 0x%X' % (pcid, PciReg32.CardBusSocketReg          )
    print 'PCI%s.Cap_Ptr                   : 0x%X' % (pcid, PciReg32.Cap_Ptr                   )
    print 'PCI%s.SecondaryStatus           : 0x%X' % (pcid, PciReg32.SecondaryStatus           )
    print 'PCI%s.SecondaryBus              : 0x%X' % (pcid, PciReg32.SecondaryBus              )
    print 'PCI%s.PciBusNumber              : 0x%X' % (pcid, PciReg32.PciBusNumber              )
    print 'PCI%s.CardBusBusNumber          : 0x%X' % (pcid, PciReg32.CardBusBusNumber          )
    print 'PCI%s.SubordinateBusNumber      : 0x%X' % (pcid, PciReg32.SubordinateBusNumber      )
    print 'PCI%s.CardBusLatencyTimer       : 0x%X' % (pcid, PciReg32.CardBusLatencyTimer       )
    print 'PCI%s.MemoryBase0               : 0x%X' % (pcid, PciReg32.MemoryBase0               )
    print 'PCI%s.MemoryLimit0              : 0x%X' % (pcid, PciReg32.MemoryLimit0              )
    print 'PCI%s.MemoryBase1               : 0x%X' % (pcid, PciReg32.MemoryBase1               )
    print 'PCI%s.MemoryLimit1              : 0x%X' % (pcid, PciReg32.MemoryLimit1              )
    print 'PCI%s.IoBase0                   : 0x%X' % (pcid, PciReg32.IoBase0                   )
    print 'PCI%s.IoLimit0                  : 0x%X' % (pcid, PciReg32.IoLimit0                  )
    print 'PCI%s.IoBase1                   : 0x%X' % (pcid, PciReg32.IoBase1                   )
    print 'PCI%s.IoLimit1                  : 0x%X' % (pcid, PciReg32.IoLimit1                  )
    print 'PCI%s.InterruptLine             : 0x%X' % (pcid, PciReg32.InterruptLine             )
    print 'PCI%s.InterruptPin              : 0x%X' % (pcid, PciReg32.InterruptPin              )
    print 'PCI%s.BridgeControl             : 0x%X' % (pcid, PciReg32.BridgeControl             )
    print 'PCI%s.SubsystemDeviceID         : 0x%X' % (pcid, PciReg32.SubsystemDeviceID         )
    print 'PCI%s.SubsystemVendorID         : 0x%X' % (pcid, PciReg32.SubsystemVendorID         )
    print 'PCI%s.LegacyModeBaseAddress     : 0x%X' % (pcid, PciReg32.LegacyModeBaseAddress     )

#
# Dump PCI bus 0, device 0, function 0 MMIO
#
print
print "==== Sample 5. Dump MMIO space by ACPI Mcfg"
import sys
import traceback
try:
  import EfiPy
  from EfiPyLib.EfiPyHexDump import EfiPyHexDump
  from EfiPyLib.Acpi.AcpiMcfg import Table as McfgTable

  for pcid in PciList:
    print
    DeviceMmioBase = McfgTable.McfgEntry[0].BaseAddress + PciMmioConfigOffset (pcid[0], pcid[1], pcid[2], 0)
    Memory = (EfiPy.CHAR8 * 0x100).from_address (DeviceMmioBase)
    EfiPyHexDump (2, DeviceMmioBase, Memory, True, "PCI%s" % str(pcid))

except Exception as e:
  exc_type, exc_value, exc_traceback_obj = sys.exc_info()
  traceback.print_tb(exc_traceback_obj)
  DeviceMmioBase = 0

print
print "==== Sample 6. Dump VID, PID by _PciIoR32"
from  EfiPyLib.PciEmulate import _PciIoR32
for pcid in PciList:
  print "pci%s[0]: 0x%08X" % (pcid, _PciIoR32(pcid[0], pcid[1], pcid[2], 0))
  print "pci%s[4]: 0x%08X" % (pcid, _PciIoR32(pcid[0], pcid[1], pcid[2], 4))
