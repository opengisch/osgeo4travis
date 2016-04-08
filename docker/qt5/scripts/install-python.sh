#!/bin/bash

wget -O python-3.3.tar.bz2 https://s3.amazonaws.com/travis-python-archives/binaries/$(lsb_release -is | tr "A-Z" "a-z")/$(lsb_release -rs)/$(uname -m)/python-3.3.tar.bz2
tar -xvjf python-3.3.tar.bz2 -C /
