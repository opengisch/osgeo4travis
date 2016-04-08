# Create the OSGeo stack for using on container based travis
#
# VERSION               1.0.0

FROM      ubuntu:12.04
MAINTAINER Matthias Kuhn <matthias@opengis.ch>

LABEL Description="Creates dependencies based on Ubuntu 12.04 for the OSGeo stack" Vendor="OPENGIS.ch" Version="1.0"

ENV CORES 8

COPY apt/*.list /etc/apt/sources.list.d/
COPY apt/*.key /tmp/
ENV CC clang-3.6
ENV CXX clang++-3.6
RUN apt-key add /tmp/llvm-snapshot.gpg.key
RUN apt-key add /tmp/toolchain.key
RUN apt-get update
RUN apt-get install -y python-software-properties
RUN add-apt-repository ppa:george-edison55/precise-backports
RUN apt-get update
RUN apt-get install -y clang-3.6 wget bison flex libsqlite3-dev libcairo-dev libfftw3-dev libglu1-mesa-dev libtiff4-dev libpng-dev pkg-config make bzip2 cmake cmake-data g++ patch libssl-dev libxkbcommon-dev libqt4-dev python-numpy

RUN ln -s /usr/bin/clang-3.6 /usr/bin/clang
RUN ln -s /usr/bin/clang++-3.6 /usr/bin/clang++

ENV PREFIX /home/travis/osgeo4travis
ENV PATH ${PREFIX}/bin:${PATH}

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY scripts/build-geos.sh /root/scripts/
RUN /root/scripts/build-geos.sh
COPY scripts/build-proj.sh /root/scripts/
RUN /root/scripts/build-proj.sh
COPY scripts/build-spatialite.sh /root/scripts/
RUN /root/scripts/build-spatialite.sh
RUN apt-get install -y python-dev
COPY scripts/build-gdal.sh /root/scripts/
RUN /root/scripts/build-gdal.sh
COPY scripts/build-grass7.sh /root/scripts/
RUN /root/scripts/build-grass7.sh
COPY scripts/build-qca.sh /root/scripts/
RUN /root/scripts/build-qca.sh
COPY scripts/build-ccache.sh /root/scripts/
RUN /root/scripts/build-ccache.sh
COPY scripts/patches/fcgi.patch /root/scripts/patches/
COPY scripts/build-fcgi.sh /root/scripts/
RUN /root/scripts/build-fcgi.sh
COPY scripts/build-spawn-fcgi.sh /root/scripts/
RUN /root/scripts/build-spawn-fcgi.sh
#RUN wget https://github.com/qgis/QGIS/archive/master.tar.gz
#RUN tar -xvf master.tar.gz
# RUN mkdir /usr/src/QGIS-master/build
# WORKDIR /usr/src/QGIS-master/build
# ENV PYTHONPATH ${PREFIX}/lib/python3/dist-packages/
# RUN cmake -DCMAKE_PREFIX_PATH=/home/travis/osgeo4travis -DENABLE_QT5=ON -DWITH_QTWEBKIT=OFF -DPYTHON_LIBRARY=/usr/lib/libpython3.2mu.so ..
# RUN make
COPY scripts/create-osgeo4travis.sh /root/scripts/
RUN /root/scripts/create-osgeo4travis.sh
