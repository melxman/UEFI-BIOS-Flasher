#
# _MsrCode.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# _MsrCode.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# _MsrCode.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy import *
import corepy.arch.x86_64.platform as env

Msrproc          = env.Processor()
MsrParams        = env.ExecParams()

WrMsrAsm = None
RdMsrAsm = None

def MsrAsmInit ():

  import corepy.arch.x86_64.isa as x86
  import corepy.arch.x86_64.types.registers as reg
  import corepy.arch.x86_64.lib.memory as mem

  # WrMsrAsm (EDX, EAX, ECX)
  # MSR[ECX] = EDX:EAX;
  global WrMsrAsm
  WrMsrAsm   = env.InstructionStream()
  WrMsrAsm.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx, IN
  WrMsrAsm.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 24)))  # parameter 2, rax, IN
  WrMsrAsm.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 32)))  # parameter 3, rcx, IN
  WrMsrAsm.add(x86.push(reg.rcx))
  WrMsrAsm.add(x86.wrmsr())
  WrMsrAsm.add(x86.pop(reg.rax))

  # RdMsrAsm (EDX, EAX, ECX)
  # EDX:EAX = MSR[ECX];
  global RdMsrAsm
  RdMsrAsm   = env.InstructionStream()
  RdMsrAsm.add(x86.mov(reg.rdi, mem.MemRef(reg.rbp, 16)))  # parameter 1, rdx, OUT
  RdMsrAsm.add(x86.mov(reg.rsi, mem.MemRef(reg.rbp, 24)))  # parameter 2, rax, OUT
  RdMsrAsm.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 32)))  # parameter 3, rcx, IN
  WrMsrAsm.add(x86.push(reg.rcx))
  RdMsrAsm.add(x86.rdmsr())
  RdMsrAsm.add(x86.mov(mem.MemRef(reg.rdi), reg.rdx))  # parameter 1, rdx, OUT
  RdMsrAsm.add(x86.mov(mem.MemRef(reg.rsi), reg.rax))  # parameter 2, rax, OUT
  WrMsrAsm.add(x86.pop(reg.rax))

# def WrMsr (edx, eax, ecx):
def WrMsrFunc (self, ecx, value):
  # MSR[ECX] = EDX:EAX;
  edx = (value >> 32) & 0xFFFFFFFF
  eax =  value        & 0xFFFFFFFF
  MsrParams.p1 = edx # EDX
  MsrParams.p2 = eax # EAX
  MsrParams.p3 = ecx
  Msrproc.execute(WrMsrAsm, params = MsrParams, mode = 'int')
  self.KeyObj.__setattr__ (self.CellType, value)

def RdMsrFunc (self, ecx):
  # EDX:EAX = MSR[ECX];
  edx = UINT32 (0)
  eax = UINT32 (0)
  MsrParams.p1 = addressof (edx)    # EDX
  MsrParams.p2 = addressof (eax)    # EAX
  MsrParams.p3 = ecx                # ECX
  Msrproc.execute(RdMsrAsm, params = MsrParams, mode = 'int')
  ret = (edx.value << 32) + eax.value
  self.KeyObj.__setattr__ (self.CellType, ret)
  return ret

MsrAsmInit ()
