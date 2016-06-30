#!/usr/bin/env python
# encoding: utf-8
"""
Supported Platforms
-------------------

- OpenWrt

Import
------

.. code:: python

from pocketsphinx.pocketsphinx import *
"""

import sys
from glob import glob
try:
    from setuptools import setup, Extension
    from distutils.command.build import build
    from setuptools.command.install import install
except Extension as err:
    from distutils.core import setup
    from distutils.extension import Extension
    from distutils.command.build import build
    from distutils.command.install import install

PY2 = sys.version_info[0] == 2

sb_include_dirs = ['sphinxbase', 'sphinxbase/include']
ps_include_dirs = ['pocketsphinx/include']

sb_libraries = ['sphinxbase']
ps_libraries = ['sphinxbase', 'pocketsphinx']

sb_sources = ['sphinxbase/swig/sphinxbase.i']
ps_sources = ['pocketsphinx/swig/pocketsphinx.i']

swig_opts = ['-modern']

sb_swig_opts = (
    swig_opts +
    ['-I' + h for h in sb_include_dirs] +
    ['-outdir', 'sphinxbase/swig/python']
)

ps_swig_opts = (
    swig_opts +
    ['-I' + h for h in sb_include_dirs] +
    ['-I' + h for h in ps_include_dirs] +
    ['-Isphinxbase/swig'] +
    ['-outdir', 'pocketsphinx/swig/python']
)

setup(
    name='pocketsphinx-python-light',
    version='0.0.1',
    description='Python interface to CMU SphinxBase and PocketSphinx libraries',
    long_description=__doc__,
    author='Yihui Xiong',
    author_email='yihui.xiong@163.com',
    maintainer='Yihui Xiong',
    maintainer_email='yihui.xiong@163.com',
    url='https://github.com/xiongyihui/pocketsphinx-python-light',
    download_url='https://pypi.python.org/pypi/pocketsphinx',
    packages=['sphinxbase', 'pocketsphinx'],
    ext_modules=[
        Extension(
            name='sphinxbase._sphinxbase',
            sources=sb_sources,
            swig_opts=sb_swig_opts,
            include_dirs=sb_include_dirs,
            libraries=sb_libraries
        ),
        Extension(
            name='pocketsphinx._pocketsphinx',
            sources=ps_sources,
            swig_opts=ps_swig_opts,
            include_dirs=sb_include_dirs + ps_include_dirs,
            libraries=ps_libraries
        )
    ],
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: C'
    ],
    license='BSD',
    keywords=['sphinxbase', 'pocketsphinx'],
    platforms=['Linux'],
    package_dir={
        'sphinxbase': 'sphinxbase/swig/python',
        'pocketsphinx': 'pocketsphinx/swig/python'
    }
)
