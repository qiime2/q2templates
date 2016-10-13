# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import os
import shutil


def copy_assets(source_dir, output_dir, filter=None):
    # Copy into existing dir: http://stackoverflow.com/a/12514470/4760331
    for item in os.listdir(source_dir):
        src = os.path.join(source_dir, item)
        dest = os.path.join(output_dir, item)

        if filter is not None and src.endswith(filter):
            continue

        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
