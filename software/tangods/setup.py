#!/usr/bin/env python

# ******************************************************************************
# ESP8266ARS: Tango DS for a ALBA Remote Sensors base on ESP8266.
#
# Author(s): Roberto J. Homs Puron <rhoms@cells.es>,
#            Alberto Rubio Garcia <arubio@cells.es>
#            Sergio Astorga Sanchez <sastorga@cells.es>
#
# Copyright (C) 2017, CELLS / ALBA Synchrotron
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ******************************************************************************
from setuptools import setup, find_packages

# Do not update manually
__version = '0.1.0'

long_description = """ Tango Device Server to control the Esp8266ARS
"""


classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: GNU Library or Lesser General Public ' + \
    'License (LGPLv3)',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
]

setup(
    name='TangoEspARS',
    version=__version,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['TangoEspARS = tangoespars.__main__:main']
    },
    author='Roberto J. Homs Puron',
    author_email='rhoms@cells.es',
    maintainer='ctbeamlines',
    maintainer_email='ctbeamlines@cells.es',
    url='https://git.cells.es/controls/BL22GasFilling',
    keywords='APP',
    license='LGPLv3',
    description='Tango DS to control the IO Chamber filling',
    long_description=long_description,
    requires=['setuptools (>=1.1)'],  # In PyPI
    install_requires=['pytango', 'esp8266ARS'],  # In PyPI
    classifiers=classifiers
)
