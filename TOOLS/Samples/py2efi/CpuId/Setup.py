# from distutils.core import setup
# import py2exe

# setup(console=['hello.py'])

from distutils.core import setup
import sys
import py2efi

sys.argv.append('py2efi')

options = {
    "packages": ['corepy'],
    "ascii": 1,
    }

setup(
    options = {'py2efi': options},
    console=['CpuIds.py'],
    zipfile = None,
)