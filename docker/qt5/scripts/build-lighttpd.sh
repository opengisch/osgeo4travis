#!/bin/bash
# Build spawn-fcgi
wget http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.39.tar.gz
tar -xf lighttpd-1.4.39.tar.gz
mkdir build-lighttpd
pushd build-lighttpd
cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \
  ../lighttpd-1.4.39
make -j${CORES} > /dev/null
make install > /dev/null
popd
