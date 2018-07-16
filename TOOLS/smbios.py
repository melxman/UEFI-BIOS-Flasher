#!/usr/bin/python

#
# smbios.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# smbios.py is free software: you can redistribute it and/or modify
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

import sys
import EfiPy

from EfiPy.MdePkg.Protocol import Smbios as sb
import EfiPy.MdePkg.IndustryStandard.SmBios as Isb

def StructDump (c_p, _class, _obj, leading = 0):

  for field in _class._fields_:

    _c = field[1]
    _o = getattr (_obj, field[0])

    print " " * leading, "%s: " % field[0],

    if issubclass (field[1], Isb.SMBIOS_TABLE_STRING):

      print "%d(0x%X," % (_o.value, _o.value),
      if _o.value != 0:
        c_t = c_p
        for idx in range (_o.value - 1):
          c_t = c_t + len (EfiPy.PCHAR8(c_t).value) + 1
        c_s = EfiPy.PCHAR8(c_t)
        print 'String: "%s")' % c_s.value
      else:
        print "String: [Empty])"
        
    elif issubclass (field[1], EfiPy._SimpleCData):

      print "%d(0x%X)" % (_o, _o)

    elif isinstance (_o, EfiPy.GUID):

      print "%s" % _o

    elif isinstance (_o, EfiPy.Structure):

      print "(Structure)"
      StructDump (c_p, _c, _o, leading + 2)

    elif isinstance (_o, EfiPy.Array):

      print "Array * %d" % len(_o)

      for idx in range(len(_o)):

        print " " * (leading + 2), "%s[%d]:" % (field[0], idx),
        if type(_o[idx]) in [int, long]:
          print "%d(0x%X)" % (_o[idx], _o[idx])
        else:
          print
          StructDump (c_p, type(_o[idx]), _o[idx], leading + 4)

def SmbiosDump (Record):

  print "=========================================================="

  try:
    SmbiosClass = getattr(Isb, "SMBIOS_TABLE_TYPE%d" % Record[0].Type)

    sbObjp = EfiPy.cast (Record, EfiPy.PVOID)
    sbObj  = EfiPy.cast (Record, EfiPy.POINTER(SmbiosClass))[0]

    print "Type %3d, Length: %d, Handle: 0x%08X" % (sbObj.Hdr.Type, sbObj.Hdr.Length, sbObj.Hdr.Handle)

    c_p = sbObjp.value + sbObj.Hdr.Length

    StructDump (c_p, SmbiosClass, sbObj, 0)

  except:

    SmbiosClass = Isb.SMBIOS_STRUCTURE
    sbObj = EfiPy.cast (Record, EfiPy.POINTER(SmbiosClass))[0]

    print "Type %3d, Length: %d, Handle: 0x%08X" % (sbObj.Type, sbObj.Length, sbObj.Handle)


if __name__ == "__main__":

  showall  = False
  showlist = []

  if len (sys.argv) < 3:
    showall = True
  else:
    try:
      showlist = map (int, sys.argv[1:])
    except:
      showall = True

  Interface = EfiPy.PVOID ()

  Status = EfiPy.gBS.LocateProtocol (
                  EfiPy.byref (sb.gEfiSmbiosProtocolGuid),
                  None,
                  EfiPy.byref (Interface)
                  )
  if EfiPy.EFI_ERROR(Status):
    print "Error: %x" % Status
    exit (0)

  Smbios = EfiPy.cast (Interface, EfiPy.POINTER(sb.EFI_SMBIOS_PROTOCOL))

  SmbiosHandle = sb.EFI_SMBIOS_HANDLE (Isb.SMBIOS_HANDLE_PI_RESERVED)

  Record = EfiPy.POINTER(sb.EFI_SMBIOS_TABLE_HEADER)()

  # Isb = __import__ ("EfiPy.MdePkg.IndustryStandard.SmBios", globals(), locals(), ['dummy'])

  while (1):
    Status = Smbios[0].GetNext (
               Smbios,
               EfiPy.byref (SmbiosHandle),
               None,
               EfiPy.byref (Record),
               None)
    if EfiPy.EFI_ERROR (Status):
      break

    if showall == True:
      SmbiosDump (Record)
    else:
      if Record[0].Type in showlist:
        SmbiosDump (Record)
