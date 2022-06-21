import logging

import click
from pystac import CatalogType

from stactools.drcog_lulc import stac

logger = logging.getLogger(__name__)


def create_drcog_lulc_command(cli):
    """Creates the stactools-drcog-lulc command line utility."""

    @cli.group(
        "drcog-lulc",
        short_help=("Commands for working with stactools-drcog-lulc"),
    )
    def drcog_lulc():
        pass

    @drcog_lulc.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    @click.option(
        "--validate/--no-validate",
        help="Validate the collection before saving",
        default=True,
    )
    def create_collection_command(
        destination: str,
        validate: bool,
    ):
        """Creates a STAC Collection

        \b
        Args:
            destination (str): The destination directory
            asset_href (optional, str): Href of asset to create an item, which
                will be added to the collection
        """
        collection = stac.create_collection()
        collection.normalize_hrefs(destination)
        if validate:
            collection.validate_all()
        collection.make_all_asset_hrefs_relative()
        collection.save(catalog_type=CatalogType.SELF_CONTAINED)

        return None

    @drcog_lulc.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("year", type=int)
    @click.argument("destination")
    def create_item_command(source: str, year: int, destination: str):
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Collection
            year (int): year of data collection
        """
        item = stac.create_item(source, year)

        item.save_object(dest_href=destination)

        return None

    return drcog_lulc
