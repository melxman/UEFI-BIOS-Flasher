from distutils.core import setup
import sys
import py2efi

sys.argv.append('py2efi')

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "0.5.0"
        self.company_name = "No Company"
        self.copyright = "no copyright"
        self.name = "py2efi sample files"

gMornig = Target(
    description     = "A sample Python EFI app",
    script          = "gMornig.py",
    # other_resources = [(RT_MANIFEST, 1, manifest_template % dict(prog="test_wx"))],
    dest_base       = "goodmorning"
  )

hello = Target(
    description = "A sample Python EFI app with console",
    script = "hello.py",
    # other_resources = [(RT_MANIFEST, 1, manifest_template % dict(prog="test_wx"))],
    dest_base = "hello1"
  )

setup(
    options = {'py2efi': {'bundle_files': 3}},
    console=[gMornig, hello],
    zipfile = None,
)