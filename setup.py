# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import q2templates

setup(
    name="q2templates",
    version=q2templates.__version__,
    license='BSD-3-Clause',
    packages=find_packages(),
    install_requires=['jinja2']
)
