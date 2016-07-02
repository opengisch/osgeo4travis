#############################################################################
#
# MODULE:   	Grass Compilation
# AUTHOR(S):	Original author unknown - probably CERL
#		Markus Neteler - Germany/Italy - neteler@itc.it
#   	    	Justin Hickey - Thailand - jhickey@hpcc.nectec.or.th
#   	    	Huidae Cho - Korea - grass4u@gmail.com
#   	    	Eric G. Miller - egm2@jps.net
# PURPOSE:  	The source file for this Makefile is in src/CMD/head/head.in.
#		It is the top part of a file called make.rules which is used
#		for compiling all GRASS modules. This part of the file provides
#		make variables that are dependent on the results of the
#		configure script.
# COPYRIGHT:    (C) 2000 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#   	    	License (>=v2). Read the file COPYING that comes with GRASS
#   	    	for details.
#
#############################################################################

############################## Make Variables ###############################

CC                  = clang-3.6
CXX                 = clang++-3.6
LEX                 = flex
YACC                = bison -y
PERL                = /usr/bin/perl
AR                  = ar
RANLIB              = ranlib
MKDIR               = mkdir -p
CHMOD               = chmod
INSTALL             = /usr/bin/install -c 
INSTALL_DATA        = ${INSTALL} -m 644

prefix              = /home/travis/osgeo4travis
exec_prefix         = ${prefix}
ARCH                = x86_64-pc-linux-gnu
UNIX_BIN            = ${exec_prefix}/bin
INST_DIR            = ${prefix}/grass-7.0.4

GRASS_HOME          = /home/travis/osgeo4travis/grass-7.0.4
RUN_GISBASE         = /home/travis/osgeo4travis/grass-7.0.4

GRASS_VERSION_MAJOR = 7
GRASS_VERSION_MINOR = 0
GRASS_VERSION_RELEASE = 4
GRASS_VERSION_DATE  = 2016
GRASS_VERSION_SVN   = 00000

STRIPFLAG           = 
LD_SEARCH_FLAGS     = -Wl,-rpath-link,${LIB_RUNTIME_DIR}
LD_LIBRARY_PATH_VAR = LD_LIBRARY_PATH

#generate static (ST) or shared (SH)
GRASS_LIBRARY_TYPE  = shlib

#static libs:
STLIB_LD            = ${AR} cr
STLIB_PREFIX        = lib
STLIB_SUFFIX        = .a

#shared libs
SHLIB_PREFIX        = lib
SHLIB_LD            = clang-3.6 -shared
SHLIB_LDFLAGS       = -Wl,-soname,$(notdir $@)
SHLIB_CFLAGS        = -fPIC
SHLIB_SUFFIX        = .so
EXE                 = 

DEFAULT_DATABASE    =
DEFAULT_LOCATION    =

CPPFLAGS            = 
CFLAGS              = -g -O2 
CXXFLAGS            = -g -O2
INCLUDE_DIRS        = 
LINK_FLAGS          =  -Wl,--export-dynamic

DLLIB               = -ldl
XCFLAGS             = 
XLIBPATH            = 
XLIB                =  
XEXTRALIBS          = 
USE_X11             = 

MATHLIB             = -lm 
ICONVLIB            = 
INTLLIB             = 
SOCKLIB             = 

#ZLIB:
ZLIB                =  -lz 
ZLIBINCPATH         = 
ZLIBLIBPATH         = 

DBMIEXTRALIB        = 

#readline
READLINEINCPATH     = 
READLINELIBPATH     = 
READLINELIB         = 
HISTORYLIB          = 

#PostgreSQL:
PQINCPATH           = 
PQLIBPATH           = 
PQLIB               = 
USE_POSTGRES        = 

#MySQL:
MYSQLINCPATH        = 
MYSQLLIBPATH        = 
MYSQLLIB            = 
MYSQLDLIB           = 

#SQLite:
SQLITEINCPATH       = 
SQLITELIBPATH       = 
SQLITELIB           =  -lsqlite3 

#ODBC:
ODBCINC             = 
ODBCLIB             = 

#Image formats:
PNGINC              = 
PNGLIB              =  -lpng  -lz  -lm
USE_PNG             = 1

TIFFINCPATH         = 
TIFFLIBPATH         = 
TIFFLIB             =  -ltiff 

#openGL files for NVIZ/r3.showdspf
OPENGLINC           = 
OPENGLLIB           =   -lGL 
OPENGLULIB          =   -lGLU 
OPENGL_X11          = 1
OPENGL_AQUA         = 
OPENGL_WINDOWS      = 
USE_OPENGL          = 1

#FFTW:
FFTWINC             = 
FFTWLIB             =  -lfftw3 -lm

#LAPACK/BLAS stuff for gmath lib:
BLASLIB             = 
BLASINC             = 
LAPACKLIB           = 
LAPACKINC           = 

#GDAL/OGR
GDALLIBS            = -L/home/travis/osgeo4travis/lib -lgdal
GDALCFLAGS          = -I/home/travis/osgeo4travis/include
USE_GDAL            = 1
USE_OGR             = 1

#NetCDF
NETCDFLIBS          = 
NETCDFCFLAGS        =     
USE_NETCDF          = 

#LAS LiDAR through libLAS
LASLIBS             = 
LASCFLAGS           = 
LASINC              = 
USE_LIBLAS          = 

#GEOS
GEOSLIBS            = -L/home/travis/osgeo4travis/lib -lgeos -lgeos_c 
GEOSCFLAGS          = -I/home/travis/osgeo4travis/include
USE_GEOS            = 1

#FreeType:
FTINC               = 
FTLIB               = 

#PROJ.4:
PROJINC             =  -I/home/travis/osgeo4travis/include/ $(GDALCFLAGS)
PROJLIB             =  -L/home/travis/osgeo4travis/lib/ -lproj 
NAD2BIN             = /home/travis/osgeo4travis/bin/nad2bin
PROJSHARE           = /usr/share/proj

#OPENDWG:
OPENDWGINCPATH      = 
OPENDWGLIBPATH      = 
OPENDWGLIB          = 
USE_OPENDWG         = 

#cairo
CAIROINC                  = -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12  
CAIROLIB                  = -lfreetype -lz -lcairo -lfontconfig    
USE_CAIRO                 = 1
CAIRO_HAS_XRENDER         = 1
CAIRO_HAS_XRENDER_SURFACE = 1

#Python
PYTHON              = python

#wxWidgets
WXVERSION           = 
WXWIDGETSCXXFLAGS   = 
WXWIDGETSCPPFLAGS   = 
WXWIDGETSLIB        = 
USE_WXWIDGETS       = 
MACOSX_ARCHS_WXPYTHON = 

#regex
REGEXINCPATH        = 
REGEXLIBPATH        = 
REGEXLIB            =  
USE_REGEX           = 1

#pthreads
PTHREADINCPATH      = 
PTHREADLIBPATH      = 
PTHREADLIB          = 
USE_PTHREAD         = 

#OpenMP
OMPINCPATH          = 
OMPLIBPATH          = 
OMPLIB              = 
OMPCFLAGS           = 
USE_OPENMP          = 

#OpenCL
OCLINCPATH          = 
OCLLIBPATH          = 
OCLLIB              = 
USE_OPENCL          = 

#i18N
HAVE_NLS            = 

#Large File Support (LFS)
USE_LARGEFILES      = 1
LFS_CFLAGS          = 

#BSD sockets
HAVE_SOCKET         = 1

MINGW		    = 
MACOSX_APP	    = 
MACOSX_ARCHS        = 
MACOSX_SDK          = 

# Cross compilation
CROSS_COMPILING     =  
