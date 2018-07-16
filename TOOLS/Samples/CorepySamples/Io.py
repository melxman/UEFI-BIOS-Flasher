#
# Io.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# Io.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# Io.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy import *
import corepy.arch.x86_64.platform as env

IoProc          = env.Processor()
IoParams        = env.ExecParams()
IoCodeSet8      = None
IoCodeSet16     = None
IoCodeSet32     = None
IoCodeGet8      = None
IoCodeGet16     = None
IoCodeGet32     = None

def IoAsm ():

    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.lib.memory as mem

    # IoCodeSet8 (dx, al), IoCodeSet8 (port, value)
    global IoCodeSet8
    IoCodeSet8   = env.InstructionStream()
    IoCodeSet8.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx
    IoCodeSet8.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 24)))  # parameter 2, rax
    IoCodeSet8.add(x86.push(reg.rax))
    IoCodeSet8.add(x86.out(reg.dx, reg.al))
    IoCodeSet8.add(x86.pop(reg.rax))

    # IoCodeSet16 (dx, ax), IoCodeSet16 (port, value)
    global IoCodeSet16
    IoCodeSet16   = env.InstructionStream()
    IoCodeSet16.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx
    IoCodeSet16.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 24)))  # parameter 2, rax
    IoCodeSet16.add(x86.push(reg.rax))
    IoCodeSet16.add(x86.out(reg.dx, reg.ax))
    IoCodeSet16.add(x86.pop(reg.rax))

    # IoCodeSet32 (dx, eax), IoCodeSet16 (port, value)
    global IoCodeSet32
    IoCodeSet32   = env.InstructionStream()
    IoCodeSet32.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx
    IoCodeSet32.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 24)))  # parameter 2, rax
    IoCodeSet32.add(x86.push(reg.rax))
    IoCodeSet32.add(x86.out(reg.dx, reg.eax))
    IoCodeSet32.add(x86.pop(reg.rax))

    # IoCodeGet8 (dx), ret = IoCodeGet8 (port)
    global IoCodeGet8
    IoCodeGet8   = env.InstructionStream()
    IoCodeGet8.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx
    IoCodeGet8.add(x86.in_(reg.al, reg.dx))

    # IoCodeGet16 (dx), ret = IoCodeGet8 (port)
    global IoCodeGet16
    IoCodeGet16   = env.InstructionStream()
    IoCodeGet16.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx
    IoCodeGet16.add(x86.in_(reg.ax, reg.dx))

    # IoCodeGet32 (dx), ret = IoCodeGet8 (port)
    global IoCodeGet32
    IoCodeGet32   = env.InstructionStream()
    IoCodeGet32.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx
    IoCodeGet32.add(x86.in_(reg.eax, reg.dx))

IoAsm ()

from BitOp import _MemCell, _MemArray

class _IoBit (_MemCell):

  def __str__ (self):
    tBitForm = "%%0%dX" % (self.Width >> 2)
    tOutForm = "%s[0x" + tBitForm + "] = 0x" + tBitForm
    # output sample: "%s[0x%02X] = 0x%02X" % (self.Index, int (self))
    return tOutForm % (
             self.__name__,
             self.Index,
             int (self)
             )

class _IoBit32 (_IoBit):

  def MemGet (self, port):
    IoParams.p1 = port
    ret = IoProc.execute(IoCodeGet32, params = IoParams, mode = 'int')
    return ret & 0xFFFFFFFF

  def MemSet (self, port, val):
    IoParams.p1 = port
    IoParams.p2 = val & 0xFFFFFFFF
    IoProc.execute(IoCodeSet32, params = IoParams, mode = 'int')

class _IoBit16 (_IoBit):

  def MemGet (self, port):
    IoParams.p1 = port
    ret = IoProc.execute(IoCodeGet16, params = IoParams, mode = 'int')
    return ret & 0xFFFF

  def MemSet (self, port, val):
    IoParams.p1 = port
    IoParams.p2 = val & 0xFFFF
    IoProc.execute(IoCodeSet16, params = IoParams, mode = 'int')

class _IoBit8 (_IoBit):

  def MemGet (self, port):
    IoParams.p1 = port
    ret = IoProc.execute(IoCodeGet8, params = IoParams, mode = 'int')
    return ret & 0xFF

  def MemSet (self, port, val):
    IoParams.p1 = port
    IoParams.p2 = val & 0xFF
    IoProc.execute(IoCodeSet8, params = IoParams, mode = 'int')

Io8   = _MemArray ("Io8",   8, CellClass = _IoBit8)
Io16  = _MemArray ("Io16", 16, CellClass = _IoBit16)
Io32  = _MemArray ("Io32", 32, CellClass = _IoBit32)
