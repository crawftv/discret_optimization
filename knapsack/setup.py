from setuptools import setup
from Cython.Build import cythonize

setup(
    name="dynamic solver", ext_modules=cythonize("dynamic.pyx"), zip_safe=False,
)
