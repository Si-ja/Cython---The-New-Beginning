from setuptools import setup
from Cython.Build import cythonize

setup (
    name="Hello World app",
    ext_modules=cythonize("hello_c.pyx"),
    zip_safe=False
)