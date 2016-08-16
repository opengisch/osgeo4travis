CONFIG +=  compile_examples qpa largefile precompile_header use_gold_linker enable_new_dtags sse2 sse3 ssse3 sse4_1 sse4_2 avx avx2 avx512f pcre
QT_BUILD_PARTS += libs tools examples
QT_NO_DEFINES =  ALSA CUPS EGL EGLFS EGL_X11 IMAGEFORMAT_JPEG LIBPROXY OPENVG PULSEAUDIO TSLIB ZLIB
QT_QCONFIG_PATH = 
host_build {
    QT_CPU_FEATURES.x86_64 =  mmx sse sse2
} else {
    QT_CPU_FEATURES.x86_64 =  mmx sse sse2
}
QT_COORD_TYPE = double
QT_LFLAGS_ODBC   = -lodbc
QMAKE_CC = clang-3.6
QMAKE_CXX = clang++-3.6
styles += mac fusion windows
DEFINES += QT_NO_MTDEV
QT_CFLAGS_GLIB = -pthread -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include  
QT_LIBS_GLIB = -pthread -lgthread-2.0 -lrt -lglib-2.0  
QMAKE_INCDIR_OPENGL = 
QMAKE_LIBDIR_OPENGL = 
QMAKE_LIBS_OPENGL =  "-lGL"
QMAKE_CFLAGS_OPENGL = 
QMAKE_CFLAGS_FONTCONFIG = -I/usr/include/freetype2  
QMAKE_LIBS_FONTCONFIG = -lfontconfig -lfreetype  
DEFINES += QT_NO_LIBUDEV
DEFINES += QT_NO_TSLIB
QMAKE_INCDIR_XKBCOMMON_EVDEV =  
QMAKE_LIBS_XKBCOMMON_EVDEV = -lxkbcommon  
DEFINES += QT_NO_LIBINPUT
QMAKE_X11_PREFIX = /usr
QMAKE_XKB_CONFIG_ROOT = /usr/share/X11/xkb
QMAKE_CFLAGS_XCB =  
QMAKE_LIBS_XCB = -lxcb  
sql-drivers = 
sql-plugins =  odbc sqlite
