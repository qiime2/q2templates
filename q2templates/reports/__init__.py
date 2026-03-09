# ----------------------------------------------------------------------------
# Copyright (c) 2025, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib.resources
import shutil
from pathlib import Path


def _copy_traversable(src, dst):
    if src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        for item in src.iterdir():
            _copy_traversable(item, dst / item.name)
    else:
        with src.open('rb') as src_fh, dst.open('wb') as dst_fh:
            shutil.copyfileobj(src_fh, dst_fh)


def _copy_assets_dir(name, output_dir):
    output_dir = Path(output_dir)
    package = '.'.join(['q2templates', 'reports', 'built_assets', name])
    resource_path = importlib.resources.files(package)
    for item in resource_path.iterdir():
        _copy_traversable(item, output_dir / item.name)


def matryoshka_template(output_dir, index):
    # `index` is discovered by the webapp, so not used here
    _copy_assets_dir('matryoshka', output_dir)
