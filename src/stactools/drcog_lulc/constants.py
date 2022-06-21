from typing import Any, Dict

from pystac import (
    Extent,
    Link,
    MediaType,
    Provider,
    ProviderRole,
    SpatialExtent,
    Summaries,
    TemporalExtent,
)
from pystac.extensions.item_assets import AssetDefinition

ITEM_ID = {
    2018: {
        "drcog-lulc-2018"
        },
    2020: {
        "drcog-lulc-2020"
    }
}
ITEM_DESCRIPTION = "DRCOG LULC at 1m resolution"
MISSION = "DRCOG LULC"
EPSG = 26913
CLASSIFICATION_SCHEMA = (
    "https://stac-extensions.github.io/classification/v1.1.0/schema.json"
)

ASSET_PROPS: Dict[str, Any] = {
    "data": {
        "title": "DRCOG LULC",
        "description": "Denver Regional Council of Governments (DRCOG) Land Use Land Cover (LULC) classifications",  # noqa
        "type": "image/tiff; application=geotiff; profile=cloud-optimized",
        "roles": ["data"],
        "raster:bands": [
            {
                "description": "Classification values",
                "sampling": "area",
                "data_type": "uint8",
                "spatial_resolution": 1,
            }
        ],
        "classification:classes": [
            {"value": 1, "description": "Structures", "color_hint": "FF0000"},
            {"value": 2, "description": "Impervious Surfaces", "color_hint": "B2B2B2"},
            {"value": 3, "description": "Water", "color_hint": "00A9E6"},
            {
                "value": 4,
                "description": "Prairie/Grassland/Natural Ground Cover",
                "color_hint": "C7D79E",
            },
            {"value": 5, "description": "Tree Canopy", "color_hint": "267300"},
            {"value": 6, "description": "Turf/Irrigated Land", "color_hint": "70A800"},
            {"value": 7, "description": "Barren Land", "color_hint": "FFEBAF"},
            {"value": 8, "description": "Cropland", "color_hint": "FFAE42"},
        ],
    }
}

COLLECTION_ID = "drcog-lulc"
COLLECTION_TITLE = "DRCOG LULC"
COLLECTION_DESCRIPTION = "The Denver Regional Council of Governments (DRCOG) Land Use/Land Cover (LULC) datasets are developed in partnership with Babbit Center for Land and Water Policy and the Chesapeake Conservancy's Conservation Innovation Center (CIC). DRCOG LULC includes 2018 data covering 1,000 square miles and 2020 data covering 6,000 square miles of the Denver, Colorado region at 1 meter resolution. The data is based on USDA's 1 meter National Agricultural Imagery Program (NAIP) aerial imagery and leaf-off aerial ortho-imagery captured as part of the Denver Regional Aerial Photography Project (6-inch resolution everywhere except the mountainous regions to the west, which came in 1-foot resolution)."  # noqa
LICENSE = "proprietary"
LICENSE_LINK = Link(
    rel="license", target="https://drcog.org/legal-terms", title="DRCOG Legal Terms"
)
KEYWORDS = ["Land Cover", "Land Use", "NAIP", "USDA"]
PROVIDERS = [
    Provider(
        name="Denver Regional Council of Governments",
        roles=[
            ProviderRole.LICENSOR,
            ProviderRole.PRODUCER,
            ProviderRole.HOST,
            ProviderRole.PROCESSOR,
        ],
        url=(
            "https://drcog.org/services-and-resources/data-maps-and-modeling/"
            "regional-land-use-land-cover-project"
        ),
    )
]
EXTENT = Extent(
    SpatialExtent([[-105.939624, 39.104426, -103.668018, 40.321386]]),
    TemporalExtent([[START_TIME, END_TIME]]),
)
SUMMARIES = Summaries({"mission": [MISSION]})
ITEM_ASSETS = {
    "data": AssetDefinition(
        {
            "type": MediaType.COG,
            "title": ASSET_PROPS["data"]["title"],
            "description": ASSET_PROPS["data"]["description"],
            "raster:bands": ASSET_PROPS["data"]["raster:bands"],
            "classification:classes": ASSET_PROPS["data"]["classification:classes"],
            "roles": ASSET_PROPS["data"]["roles"],
        }
    )
}
REPORT_LINK = Link(
    rel="describedby",
    target="https://gis.drcog.org/rdc/supplemental/lulc_pilot_report.zip",
    title="Supplemental Information",
)
DATA_LINK = Link(
    rel="original",
    target="https://www.dropbox.com/s/0v2g1nqigm8604h/DRCOG_Final_Classification.zip?dl=0",
    title="DRCOG_Final_Classification",
)
