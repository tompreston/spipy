[PiFace Digital IO](https://github.com/piface/pifacedigitalio) no
longer requires this module. I'm leaving it here in case anyone finds
it useful. You can write to SPI directly from within Python 3.

[Here](https://github.com/lthiery/SPI-Py) is another version by someone
else.

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
