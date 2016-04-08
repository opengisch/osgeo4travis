#!/bin/bash
# Build ccache
wget https://www.samba.org/ftp/ccache/ccache-3.2.4.tar.gz
tar xvf ccache-3.2.4.tar.gz
pushd ccache-3.2.4
./configure --prefix=${PREFIX}
make -j${CORES} > /dev/null
make install > /dev/null
popd
