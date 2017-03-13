#!/bin/bash
# Build Qt5KeyChain
wget -O qtkeychain.zip https://github.com/frankosterfeld/qtkeychain/archive/master.zip
unzip qtkeychain.zip

mkdir build-qtkeychain
pushd build-qtkeychain
cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \
  -DLIBSECRET_SUPPORT=OFF \
  ../qtkeychain-master
make -j${CORES} > /dev/null
make install > /dev/null
popd
