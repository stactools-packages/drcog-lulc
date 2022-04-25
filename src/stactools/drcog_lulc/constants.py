import datetime
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

ITEM_ID = "drcog-hrlulc-pilot"
ITEM_DESCRIPTION = "DRCOG LULC at 1m resolution for year 2018"
# Per the discussion in https://github.com/radiantearth/stac-spec/issues/216,
# the recommendation for multi-platform datasets is to include all platforms
# and use a string separator. The same logic is applied to the mission.
MISSION = "DRCOG LULC"
EPSG = "26913"
START_TIME = datetime.datetime.fromisoformat("2018-01-01T00:00:00+00:00")
END_TIME = datetime.datetime.fromisoformat("2018-12-31T23:59:59+00:00")
CLASSIFICATION_SCHEMA = (
    "https://stac-extensions.github.io/classification/v1.0.0/schema.json"
)

ASSET_PROPS: Dict[str, Any] = {
    "data": {
        "title": "DRCOG LULC",
        "description": "Denver Regional Council of Governments (DRCOG) Land Use Land Cover (LULC) classifications",  # noqa
        "roles": ["data"],
        "bands": [
            {
                "description": "Classification values",
                "sampling": "area",
                "data_type": "uint8",
                "spatial_resolution": 1,
            }
        ],
        "classes": [
            {"value": 1, "description": "Structures", "color-hint": "FF0000"},
            {"value": 2, "description": "Impervious Surfaces", "color-hint": "B2B2B2"},
            {"value": 3, "description": "Water", "color-hint": "00A9E6"},
            {
                "value": 4,
                "description": "Prairie/Grassland/Natural Ground Cover",
                "color-hint": "C7D79E",
            },
            {"value": 5, "description": "Tree Canopy", "color-hint": "267300"},
            {"value": 6, "description": "Turf/Irrigated Land", "color-hint": "70A800"},
            {"value": 7, "description": "Barren Land", "color-hint": "FFEBAF"},
            {"value": 8, "description": "Cropland", "color-hint": "FFAE42"},
        ],
    }
}

COLLECTION_ID = "drcog-hrlulc"
COLLECTION_TITLE = "DRCOG LULC 2018"
COLLECTION_DESCRIPTION = (
    "1,000 square miles were classified by Land Use Land Cover at 1-meter resolution"
)
LICENSE = "proprietary"
LICENSE_LINK = Link(
    rel="license", target="https://drcog.org/legal-terms", title="DRCOG Legal Terms"
)
KEYWORDS = ["Land Cover", "Land Use", "NAIP", "USDA"]
PROVIDERS = [
    Provider(
        name="DRCOG",
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
    SpatialExtent([[-104.867784, -104.641093, 39.667712, 39.549871]]),
    TemporalExtent([[START_TIME, END_TIME]]),
)
SUMMARIES = Summaries({"mission": [MISSION]})
ITEM_ASSETS = {
    "data": AssetDefinition(
        {
            "type": MediaType.COG,
            "title": ASSET_PROPS["data"]["title"],
            "description": ASSET_PROPS["data"]["description"],
            "raster:bands": ASSET_PROPS["data"]["bands"],
            "classification:classes": ASSET_PROPS["data"]["classes"],
            "roles": ASSET_PROPS["data"]["roles"],
        }
    )
}
REPORT_LINK = Link(
    rel="describedby",
    target="https://gis.drcog.org//rdc/supplemental/lulc_pilot_report.zip",  # noqa
    title="Supplemental Information",
)
DATA_LINK = Link(
    rel="original",
    target="https://www.dropbox.com/s/0v2g1nqigm8604h/DRCOG_Final_Classification.zip?dl=0",
    title="DRCOG_Final_Classification",
)
