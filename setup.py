from setuptools import setup, find_packages

setup(
      name="ArchiverTool",
      author = "Ed Rial",
      version = "0.1",
      packages = find_packages(),
      dependency_links=['http://github.com/eddrial/aapy/tarball/master#egg=package-1.0'],
      install_requires = ['numpy'],
      )
#