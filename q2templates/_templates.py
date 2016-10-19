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


def render(source_files, output_dir, styles=None, context=None):
    if context is None:
        context = {}
    if styles is None:
        styles = "base.html"

    # TODO: Hook into qiime.sdk.config.TemporaryDirectory() when it exists
    temp_dir = tempfile.TemporaryDirectory()
    template_data = pkg_resources.resource_filename('q2templates', 'templates')
    env = Environment(loader=FileSystemLoader(temp_dir.name), auto_reload=True)

    # Allow for the possibility of multiple style templates to choose from
    for style in get_iterable(styles):
        q2template = os.path.join(template_data, style)
        shutil.copy2(q2template, temp_dir.name)

    # Copy user files to the environment for rendering to the output_dir
    for path in get_iterable(source_files):
        shutil.copy2(path, temp_dir.name)
        filename = os.path.split(path)[1]
        template = env.get_template(filename)
        rendered_content = template.render(**context)
        with open(os.path.join(output_dir, filename), "w") as fh:
            fh.write(rendered_content)

    # Move the style assets to the output_dir
    template_assets = os.path.join(template_data, 'assets')
    output_assets = os.path.join(output_dir, 'q2templateassets')
    copy_assets(template_assets, output_assets)
