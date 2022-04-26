import os.path
from tempfile import TemporaryDirectory

import pystac
from stactools.testing import CliTestCase

from stactools.drcog_lulc.commands import create_drcog_lulc_command

from . import test_data


class CommandsTest(CliTestCase):
    def create_subcommand_functions(self):
        return [create_drcog_lulc_command]

    def test_create_collection(self):
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-collection command and validate

            # Example:
            destination = os.path.join(tmp_dir, "collection.json")

            result = self.run_command(["drcog_lulc", "create-collection", destination])

            self.assertEqual(result.exit_code, 0, msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            collection = pystac.read_file(destination)
            self.assertEqual(collection.id, "drcog-hrlulc")
            # self.assertEqual(item.other_attr...

            collection.validate()

    def test_create_item(self):
        href = test_data.get_path("data-files/DRCOG_HRLULC_Pilot_1m_Cropped.tif")
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-item command and validate

            # Example:
            destination = os.path.join(tmp_dir, "item.json")
            result = self.run_command(
                [
                    "drcog_lulc",
                    "create-item",
                    href,
                    destination,
                ]
            )
            self.assertEqual(result.exit_code, 0, msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            item = pystac.read_file(destination)
            self.assertEqual(item.id, "drcog-lulc-hr-pilot")
            # self.assertEqual(item.other_attr...

            item.validate()
