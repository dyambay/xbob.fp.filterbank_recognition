#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# author: David Yambay <yambayda@gmail.com>
# date:   Tue Apr 15 13:10 2014

# This file contains the python (distutils/setuptools) instructions so your
# package can be installed on **any** host system. It defines some basic
# information like the package name for instance, or its homepage.
#
# It also defines which other packages this python package depends on and that
# are required for this package's operation. The python subsystem will make
# sure all dependent packages are installed or will install them for you upon
# the installation of this package.
#
# The 'buildout' system we use here will go further and wrap this package in
# such a way to create an isolated python working environment. Buildout will
# make sure that dependencies which are not yet installed do get installed, but
# **without** requiring administrative privileges on the host system. This
# allows you to test your package with new python dependencies w/o requiring
# administrative interventions.

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    # This is the basic information about your project. Modify all this
    # information before releasing code publicly.
    name='xbob.fp.filterbank_recognition',
    version='1.0.0',
    description='Example for using Bob to create fingeprint verification systems',
    url='http://pypi.python.org/pypi/xbob.fp.filterbank_recognition',
    license='GPLv3',
    author='David Yambay',
    author_email='yambayda@gmail.com,

    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,

    # This line defines which packages should be installed when you "install"
    # this package. All packages that are mentioned here, but are not installed
    # on the current system will be installed locally and only visible to the
    # scripts of this package. Don't worry - You won't need administrative
    # privileges when using buildout.

    install_requires=[
        "setuptools",
        "bob >= 1.2.0",               # base signal proc./machine learning library
        "xbob.fp.filterbank_recognition",               # the LivDet Crossmatch fingerprint database
    ],

    # This package is good examples of namespace implementations
    # using several layers. You can check them out here:
    # https://github.com/idiap/bob/wiki/Satellite-Packages
    namespace_packages = [
      'xbob',
      'xbob.fp',
    ],

    # This entry defines which scripts you will have inside the 'bin' directory
    # once you install the package (or run 'bin/buildout'). The order of each
    # entry under 'console_scripts' is like this:
    #   script-name-at-bin-directory = module.at.your.library:function
    entry_points={
      'console_scripts': [
        'cropping.py = xbob.example.fingerverify.cropping:main',
        'findsector.py = xbob.example.fingerverify.findsector:main',
	'gabor2d.py = xbob.example.fingerverify.gabor2d:main',
	'ImageLoader.py = xbob.example.fingerverify.ImageLoader:main',
	'match.py = xbob.example.fingerverify.match:main',
	'matching.py = xbob.example.fingerverify.matching:main',
	'sectornorm.py = xbob.example.fingerverify.sectornorm:main',
	'templates.py = xbob.example.fingerverify.templates:main',
	'Wrapper.py = xbob.example.fingerverify.Wrapper:main',
        ],
     },

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      ],
)
