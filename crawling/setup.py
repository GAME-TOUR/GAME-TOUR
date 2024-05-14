from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
  name='my_package',
  version='0.1',
  packages=find_packages(where='src'),
  package_dir={":src"},
)