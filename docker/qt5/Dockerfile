# Create the OSGeo stack for using on container based travis-wxgtk
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
RUN apt-get  update
RUN apt-get install -y clang-3.6 wget bison flex libsqlite3-dev libcairo-dev libfftw3-dev libglu1-mesa-dev libtiff4-dev libpng-dev pkg-config make bzip2 cmake cmake-data g++ patch libssl-dev libxkbcommon-dev ruby gperf perl libxcb-icccm4-dev libxcb-xfixes0-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-sync0-dev libxcb-randr0-dev unixodbc-dev libicu-dev python-numpy python-wxgtk2.8 libxcb-xinerama0-dev libxcb-render-util0-dev

RUN ln -s /usr/bin/clang-3.6 /usr/bin/clang
RUN ln -s /usr/bin/clang++-3.6 /usr/bin/clang++

ENV PREFIX /home/travis/osgeo4travis
ENV PATH ${PREFIX}/bin:${PATH}

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY scripts/install-python.sh /root/scripts/
RUN /root/scripts/install-python.sh
# RUN source /home/travis/virtualenv/bin/activate
ENV PATH /home/travis/virtualenv/python3.3.6/bin:$PATH

COPY scripts/build-qt5.sh /root/scripts/
RUN /root/scripts/build-qt5.sh
COPY scripts/build-qtwebkit.sh /root/scripts/
RUN /root/scripts/build-qtwebkit.sh

COPY scripts/build-geos.sh /root/scripts/
RUN /root/scripts/build-geos.sh
COPY scripts/build-proj.sh /root/scripts/
RUN /root/scripts/build-proj.sh
COPY scripts/build-spatialite.sh /root/scripts/
RUN /root/scripts/build-spatialite.sh
COPY scripts/build-qca.sh /root/scripts/
RUN /root/scripts/build-qca.sh
COPY scripts/build-lighttpd.sh /root/scripts/
RUN /root/scripts/build-lighttpd.sh
COPY scripts/build-spawn-fcgi.sh /root/scripts/
RUN /root/scripts/build-spawn-fcgi.sh
COPY scripts/build-gdal.sh /root/scripts/
RUN /root/scripts/build-gdal.sh
COPY scripts/build-grass7.sh /root/scripts/
RUN /root/scripts/build-grass7.sh
COPY scripts/build-sip.sh /root/scripts/
RUN /root/scripts/build-sip.sh
COPY scripts/build-pyqt5.sh /root/scripts/
RUN /root/scripts/build-pyqt5.sh
COPY scripts/build-qscintilla.sh /root/scripts/
COPY scripts/patches/qscintilla.patch /root/scripts/patches/
RUN /root/scripts/build-qscintilla.sh
COPY scripts/build-spatialindex.sh /root/scripts/
RUN /root/scripts/build-spatialindex.sh
COPY scripts/build-qwt.sh /root/scripts/
COPY scripts/patches/qwt.patch /root/scripts/patches/
RUN /root/scripts/build-qwt.sh
COPY scripts/build-ccache.sh /root/scripts/
RUN /root/scripts/build-ccache.sh
#RUN wget https://github.com/qgis/QGIS/archive/master.tar.gz
#RUN tar -xvf master.tar.gz
# RUN mkdir /usr/src/QGIS-master/build
# WORKDIR /usr/src/QGIS-master/build
# ENV PYTHONPATH ${PREFIX}/lib/python3/dist-packages/
# RUN cmake -DCMAKE_PREFIX_PATH=/home/travis/osgeo4travis -DENABLE_QT5=ON -DWITH_QTWEBKIT=OFF -DPYTHON_LIBRARY=/usr/lib/libpython3.2mu.so ..
# RUN make
COPY scripts/create-osgeo4travis.sh /root/scripts/
RUN /root/scripts/create-osgeo4travis.sh
