#!/bin/bash
pushd /home/travis
tar -cf - osgeo4travis/ | xz -9 -c - > osgeo4travis.tar.xz
popd
