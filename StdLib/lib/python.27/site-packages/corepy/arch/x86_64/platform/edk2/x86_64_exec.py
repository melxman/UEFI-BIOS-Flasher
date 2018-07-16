# /* Copyright (c) 2006-2008 The Trustees of Indiana University.
#  * All rights reserved.
#  * 
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  * 
#  * - Redistributions of source code must retain the above copyright notice, this
#  *   list of conditions and the following disclaimer.
#  * 
#  * - Redistributions in binary form must reproduce the above copyright notice,
#  *   this list of conditions and the following disclaimer in the documentation
#  *   and/or other materials provided with the distribution.
#  * 
#  * - Neither the Indiana University nor the names of its contributors may be
#  *   used to endorse or promote products derived from this software without
#  *   specific prior written permission.
#  * 
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  * POSSIBILITY OF SUCH DAMAGE.
#  */
# 
# // Native code for executing instruction streams on Linux.
# 
import EfiPy

class ExecParams (EfiPy.Structure):
  _pack_ = 1
  _fields_ = [
    ("p1", EfiPy.UINT64),
    ("p2", EfiPy.UINT64),
    ("p3", EfiPy.UINT64),
    ("p4", EfiPy.UINT64),
    ("p5", EfiPy.UINT64),
    ("p6", EfiPy.UINT64),
    ("p7", EfiPy.UINT64),
    ("p8", EfiPy.UINT64)
  ]

Stream_func_int = EfiPy.CFUNCTYPE (
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64
  )

Stream_func_fp = EfiPy.CFUNCTYPE (
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64
  )


def make_executable (addr, size):
  return 0

def execute_int (addr, params):

  func = Stream_func_int(addr)
  
  # return func (params)
  return func (params.p1, params.p2, params.p3, params.p4, params.p5, params.p6, params.p7, params.p8)

def execute_fp (addr, params):

  func = Stream_func_fp(addr)

  return func (params.p1, params.p2, params.p3, params.p4, params.p5, params.p6, params.p7, params.p8)
