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

options = {
    "ascii": 0,
    }

EfiPyShell = Target(
    description     = "Shell program",
    script          = "EfiPyShell.py",
    # other_resources = [(RT_MANIFEST, 1, manifest_template % dict(prog="test_wx"))],
    dest_base       = "EfiPyShell"
  )

PanelTest = Target(
    description = "Panel Test program",
    script = "PanelTest.py",
    # other_resources = [(RT_MANIFEST, 1, manifest_template % dict(prog="test_wx"))],
    dest_base = "PanelTest"
  )

PaTest = Target(
    description = "Protocol analyzer",
    script = "PaTest.py",
    # other_resources = [(RT_MANIFEST, 1, manifest_template % dict(prog="test_wx"))],
    dest_base = "PaTest"
  )

setup(
    options = {'py2efi': options},
    console=[EfiPyShell, PanelTest, PaTest],
    # zipfile = None,
)