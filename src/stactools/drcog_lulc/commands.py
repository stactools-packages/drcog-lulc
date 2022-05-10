import logging

import click

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
    @click.option("asset_href")
    def create_collection_command(
        destination: str,
        asset_href: str,
    ):
        """Creates a STAC Collection

        \b
        Args:
            asset_href (str): Href of asset for the Collection JSON
            destination (str): An HREF for the Collection JSON
        """
        collection = stac.create_collection()

        collection.set_self_href(destination)

        collection.save_object()

        return None

    @drcog_lulc.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str):
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Collection
        """
        item = stac.create_item(source)

        item.save_object(dest_href=destination)

        return None

    return drcog_lulc
