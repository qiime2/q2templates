# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources
import tempfile

from .util import copy_assets
from jinja2 import Environment, FileSystemLoader


def render(source_dir, output_dir, style=None, context={}):
    # TODO: Hook into qiime.sdk.config.TemporaryDirectory() when it exists
    temp_dir = tempfile.TemporaryDirectory()
    template_data = pkg_resources.resource_filename('q2templates', 'templates')

    copy_assets(template_data, temp_dir.name)
    copy_assets(source_dir, temp_dir.name)

    env = Environment(loader=FileSystemLoader(temp_dir.name))
    template = env.get_template('index.html')

    copy_assets(temp_dir.name, output_dir, filter='index.html')

    rendered_content = template.render(**context)
    with open(os.path.join(output_dir, 'index.html'), "w") as fh:
        fh.write(rendered_content)
