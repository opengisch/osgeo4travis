#!/bin/bash
# Build qwt

wget http://downloads.sourceforge.net/qwt/qwt/6.1.2/qwt-6.1.2.tar.bz2

tar -xjf qwt-6.1.2.tar.bz2
pushd qwt-6.1.2
patch -p1 < ${DIR}/patches/qwt.patch
sed -i "s|QWT_INSTALL_PREFIX *=.*|QWT_INSTALL_PREFIX = ${PREFIX}|g" qwtconfig.pri
qmake
make -j${CORES} > /dev/null
make install > /dev/null
popd
