#!/bin/bash
# Build pyqt5

export C_INCLUDE_PATH=/usr/include/python3.2mu/
export CPLUS_INCLUDE_PATH=/usr/include/python3.2mu/

wget http://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.9.1/QScintilla-gpl-2.9.1.tar.gz
tar xzf QScintilla-gpl-2.9.1.tar.gz
pushd QScintilla-gpl-2.9.1/Qt4Qt5
qmake
make -j${CORES} > /dev/null
make install > /dev/null
popd
