# from distutils.core import setup
# import py2exe

# setup(console=['hello.py'])

from distutils.core import setup
import sys
import py2efi

sys.argv.append('py2efi')

options = {
    "dist_dir": "DistFolder", # OK
    # "excludes": ['ctypes'], # OK
    # "ignores": ['bbas'],    # Check again
    # "includes": ['abc'],    # OK
    # "packages": ['EfiPy'],  # OK
    # "ascii": 1,             # OK
    # "custom_boot_script": "boot_script.py", # OK
    #"unbuffered": 1          # OK

    # "optimize": 1,          # NG, whle value is 1 or 2
    # "compressed": 1,        # Ignore.
    # "bundle_files": 3,      # Ignore, it required zipextimporter, which is not included in Py2Efi
    #"skip_archive": 0,       # PASS, not verify
    # "xref": 0,              # PASS, Not used by Py2Efi
    # "dll_excludes": Non,    # PASS, Py2Efi does not use DLL.
    }

setup(
    options = {'py2efi': options},
    console=['hello.py'],
    # zipfile = None, # PASS
)