#!/bin/bash
# Build sip

export C_INCLUDE_PATH=/usr/include/python3.2mu/
export CPLUS_INCLUDE_PATH=/usr/include/python3.2mu/

wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.18/sip-4.18.tar.gz
tar xzf sip-4.18.tar.gz
pushd sip-4.18
python3 configure.py --sysroot=${PREFIX}
make -j${CORES}
make install
popd
