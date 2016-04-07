#!/bin/bash
# Build spatialindex

wget http://download.osgeo.org/libspatialindex/spatialindex-src-1.8.5.tar.bz2
tar -xjf spatialindex-src-1.8.5.tar.bz2
pushd spatialindex-src-1.8.5
./configure --prefix=${PREFIX}
make -j${CORES} > /dev/null
make install > /dev/null
popd
