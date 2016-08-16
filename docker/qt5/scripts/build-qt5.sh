#!/bin/bash
wget http://download.qt.io/official_releases/qt/5.7/5.7.0/single/qt-everywhere-opensource-src-5.7.0.tar.gz
tar -xvf qt-everywhere-opensource-src-5.7.0.tar.gz
pushd qt-everywhere-opensource-src-5.7.0
./configure --opensource --confirm-license=yes --platform=linux-clang --prefix=${PREFIX} -qt-xcb
make -j${CORES}
make install
popd  
