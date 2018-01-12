# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

import pandas as pd

from q2templates import df_to_html


class TestDataFrameToHTML(unittest.TestCase):
    def test_no_truncation(self):
        long_cell = 'baz' * 100
        df = pd.DataFrame({'col': ['foo', 'bar', long_cell]})

        obs = df_to_html(df)

        self.assertIn('col', obs)
        self.assertIn('foo', obs)
        self.assertIn('bar', obs)
        self.assertIn(long_cell, obs)

    def test_defaults(self):
        df = pd.DataFrame({'col1': ['foo', 'bar', 'baz'], 'col2': [1, 2, 4.2]})

        obs = df_to_html(df)

        self.assertIn('border="0"', obs)
        self.assertIn('table table-striped table-hover', obs)

    def test_defaults_override(self):
        df = pd.DataFrame({'col1': ['foo', 'bar', 'baz'], 'col2': [1, 2, 4.2]},
                          index=['id1', 'id2', 'id3'])

        obs = df_to_html(df, border=1, classes=('class1', 'class2'),
                         index=False)

        self.assertIn('border="1"', obs)
        self.assertIn('class1 class2', obs)
        self.assertNotIn('id1', obs)
        self.assertNotIn('id2', obs)
        self.assertNotIn('id3', obs)


if __name__ == "__main__":
    unittest.main()
