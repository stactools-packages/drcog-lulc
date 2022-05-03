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

    def test_create_item(self):
        href = test_data.get_path("data-files/DRCOG_HRLULC_Pilot_1m_Cropped.tif")
        item = stac.create_item(href)
        self.assertEqual(item.id, "drcog-lulc-hr-pilot")
        item.validate()
