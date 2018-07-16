import ctypes

a = ctypes.c_uint32

try:

  print "== Project Information =="
  print "ProductName:",       __ProductName__
  print "CompanyName:",       __CompanyName__
  print "ProductVersion:",    __ProductVersion__
  print "LegalCopyright:",    __LegalCopyright__
  print "LegalTrademarks:",   __LegalTrademarks__
  print "Comments:",          __Comments__
  print
  print "== File Information =="
  print "OriginalFilename:",  __OriginalFilename__
  print "FileDescription:",   __FileDescription__
  print "FileVersion:",       __FileVersion__

except:
  print "Error to read information"