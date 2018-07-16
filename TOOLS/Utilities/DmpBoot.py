#!/usr/bin/python

#
# DmpBoot.py
#
# Copyright (C) 2015 - 2018 efipy.core@gmail.com All rights reserved.
#
# DmpBoot.py is free software: you can redistribute it and/or modify
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

import EfiPy

from   EfiPy.MdePkg.Guid.GlobalVariable       import *
from   EfiPy.MdePkg.Protocol.DevicePathEfiPy  import *
from   EfiPyLib.EfiPyVariableDump             import DmpVariable
from   EfiPyLib.EfiPyHexDump                  import EfiPyHexDump

#
# EfiPy Utilities dump boot####
#
def EfiPyDumpBoot ():

  DataSize  = EfiPy.UINTN (0x00)
  Status    = EfiPy.gRT.GetVariable (
                          EFI_BOOT_ORDER_VARIABLE_NAME,
                          EfiPy.byref (gEfiGlobalVariableGuid),
                          None,
                          EfiPy.byref (DataSize),
                          None
                          )
  if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
    return 0

  Attributes  = EfiPy.UINT32(0x00)
  DataBuffer  =(EfiPy.CHAR8 * DataSize.value)("\00")
  Status      = EfiPy.gRT.GetVariable (
                            EFI_BOOT_ORDER_VARIABLE_NAME,
                            EfiPy.byref (gEfiGlobalVariableGuid),
                            EfiPy.byref (Attributes),
                            EfiPy.byref (DataSize),
                            EfiPy.byref (DataBuffer)
                            )

  if Status != EfiPy.EFI_SUCCESS:
    return 0

  import struct

  BootOrder = struct.unpack ("H" * (DataSize.value / 2), DataBuffer)

  BootOrder = [u"Boot" + ("%04X" % s) for s in BootOrder]
  BootOrder.append (EFI_BOOT_NEXT_VARIABLE_NAME)

  print str(BootOrder)

  print "Boot### content"

  for LoadOptionName in BootOrder:

    DataSize  = EfiPy.UINTN (0x00)
    Status    = EfiPy.gRT.GetVariable (
                            LoadOptionName,
                            EfiPy.byref (gEfiGlobalVariableGuid),
                            None,
                            EfiPy.byref (DataSize),
                            None
                            )
    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      continue

    Attributes  = EfiPy.UINT32(0x00)
    DataBuffer  =(EfiPy.CHAR8 * DataSize.value)("\00")
    Status      = EfiPy.gRT.GetVariable (
                              LoadOptionName,
                              EfiPy.byref (gEfiGlobalVariableGuid),
                              EfiPy.byref (Attributes),
                              EfiPy.byref (DataSize),
                              EfiPy.byref (DataBuffer)
                              )

    if RETURN_ERROR (Status):
      print LoadOptionName + " does not exit!"
      continue

    DmpVariable (LoadOptionName, gEfiGlobalVariableGuid)

    (LoAttributes, LoFlen) = struct.unpack_from ('IH', DataBuffer, 0)
    DescriptionEnd  = len(DataBuffer[6:].split('\x00\x00')[0]) + 9
    FilePathListEnd = DescriptionEnd + LoFlen - 2
    DescriptionVar  = DataBuffer[6: DescriptionEnd - 2].decode('utf_16')
    FilePathListVar = DataBuffer[DescriptionEnd:FilePathListEnd]
    print "Attributes: 0x%04X, FilePathListLength: 0x%02X " % (LoAttributes, LoFlen)
    print "Description: '%s'" % DescriptionVar

    DevicePath = EfiPy.cast (FilePathListVar, POINTER (EFI_DEVICE_PATH_PROTOCOL)).contents
    DevicePath.DisplayOnly    = True
    # DevicePath.DisplayOnly    = False
    DevicePath.AllowShortcuts = False

    print "DevicePath:\n  %s" % DevicePath

    print "OptionalData:"
    EfiPyHexDump (0, 0x0000, DataBuffer[FilePathListEnd:], True)

  return 0

if __name__ == '__main__':

  EfiPyDumpBoot ()
