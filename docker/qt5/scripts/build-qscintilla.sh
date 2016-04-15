#!/bin/bash
# Build pyqt5

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export C_INCLUDE_PATH=/usr/include/python3.2mu/
export CPLUS_INCLUDE_PATH=/usr/include/python3.2mu/
export PYTHONPATH=

wget http://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.9.1/QScintilla-gpl-2.9.1.tar.gz
tar xzf QScintilla-gpl-2.9.1.tar.gz
pushd QScintilla-gpl-2.9.1
patch -p1 < ${DIR}/patches/qscintilla.patch
pushd Qt4Qt5
mv features/qscintilla2.prf features/qscintilla2-qt5.prf
qmake
make -j${CORES}
make install
popd
pushd Python
export PYTHONPATH=${PREFIX}/lib/python3.3/site-packages/
python3 configure.py --pyqt=PyQt5 --qsci-incdir=/home/travis/osgeo4travis/include/ --qsci-libdir=/home/travis/osgeo4travis/lib --destdir=/home/travis/osgeo4travis/lib/python3.3/site-packages/PyQt5/ --pyqt-sipdir=/home/travis/osgeo4travis/share/sip/PyQt5/ --sip-incdir=/home/travis/osgeo4travis/include/python3.3m
make -j${CORES}
make install
popd
popd
