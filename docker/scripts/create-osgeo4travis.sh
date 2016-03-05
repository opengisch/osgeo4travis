#!/bin/bash
pushd /home/travis
tar -zcvf osgeo4travis.tar.gz deps
popd
