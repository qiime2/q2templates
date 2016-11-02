# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import re
import ast

from setuptools import setup, find_packages

# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('q2templates/__init__.py', 'rb') as f:
    hit = _version_re.search(f.read().decode('utf-8')).group(1)
    version = str(ast.literal_eval(hit))

setup(
    name="q2templates",
    version=version,
    license='BSD-3-Clause',
    packages=find_packages(exclude=['tests']),
    package_data={
        'q2templates': [
            'templates/*.html',
            'templates/assets/css/*.css',
            'templates/assets/img/*.png',
            'templates/assets/fonts/glyphicons-*'
        ]
    },
    install_requires=['jinja2']
)
