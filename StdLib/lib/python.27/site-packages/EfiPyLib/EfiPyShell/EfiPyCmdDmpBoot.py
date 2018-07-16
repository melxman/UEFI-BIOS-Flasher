#!/usr/bin/python

#
# EfiPyCmdDmpBoot.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdDmpBoot.py is free software: you can redistribute it and/or modify
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
import EfiPyCmdBase
import EfiPyCmdDmpStore

from   EfiPy.MdePkg.Guid.GlobalVariable       import *
from   EfiPy.MdePkg.Protocol.DevicePathEfiPy  import *

from   Utility.EfiPyUtility     import EfiPyHexDump

#
# EfiPy Command dump boot#### class
#

class EFIPY_CMD_DMP_BOOT (EfiPyCmdBase.EFIPY_CMD_BASE, EfiPyCmdDmpStore.EFIPY_CMD_DMP_STORE):
  '''[INIT] EfiPy Command utility Dump Boot#### variable'''

  name    = u"dmpboot"

  #
  # Dump boot#### working function
  #
  def Run (self):

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

    self.StdOut.printf(str(BootOrder) + "\r\n")

    self.StdOut.printf("Boot### content")

    for LoadOptionName in BootOrder:

      self.StdOut.printf("\r\n")

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
        self.StdOut.printf(LoadOptionName + u" does not exit!\r\n")
        continue

      self._DmpVariable (LoadOptionName, gEfiGlobalVariableGuid)

      (LoAttributes, LoFlen) = struct.unpack_from ('IH', DataBuffer, 0)
      DescriptionEnd  = len(DataBuffer[6:].split('\x00\x00')[0]) + 9
      FilePathListEnd = DescriptionEnd + LoFlen - 2
      DescriptionVar  = DataBuffer[6: DescriptionEnd - 2].decode('utf_16')
      FilePathListVar = DataBuffer[DescriptionEnd:FilePathListEnd]
      self.StdOut.printf(u"Attributes: 0x%04X, FilePathListLength: 0x%02X " % (LoAttributes, LoFlen))
      self.StdOut.printf(u"Description: \"%s\"\r\n" % DescriptionVar)

      DevicePath = EfiPy.cast (FilePathListVar, POINTER (EFI_DEVICE_PATH_PROTOCOL)).contents
      DevicePath.DisplayOnly    = True
      # DevicePath.DisplayOnly    = False
      DevicePath.AllowShortcuts = False

      self.StdOut.printf(u"DevicePath:\r\n  %s\r\n" % DevicePath)

      self.StdOut.printf(u"OptionalData:\r\n")
      EfiPyHexDump (self.StdOut, 2, 0x0000, DataBuffer[FilePathListEnd:], True)

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_DMP_BOOT.name + ""
  Args    = Para.split()

  class CMD_SET:
    def __init__ (self):

      import EfiPyShellIo
      import EfiPy

      self.StdIn  = EfiPyShellIo.SHELL_INPUT (EfiPy.gST.ConIn)
      self.StdOut = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.ConOut)
      self.StdErr = EfiPyShellIo.SHELL_OUTPUT(EfiPy.gST.StdErr)

      self.StdOut.ConOutModeDefault()

      self.CmdSet = {}

  CmdSet  = CMD_SET ()

  EfiPyCmdObj = EFIPY_CMD_DMP_BOOT(CmdSet)
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)

  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
