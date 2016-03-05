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
RUN apt-get install -y clang-3.6 wget python3-dev bison flex libsqlite3-dev libcairo-dev libfftw3-dev libglu1-mesa-dev libtiff4-dev libpng-dev pkg-config make bzip2 cmake cmake-data
RUN ln -s /usr/bin/clang-3.6 /usr/bin/clang
RUN ln -s /usr/bin/clang++-3.6 /usr/bin/clang++

RUN wget http://download.qt.io/official_releases/qt/5.5/5.5.1/single/qt-everywhere-opensource-src-5.5.1.tar.gz
COPY scripts/build-qt5.sh /root/scripts/
RUN /root/scripts/build-qt5.sh
RUN mkdir -p /home/travis/deps/src
RUN cd /home/travis/ && tar -cvzf qt5.tgz qt5/ && cd /

WORKDIR /usr/src

ENV PREFIX /home/travis/deps
ENV PATH /home/travis/qt5/bin:${PREFIX}/bin:${PATH}

COPY scripts/build-geos.sh /root/scripts/
RUN /root/scripts/build-geos.sh
COPY scripts/build-proj.sh /root/scripts/
RUN /root/scripts/build-proj.sh
COPY scripts/build-spatialite.sh /root/scripts/
RUN /root/scripts/build-spatialite.sh
COPY scripts/build-qca.sh /root/scripts/
RUN /root/scripts/build-qca.sh
COPY scripts/build-spawn-fcgi.sh /root/scripts/
RUN /root/scripts/build-spawn-fcgi.sh
COPY scripts/build-gdal.sh /root/scripts/
RUN /root/scripts/build-gdal.sh
COPY scripts/build-grass7.sh /root/scripts/
RUN /root/scripts/build-grass7.sh
COPY scripts/build-grass.sh /root/scripts/
RUN /root/scripts/build-grass.sh
RUN apt-get install -y python-sip-dev g++
COPY scripts/build-sip.sh /root/scripts/
RUN /root/scripts/build-sip.sh
COPY scripts/build-pyqt5.sh /root/scripts/
RUN /root/scripts/build-pyqt5.sh
COPY scripts/build-qscintilla.sh /root/scripts/
RUN /root/scripts/build-qscintilla.sh
COPY scripts/build-spatialindex.sh /root/scripts/
RUN /root/scripts/build-spatialindex.sh
COPY scripts/build-qwt.sh /root/scripts/
RUN /root/scripts/build-qwt.sh
COPY scripts/create-osgeo4travis.sh /root/scripts/
RUN /root/scripts/create-osgeo4travis.sh
