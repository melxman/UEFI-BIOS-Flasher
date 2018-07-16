# print.py
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
# HelloWorld.py is free software: you can redistribute it and/or modify
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

import EfiPy
import os

# Required to retrieve BIOS Date and BIOS Version
os.system("smbiosview -t 0 > bios.txt")
bios_file = open('bios.txt', 'r')
bios_str = bios_file(

# Required to retrive Baseboard Product Name
os.system("smbiosview -t 2 > board.txt")

#f=open('out.txt', 'r')
#x=f.read().replace('\x00',"").split('\r\n')
#print(x)

#f=os.popen('smbiosview -t 2').read()

#f=proc.communicate()[0]
#x=f.replace('\x00',"").split('\r\n')
#for i in range(len(x)):
#    if "ProductName" in x[i]:
#        print(x[i])

print("Hi")

#input("Press any key to exit")

import sys
sys.exit()
