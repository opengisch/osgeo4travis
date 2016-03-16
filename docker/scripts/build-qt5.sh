#!/bin/bash
wget http://download.qt.io/official_releases/qt/5.5/5.5.1/single/qt-everywhere-opensource-src-5.5.1.tar.gz
tar -xvf qt-everywhere-opensource-src-5.5.1.tar.gz
pushd qt-everywhere-opensource-src-5.5.1
./configure --opensource --confirm-license=yes --platform=linux-clang --prefix=${PREFIX} -system-xcb
make -j${CORES}
make install
popd  
