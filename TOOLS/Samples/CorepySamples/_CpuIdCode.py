#
# _CpuIdCode.py
#
# Copyright (C) 2016-2017 efipy.core@gmail.com All rights reserved.
#
# _CpuIdCode.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# _CpuIdCode.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

CpuidCode    = None
CpuidProc    = None
CpuidParams  = None

def CpuidAsmInit ():

    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.platform as env
    import corepy.arch.x86_64.lib.memory as mem

    global CpuidCode
    global CpuidProc
    global CpuidParams
    CpuidCode   = env.InstructionStream()
    CpuidProc   = env.Processor()
    CpuidParams = env.ExecParams()

    CpuidCode.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 16)))  # parameter 1
    CpuidCode.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 24)))  # parameter 2
    CpuidCode.add(x86.mov(reg.rdi, mem.MemRef(reg.rbp, 32)))  # parameter 3

    CpuidCode.add(x86.push(reg.rax))                          # save input parameter

    CpuidCode.add(x86.cpuid())

    CpuidCode.add(x86.mov(mem.MemRef(reg.edi,  0, data_size = 32), reg.eax))
    CpuidCode.add(x86.mov(mem.MemRef(reg.edi,  4, data_size = 32), reg.ebx))
    CpuidCode.add(x86.mov(mem.MemRef(reg.edi,  8, data_size = 32), reg.ecx))
    CpuidCode.add(x86.mov(mem.MemRef(reg.edi, 12, data_size = 32), reg.edx))

    CpuidCode.add(x86.pop(reg.rax))                           # restore input parameter as return value


CpuidAsmInit ()
