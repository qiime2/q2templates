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


def matryoshka_template(output_dir, _):
    # index (`_`) is discovered by the webapp, so not needed here
    _copy_assets_dir('matryoshka', output_dir)