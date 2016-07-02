'''Wrapper for rowio.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_rowio.7.0.4 /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/rowio.h /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h -o OBJ.x86_64-pc-linux-gnu/rowio.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'


_libs = {}
_libdirs = []

from ctypes_preamble import *
from ctypes_preamble import _variadic_function
from ctypes_loader import *

add_library_search_dirs([])

# Begin libraries

_libs["grass_rowio.7.0.4"] = load_library("grass_rowio.7.0.4")

# 1 libraries
# End libraries

# No modules

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/rowio.h: 14
class struct_ROWIO_RCB(Structure):
    pass

struct_ROWIO_RCB.__slots__ = [
    'buf',
    'age',
    'row',
    'dirty',
]
struct_ROWIO_RCB._fields_ = [
    ('buf', POINTER(None)),
    ('age', c_int),
    ('row', c_int),
    ('dirty', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/rowio.h: 21
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'fd',
    'nrows',
    'len',
    'cur',
    'buf',
    'getrow',
    'putrow',
    'rcb',
]
struct_anon_1._fields_ = [
    ('fd', c_int),
    ('nrows', c_int),
    ('len', c_int),
    ('cur', c_int),
    ('buf', POINTER(None)),
    ('getrow', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int)),
    ('putrow', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int)),
    ('rcb', POINTER(struct_ROWIO_RCB)),
]

ROWIO = struct_anon_1 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/rowio.h: 21

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 4
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_fileno'):
    Rowio_fileno = _libs['grass_rowio.7.0.4'].Rowio_fileno
    Rowio_fileno.restype = c_int
    Rowio_fileno.argtypes = [POINTER(ROWIO)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 5
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_forget'):
    Rowio_forget = _libs['grass_rowio.7.0.4'].Rowio_forget
    Rowio_forget.restype = None
    Rowio_forget.argtypes = [POINTER(ROWIO), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 6
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_get'):
    Rowio_get = _libs['grass_rowio.7.0.4'].Rowio_get
    Rowio_get.restype = POINTER(None)
    Rowio_get.argtypes = [POINTER(ROWIO), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 7
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_flush'):
    Rowio_flush = _libs['grass_rowio.7.0.4'].Rowio_flush
    Rowio_flush.restype = None
    Rowio_flush.argtypes = [POINTER(ROWIO)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 8
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_put'):
    Rowio_put = _libs['grass_rowio.7.0.4'].Rowio_put
    Rowio_put.restype = c_int
    Rowio_put.argtypes = [POINTER(ROWIO), POINTER(None), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 9
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_release'):
    Rowio_release = _libs['grass_rowio.7.0.4'].Rowio_release
    Rowio_release.restype = None
    Rowio_release.argtypes = [POINTER(ROWIO)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/rowio.h: 10
if hasattr(_libs['grass_rowio.7.0.4'], 'Rowio_setup'):
    Rowio_setup = _libs['grass_rowio.7.0.4'].Rowio_setup
    Rowio_setup.restype = c_int
    Rowio_setup.argtypes = [POINTER(ROWIO), c_int, c_int, c_int, CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int), CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int)]

ROWIO_RCB = struct_ROWIO_RCB # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/rowio.h: 14

# No inserted files

