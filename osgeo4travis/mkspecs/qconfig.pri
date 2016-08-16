#configuration
CONFIG +=  shared qpa release qt_no_framework
host_build {
    QT_ARCH = x86_64
    QT_TARGET_ARCH = x86_64
} else {
    QT_ARCH = x86_64
}
QT_CONFIG +=  minimal-config small-config medium-config large-config full-config fontconfig evdev xlib xrender xcb-plugin xcb-qt xcb-sm xkbcommon-qt accessibility-atspi-bridge linuxfb kms c++11 c++14 c++1z accessibility opengl shared qpa reduce_exports reduce_relocations clock-gettime clock-monotonic posix_fallocate mremap getaddrinfo ipv6ifname getifaddrs inotify eventfd threadsafe-cloexec poll_poll system-jpeg system-png png doubleconversion system-freetype harfbuzz system-zlib nis iconv glib dbus openssl xcb rpath icu concurrent audio-backend release

#versioning
QT_VERSION = 5.7.0
QT_MAJOR_VERSION = 5
QT_MINOR_VERSION = 7
QT_PATCH_VERSION = 0

#namespaces
QT_LIBINFIX = 
QT_NAMESPACE = 

QT_EDITION = OpenSource

QT_COMPILER_STDCXX = 199711
