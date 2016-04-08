#!/bin/bash
# Build geos
wget https://github.com/libgeos/libgeos/archive/3.5.0.tar.gz -O libgeos-3.5.0.tar.gz
tar xvf libgeos-3.5.0.tar.gz > /dev/null
mkdir build-geos
pushd build-geos
cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \
  -DCMAKE_BUILD_TYPE=Release \
  -DGEOS_ENABLE_TESTS=OFF \
  ../libgeos-3.5.0
make -j${CORES} > make.log
make install
popd
