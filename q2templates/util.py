# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import shutil

import pandas as pd


def df_to_html(df, border=0, classes=('table', 'table-striped', 'table-hover'),
               **kwargs):
    """Convert a dataframe to HTML without truncating contents.

    pandas will truncate cell contents that exceed 50 characters by default.
    Use this function to avoid this truncation behavior.

    This function uses different default parameters than `DataFrame.to_html` to
    give uniform styling to HTML tables that are compatible with q2template
    themes. These parameters can be overridden, and they (along with any other
    parameters) will be passed through to `DataFrame.to_html`.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to convert to HTML.
    kwargs : dict
        Parameters passed through to `pd.DataFrame.to_html`.

    Returns
    -------
    str
        DataFrame converted to HTML.

    References
    ----------
    .. [1] https://stackoverflow.com/q/26277757/3776794
    .. [2] https://github.com/pandas-dev/pandas/issues/1852

    """
    with pd.option_context('display.max_colwidth', -1):
        return df.to_html(border=border, classes=classes, **kwargs)


def copy_assets(source_dir, output_dir):
    # Copy into existing dir: http://stackoverflow.com/a/12514470/4760331
    for item in os.listdir(source_dir):
        # Ignore dotfiles
        if item.startswith('.'):
            continue

        src = os.path.join(source_dir, item)
        dest = os.path.join(output_dir, item)

        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)


def get_iterable(src):
    if isinstance(src, str):
        return (src,)
    return src
