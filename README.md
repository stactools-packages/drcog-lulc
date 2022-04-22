# stactools-drcog-lulc

- Name: drcog-lulc
- Package: `stactools.drcog-lulc`
- PyPI: https://pypi.org/project/stactools-drcog-lulc/
- Owner: @pholleway
- Dataset homepage: https://drcog.org/services-and-resources/data-maps-and-modeling/regional-land-use-land-cover-project
- STAC extensions used:
  - [classification](https://github.com/stac-extensions/classification/)
  - [item-assets](https://github.com/stac-extensions/item-assets)
  - [proj](https://github.com/stac-extensions/projection)
  - [raster](https://github.com/stac-extensions/raster)
  - [scientific](https://github.com/stac-extensions/scientific)

This repository will assist you in the generation of STAC files for 2018 Denver Regional Council of Goverments (DRCOG) high resolution Land Use Land Cover (LULC) dataset.

## Examples

### STAC objects

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

### Command-line usage

To create a STAC `Item`:

```shell
$ stac drcog-lulc create-item tests/data-files/XXXX.hdf.xml build
```

To create a STAC `Catalog` from a list of DRCOG asset hrefs:

```shell
$ stac drcog-lulc create-catalog examples/XXXX.txt examples/XXXX
```

Use `stac drcog-lulc --help` to see all subcommands and options.
