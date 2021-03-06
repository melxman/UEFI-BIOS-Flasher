#
# CpuId.py
#
# Copyright (C) 2017 efipy.core@gmail.com All rights reserved.
#
# CpuId.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CpuId.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy import Structure, Union, UINT32, addressof
import EfiPy.UefiCpuPkg.Register.Cpuid as CpuIdReg
from rUnionOp import COMMON_REG_32BITS_OUTPUT, COMMON_REG_32BITS, rUnionOp
from _CpuIdCode import CpuidCode, CpuidProc, CpuidParams

#
# Register for each CPUID function
#

# CPUID(0)
# EFIPY_CPUID_SIGNATURE_Regs = COMMON_REG_32BITS_OUTPUT
class EFIPY_CPUID_SIGNATURE_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_SIGNATURE_EAX),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(1)
class EFIPY_CPUID_VERSION_INFO_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_VERSION_INFO_EAX),
    ('EBX',  CpuIdReg.CPUID_VERSION_INFO_EBX),
    ('ECX',  CpuIdReg.CPUID_VERSION_INFO_ECX),
    ('EDX',  CpuIdReg.CPUID_VERSION_INFO_EDX)
  ]

# CPUID(2)
class EFIPY_CPUID_CACHE_INFO_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_CACHE_INFO_CACHE_TLB),
    ('EBX',  CpuIdReg.CPUID_CACHE_INFO_CACHE_TLB),
    ('ECX',  CpuIdReg.CPUID_CACHE_INFO_CACHE_TLB),
    ('EDX',  CpuIdReg.CPUID_CACHE_INFO_CACHE_TLB)
  ]

# CPUID(3)
# EFIPY_CPUID_SERIAL_NUMBER_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(4)
class EFIPY_CPUID_CACHE_PARAMS_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_CACHE_PARAMS_EAX),
    ('EBX',  CpuIdReg.CPUID_CACHE_PARAMS_EBX),
    ('ECX',  CpuIdReg.CPUID_CACHE_PARAMS_ECX),
    ('EDX',  CpuIdReg.CPUID_CACHE_PARAMS_EDX)
  ]

# CPUID(5)
class EFIPY_CPUID_MONITOR_MWAIT_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_MONITOR_MWAIT_EAX),
    ('EBX',  CpuIdReg.CPUID_MONITOR_MWAIT_EBX),
    ('ECX',  CpuIdReg.CPUID_MONITOR_MWAIT_ECX),
    ('EDX',  CpuIdReg.CPUID_MONITOR_MWAIT_EDX)
  ]

# CPUID(6)
class EFIPY_CPUID_THERMAL_POWER_MANAGEMENT_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_THERMAL_POWER_MANAGEMENT_EAX),
    ('EBX',  CpuIdReg.CPUID_THERMAL_POWER_MANAGEMENT_EBX),
    ('ECX',  CpuIdReg.CPUID_THERMAL_POWER_MANAGEMENT_ECX),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(7)
class EFIPY_CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  CpuIdReg.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EBX),
    ('ECX',  CpuIdReg.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_ECX),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(9)
# EFIPY_CPUID_DIRECT_CACHE_ACCESS_INFO_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x0A)
class EFIPY_CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EAX),
    ('EBX',  CpuIdReg.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EBX),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  CpuIdReg.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EDX)
  ]

# CPUID(0x0B)
class EFIPY_CPUID_EXTENDED_TOPOLOGY_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_EXTENDED_TOPOLOGY_EAX),
    ('EBX',  CpuIdReg.CPUID_EXTENDED_TOPOLOGY_EBX),
    ('ECX',  CpuIdReg.CPUID_EXTENDED_TOPOLOGY_ECX),
    ('EDX',  CpuIdReg.CPUID_EXTENDED_TOPOLOGY_EDX)
  ]

# CPUID(0x0D, 0x00)
class EFIPY_CPUID_EXTENDED_STATE_MAIN_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_EXTENDED_STATE_MAIN_LEAF_EAX),
    ('EBX',  CpuIdReg.CPUID_EXTENDED_STATE_MAIN_LEAF_EBX),
    ('ECX',  CpuIdReg.CPUID_EXTENDED_STATE_MAIN_LEAF_ECX),
    ('EDX',  CpuIdReg.CPUID_EXTENDED_STATE_MAIN_LEAF_EDX)
  ]

# CPUID(0x0D, 0x01)
class EFIPY_CPUID_EXTENDED_STATE_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_EXTENDED_STATE_SUB_LEAF_EAX),
    ('EBX',  CpuIdReg.CPUID_EXTENDED_STATE_SUB_LEAF_EBX),
    ('ECX',  CpuIdReg.CPUID_EXTENDED_STATE_SUB_LEAF_ECX),
    ('EDX',  CpuIdReg.CPUID_EXTENDED_STATE_SUB_LEAF_EDX)
  ]

# CPUID(0x0D, 0x02)
class EFIPY_CPUID_EXTENDED_STATE_SIZE_OFFSET_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_EXTENDED_STATE_SIZE_OFFSET_EAX),
    ('EBX',  CpuIdReg.CPUID_EXTENDED_STATE_SIZE_OFFSET_EBX),
    ('ECX',  CpuIdReg.CPUID_EXTENDED_STATE_SIZE_OFFSET_ECX),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x0F, 0x00)
class EFIPY_CPUID_PLATFORM_QOS_MONITORING_ENUMERATION_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  CpuIdReg.CPUID_PLATFORM_QOS_MONITORING_ENUMERATION_SUB_LEAF_EBX),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  CpuIdReg.CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF_EDX)
  ]

# CPUID(0x0F, 0x01)
class EFIPY_CPUID_PLATFORM_QOS_MONITORING_CAPABILITY_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  CpuIdReg.CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_EBX),
    ('ECX',  CpuIdReg.CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_ECX),
    ('EDX',  CpuIdReg.CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_EDX)
  ]

# CPUID(0x10, 0x00)
class EFIPY_CPUID_PLATFORM_QOS_ENFORCEMENT_MAIN_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  CpuIdReg.CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF_EBX),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x10, 0x01)
class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EAX),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  CpuIdReg.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_ECX),
    ('EDX',  CpuIdReg.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EDX)
  ]

# CPUID(0x12, 0x00)
class EFIPY_CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EAX),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  CpuIdReg.CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EDX)
  ]

# CPUID(0x12, 0x01)
# EFIPY_CPUID_INTEL_SGX_CAPABILITIES_1_SUB_LEAF_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x12, 0x02)
class EFIPY_CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EAX),
    ('EBX',  CpuIdReg.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EBX),
    ('ECX',  CpuIdReg.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_ECX),
    ('EDX',  CpuIdReg.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EDX)
  ]

# CPUID(0x14, 0x00)
class EFIPY_CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_EAX),
    ('EBX',  CpuIdReg.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_EBX),
    ('ECX',  CpuIdReg.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_ECX),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x14, 0x01)
class EFIPY_CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EAX),
    ('EBX',  CpuIdReg.CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EBX),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x15, 0x00)
# EFIPY_CPUID_TIME_STAMP_COUNTER_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x16, 0x00)
class EFIPY_CPUID_PROCESSOR_FREQUENCY_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_PROCESSOR_FREQUENCY_EAX),
    ('EBX',  CpuIdReg.CPUID_PROCESSOR_FREQUENCY_EBX),
    ('ECX',  CpuIdReg.CPUID_PROCESSOR_FREQUENCY_ECX),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x17, 0x00)
class EFIPY_CPUID_SOC_VENDOR_MAIN_LEAF_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_SOC_VENDOR_MAIN_LEAF_EAX),
    ('EBX',  CpuIdReg.CPUID_SOC_VENDOR_MAIN_LEAF_EBX),
    ('ECX',  CpuIdReg.CPUID_SOC_VENDOR_MAIN_LEAF_ECX),
    ('EDX',  CpuIdReg.CPUID_SOC_VENDOR_MAIN_LEAF_EDX)
  ]

# CPUID(0x17, 0x01)
# EFIPY_CPUID_SOC_VENDOR_BRAND_STRING1_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x17, 0x02)
# EFIPY_CPUID_SOC_VENDOR_BRAND_STRING2_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x17, 0x03)
# EFIPY_CPUID_SOC_VENDOR_BRAND_STRING3_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x80000000, 0x00)
class EFIPY_CPUID_EXTENDED_FUNCTION_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_EXTENDED_FUNCTION_EAX),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x80000001, 0x00)
class EFIPY_CPUID_EXTENDED_CPU_SIG_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  CpuIdReg.CPUID_EXTENDED_CPU_SIG_ECX),
    ('EDX',  CpuIdReg.CPUID_EXTENDED_CPU_SIG_EDX)
  ]

# CPUID(0x80000002, 0x00)
# EFIPY_CPUID_BRAND_STRING1_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x80000003, 0x00)
# EFIPY_CPUID_BRAND_STRING2_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x80000004, 0x00)
# EFIPY_CPUID_BRAND_STRING3_Regs = COMMON_REG_32BITS_OUTPUT

# CPUID(0x80000006, 0x00)
class EFIPY_CPUID_EXTENDED_CACHE_INFO_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  CpuIdReg.CPUID_EXTENDED_CACHE_INFO_ECX),
    ('EDX',  COMMON_REG_32BITS)
  ]

# CPUID(0x80000007, 0x00)
class EFIPY_CPUID_EXTENDED_TIME_STAMP_COUNTER_Regs (Structure):
  _fields_ = [
    ('EAX',  COMMON_REG_32BITS),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  CpuIdReg.CPUID_EXTENDED_TIME_STAMP_COUNTER_EDX)
  ]

# CPUID(0x80000008, 0x00)
class EFIPY_CPUID_VIR_PHY_ADDRESS_SIZE_Regs (Structure):
  _fields_ = [
    ('EAX',  CpuIdReg.CPUID_VIR_PHY_ADDRESS_SIZE_EAX),
    ('EBX',  COMMON_REG_32BITS),
    ('ECX',  COMMON_REG_32BITS),
    ('EDX',  COMMON_REG_32BITS)
  ]

#
# CPUID index
#
CpuIdIndex = {
         (0x00, 0x00): EFIPY_CPUID_SIGNATURE_Regs,
         (0x01, 0x00): EFIPY_CPUID_VERSION_INFO_Regs,
         (0x02, 0x00): EFIPY_CPUID_CACHE_INFO_Regs,
         # (0x03, 0x00): EFIPY_CPUID_SERIAL_NUMBER_Regs,
         (0x04, 0x00): EFIPY_CPUID_CACHE_PARAMS_Regs,
         (0x05, 0x00): EFIPY_CPUID_MONITOR_MWAIT_Regs,
         (0x06, 0x00): EFIPY_CPUID_THERMAL_POWER_MANAGEMENT_Regs,
         (0x07, 0x00): EFIPY_CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_Regs,
         # (0x09, 0x00): EFIPY_CPUID_DIRECT_CACHE_ACCESS_INFO_Regs,
         (0x0A, 0x00): EFIPY_CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_Regs,
         (0x0B, 0x00): EFIPY_CPUID_EXTENDED_TOPOLOGY_Regs,
         (0x0D, 0x00): EFIPY_CPUID_EXTENDED_STATE_MAIN_LEAF_Regs,
         (0x0D, 0x01): EFIPY_CPUID_EXTENDED_STATE_SUB_LEAF_Regs,
         (0x0D, 0x02): EFIPY_CPUID_EXTENDED_STATE_SIZE_OFFSET_Regs,
         (0x0F, 0x00): EFIPY_CPUID_PLATFORM_QOS_MONITORING_ENUMERATION_SUB_LEAF_Regs,
         (0x0F, 0x01): EFIPY_CPUID_PLATFORM_QOS_MONITORING_CAPABILITY_SUB_LEAF_Regs,
         (0x10, 0x00): EFIPY_CPUID_PLATFORM_QOS_ENFORCEMENT_MAIN_LEAF_Regs,
         (0x10, 0x01): CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_Regs,
         (0x12, 0x00): EFIPY_CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_Regs,
         # (0x12, 0x01): EFIPY_CPUID_INTEL_SGX_CAPABILITIES_1_SUB_LEAF_Regs,
         (0x12, 0x02): EFIPY_CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_Regs,
         (0x14, 0x00): EFIPY_CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_Regs,
         (0x14, 0x01): EFIPY_CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_Regs,
         # (0x15, 0x00): EFIPY_CPUID_TIME_STAMP_COUNTER_Regs,
         (0x16, 0x00): EFIPY_CPUID_PROCESSOR_FREQUENCY_Regs,
         (0x17, 0x00): EFIPY_CPUID_SOC_VENDOR_MAIN_LEAF_Regs,
         # (0x17, 0x01): EFIPY_CPUID_SOC_VENDOR_BRAND_STRING1_Regs,
         # (0x17, 0x02): EFIPY_CPUID_SOC_VENDOR_BRAND_STRING2_Regs,
         # (0x17, 0x03): EFIPY_CPUID_SOC_VENDOR_BRAND_STRING3_Regs,
   (0x80000000, 0x00): EFIPY_CPUID_EXTENDED_FUNCTION_Regs,
   (0x80000001, 0x00): EFIPY_CPUID_EXTENDED_CPU_SIG_Regs,
   # (0x80000002, 0x00): EFIPY_CPUID_BRAND_STRING1_Regs,
   # (0x80000003, 0x00): EFIPY_CPUID_BRAND_STRING2_Regs,
   # (0x80000004, 0x00): EFIPY_CPUID_BRAND_STRING3_Regs,
   (0x80000006, 0x00): EFIPY_CPUID_EXTENDED_CACHE_INFO_Regs,
   (0x80000007, 0x00): EFIPY_CPUID_EXTENDED_TIME_STAMP_COUNTER_Regs,
   (0x80000008, 0x00): EFIPY_CPUID_VIR_PHY_ADDRESS_SIZE_Regs,
        }

CpuIdObjCache = {}

class rCpuId (object):

  def __init__ (self, Eax, Ecx = 0x00):

    self.__para__ = (Eax, Ecx)

  def __str__ (self):
    return "cpuid(0x%X, 0x%X)" % (self.__para__[0], self.__para__[1]) + '''
''' + str (self.EAX) + '''
''' + str (self.EBX) + '''
''' + str (self.ECX) + '''
''' + str (self.EDX)

class sCpuId (rUnionOp):
  def MemGet (self, Key):
    CellType = getattr (self.KeyObj, self.CellType)
    return CellType

  def MemSet (self, Key, Value):
    self.KeyObj.__setattr__ (self.CellType, Value)

def CPUID (Eax, Ecx = 0):

  global CpuIdObjCache

  try:
    return CpuIdObjCache[(Eax, Ecx)]
  except:
    pass

  _reg = COMMON_REG_32BITS_OUTPUT()
  _CpuR = addressof (_reg)

  CpuidParams.p1 = Eax
  CpuidParams.p2 = Ecx
  CpuidParams.p3 = _CpuR
  CpuidProc.execute(CpuidCode, params = CpuidParams, mode = 'int')

  CpuIdObj = rCpuId (Eax, Ecx)
  CpuIdObjCache [(Eax, Ecx)] = CpuIdObj

  RegStruct = CpuIdIndex.get ((Eax, Ecx), COMMON_REG_32BITS_OUTPUT)

  CpuIdObj.EAX = sCpuId('EAX', 0, 0, 32, 32,
                   CellUnion  = RegStruct._fields_[0][1],
                   CellType   = 'Uint32',
                   CellBits   = 'Bits',
                   Value      = _reg.EAX.Uint32)

  CpuIdObj.EBX = sCpuId('EBX', 0, 0, 32, 32,
                   CellUnion  = RegStruct._fields_[1][1],
                   CellType   = 'Uint32',
                   CellBits   = 'Bits',
                   Value      = _reg.EBX.Uint32)

  CpuIdObj.ECX = sCpuId('ECX', 0, 0, 32, 32,
                   CellUnion  = RegStruct._fields_[2][1],
                   CellType   = 'Uint32',
                   CellBits   = 'Bits',
                   Value      = _reg.ECX.Uint32)

  CpuIdObj.EDX = sCpuId('EDX', 0, 0, 32, 32,
                   CellUnion  = RegStruct._fields_[3][1],
                   CellType   = 'Uint32',
                   CellBits   = 'Bits',
                   Value      = _reg.EDX.Uint32)

  return CpuIdObj
