#!/bin/bash

VERSION_qt5=5.8
VERSION_qt5_complete=5.8.0-beta

#wget http://download.qt.io/official_releases/qt/5.7/${VERSION_qt5}/single/qt-everywhere-opensource-src-${VERSION_qt5}.tar.gz
wget http://download.qt.io/development_releases/qt/${VERSION_qt5}/${VERSION_qt5_complete}/single/qt-everywhere-opensource-src-${VERSION_qt5_complete}.tar.gz
tar -xvf qt-everywhere-opensource-src-${VERSION_qt5_complete}.tar.gz
pushd qt-everywhere-opensource-src-${VERSION_qt5_complete}
./configure -confirm-license -opensource -platform linux-clang -prefix ${PREFIX} -qt-xcb
make -j${CORES}
make install
popd  

