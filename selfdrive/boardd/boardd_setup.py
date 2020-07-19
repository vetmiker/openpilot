import subprocess
from distutils.core import Extension, setup

from Cython.Build import cythonize

from common.cython_hacks import BuildExtWithoutPlatformSuffix
from common.basedir import BASEDIR
import os

PHONELIBS = os.path.join(BASEDIR, 'phonelibs')

ARCH = subprocess.check_output(["uname", "-m"], encoding='utf8').rstrip()
<<<<<<< HEAD

if ARCH == "x86_64":
  if platform.system() == "Darwin":
    libraries = ['can_list_to_can_capnp', 'capnp', 'kj']
    ARCH_DIR = 'mac'
  else:
    libraries = [':libcan_list_to_can_capnp.a', ':libcapnp.a', ':libkj.a']
    ARCH_DIR = 'x64'
else:
  libraries = [':libcan_list_to_can_capnp.a', 'capnp', 'kj']
  if os.path.isdir("/system"):
    ARCH_DIR = 'aarch64'
  else:
    ARCH_DIR = 'larch64'
=======
libraries = ['can_list_to_can_capnp', 'capnp', 'kj']
>>>>>>> b205dd6954ad6d795fc04d66e0150675b4fae28d

setup(name='Boardd API Implementation',
      cmdclass={'build_ext': BuildExtWithoutPlatformSuffix},
      ext_modules=cythonize(
        Extension(
          "boardd_api_impl",
          libraries=libraries,
          library_dirs=[
            './',
          ],
          sources=['boardd_api_impl.pyx'],
          language="c++",
          extra_compile_args=["-std=c++11"],
        )
      )
)
