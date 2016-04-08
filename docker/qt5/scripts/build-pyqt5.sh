#!/bin/bash
# Build pyqt5

export C_INCLUDE_PATH=/usr/include/python3.2mu/
export CPLUS_INCLUDE_PATH=/usr/include/python3.2mu/

wget http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz
tar xzf PyQt-gpl-5.5.1.tar.gz
pushd PyQt-gpl-5.5.1
python3 configure.py --sysroot=${PREFIX} --confirm-license
make -j${CORES} > /dev/null
make install > /dev/null
popd
