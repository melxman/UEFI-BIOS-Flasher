#
# AcpiFacpSample.py
#
# Copyright (C) 2018 efipy.core@gmail.com All rights reserved.
#
# AcpiFacpSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# AcpiFacpSample.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

print "==== FACP Table"
import EfiPyLib.Acpi.AcpiFacp             as AcpiFacp
print "   FACP Revision:  0x%02X" % AcpiFacp.Revision
print "   FACP Address:   0x%08X" % AcpiFacp.Address
print "   FACP Size:      0x%08X" % AcpiFacp.Size

#
# FACP dump, style one.
#
for _fName, _type in AcpiFacp.Table._fields_:
  try:
    print "   FACP %s: 0x%08X" % (_fName, getattr(AcpiFacp.Table, _fName))
  except:
    print "   FACP %s: %s" % (_fName, getattr(AcpiFacp.Table, _fName))

print
#
# FACP dump, style two.
#
import struct
print "   AcpiFacp:Signature:        %s"       % struct.pack ("I", AcpiFacp.Table.Header.Signature)
print "   AcpiFacp:Length:           0x%08X"   % AcpiFacp.Table.Header.Length
print "   AcpiFacp:Revision:         0x%02X"   % AcpiFacp.Table.Header.Revision
print "   AcpiFacp:Checksum:         0x%02X"   % AcpiFacp.Table.Header.Checksum
print "   AcpiFacp:OemId:            %s"       % bytearray (AcpiFacp.Table.Header.OemId)
print "   AcpiFacp:OemTableId:       %s"       % struct.pack ("Q", AcpiFacp.Table.Header.OemTableId)
print "   AcpiFacp:OemRevision:      0x%08X"   % AcpiFacp.Table.Header.OemRevision
print "   AcpiFacp:CreatorId:        %s"       % struct.pack ("I", AcpiFacp.Table.Header.CreatorId)
print "   AcpiFacp:CreatorRevision:  0x%08X"   % AcpiFacp.Table.Header.CreatorRevision

if    AcpiFacp.Table.Header.Revision == 0x01:
  print "   AcpiFacp:FirmwareCtrl:     0x%08X" % AcpiFacp.Table.FirmwareCtrl
  print "   AcpiFacp:Dsdt:             0x%08X" % AcpiFacp.Table.Dsdt
  print "   AcpiFacp:IntModel:         0x%08X" % AcpiFacp.Table.IntModel
  print "   AcpiFacp:Reserved1:        0x%08X" % AcpiFacp.Table.Reserved1
  print "   AcpiFacp:SciInt:           0x%08X" % AcpiFacp.Table.SciInt
  print "   AcpiFacp:SmiCmd:           0x%08X" % AcpiFacp.Table.SmiCmd
  print "   AcpiFacp:AcpiEnable:       0x%08X" % AcpiFacp.Table.AcpiEnable
  print "   AcpiFacp:AcpiDisable:      0x%08X" % AcpiFacp.Table.AcpiDisable
  print "   AcpiFacp:S4BiosReq:        0x%08X" % AcpiFacp.Table.S4BiosReq
  print "   AcpiFacp:Reserved2:        0x%08X" % AcpiFacp.Table.Reserved2
  print "   AcpiFacp:Pm1aEvtBlk:       0x%08X" % AcpiFacp.Table.Pm1aEvtBlk
  print "   AcpiFacp:Pm1bEvtBlk:       0x%08X" % AcpiFacp.Table.Pm1bEvtBlk
  print "   AcpiFacp:Pm1aCntBlk:       0x%08X" % AcpiFacp.Table.Pm1aCntBlk
  print "   AcpiFacp:Pm1bCntBlk:       0x%08X" % AcpiFacp.Table.Pm1bCntBlk
  print "   AcpiFacp:Pm2CntBlk:        0x%08X" % AcpiFacp.Table.Pm2CntBlk
  print "   AcpiFacp:PmTmrBlk:         0x%08X" % AcpiFacp.Table.PmTmrBlk
  print "   AcpiFacp:Gpe0Blk:          0x%08X" % AcpiFacp.Table.Gpe0Blk
  print "   AcpiFacp:Gpe1Blk:          0x%08X" % AcpiFacp.Table.Gpe1Blk
  print "   AcpiFacp:Pm1EvtLen:        0x%08X" % AcpiFacp.Table.Pm1EvtLen
  print "   AcpiFacp:Pm1CntLen:        0x%08X" % AcpiFacp.Table.Pm1CntLen
  print "   AcpiFacp:Pm2CntLen:        0x%08X" % AcpiFacp.Table.Pm2CntLen
  print "   AcpiFacp:PmTmLen:          0x%08X" % AcpiFacp.Table.PmTmLen
  print "   AcpiFacp:Gpe0BlkLen:       0x%08X" % AcpiFacp.Table.Gpe0BlkLen
  print "   AcpiFacp:Gpe1BlkLen:       0x%08X" % AcpiFacp.Table.Gpe1BlkLen
  print "   AcpiFacp:Gpe1Base:         0x%08X" % AcpiFacp.Table.Gpe1Base
  print "   AcpiFacp:Reserved3:        0x%08X" % AcpiFacp.Table.Reserved3
  print "   AcpiFacp:PLvl2Lat:         0x%08X" % AcpiFacp.Table.PLvl2Lat
  print "   AcpiFacp:PLvl3Lat:         0x%08X" % AcpiFacp.Table.PLvl3Lat
  print "   AcpiFacp:FlushSize:        0x%08X" % AcpiFacp.Table.FlushSize
  print "   AcpiFacp:FlushStride:      0x%08X" % AcpiFacp.Table.FlushStride
  print "   AcpiFacp:DutyOffset:       0x%08X" % AcpiFacp.Table.DutyOffset
  print "   AcpiFacp:DutyWidth:        0x%08X" % AcpiFacp.Table.DutyWidth
  print "   AcpiFacp:DayAlrm:          0x%08X" % AcpiFacp.Table.DayAlrm
  print "   AcpiFacp:MonAlrm:          0x%08X" % AcpiFacp.Table.MonAlrm
  print "   AcpiFacp:Century:          0x%08X" % AcpiFacp.Table.Century
  print "   AcpiFacp:Reserved4:        0x%08X" % AcpiFacp.Table.Reserved4
  print "   AcpiFacp:Reserved5:        0x%08X" % AcpiFacp.Table.Reserved5
  print "   AcpiFacp:Reserved6:        0x%08X" % AcpiFacp.Table.Reserved6
  print "   AcpiFacp:Flags:            0x%08X" % AcpiFacp.Table.Flags
elif  AcpiFacp.Table.Header.Revision == 0x03:
  print "   AcpiFacp:FirmwareCtrl:     0x%08X" % AcpiFacp.Table.FirmwareCtrl
  print "   AcpiFacp:Dsdt:             0x%08X" % AcpiFacp.Table.Dsdt
  print "   AcpiFacp:Reserved0:        0x%08X" % AcpiFacp.Table.Reserved0
  print "   AcpiFacp:PreferredPmProfile:0x%08X" % AcpiFacp.Table.PreferredPmProfile
  print "   AcpiFacp:SciInt:           0x%08X" % AcpiFacp.Table.SciInt
  print "   AcpiFacp:SmiCmd:           0x%08X" % AcpiFacp.Table.SmiCmd
  print "   AcpiFacp:AcpiEnable:       0x%08X" % AcpiFacp.Table.AcpiEnable
  print "   AcpiFacp:AcpiDisable:      0x%08X" % AcpiFacp.Table.AcpiDisable
  print "   AcpiFacp:S4BiosReq:        0x%08X" % AcpiFacp.Table.S4BiosReq
  print "   AcpiFacp:PstateCnt:        0x%08X" % AcpiFacp.Table.PstateCnt
  print "   AcpiFacp:Pm1aEvtBlk:       0x%08X" % AcpiFacp.Table.Pm1aEvtBlk
  print "   AcpiFacp:Pm1bEvtBlk:       0x%08X" % AcpiFacp.Table.Pm1bEvtBlk
  print "   AcpiFacp:Pm1aCntBlk:       0x%08X" % AcpiFacp.Table.Pm1aCntBlk
  print "   AcpiFacp:Pm1bCntBlk:       0x%08X" % AcpiFacp.Table.Pm1bCntBlk
  print "   AcpiFacp:Pm2CntBlk:        0x%08X" % AcpiFacp.Table.Pm2CntBlk
  print "   AcpiFacp:PmTmrBlk:         0x%08X" % AcpiFacp.Table.PmTmrBlk
  print "   AcpiFacp:Gpe0Blk:          0x%08X" % AcpiFacp.Table.Gpe0Blk
  print "   AcpiFacp:Gpe1Blk:          0x%08X" % AcpiFacp.Table.Gpe1Blk
  print "   AcpiFacp:Pm1EvtLen:        0x%08X" % AcpiFacp.Table.Pm1EvtLen
  print "   AcpiFacp:Pm1CntLen:        0x%08X" % AcpiFacp.Table.Pm1CntLen
  print "   AcpiFacp:Pm2CntLen:        0x%08X" % AcpiFacp.Table.Pm2CntLen
  print "   AcpiFacp:PmTmrLen:         0x%08X" % AcpiFacp.Table.PmTmrLen
  print "   AcpiFacp:Gpe0BlkLen:       0x%08X" % AcpiFacp.Table.Gpe0BlkLen
  print "   AcpiFacp:Gpe1BlkLen:       0x%08X" % AcpiFacp.Table.Gpe1BlkLen
  print "   AcpiFacp:Gpe1Base:         0x%08X" % AcpiFacp.Table.Gpe1Base
  print "   AcpiFacp:CstCnt:           0x%08X" % AcpiFacp.Table.CstCnt
  print "   AcpiFacp:PLvl2Lat:         0x%08X" % AcpiFacp.Table.PLvl2Lat
  print "   AcpiFacp:PLvl3Lat:         0x%08X" % AcpiFacp.Table.PLvl3Lat
  print "   AcpiFacp:FlushSize:        0x%08X" % AcpiFacp.Table.FlushSize
  print "   AcpiFacp:FlushStride:      0x%08X" % AcpiFacp.Table.FlushStride
  print "   AcpiFacp:DutyOffset:       0x%08X" % AcpiFacp.Table.DutyOffset
  print "   AcpiFacp:DutyWidth:        0x%08X" % AcpiFacp.Table.DutyWidth
  print "   AcpiFacp:DayAlrm:          0x%08X" % AcpiFacp.Table.DayAlrm
  print "   AcpiFacp:MonAlrm:          0x%08X" % AcpiFacp.Table.MonAlrm
  print "   AcpiFacp:Century:          0x%08X" % AcpiFacp.Table.Century
  print "   AcpiFacp:IaPcBootArch:     0x%08X" % AcpiFacp.Table.IaPcBootArch
  print "   AcpiFacp:Reserved1:        0x%08X" % AcpiFacp.Table.Reserved1
  print "   AcpiFacp:Flags:            0x%08X" % AcpiFacp.Table.Flags
  print "   AcpiFacp:ResetReg.AddressSpaceId:     0x%08X" % AcpiFacp.Table.ResetReg.AddressSpaceId
  print "   AcpiFacp:ResetReg.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitWidth
  print "   AcpiFacp:ResetReg.Reserved:           0x%08X" % AcpiFacp.Table.ResetReg.Reserved
  print "   AcpiFacp:ResetReg.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitOffset
  print "   AcpiFacp:ResetReg.Address:            0x%08X" % AcpiFacp.Table.ResetReg.Address
  print "   AcpiFacp:ResetValue:       0x%08X" % AcpiFacp.Table.ResetValue
  print "   AcpiFacp:XFirmwareCtrl:    0x%08X" % AcpiFacp.Table.XFirmwareCtrl
  print "   AcpiFacp:XDsdt:            0x%08X" % AcpiFacp.Table.XDsdt
  print "   AcpiFacp:XPm1aEvtBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AddressSpaceId
  print "   AcpiFacp:XPm1aEvtBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1aEvtBlk.Reserved:           0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.Reserved
  print "   AcpiFacp:XPm1aEvtBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1aEvtBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.Address
  print "   AcpiFacp:XPm1bEvtBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AddressSpaceId
  print "   AcpiFacp:XPm1bEvtBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1bEvtBlk.Reserved:           0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.Reserved
  print "   AcpiFacp:XPm1bEvtBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1bEvtBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.Address
  print "   AcpiFacp:XPm1aCntBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AddressSpaceId
  print "   AcpiFacp:XPm1aCntBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1aCntBlk.Reserved:           0x%08X" % AcpiFacp.Table.XPm1aCntBlk.Reserved
  print "   AcpiFacp:XPm1aCntBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1aCntBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1aCntBlk.Address
  print "   AcpiFacp:XPm1bCntBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AddressSpaceId
  print "   AcpiFacp:XPm1bCntBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1bCntBlk.Reserved:           0x%08X" % AcpiFacp.Table.XPm1bCntBlk.Reserved
  print "   AcpiFacp:XPm1bCntBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1bCntBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1bCntBlk.Address
  print "   AcpiFacp:XPm2CntBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm2CntBlk.AddressSpaceId
  print "   AcpiFacp:XPm2CntBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm2CntBlk.Reserved:           0x%08X" % AcpiFacp.Table.XPm2CntBlk.Reserved
  print "   AcpiFacp:XPm2CntBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm2CntBlk.Address:            0x%08X" % AcpiFacp.Table.XPm2CntBlk.Address
  print "   AcpiFacp:XPmTmrBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPmTmrBlk.AddressSpaceId
  print "   AcpiFacp:XPmTmrBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitWidth
  print "   AcpiFacp:XPmTmrBlk.Reserved:           0x%08X" % AcpiFacp.Table.XPmTmrBlk.Reserved
  print "   AcpiFacp:XPmTmrBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitOffset
  print "   AcpiFacp:XPmTmrBlk.Address:            0x%08X" % AcpiFacp.Table.XPmTmrBlk.Address
  print "   AcpiFacp:XGpe0Blk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XGpe0Blk.AddressSpaceId
  print "   AcpiFacp:XGpe0Blk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitWidth
  print "   AcpiFacp:XGpe0Blk.Reserved:           0x%08X" % AcpiFacp.Table.XGpe0Blk.Reserved
  print "   AcpiFacp:XGpe0Blk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitOffset
  print "   AcpiFacp:XGpe0Blk.Address:            0x%08X" % AcpiFacp.Table.XGpe0Blk.Address
  print "   AcpiFacp:XGpe1Blk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XGpe1Blk.AddressSpaceId
  print "   AcpiFacp:XGpe1Blk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitWidth
  print "   AcpiFacp:XGpe1Blk.Reserved:           0x%08X" % AcpiFacp.Table.XGpe1Blk.Reserved
  print "   AcpiFacp:XGpe1Blk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitOffset
  print "   AcpiFacp:XGpe1Blk.Address:            0x%08X" % AcpiFacp.Table.XGpe1Blk.Address
elif  AcpiFacp.Table.Header.Revision == 0x04:
  print "   AcpiFacp:FirmwareCtrl:     0x%08X" % AcpiFacp.Table.FirmwareCtrl
  print "   AcpiFacp:Dsdt:             0x%08X" % AcpiFacp.Table.Dsdt
  print "   AcpiFacp:Reserved0:        0x%08X" % AcpiFacp.Table.Reserved0
  print "   AcpiFacp:PreferredPmProfile:0x%08X" % AcpiFacp.Table.PreferredPmProfile
  print "   AcpiFacp:SciInt:           0x%08X" % AcpiFacp.Table.SciInt
  print "   AcpiFacp:SmiCmd:           0x%08X" % AcpiFacp.Table.SmiCmd
  print "   AcpiFacp:AcpiEnable:       0x%08X" % AcpiFacp.Table.AcpiEnable
  print "   AcpiFacp:AcpiDisable:      0x%08X" % AcpiFacp.Table.AcpiDisable
  print "   AcpiFacp:S4BiosReq:        0x%08X" % AcpiFacp.Table.S4BiosReq
  print "   AcpiFacp:PstateCnt:        0x%08X" % AcpiFacp.Table.PstateCnt
  print "   AcpiFacp:Pm1aEvtBlk:       0x%08X" % AcpiFacp.Table.Pm1aEvtBlk
  print "   AcpiFacp:Pm1bEvtBlk:       0x%08X" % AcpiFacp.Table.Pm1bEvtBlk
  print "   AcpiFacp:Pm1aCntBlk:       0x%08X" % AcpiFacp.Table.Pm1aCntBlk
  print "   AcpiFacp:Pm1bCntBlk:       0x%08X" % AcpiFacp.Table.Pm1bCntBlk
  print "   AcpiFacp:Pm2CntBlk:        0x%08X" % AcpiFacp.Table.Pm2CntBlk
  print "   AcpiFacp:PmTmrBlk:         0x%08X" % AcpiFacp.Table.PmTmrBlk
  print "   AcpiFacp:Gpe0Blk:          0x%08X" % AcpiFacp.Table.Gpe0Blk
  print "   AcpiFacp:Gpe1Blk:          0x%08X" % AcpiFacp.Table.Gpe1Blk
  print "   AcpiFacp:Pm1EvtLen:        0x%08X" % AcpiFacp.Table.Pm1EvtLen
  print "   AcpiFacp:Pm1CntLen:        0x%08X" % AcpiFacp.Table.Pm1CntLen
  print "   AcpiFacp:Pm2CntLen:        0x%08X" % AcpiFacp.Table.Pm2CntLen
  print "   AcpiFacp:PmTmrLen:         0x%08X" % AcpiFacp.Table.PmTmrLen
  print "   AcpiFacp:Gpe0BlkLen:       0x%08X" % AcpiFacp.Table.Gpe0BlkLen
  print "   AcpiFacp:Gpe1BlkLen:       0x%08X" % AcpiFacp.Table.Gpe1BlkLen
  print "   AcpiFacp:Gpe1Base:         0x%08X" % AcpiFacp.Table.Gpe1Base
  print "   AcpiFacp:CstCnt:           0x%08X" % AcpiFacp.Table.CstCnt
  print "   AcpiFacp:PLvl2Lat:         0x%08X" % AcpiFacp.Table.PLvl2Lat
  print "   AcpiFacp:PLvl3Lat:         0x%08X" % AcpiFacp.Table.PLvl3Lat
  print "   AcpiFacp:FlushSize:        0x%08X" % AcpiFacp.Table.FlushSize
  print "   AcpiFacp:FlushStride:      0x%08X" % AcpiFacp.Table.FlushStride
  print "   AcpiFacp:DutyOffset:       0x%08X" % AcpiFacp.Table.DutyOffset
  print "   AcpiFacp:DutyWidth:        0x%08X" % AcpiFacp.Table.DutyWidth
  print "   AcpiFacp:DayAlrm:          0x%08X" % AcpiFacp.Table.DayAlrm
  print "   AcpiFacp:MonAlrm:          0x%08X" % AcpiFacp.Table.MonAlrm
  print "   AcpiFacp:Century:          0x%08X" % AcpiFacp.Table.Century
  print "   AcpiFacp:IaPcBootArch:     0x%08X" % AcpiFacp.Table.IaPcBootArch
  print "   AcpiFacp:Reserved1:        0x%08X" % AcpiFacp.Table.Reserved1
  print "   AcpiFacp:Flags:            0x%08X" % AcpiFacp.Table.Flags
  print "   AcpiFacp:ResetReg.AddressSpaceId:     0x%08X" % AcpiFacp.Table.ResetReg.AddressSpaceId
  print "   AcpiFacp:ResetReg.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitWidth
  print "   AcpiFacp:ResetReg.AccessSize:         0x%08X" % AcpiFacp.Table.ResetReg.AccessSize
  print "   AcpiFacp:ResetReg.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitOffset
  print "   AcpiFacp:ResetReg.Address:            0x%08X" % AcpiFacp.Table.ResetReg.Address
  print "   AcpiFacp:ResetValue:       0x%08X" % AcpiFacp.Table.ResetValue
  print "   AcpiFacp:XFirmwareCtrl:    0x%08X" % AcpiFacp.Table.XFirmwareCtrl
  print "   AcpiFacp:XDsdt:            0x%08X" % AcpiFacp.Table.XDsdt
  print "   AcpiFacp:XPm1aEvtBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AddressSpaceId
  print "   AcpiFacp:XPm1aEvtBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1aEvtBlk.AccessSize:         0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AccessSize
  print "   AcpiFacp:XPm1aEvtBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1aEvtBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.Address
  print "   AcpiFacp:XPm1bEvtBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AddressSpaceId
  print "   AcpiFacp:XPm1bEvtBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1bEvtBlk.AccessSize:         0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AccessSize
  print "   AcpiFacp:XPm1bEvtBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1bEvtBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.Address
  print "   AcpiFacp:XPm1aCntBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AddressSpaceId
  print "   AcpiFacp:XPm1aCntBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1aCntBlk.AccessSize:         0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AccessSize
  print "   AcpiFacp:XPm1aCntBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1aCntBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1aCntBlk.Address
  print "   AcpiFacp:XPm1bCntBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AddressSpaceId
  print "   AcpiFacp:XPm1bCntBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1bCntBlk.AccessSize:         0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AccessSize
  print "   AcpiFacp:XPm1bCntBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1bCntBlk.Address:            0x%08X" % AcpiFacp.Table.XPm1bCntBlk.Address
  print "   AcpiFacp:XPm2CntBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPm2CntBlk.AddressSpaceId
  print "   AcpiFacp:XPm2CntBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm2CntBlk.AccessSize:         0x%08X" % AcpiFacp.Table.XPm2CntBlk.AccessSize
  print "   AcpiFacp:XPm2CntBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm2CntBlk.Address:            0x%08X" % AcpiFacp.Table.XPm2CntBlk.Address
  print "   AcpiFacp:XPmTmrBlk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XPmTmrBlk.AddressSpaceId
  print "   AcpiFacp:XPmTmrBlk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitWidth
  print "   AcpiFacp:XPmTmrBlk.AccessSize:         0x%08X" % AcpiFacp.Table.XPmTmrBlk.AccessSize
  print "   AcpiFacp:XPmTmrBlk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitOffset
  print "   AcpiFacp:XPmTmrBlk.Address:            0x%08X" % AcpiFacp.Table.XPmTmrBlk.Address
  print "   AcpiFacp:XGpe0Blk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XGpe0Blk.AddressSpaceId
  print "   AcpiFacp:XGpe0Blk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitWidth
  print "   AcpiFacp:XGpe0Blk.AccessSize:         0x%08X" % AcpiFacp.Table.XGpe0Blk.AccessSize
  print "   AcpiFacp:XGpe0Blk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitOffset
  print "   AcpiFacp:XGpe0Blk.Address:            0x%08X" % AcpiFacp.Table.XGpe0Blk.Address
  print "   AcpiFacp:XGpe1Blk.AddressSpaceId:     0x%08X" % AcpiFacp.Table.XGpe1Blk.AddressSpaceId
  print "   AcpiFacp:XGpe1Blk.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitWidth
  print "   AcpiFacp:XGpe1Blk.AccessSize:         0x%08X" % AcpiFacp.Table.XGpe1Blk.AccessSize
  print "   AcpiFacp:XGpe1Blk.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitOffset
  print "   AcpiFacp:XGpe1Blk.Address:            0x%08X" % AcpiFacp.Table.XGpe1Blk.Address
elif  AcpiFacp.Table.Header.Revision == 0x05:
  try:
    # ACPI 51
    MinorVersion = AcpiFacp.Table.MinorVersion
    print "   AcpiFacp:FirmwareCtrl:                       0x%08X" % AcpiFacp.Table.FirmwareCtrl
    print "   AcpiFacp:Dsdt:                               0x%08X" % AcpiFacp.Table.Dsdt
    print "   AcpiFacp:Reserved0:                          0x%08X" % AcpiFacp.Table.Reserved0
    print "   AcpiFacp:PreferredPmProfile:                 0x%08X" % AcpiFacp.Table.PreferredPmProfile
    print "   AcpiFacp:SciInt:                             0x%08X" % AcpiFacp.Table.SciInt
    print "   AcpiFacp:SmiCmd:                             0x%08X" % AcpiFacp.Table.SmiCmd
    print "   AcpiFacp:AcpiEnable:                         0x%08X" % AcpiFacp.Table.AcpiEnable
    print "   AcpiFacp:AcpiDisable:                        0x%08X" % AcpiFacp.Table.AcpiDisable
    print "   AcpiFacp:S4BiosReq:                          0x%08X" % AcpiFacp.Table.S4BiosReq
    print "   AcpiFacp:PstateCnt:                          0x%08X" % AcpiFacp.Table.PstateCnt
    print "   AcpiFacp:Pm1aEvtBlk:                         0x%08X" % AcpiFacp.Table.Pm1aEvtBlk
    print "   AcpiFacp:Pm1bEvtBlk:                         0x%08X" % AcpiFacp.Table.Pm1bEvtBlk
    print "   AcpiFacp:Pm1aCntBlk:                         0x%08X" % AcpiFacp.Table.Pm1aCntBlk
    print "   AcpiFacp:Pm1bCntBlk:                         0x%08X" % AcpiFacp.Table.Pm1bCntBlk
    print "   AcpiFacp:Pm2CntBlk:                          0x%08X" % AcpiFacp.Table.Pm2CntBlk
    print "   AcpiFacp:PmTmrBlk:                           0x%08X" % AcpiFacp.Table.PmTmrBlk
    print "   AcpiFacp:Gpe0Blk:                            0x%08X" % AcpiFacp.Table.Gpe0Blk
    print "   AcpiFacp:Gpe1Blk:                            0x%08X" % AcpiFacp.Table.Gpe1Blk
    print "   AcpiFacp:Pm1EvtLen:                          0x%08X" % AcpiFacp.Table.Pm1EvtLen
    print "   AcpiFacp:Pm1CntLen:                          0x%08X" % AcpiFacp.Table.Pm1CntLen
    print "   AcpiFacp:Pm2CntLen:                          0x%08X" % AcpiFacp.Table.Pm2CntLen
    print "   AcpiFacp:PmTmrLen:                           0x%08X" % AcpiFacp.Table.PmTmrLen
    print "   AcpiFacp:Gpe0BlkLen:                         0x%08X" % AcpiFacp.Table.Gpe0BlkLen
    print "   AcpiFacp:Gpe1BlkLen:                         0x%08X" % AcpiFacp.Table.Gpe1BlkLen
    print "   AcpiFacp:Gpe1Base:                           0x%08X" % AcpiFacp.Table.Gpe1Base
    print "   AcpiFacp:CstCnt:                             0x%08X" % AcpiFacp.Table.CstCnt
    print "   AcpiFacp:PLvl2Lat:                           0x%08X" % AcpiFacp.Table.PLvl2Lat
    print "   AcpiFacp:PLvl3Lat:                           0x%08X" % AcpiFacp.Table.PLvl3Lat
    print "   AcpiFacp:FlushSize:                          0x%08X" % AcpiFacp.Table.FlushSize
    print "   AcpiFacp:FlushStride:                        0x%08X" % AcpiFacp.Table.FlushStride
    print "   AcpiFacp:DutyOffset:                         0x%08X" % AcpiFacp.Table.DutyOffset
    print "   AcpiFacp:DutyWidth:                          0x%08X" % AcpiFacp.Table.DutyWidth
    print "   AcpiFacp:DayAlrm:                            0x%08X" % AcpiFacp.Table.DayAlrm
    print "   AcpiFacp:MonAlrm:                            0x%08X" % AcpiFacp.Table.MonAlrm
    print "   AcpiFacp:Century:                            0x%08X" % AcpiFacp.Table.Century
    print "   AcpiFacp:IaPcBootArch:                       0x%08X" % AcpiFacp.Table.IaPcBootArch
    print "   AcpiFacp:Reserved1:                          0x%08X" % AcpiFacp.Table.Reserved1
    print "   AcpiFacp:Flags:                              0x%08X" % AcpiFacp.Table.Flags
    print "   AcpiFacp:ResetReg.AddressSpaceId:            0x%08X" % AcpiFacp.Table.ResetReg.AddressSpaceId
    print "   AcpiFacp:ResetReg.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitWidth
    print "   AcpiFacp:ResetReg.AccessSize:                0x%08X" % AcpiFacp.Table.ResetReg.AccessSize
    print "   AcpiFacp:ResetReg.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitOffset
    print "   AcpiFacp:ResetReg.Address:                   0x%08X" % AcpiFacp.Table.ResetReg.Address
    print "   AcpiFacp:ResetValue:                         0x%08X" % AcpiFacp.Table.ResetValue
    print "   AcpiFacp:ArmBootArch:                        0x%08X" % AcpiFacp.Table.ArmBootArch
    print "   AcpiFacp:MinorVersion:                       0x%08X" % AcpiFacp.Table.MinorVersion
    print "   AcpiFacp:XDsdt:                              0x%08X" % AcpiFacp.Table.XDsdt
    print "   AcpiFacp:XPm1aEvtBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AddressSpaceId
    print "   AcpiFacp:XPm1aEvtBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1aEvtBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AccessSize
    print "   AcpiFacp:XPm1aEvtBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1aEvtBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.Address
    print "   AcpiFacp:XPm1bEvtBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AddressSpaceId
    print "   AcpiFacp:XPm1bEvtBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1bEvtBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AccessSize
    print "   AcpiFacp:XPm1bEvtBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1bEvtBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.Address
    print "   AcpiFacp:XPm1aCntBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AddressSpaceId
    print "   AcpiFacp:XPm1aCntBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1aCntBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AccessSize
    print "   AcpiFacp:XPm1aCntBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1aCntBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1aCntBlk.Address
    print "   AcpiFacp:XPm1bCntBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AddressSpaceId
    print "   AcpiFacp:XPm1bCntBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1bCntBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AccessSize
    print "   AcpiFacp:XPm1bCntBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1bCntBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1bCntBlk.Address
    print "   AcpiFacp:XPm2CntBlk.AddressSpaceId:          0x%08X" % AcpiFacp.Table.XPm2CntBlk.AddressSpaceId
    print "   AcpiFacp:XPm2CntBlk.RegisterBitWidth:        0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitWidth
    print "   AcpiFacp:XPm2CntBlk.AccessSize:              0x%08X" % AcpiFacp.Table.XPm2CntBlk.AccessSize
    print "   AcpiFacp:XPm2CntBlk.RegisterBitOffset:       0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitOffset
    print "   AcpiFacp:XPm2CntBlk.Address:                 0x%08X" % AcpiFacp.Table.XPm2CntBlk.Address
    print "   AcpiFacp:XPmTmrBlk.AddressSpaceId:           0x%08X" % AcpiFacp.Table.XPmTmrBlk.AddressSpaceId
    print "   AcpiFacp:XPmTmrBlk.RegisterBitWidth:         0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitWidth
    print "   AcpiFacp:XPmTmrBlk.AccessSize:               0x%08X" % AcpiFacp.Table.XPmTmrBlk.AccessSize
    print "   AcpiFacp:XPmTmrBlk.RegisterBitOffset:        0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitOffset
    print "   AcpiFacp:XPmTmrBlk.Address:                  0x%08X" % AcpiFacp.Table.XPmTmrBlk.Address
    print "   AcpiFacp:XGpe0Blk.AddressSpaceId:            0x%08X" % AcpiFacp.Table.XGpe0Blk.AddressSpaceId
    print "   AcpiFacp:XGpe0Blk.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitWidth
    print "   AcpiFacp:XGpe0Blk.AccessSize:                0x%08X" % AcpiFacp.Table.XGpe0Blk.AccessSize
    print "   AcpiFacp:XGpe0Blk.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitOffset
    print "   AcpiFacp:XGpe0Blk.Address:                   0x%08X" % AcpiFacp.Table.XGpe0Blk.Address
    print "   AcpiFacp:XGpe1Blk.AddressSpaceId:            0x%08X" % AcpiFacp.Table.XGpe1Blk.AddressSpaceId
    print "   AcpiFacp:XGpe1Blk.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitWidth
    print "   AcpiFacp:XGpe1Blk.AccessSize:                0x%08X" % AcpiFacp.Table.XGpe1Blk.AccessSize
    print "   AcpiFacp:XGpe1Blk.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitOffset
    print "   AcpiFacp:XGpe1Blk.Address:                   0x%08X" % AcpiFacp.Table.XGpe1Blk.Address
    print "   AcpiFacp:SleepControlReg.AddressSpaceId:     0x%08X" % AcpiFacp.Table.SleepControlReg.AddressSpaceId
    print "   AcpiFacp:SleepControlReg.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.SleepControlReg.RegisterBitWidth
    print "   AcpiFacp:SleepControlReg.AccessSize:         0x%08X" % AcpiFacp.Table.SleepControlReg.AccessSize
    print "   AcpiFacp:SleepControlReg.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.SleepControlReg.RegisterBitOffset
    print "   AcpiFacp:SleepControlReg.Address:            0x%08X" % AcpiFacp.Table.SleepControlReg.Address
    print "   AcpiFacp:SleepStatusReg.AddressSpaceId:      0x%08X" % AcpiFacp.Table.SleepStatusReg.AddressSpaceId
    print "   AcpiFacp:SleepStatusReg.RegisterBitWidth:    0x%08X" % AcpiFacp.Table.SleepStatusReg.RegisterBitWidth
    print "   AcpiFacp:SleepStatusReg.AccessSize:          0x%08X" % AcpiFacp.Table.SleepStatusReg.AccessSize
    print "   AcpiFacp:SleepStatusReg.RegisterBitOffset:   0x%08X" % AcpiFacp.Table.SleepStatusReg.RegisterBitOffset
    print "   AcpiFacp:SleepStatusReg.Address:             0x%08X" % AcpiFacp.Table.SleepStatusReg.Address
  except:
    # ACPI 50
    print "   AcpiFacp:FirmwareCtrl:                       0x%08X" % AcpiFacp.Table.FirmwareCtrl
    print "   AcpiFacp:Dsdt:                               0x%08X" % AcpiFacp.Table.Dsdt
    print "   AcpiFacp:Reserved0:                          0x%08X" % AcpiFacp.Table.Reserved0
    print "   AcpiFacp:PreferredPmProfile:                 0x%08X" % AcpiFacp.Table.PreferredPmProfile
    print "   AcpiFacp:SciInt:                             0x%08X" % AcpiFacp.Table.SciInt
    print "   AcpiFacp:SmiCmd:                             0x%08X" % AcpiFacp.Table.SmiCmd
    print "   AcpiFacp:AcpiEnable:                         0x%08X" % AcpiFacp.Table.AcpiEnable
    print "   AcpiFacp:AcpiDisable:                        0x%08X" % AcpiFacp.Table.AcpiDisable
    print "   AcpiFacp:S4BiosReq:                          0x%08X" % AcpiFacp.Table.S4BiosReq
    print "   AcpiFacp:PstateCnt:                          0x%08X" % AcpiFacp.Table.PstateCnt
    print "   AcpiFacp:Pm1aEvtBlk:                         0x%08X" % AcpiFacp.Table.Pm1aEvtBlk
    print "   AcpiFacp:Pm1bEvtBlk:                         0x%08X" % AcpiFacp.Table.Pm1bEvtBlk
    print "   AcpiFacp:Pm1aCntBlk:                         0x%08X" % AcpiFacp.Table.Pm1aCntBlk
    print "   AcpiFacp:Pm1bCntBlk:                         0x%08X" % AcpiFacp.Table.Pm1bCntBlk
    print "   AcpiFacp:Pm2CntBlk:                          0x%08X" % AcpiFacp.Table.Pm2CntBlk
    print "   AcpiFacp:PmTmrBlk:                           0x%08X" % AcpiFacp.Table.PmTmrBlk
    print "   AcpiFacp:Gpe0Blk:                            0x%08X" % AcpiFacp.Table.Gpe0Blk
    print "   AcpiFacp:Gpe1Blk:                            0x%08X" % AcpiFacp.Table.Gpe1Blk
    print "   AcpiFacp:Pm1EvtLen:                          0x%08X" % AcpiFacp.Table.Pm1EvtLen
    print "   AcpiFacp:Pm1CntLen:                          0x%08X" % AcpiFacp.Table.Pm1CntLen
    print "   AcpiFacp:Pm2CntLen:                          0x%08X" % AcpiFacp.Table.Pm2CntLen
    print "   AcpiFacp:PmTmrLen:                           0x%08X" % AcpiFacp.Table.PmTmrLen
    print "   AcpiFacp:Gpe0BlkLen:                         0x%08X" % AcpiFacp.Table.Gpe0BlkLen
    print "   AcpiFacp:Gpe1BlkLen:                         0x%08X" % AcpiFacp.Table.Gpe1BlkLen
    print "   AcpiFacp:Gpe1Base:                           0x%08X" % AcpiFacp.Table.Gpe1Base
    print "   AcpiFacp:CstCnt:                             0x%08X" % AcpiFacp.Table.CstCnt
    print "   AcpiFacp:PLvl2Lat:                           0x%08X" % AcpiFacp.Table.PLvl2Lat
    print "   AcpiFacp:PLvl3Lat:                           0x%08X" % AcpiFacp.Table.PLvl3Lat
    print "   AcpiFacp:FlushSize:                          0x%08X" % AcpiFacp.Table.FlushSize
    print "   AcpiFacp:FlushStride:                        0x%08X" % AcpiFacp.Table.FlushStride
    print "   AcpiFacp:DutyOffset:                         0x%08X" % AcpiFacp.Table.DutyOffset
    print "   AcpiFacp:DutyWidth:                          0x%08X" % AcpiFacp.Table.DutyWidth
    print "   AcpiFacp:DayAlrm:                            0x%08X" % AcpiFacp.Table.DayAlrm
    print "   AcpiFacp:MonAlrm:                            0x%08X" % AcpiFacp.Table.MonAlrm
    print "   AcpiFacp:Century:                            0x%08X" % AcpiFacp.Table.Century
    print "   AcpiFacp:IaPcBootArch:                       0x%08X" % AcpiFacp.Table.IaPcBootArch
    print "   AcpiFacp:Reserved1:                          0x%08X" % AcpiFacp.Table.Reserved1
    print "   AcpiFacp:Flags:                              0x%08X" % AcpiFacp.Table.Flags
    print "   AcpiFacp:ResetReg.AddressSpaceId:            0x%08X" % AcpiFacp.Table.ResetReg.AddressSpaceId
    print "   AcpiFacp:ResetReg.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitWidth
    print "   AcpiFacp:ResetReg.AccessSize:                0x%08X" % AcpiFacp.Table.ResetReg.AccessSize
    print "   AcpiFacp:ResetReg.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitOffset
    print "   AcpiFacp:ResetReg.Address:                   0x%08X" % AcpiFacp.Table.ResetReg.Address
    print "   AcpiFacp:ResetValue:                         0x%08X" % AcpiFacp.Table.ResetValue
    print "   AcpiFacp:XFirmwareCtrl:                      0x%08X" % AcpiFacp.Table.XFirmwareCtrl
    print "   AcpiFacp:XDsdt:                              0x%08X" % AcpiFacp.Table.XDsdt
    print "   AcpiFacp:XPm1aEvtBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AddressSpaceId
    print "   AcpiFacp:XPm1aEvtBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1aEvtBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AccessSize
    print "   AcpiFacp:XPm1aEvtBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1aEvtBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.Address
    print "   AcpiFacp:XPm1bEvtBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AddressSpaceId
    print "   AcpiFacp:XPm1bEvtBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1bEvtBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AccessSize
    print "   AcpiFacp:XPm1bEvtBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1bEvtBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.Address
    print "   AcpiFacp:XPm1aCntBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AddressSpaceId
    print "   AcpiFacp:XPm1aCntBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1aCntBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AccessSize
    print "   AcpiFacp:XPm1aCntBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1aCntBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1aCntBlk.Address
    print "   AcpiFacp:XPm1bCntBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AddressSpaceId
    print "   AcpiFacp:XPm1bCntBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitWidth
    print "   AcpiFacp:XPm1bCntBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AccessSize
    print "   AcpiFacp:XPm1bCntBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitOffset
    print "   AcpiFacp:XPm1bCntBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1bCntBlk.Address
    print "   AcpiFacp:XPm2CntBlk.AddressSpaceId:          0x%08X" % AcpiFacp.Table.XPm2CntBlk.AddressSpaceId
    print "   AcpiFacp:XPm2CntBlk.RegisterBitWidth:        0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitWidth
    print "   AcpiFacp:XPm2CntBlk.AccessSize:              0x%08X" % AcpiFacp.Table.XPm2CntBlk.AccessSize
    print "   AcpiFacp:XPm2CntBlk.RegisterBitOffset:       0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitOffset
    print "   AcpiFacp:XPm2CntBlk.Address:                 0x%08X" % AcpiFacp.Table.XPm2CntBlk.Address
    print "   AcpiFacp:XPmTmrBlk.AddressSpaceId:           0x%08X" % AcpiFacp.Table.XPmTmrBlk.AddressSpaceId
    print "   AcpiFacp:XPmTmrBlk.RegisterBitWidth:         0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitWidth
    print "   AcpiFacp:XPmTmrBlk.AccessSize:               0x%08X" % AcpiFacp.Table.XPmTmrBlk.AccessSize
    print "   AcpiFacp:XPmTmrBlk.RegisterBitOffset:        0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitOffset
    print "   AcpiFacp:XPmTmrBlk.Address:                  0x%08X" % AcpiFacp.Table.XPmTmrBlk.Address
    print "   AcpiFacp:XGpe0Blk.AddressSpaceId:            0x%08X" % AcpiFacp.Table.XGpe0Blk.AddressSpaceId
    print "   AcpiFacp:XGpe0Blk.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitWidth
    print "   AcpiFacp:XGpe0Blk.AccessSize:                0x%08X" % AcpiFacp.Table.XGpe0Blk.AccessSize
    print "   AcpiFacp:XGpe0Blk.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitOffset
    print "   AcpiFacp:XGpe0Blk.Address:                   0x%08X" % AcpiFacp.Table.XGpe0Blk.Address
    print "   AcpiFacp:XGpe1Blk.AddressSpaceId:            0x%08X" % AcpiFacp.Table.XGpe1Blk.AddressSpaceId
    print "   AcpiFacp:XGpe1Blk.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitWidth
    print "   AcpiFacp:XGpe1Blk.AccessSize:                0x%08X" % AcpiFacp.Table.XGpe1Blk.AccessSize
    print "   AcpiFacp:XGpe1Blk.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitOffset
    print "   AcpiFacp:XGpe1Blk.Address:                   0x%08X" % AcpiFacp.Table.XGpe1Blk.Address
    print "   AcpiFacp:SleepControlReg.AddressSpaceId:     0x%08X" % AcpiFacp.Table.SleepControlReg.AddressSpaceId
    print "   AcpiFacp:SleepControlReg.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.SleepControlReg.RegisterBitWidth
    print "   AcpiFacp:SleepControlReg.AccessSize:         0x%08X" % AcpiFacp.Table.SleepControlReg.AccessSize
    print "   AcpiFacp:SleepControlReg.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.SleepControlReg.RegisterBitOffset
    print "   AcpiFacp:SleepControlReg.Address:            0x%08X" % AcpiFacp.Table.SleepControlReg.Address
    print "   AcpiFacp:SleepStatusReg.AddressSpaceId:      0x%08X" % AcpiFacp.Table.SleepStatusReg.AddressSpaceId
    print "   AcpiFacp:SleepStatusReg.RegisterBitWidth:    0x%08X" % AcpiFacp.Table.SleepStatusReg.RegisterBitWidth
    print "   AcpiFacp:SleepStatusReg.AccessSize:          0x%08X" % AcpiFacp.Table.SleepStatusReg.AccessSize
    print "   AcpiFacp:SleepStatusReg.RegisterBitOffset:   0x%08X" % AcpiFacp.Table.SleepStatusReg.RegisterBitOffset
    print "   AcpiFacp:SleepStatusReg.Address:             0x%08X" % AcpiFacp.Table.SleepStatusReg.Address
elif  AcpiFacp.Table.Header.Revision == 0x06:
  print "   AcpiFacp:FirmwareCtrl:                       0x%08X" % AcpiFacp.Table.FirmwareCtrl
  print "   AcpiFacp:Dsdt:                               0x%08X" % AcpiFacp.Table.Dsdt
  print "   AcpiFacp:Reserved0:                          0x%08X" % AcpiFacp.Table.Reserved0
  print "   AcpiFacp:PreferredPmProfile:                 0x%08X" % AcpiFacp.Table.PreferredPmProfile
  print "   AcpiFacp:SciInt:                             0x%08X" % AcpiFacp.Table.SciInt
  print "   AcpiFacp:SmiCmd:                             0x%08X" % AcpiFacp.Table.SmiCmd
  print "   AcpiFacp:AcpiEnable:                         0x%08X" % AcpiFacp.Table.AcpiEnable
  print "   AcpiFacp:AcpiDisable:                        0x%08X" % AcpiFacp.Table.AcpiDisable
  print "   AcpiFacp:S4BiosReq:                          0x%08X" % AcpiFacp.Table.S4BiosReq
  print "   AcpiFacp:PstateCnt:                          0x%08X" % AcpiFacp.Table.PstateCnt
  print "   AcpiFacp:Pm1aEvtBlk:                         0x%08X" % AcpiFacp.Table.Pm1aEvtBlk
  print "   AcpiFacp:Pm1bEvtBlk:                         0x%08X" % AcpiFacp.Table.Pm1bEvtBlk
  print "   AcpiFacp:Pm1aCntBlk:                         0x%08X" % AcpiFacp.Table.Pm1aCntBlk
  print "   AcpiFacp:Pm1bCntBlk:                         0x%08X" % AcpiFacp.Table.Pm1bCntBlk
  print "   AcpiFacp:Pm2CntBlk:                          0x%08X" % AcpiFacp.Table.Pm2CntBlk
  print "   AcpiFacp:PmTmrBlk:                           0x%08X" % AcpiFacp.Table.PmTmrBlk
  print "   AcpiFacp:Gpe0Blk:                            0x%08X" % AcpiFacp.Table.Gpe0Blk
  print "   AcpiFacp:Gpe1Blk:                            0x%08X" % AcpiFacp.Table.Gpe1Blk
  print "   AcpiFacp:Pm1EvtLen:                          0x%08X" % AcpiFacp.Table.Pm1EvtLen
  print "   AcpiFacp:Pm1CntLen:                          0x%08X" % AcpiFacp.Table.Pm1CntLen
  print "   AcpiFacp:Pm2CntLen:                          0x%08X" % AcpiFacp.Table.Pm2CntLen
  print "   AcpiFacp:PmTmrLen:                           0x%08X" % AcpiFacp.Table.PmTmrLen
  print "   AcpiFacp:Gpe0BlkLen:                         0x%08X" % AcpiFacp.Table.Gpe0BlkLen
  print "   AcpiFacp:Gpe1BlkLen:                         0x%08X" % AcpiFacp.Table.Gpe1BlkLen
  print "   AcpiFacp:Gpe1Base:                           0x%08X" % AcpiFacp.Table.Gpe1Base
  print "   AcpiFacp:CstCnt:                             0x%08X" % AcpiFacp.Table.CstCnt
  print "   AcpiFacp:PLvl2Lat:                           0x%08X" % AcpiFacp.Table.PLvl2Lat
  print "   AcpiFacp:PLvl3Lat:                           0x%08X" % AcpiFacp.Table.PLvl3Lat
  print "   AcpiFacp:FlushSize:                          0x%08X" % AcpiFacp.Table.FlushSize
  print "   AcpiFacp:FlushStride:                        0x%08X" % AcpiFacp.Table.FlushStride
  print "   AcpiFacp:DutyOffset:                         0x%08X" % AcpiFacp.Table.DutyOffset
  print "   AcpiFacp:DutyWidth:                          0x%08X" % AcpiFacp.Table.DutyWidth
  print "   AcpiFacp:DayAlrm:                            0x%08X" % AcpiFacp.Table.DayAlrm
  print "   AcpiFacp:MonAlrm:                            0x%08X" % AcpiFacp.Table.MonAlrm
  print "   AcpiFacp:Century:                            0x%08X" % AcpiFacp.Table.Century
  print "   AcpiFacp:IaPcBootArch:                       0x%08X" % AcpiFacp.Table.IaPcBootArch
  print "   AcpiFacp:Reserved1:                          0x%08X" % AcpiFacp.Table.Reserved1
  print "   AcpiFacp:Flags:                              0x%08X" % AcpiFacp.Table.Flags
  print "   AcpiFacp:ResetReg.AddressSpaceId:            0x%08X" % AcpiFacp.Table.ResetReg.AddressSpaceId
  print "   AcpiFacp:ResetReg.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitWidth
  print "   AcpiFacp:ResetReg.AccessSize:                0x%08X" % AcpiFacp.Table.ResetReg.AccessSize
  print "   AcpiFacp:ResetReg.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.ResetReg.RegisterBitOffset
  print "   AcpiFacp:ResetReg.Address:                   0x%08X" % AcpiFacp.Table.ResetReg.Address
  print "   AcpiFacp:ResetValue:                         0x%08X" % AcpiFacp.Table.ResetValue
  print "   AcpiFacp:ArmBootArch:                        0x%08X" % AcpiFacp.Table.ArmBootArch
  print "   AcpiFacp:MinorVersion:                       0x%08X" % AcpiFacp.Table.MinorVersion
  print "   AcpiFacp:XDsdt:                              0x%08X" % AcpiFacp.Table.XDsdt
  print "   AcpiFacp:XPm1aEvtBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AddressSpaceId
  print "   AcpiFacp:XPm1aEvtBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1aEvtBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.AccessSize
  print "   AcpiFacp:XPm1aEvtBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1aEvtBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1aEvtBlk.Address
  print "   AcpiFacp:XPm1bEvtBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AddressSpaceId
  print "   AcpiFacp:XPm1bEvtBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1bEvtBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.AccessSize
  print "   AcpiFacp:XPm1bEvtBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1bEvtBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1bEvtBlk.Address
  print "   AcpiFacp:XPm1aCntBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AddressSpaceId
  print "   AcpiFacp:XPm1aCntBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1aCntBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1aCntBlk.AccessSize
  print "   AcpiFacp:XPm1aCntBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1aCntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1aCntBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1aCntBlk.Address
  print "   AcpiFacp:XPm1bCntBlk.AddressSpaceId:         0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AddressSpaceId
  print "   AcpiFacp:XPm1bCntBlk.RegisterBitWidth:       0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm1bCntBlk.AccessSize:             0x%08X" % AcpiFacp.Table.XPm1bCntBlk.AccessSize
  print "   AcpiFacp:XPm1bCntBlk.RegisterBitOffset:      0x%08X" % AcpiFacp.Table.XPm1bCntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm1bCntBlk.Address:                0x%08X" % AcpiFacp.Table.XPm1bCntBlk.Address
  print "   AcpiFacp:XPm2CntBlk.AddressSpaceId:          0x%08X" % AcpiFacp.Table.XPm2CntBlk.AddressSpaceId
  print "   AcpiFacp:XPm2CntBlk.RegisterBitWidth:        0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitWidth
  print "   AcpiFacp:XPm2CntBlk.AccessSize:              0x%08X" % AcpiFacp.Table.XPm2CntBlk.AccessSize
  print "   AcpiFacp:XPm2CntBlk.RegisterBitOffset:       0x%08X" % AcpiFacp.Table.XPm2CntBlk.RegisterBitOffset
  print "   AcpiFacp:XPm2CntBlk.Address:                 0x%08X" % AcpiFacp.Table.XPm2CntBlk.Address
  print "   AcpiFacp:XPmTmrBlk.AddressSpaceId:           0x%08X" % AcpiFacp.Table.XPmTmrBlk.AddressSpaceId
  print "   AcpiFacp:XPmTmrBlk.RegisterBitWidth:         0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitWidth
  print "   AcpiFacp:XPmTmrBlk.AccessSize:               0x%08X" % AcpiFacp.Table.XPmTmrBlk.AccessSize
  print "   AcpiFacp:XPmTmrBlk.RegisterBitOffset:        0x%08X" % AcpiFacp.Table.XPmTmrBlk.RegisterBitOffset
  print "   AcpiFacp:XPmTmrBlk.Address:                  0x%08X" % AcpiFacp.Table.XPmTmrBlk.Address
  print "   AcpiFacp:XGpe0Blk.AddressSpaceId:            0x%08X" % AcpiFacp.Table.XGpe0Blk.AddressSpaceId
  print "   AcpiFacp:XGpe0Blk.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitWidth
  print "   AcpiFacp:XGpe0Blk.AccessSize:                0x%08X" % AcpiFacp.Table.XGpe0Blk.AccessSize
  print "   AcpiFacp:XGpe0Blk.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.XGpe0Blk.RegisterBitOffset
  print "   AcpiFacp:XGpe0Blk.Address:                   0x%08X" % AcpiFacp.Table.XGpe0Blk.Address
  print "   AcpiFacp:XGpe1Blk.AddressSpaceId:            0x%08X" % AcpiFacp.Table.XGpe1Blk.AddressSpaceId
  print "   AcpiFacp:XGpe1Blk.RegisterBitWidth:          0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitWidth
  print "   AcpiFacp:XGpe1Blk.AccessSize:                0x%08X" % AcpiFacp.Table.XGpe1Blk.AccessSize
  print "   AcpiFacp:XGpe1Blk.RegisterBitOffset:         0x%08X" % AcpiFacp.Table.XGpe1Blk.RegisterBitOffset
  print "   AcpiFacp:XGpe1Blk.Address:                   0x%08X" % AcpiFacp.Table.XGpe1Blk.Address
  print "   AcpiFacp:SleepControlReg.AddressSpaceId:     0x%08X" % AcpiFacp.Table.SleepControlReg.AddressSpaceId
  print "   AcpiFacp:SleepControlReg.RegisterBitWidth:   0x%08X" % AcpiFacp.Table.SleepControlReg.RegisterBitWidth
  print "   AcpiFacp:SleepControlReg.AccessSize:         0x%08X" % AcpiFacp.Table.SleepControlReg.AccessSize
  print "   AcpiFacp:SleepControlReg.RegisterBitOffset:  0x%08X" % AcpiFacp.Table.SleepControlReg.RegisterBitOffset
  print "   AcpiFacp:SleepControlReg.Address:            0x%08X" % AcpiFacp.Table.SleepControlReg.Address
  print "   AcpiFacp:SleepStatusReg.AddressSpaceId:      0x%08X" % AcpiFacp.Table.SleepStatusReg.AddressSpaceId
  print "   AcpiFacp:SleepStatusReg.RegisterBitWidth:    0x%08X" % AcpiFacp.Table.SleepStatusReg.RegisterBitWidth
  print "   AcpiFacp:SleepStatusReg.AccessSize:          0x%08X" % AcpiFacp.Table.SleepStatusReg.AccessSize
  print "   AcpiFacp:SleepStatusReg.RegisterBitOffset:   0x%08X" % AcpiFacp.Table.SleepStatusReg.RegisterBitOffset
  print "   AcpiFacp:SleepStatusReg.Address:             0x%08X" % AcpiFacp.Table.SleepStatusReg.Address
  print "   AcpiFacp:HypervisorVendorIdentity:           0x%08X" % AcpiFacp.Table.HypervisorVendorIdentity

import EfiPy
if AcpiFacp.Size != EfiPy.sizeof (AcpiFacp.Table):
  print "WARNNING: FACP size and Spec defined size are inconsistent."
  print "          FACP size: %d, Spec defined size: %d" % (AcpiFacp.Size, EfiPy.sizeof (AcpiFacp.Table))

print
from EfiPyLib.EfiPyHexDump import EfiPyHexDump
Memory = (EfiPy.CHAR8 * AcpiFacp.Size).from_address (AcpiFacp.Address)
EfiPyHexDump (2, AcpiFacp.Address, Memory, True, "ACPI: FACP")
