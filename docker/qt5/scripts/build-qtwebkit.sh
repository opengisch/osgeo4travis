#!/bin/bash
wget http://download.qt.io/community_releases/5.7/5.7.0/qtwebkit-opensource-src-5.7.0.tar.gz
tar -xvf qtwebkit-opensource-src-5.7.0.tar.gz
pushd qtwebkit-opensource-src-5.7.0
qmake PREFIX=${PREFIX} WebKit.pro
make -j${CORES}
make install
popd 
