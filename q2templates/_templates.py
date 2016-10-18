# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources
import shutil
import tempfile

from .util import copy_assets, get_iterable
from jinja2 import Environment, FileSystemLoader


def render(source_files, output_dir, style=None, context={}):
    # TODO: Hook into qiime.sdk.config.TemporaryDirectory() when it exists
    temp_dir = tempfile.TemporaryDirectory()
    template_data = pkg_resources.resource_filename('q2templates', 'templates')
    copy_assets(template_data, temp_dir.name)
    env = Environment(loader=FileSystemLoader(temp_dir.name), auto_reload=True)

    for file in get_iterable(source_files):
        shutil.copy2(file, temp_dir.name)
        _, filename = os.path.split(file)
        template = env.get_template(filename)
        rendered_content = template.render(**context)
        with open(os.path.join(output_dir, filename), "w") as fh:
            fh.write(rendered_content)

    template_assets = os.path.join(template_data, 'assets')
    output_assets = os.path.join(output_dir, 'q2templateassets')
    copy_assets(template_assets, output_assets)
