# from distutils.core import setup
# import py2exe

# setup(console=['hello.py'])

from distutils.core import setup
import sys
import py2efi

sys.argv.append('py2efi')

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)

        # for the versioninfo resources
        self.company_name     = "No Company"
        self.copyright        = "no copyright"
        self.product_version  = "0.1.0(ABCD)"
        self.comments = "comments..."
        self.trademarks = "trademarks..."
        self.name             = "py2efi sample Product"

VerTest = Target(
    script          = "VersionDump.py",
    dest_base       = "vTest",
    version         = "0.5.0(TAG)",
    description     = "A sample Python EFI app (vTest)",
  )

uTest = Target(
    script          = "VersionDump.py",
    dest_base       = "uTest",
    version         = "0.6.0",
    description     = "A sample Python EFI app (uTest)",
  )

setup(
    options = {'py2efi': {'bundle_files': 3}},
    console=[VerTest, uTest],
    zipfile = "Foundation.zip",
)