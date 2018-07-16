# from distutils.core import setup
# import py2exe

# setup(console=['hello.py'])

from distutils.core import setup
import sys
import py2efi
# sys.argv.append('py2efi')
setup(
    options = {'py2efi': {'bundle_files': 3}},
    console=['hello.py'],
    zipfile = None,
)