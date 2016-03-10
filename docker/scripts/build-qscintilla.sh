#!/bin/bash
# Build pyqt5

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export C_INCLUDE_PATH=/usr/include/python3.2mu/
export CPLUS_INCLUDE_PATH=/usr/include/python3.2mu/

# wget http://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.9.1/QScintilla-gpl-2.9.1.tar.gz
tar xzf QScintilla-gpl-2.9.1.tar.gz
pushd QScintilla-gpl-2.9.1
patch -p1 < ${DIR}/patches/qscintilla.patch
pushd Qt4Qt5
mv features/qscintilla2.prf features/qscintilla2-qt5.prf
qmake
make -j${CORES}
make install
popd
popd
