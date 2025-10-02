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


def _copy_assets_dir(name, output_dir):
    output_dir = Path(output_dir)
    package = '.'.join(['q2templates', 'reports', 'built_assets', name])
    with importlib.resources.path(package, '') as resource_path:
        for item in resource_path.iterdir():
            destination = output_dir / item.name
            if item.is_dir():
                shutil.copytree(item, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(item, destination)


def matryoshka_template(output_dir, index):
    # `index` is discovered by the webapp, so not used here
    _copy_assets_dir('matryoshka', output_dir)
