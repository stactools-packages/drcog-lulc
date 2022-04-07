import unittest

import stactools.drcog_lulc


class TestModule(unittest.TestCase):

    def test_version(self):
        self.assertIsNotNone(stactools.drcog_lulc.__version__)
