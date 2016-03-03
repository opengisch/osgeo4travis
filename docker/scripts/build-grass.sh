#!/bin/bash

apt-get install -y python-numpy python-wxtools
export LD_LIBRARY_PATH=${PREFIX}/lib
pushd grass-7.0.2 python-wx
./configure --prefix=${PREFIX} \
  --with-cxx \
  --with-sqlite \
  --with-gdal=${PREFIX}/bin/gdal-config \
  --with-geos=${PREFIX}/bin/geos-config \
  --with-freetype=no \
  --with-proj-includes=/home/travis/deps/include/ \
  --with-proj-libs=/home/travis/deps/lib/
make -j${CORES} > /dev/null
make install > /dev/null
popd
