#!/bin/bash
# Build spawn-fcgi
wget http://download.lighttpd.net/spawn-fcgi/releases-1.6.x/spawn-fcgi-1.6.4.tar.gz
tar xvf spawn-fcgi-1.6.4.tar.gz
mkdir build-spawn-fcgi
pushd build-spawn-fcgi
cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \
  ../spawn-fcgi-1.6.4
make -j${CORES} > /dev/null
make install > /dev/null
popd
