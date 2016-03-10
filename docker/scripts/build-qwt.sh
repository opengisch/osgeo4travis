#!/bin/bash
# Build qwt

wget http://downloads.sourceforge.net/qwt/qwt/6.1.2/qwt-6.1.2.tar.bz2

tar -xjf qwt-6.1.2.tar.bz2
pushd qwt-6.1.2
sed -i "s|QWT_INSTALL_PREFIX *=.*|QWT_INSTALL_PREFIX = ${PREFIX}|g" qwtconfig.pri
qmake
make -j${CORES} > /dev/null
make install > /dev/null
pushd ${PREFIX}/lib
mv libqwt.so.6.1.2 libqwt-qt5.so.6.1.2
rm libqwt-qt5.so
rm libqwt-qt5.so.6
rm libqwt-qt5.so.6.1
ln -s libqwt-qt5.so.6.1.2 libqwt-qt5.so.6.1
ln -s libqwt-qt5.so.6.1.2 libqwt-qt5.so.6  
ln -s libqwt-qt5.so.6.1.2 libqwt-qt5.so  
popd
popd
