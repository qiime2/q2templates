# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import shutil


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
