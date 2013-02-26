#!/usr/bin/env python

from distutils.core import setup, Extension

DISTUTILS_DEBUG=True

setup(name='spipy',
	version='1.0',
	description='Python module for communicating with an SPI device.',
	author='Thomas Preston',
	author_email='thomasmarkpreston@gmail.com',
	license='GPLv2',
	url='http://pi.cs.man.ac.uk/interface.htm',
	ext_modules=[Extension('spipy', ['spi.c'])],
)
