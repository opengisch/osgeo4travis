#configuration
CONFIG +=  shared qpa no_mocdepend release qt_no_framework
host_build {
    QT_ARCH = x86_64
    QT_TARGET_ARCH = x86_64
} else {
    QT_ARCH = x86_64
    QMAKE_DEFAULT_LIBDIRS = /lib /usr/lib
    QMAKE_DEFAULT_INCDIRS = /usr/include/c++/4.9 /usr/include/x86_64-linux-gnu/c++/4.9 /usr/include/c++/4.9/backward /usr/local/include /usr/lib/llvm-3.6/lib/clang/3.6.2/include /usr/include/x86_64-linux-gnu /usr/include
}
QT_CONFIG +=  minimal-config small-config medium-config large-config full-config fontconfig evdev xlib xrender xcb-plugin xcb-qt xcb-sm xkbcommon-qt accessibility-atspi-bridge linuxfb c++11 accessibility opengl shared qpa reduce_exports reduce_relocations clock-gettime clock-monotonic posix_fallocate mremap getaddrinfo ipv6ifname getifaddrs inotify eventfd system-jpeg system-png png system-freetype harfbuzz system-zlib nis iconv glib dbus openssl xcb rpath concurrent audio-backend release

#versioning
QT_VERSION = 5.5.1
QT_MAJOR_VERSION = 5
QT_MINOR_VERSION = 5
QT_PATCH_VERSION = 1

#namespaces
QT_LIBINFIX = 
QT_NAMESPACE = 

QT_EDITION = OpenSource

