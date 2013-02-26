spipy
=====
A Python SPI module

Installation
============
    $ sudo python setup.py install

Examples
========
    $ python
    >>> import spipy
    >>> s = spipy.SPI(0, 0)   # s refers to /dev/spidev0.0
    >>> s.transfer((1, 2, 3)) # transfer three bytes
    (0, 0, 0)                 # method returns three bytes (SPI is duplex)
