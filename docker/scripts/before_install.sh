# Build grass 7
if [ ! -f grass-7.0.2.tar.gz ]; then
  wget https://grass.osgeo.org/grass70/source/grass-7.0.2.tar.gz
  tar xvf grass-7.0.2.tar.gz
  pushd grass-7.0.2
  ./configure --prefix=${HOME}/deps \
    --with-cxx \
    --with-sqlite \
    --with-gdal=${HOME}/deps/bin/gdal-config \
    --with-geos=${HOME}/deps/bin/geos-config \
    --with-freetype=no
  make -j${CORES} > /dev/null
  make install > /dev/null
  popd
fi

# Build spawn-fcgi
if [ ! -f spawn-fcgi-1.6.4.tar.gz ]; then
  wget http://download.lighttpd.net/spawn-fcgi/releases-1.6.x/spawn-fcgi-1.6.4.tar.gz
  tar xvf spawn-fcgi-1.6.4.tar.gz
  mkdir build-spawn-fcgi
  pushd build-spawn-fcgi
  cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=${HOME}/deps \
    ../spawn-fcgi-1.6.4
  make -j${CORES} > /dev/null
  make install > /dev/null
  popd
fi

popd
