#!/bin/bash
tar -xvf qt-everywhere-opensource-src-5.5.1.tar.gz
pushd qt-everywhere-opensource-src-5.5.1
./configure --opensource --confirm-license=yes --platform=linux-clang --prefix=/home/travis/qt5
make -j8
make -j8 install
popd  
