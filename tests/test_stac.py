import unittest

from stactools.drcog_lulc import stac

from . import test_data


class StacTest(unittest.TestCase):
    def test_create_collection(self):
        # Write tests for each for the creation of a STAC Collection
        # Create the STAC Collection...
        collection = stac.create_collection()
        collection.set_self_href("")

        # Check that it has some required attributesƒ
        self.assertEqual(collection.id, "drcog-lulc")
        # self.assertEqual(collection.other_attr...

        # Validate
        collection.validate()

    def test_create_2018(self):
        href = test_data.get_path("data-files/DRCOG_2018_LULC_E3220000_N1710000.tif")
        item = stac.create_item(href)
        self.assertEqual(item.id, "DRCOG_2018_LULC_E3220000_N1710000")
        item.validate()

    def test_create_2020(self):
        href = test_data.get_path("data-files/DRCOG_2020_LULC_E2880000_N1680000.tif")
        item = stac.create_item(href)
        self.assertEqual(item.id, "DRCOG_2020_LULC_E2880000_N1680000")
        item.validate()
