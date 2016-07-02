#!/bin/bash
# Build grass 7
GRASS_VERSION=7.0.4

wget https://grass.osgeo.org/grass70/source/grass-${GRASS_VERSION}.tar.gz
tar xvf grass-${GRASS_VERSION}.tar.gz

export LD_LIBRARY_PATH=${PREFIX}/lib
pushd grass-${GRASS_VERSION}
./configure --prefix=${PREFIX} \
  --with-cxx \
  --with-sqlite \
  --with-gdal=${PREFIX}/bin/gdal-config \
  --with-geos=${PREFIX}/bin/geos-config \
  --with-freetype=no \
  --with-proj-includes=${PREFIX}/include/ \
  --with-proj-libs=${PREFIX}/lib/
make -j${CORES} > /dev/null
make install > /dev/null
popd
