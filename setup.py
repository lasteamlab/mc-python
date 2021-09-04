from setuptools import setup, find_packages

__project__ = 'mcpython'
__desc__ = 'A library for interfacing with the Minecraft mcpythonmod mod'
__version__ = '0.1'
__author__ = "Lisabeth Lueninghoener"
__author_email__ = 'lasteamlab.com'
__license__ = 'MIT'
__url__ = 'https://github.com/los-alamos-steam-lab/mcpython'
#__requires__ = ['py3minepi',]

__classifiers__ = [
#    "Development Status :: 3 - Alpha",
#    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "Topic :: Education",
    "Topic :: Games/Entertainment",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
]

setup(name='mcpython',
      version = __version__,
      description = __desc__,
      url = __url__,
      author = __author__,
      author_email = __author_email__,
      license= __license__,
      packages = find_packages(),
#      install_requires = __requires__,
      zip_safe=False)
