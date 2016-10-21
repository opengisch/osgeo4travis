#!/bin/bash
# Build gdal

VERSION_gdal=2.1.2

wget https://github.com/OSGeo/gdal/archive/tags/${VERSION_gdal}.tar.gz -O gdal-${VERSION_gdal}.tar.gz
tar xvf gdal-${VERSION_gdal}.tar.gz > /dev/null

pushd gdal-tags-${VERSION_gdal}/gdal
./configure --prefix=${PREFIX} \
  --with-python=python3 \
  --with-geos=${PREFIX}/bin/geos-config \
  --without-libtool \
  --with-spatialite=dlopen \
  --with-spatialite-soname=libspatialite.so
make -j${CORES}
make install > /dev/null
popd
