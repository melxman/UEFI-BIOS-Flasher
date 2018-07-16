#!/usr/bin/python

#
# EfiPyCmdDmpStore.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# EfiPyCmdDmpStore.py is free software: you can redistribute it and/or modify
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

from Utility.EfiPyUtility     import EfiPyHexDump

#
# EfiPy Command dump variable class
#

class EFIPY_CMD_DMP_STORE (EfiPyCmdBase.EFIPY_CMD_BASE):
  '''[INIT] Manages all UEFI NVRAM variables.'''

  name    = u"dmpstore"

  def _DmpVariable (self, name, guid):

    DataSize  = EfiPy.UINTN (0x00)
    Status    = EfiPy.gRT.GetVariable (
                            name,
                            EfiPy.byref (guid),
                            None,
                            EfiPy.byref (DataSize),
                            None
                            )

    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      return

    Attributes  = EfiPy.UINT32(0x00)
    DataBuffer  =(EfiPy.CHAR8 * DataSize.value)("\00")
    Status      = EfiPy.gRT.GetVariable (
                              name,
                              EfiPy.byref (guid),
                              EfiPy.byref (Attributes),
                              EfiPy.byref (DataSize),
                              EfiPy.byref (DataBuffer)
                              )

    if not EfiPy.RETURN_ERROR (Status):

      StrVarAttr     = ""
      if (Attributes.value & EfiPy.EFI_VARIABLE_NON_VOLATILE) > 0:
        StrVarAttr = "NV"
      if (Attributes.value & EfiPy.EFI_VARIABLE_RUNTIME_ACCESS) > 0:
        if len(StrVarAttr) > 0:
          StrVarAttr = StrVarAttr + "+"
        StrVarAttr = StrVarAttr + "RS"
      if (Attributes.value & EfiPy.EFI_VARIABLE_BOOTSERVICE_ACCESS) > 0:
        if len(StrVarAttr) > 0:
          StrVarAttr = StrVarAttr + "+"
        StrVarAttr = StrVarAttr + "BS"

      self.StdOut.printf("Variable - %s - '%s:%s' - DataSize = 0x%X\r\n" % (StrVarAttr, guid, name, DataSize.value))
      EfiPyHexDump (self.StdOut, 2, 0x0000, DataBuffer, True)

    else:
      self.StdOut.printf("Get Variable %s %s error\r\n" % (name, guid))

  #
  # Dump EFI variable working function
  #
  def Run (self):

    import copy

    VariableList  = []

    VariableName  = u"\x00" * 100
    VariableSize  = EfiPy.UINTN (EfiPy.sizeof (EfiPy.CHAR16) * 100)
    VariableTsize = EfiPy.UINTN (EfiPy.sizeof (EfiPy.CHAR16) * 100)
    VariableGuid  = EfiPy.EFI_GUID()

    while True:

      Status = EfiPy.gRT.GetNextVariableName(
                           EfiPy.byref (VariableTsize),
                           EfiPy.PCHAR16 (VariableName),
                           EfiPy.byref (VariableGuid)
                           )

      if Status == EfiPy.EFI_BUFFER_TOO_SMALL:

        VariableName  = VariableName + u"\x00" * 100
        VariableSize.value += EfiPy.sizeof (EfiPy.CHAR16) * 100
        VariableTsize.value = VariableSize.value
        continue

      if Status == EfiPy.EFI_SUCCESS:

        VariableList.append([VariableName[:VariableName.index (u"\x00")], copy.copy(VariableGuid)])
        VariableTsize.value = VariableSize.value
        continue

      break

    for Var in VariableList:

      self._DmpVariable (Var[0], Var[1])

    return 0

if __name__ == '__main__':

  Para    = EFIPY_CMD_MEM.name + ""
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

  EfiPyCmdObj = EFIPY_CMD_DMP_STORE(CmdSet)
  EfiPyCmdObj.ParaPreBuild (Args)
  args = EfiPyCmdObj.ParaBuild (Args)

  ret = EfiPyCmdObj.Run()

  import sys
  sys.exit(ret)
