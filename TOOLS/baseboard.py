import sys
import EfiPy
import EfiPy.MdePkg.IndustryStandard.SmBios as Isb
from EfiPy.MdePkg.Protocol import Smbios as sb

Interface= EfiPy.PVOID()
Status = EfiPy.gBS.LocateProtocol()