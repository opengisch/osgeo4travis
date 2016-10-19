#!/bin/bash

VERSION_qt5=5.7.0

wget http://download.qt.io/official_releases/qt/5.7/${VERSION_qt5}/single/qt-everywhere-opensource-src-${VERSION_qt5}.tar.gz
tar -xvf qt-everywhere-opensource-src-${VERSION_qt5}.tar.gz
pushd qt-everywhere-opensource-src-${VERSION_qt5}
./configure --opensource --confirm-license=yes --platform=linux-clang --prefix=${PREFIX} -qt-xcb
make -j${CORES}
make install
popd  
