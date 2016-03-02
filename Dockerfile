# Create the OSGeo stack for using on container based travis
#
# VERSION               1.0.0

FROM      ubuntu:12.04
MAINTAINER Matthias Kuhn <matthias@opengis.ch>

LABEL Description="Creates dependencies based on Ubuntu 12.04 for the OSGeo stack" Vendor="OPENGIS.ch" Version="1.0"
COPY apt/*.list /etc/apt/sources.list.d/
COPY apt/*.key /tmp/
COPY scripts/* /root/scripts/
RUN apt-key add /tmp/llvm-snapshot.gpg.key
RUN apt-key add /tmp/toolchain.key
RUN apt-get update
RUN apt-get install -y clang-3.6 wget
RUN wget http://download.qt.io/official_releases/qt/5.5/5.5.1/single/qt-everywhere-opensource-src-5.5.1.tar.gz
RUN apt-get install -y make
RUN ln -s /usr/bin/clang-3.6 /usr/bin/clang
RUN ln -s /usr/bin/clang++-3.6 /usr/bin/clang++
RUN /root/scripts/build-qt5.sh
RUN cd /home/travis/ && tar -cvzf qt5.tgz qt5/ && cd /
