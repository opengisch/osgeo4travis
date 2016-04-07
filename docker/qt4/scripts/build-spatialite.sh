#!/bin/bash
# Build spatialite

export C_INCLUDE_PATH=${PREFIX}/include
export CPLUS_INCLUDE_PATH=${PREFIX}/include
export LD_LIBRARY_PATH=${PREFIX}/lib
export LDFLAGS="${LDFLAGS} -L${PREFIX}/lib"

if [ ! -f libspatialite-4.3.0a.tar.gz ]; then
 wget http://www.gaia-gis.it/gaia-sins/libspatialite-sources/libspatialite-4.3.0a.tar.gz
 tar xvf libspatialite-4.3.0a.tar.gz > /dev/null
  pushd libspatialite-4.3.0a
  ./configure --prefix=${PREFIX} \
    --enable-freexl=no \
    --with-geosconfig=${PREFIX}/bin/geos-config \
    --enable-libxml2=no
  make -j${CORES} > /dev/null
  make install > /dev/null
  popd
fi
