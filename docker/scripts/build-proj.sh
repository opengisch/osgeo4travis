#!/bin/bash
# Build libproj
if [ ! -f proj-4.9.2.tar.gz ]; then
  wget http://download.osgeo.org/proj/proj-4.9.2.tar.gz
  tar xvf proj-4.9.2.tar.gz
  pushd proj-4.9.2
  ./configure --prefix=${PREFIX}
  make -j${CORES} > /dev/null
  make install > /dev/null
  popd
fi
