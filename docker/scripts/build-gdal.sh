#!/bin/bash
# Build gdal
wget https://github.com/OSGeo/gdal/archive/trunk.tar.gz
tar xvf trunk.tar.gz > /dev/null

pushd gdal-trunk/gdal
./configure --prefix=${PREFIX} \
  --with-python=python3 \
  --with-geos=${PREFIX}/bin/geos-config \
  --without-libtool
make -j${CORES}
#pushd swig/python
#python3 setup.py install --prefix=/home/travis/deps
#popd
make install > /dev/null
popd
