#!/bin/bash
# Build pyqt5

export C_INCLUDE_PATH=/usr/include/python3.2mu/
export CPLUS_INCLUDE_PATH=/usr/include/python3.2mu/

wget http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.7/PyQt5_gpl-5.7.tar.gz
tar xzf PyQt5_gpl-5.7.tar.gz
pushd PyQt5_gpl-5.7
python3 configure.py --sysroot=${PREFIX} --confirm-license
make -j${CORES} > /dev/null
make install > /dev/null
popd
