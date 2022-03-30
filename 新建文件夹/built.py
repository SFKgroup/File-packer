from distutils.core import setup
from Cython.Build import cythonize
setup(name = 'any words.....',ext_modules = cythonize(["mylib.py",]),)