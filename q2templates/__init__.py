# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._templates import render
from .util import df_to_html
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions

__all__ = ['render', 'df_to_html']
