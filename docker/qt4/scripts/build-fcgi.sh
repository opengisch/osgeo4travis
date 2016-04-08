#!/bin/bash
# Build fcgi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

wget http://pkgs.fedoraproject.org/repo/pkgs/fcgi/fcgi-2.4.0.tar.gz/d15060a813b91383a9f3c66faf84867e/fcgi-2.4.0.tar.gz
tar -xf fcgi-2.4.0.tar.gz 
pushd fcgi-2.4.0
patch -p0 < ${DIR}/patches/fcgi.patch
./configure --prefix=/home/travis/osgeo4travis
make -j${CORES} > /dev/null
make install > /dev/null
popd
