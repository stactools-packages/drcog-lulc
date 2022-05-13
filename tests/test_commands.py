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
        with TemporaryDirectory() as temporary_directory:
            result = self.run_command(
                ["drcog-lulc", "create-collection", temporary_directory]
            )
            self.assertEqual(result.exit_code, 0, msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(temporary_directory) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            collection = pystac.read_file(os.path.join(temporary_directory, jsons[0]))
            self.assertEqual(collection.id, "drcog-lulc")

            collection.validate()

    def test_create_item(self):
        asset_href = test_data.get_path("data-files/drcog_lulc_hr_pilot_1m.tif")
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-item command and validate

            # Example:
            destination = os.path.join(tmp_dir, "item.json")
            result = self.run_command(
                [
                    "drcog-lulc",
                    "create-item",
                    asset_href,
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
