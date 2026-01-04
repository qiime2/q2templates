# ----------------------------------------------------------------------------
# Copyright (c) 2016-2026, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import tempfile
import unittest
from pathlib import Path

from q2templates.reports import matryoshka_template


class TestMatryoshkaTemplate(unittest.TestCase):
    def test_matryoshka_assets_copied(self):
        # Create a temporary directory and render the template into it
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir)
            matryoshka_template(out, index=None)

            # Top-level expected entries
            expected_top = {"index.html", "_app", "conf"}
            found_top = {p.name for p in out.iterdir()}
            for name in expected_top:
                self.assertIn(
                    name, found_top,
                    "%s should be present in output dir" % name
                )

            # Check _app contains expected files and directories
            app_dir = out / "_app"
            self.assertTrue(app_dir.is_dir(), "_app should be a directory")
            self.assertTrue((app_dir / "env.js").is_file(),
                            "env.js should be copied")
            self.assertTrue((app_dir / "version.json").is_file(),
                            "version.json should be copied")

            immutable_dir = app_dir / "immutable"
            self.assertTrue(immutable_dir.is_dir(),
                            "_app/immutable should be a directory")
            # bundle file and assets subdir
            self.assertTrue(
                any(
                    p.name.startswith('bundle.') and p.suffix == '.js'
                    for p in immutable_dir.iterdir()
                ),
                "immutable should contain a bundle.<hash>.js file",
            )

            assets_dir = immutable_dir / "assets"
            self.assertTrue(
                assets_dir.is_dir(),
                "_app/immutable/assets should be a directory",
            )
            self.assertTrue(
                any(p.suffix == '.css' for p in assets_dir.iterdir()),
                "assets should contain a .css file",
            )

            # conf should be a directory (contains collapse)
            conf_dir = out / "conf"
            self.assertTrue(conf_dir.is_dir(), "conf should be a directory")
            # ensure at least one entry exists under conf (e.g., collapse)
            self.assertTrue(any(conf_dir.iterdir()),
                            "conf should not be empty")


if __name__ == "__main__":
    unittest.main()
