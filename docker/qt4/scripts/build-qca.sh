#!/bin/bash
# Build QCA
wget -O qca-2.1.1.tar.gz https://github.com/KDE/qca/archive/v2.1.1.tar.gz
tar xvf qca-2.1.1.tar.gz
mkdir build-qca
pushd build-qca
cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \
  ../qca-2.1.1
make -j${CORES} > /dev/null
make install > /dev/null
popd
