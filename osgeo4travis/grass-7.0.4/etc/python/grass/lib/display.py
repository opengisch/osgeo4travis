'''Wrapper for display.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_display.7.0.4 /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h -o OBJ.x86_64-pc-linux-gnu/display.py

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

_libs["grass_display.7.0.4"] = load_library("grass_display.7.0.4")

# 1 libraries
# End libraries

# No modules

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 382
class struct_Cell_head(Structure):
    pass

struct_Cell_head.__slots__ = [
    'format',
    'compressed',
    'rows',
    'rows3',
    'cols',
    'cols3',
    'depths',
    'proj',
    'zone',
    'ew_res',
    'ew_res3',
    'ns_res',
    'ns_res3',
    'tb_res',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct_Cell_head._fields_ = [
    ('format', c_int),
    ('compressed', c_int),
    ('rows', c_int),
    ('rows3', c_int),
    ('cols', c_int),
    ('cols3', c_int),
    ('depths', c_int),
    ('proj', c_int),
    ('zone', c_int),
    ('ew_res', c_double),
    ('ew_res3', c_double),
    ('ns_res', c_double),
    ('ns_res3', c_double),
    ('tb_res', c_double),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

CELL = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 571

DCELL = c_double # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 572

FCELL = c_float # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 573

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 575
class struct__Color_Value_(Structure):
    pass

struct__Color_Value_.__slots__ = [
    'value',
    'red',
    'grn',
    'blu',
]
struct__Color_Value_._fields_ = [
    ('value', DCELL),
    ('red', c_ubyte),
    ('grn', c_ubyte),
    ('blu', c_ubyte),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 583
class struct__Color_Rule_(Structure):
    pass

struct__Color_Rule_.__slots__ = [
    'low',
    'high',
    'next',
    'prev',
]
struct__Color_Rule_._fields_ = [
    ('low', struct__Color_Value_),
    ('high', struct__Color_Value_),
    ('next', POINTER(struct__Color_Rule_)),
    ('prev', POINTER(struct__Color_Rule_)),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 595
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'red',
    'grn',
    'blu',
    'set',
    'nalloc',
    'active',
]
struct_anon_9._fields_ = [
    ('red', POINTER(c_ubyte)),
    ('grn', POINTER(c_ubyte)),
    ('blu', POINTER(c_ubyte)),
    ('set', POINTER(c_ubyte)),
    ('nalloc', c_int),
    ('active', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 605
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
]
struct_anon_10._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct__Color_Rule_))),
    ('nalloc', c_int),
    ('active', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 590
class struct__Color_Info_(Structure):
    pass

struct__Color_Info_.__slots__ = [
    'rules',
    'n_rules',
    'lookup',
    'fp_lookup',
    'min',
    'max',
]
struct__Color_Info_._fields_ = [
    ('rules', POINTER(struct__Color_Rule_)),
    ('n_rules', c_int),
    ('lookup', struct_anon_9),
    ('fp_lookup', struct_anon_10),
    ('min', DCELL),
    ('max', DCELL),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 617
class struct_Colors(Structure):
    pass

struct_Colors.__slots__ = [
    'version',
    'shift',
    'invert',
    'is_float',
    'null_set',
    'null_red',
    'null_grn',
    'null_blu',
    'undef_set',
    'undef_red',
    'undef_grn',
    'undef_blu',
    'fixed',
    'modular',
    'cmin',
    'cmax',
    'organizing',
]
struct_Colors._fields_ = [
    ('version', c_int),
    ('shift', DCELL),
    ('invert', c_int),
    ('is_float', c_int),
    ('null_set', c_int),
    ('null_red', c_ubyte),
    ('null_grn', c_ubyte),
    ('null_blu', c_ubyte),
    ('undef_set', c_int),
    ('undef_red', c_ubyte),
    ('undef_grn', c_ubyte),
    ('undef_blu', c_ubyte),
    ('fixed', struct__Color_Info_),
    ('modular', struct__Color_Info_),
    ('cmin', DCELL),
    ('cmax', DCELL),
    ('organizing', c_int),
]

RASTER_MAP_TYPE = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/raster.h: 25

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 27
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'color',
    'r',
    'g',
    'b',
    'fr',
    'fg',
    'fb',
]
struct_anon_25._fields_ = [
    ('color', c_int),
    ('r', c_int),
    ('g', c_int),
    ('b', c_int),
    ('fr', c_double),
    ('fg', c_double),
    ('fb', c_double),
]

SYMBCOLOR = struct_anon_25 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 27

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 35
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'count',
    'alloc',
    'x',
    'y',
]
struct_anon_26._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 40
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'clock',
    'x',
    'y',
    'r',
    'a1',
    'a2',
]
struct_anon_27._fields_ = [
    ('clock', c_int),
    ('x', c_double),
    ('y', c_double),
    ('r', c_double),
    ('a1', c_double),
    ('a2', c_double),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 33
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'line',
    'arc',
]
union_anon_28._fields_ = [
    ('line', struct_anon_26),
    ('arc', struct_anon_27),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 46
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'type',
    'coor',
]
struct_anon_29._fields_ = [
    ('type', c_int),
    ('coor', union_anon_28),
]

SYMBEL = struct_anon_29 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 46

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 55
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'count',
    'alloc',
    'elem',
    'scount',
    'salloc',
    'sx',
    'sy',
]
struct_anon_30._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('elem', POINTER(POINTER(SYMBEL))),
    ('scount', c_int),
    ('salloc', c_int),
    ('sx', POINTER(c_double)),
    ('sy', POINTER(c_double)),
]

SYMBCHAIN = struct_anon_30 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 55

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 65
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'type',
    'color',
    'fcolor',
    'count',
    'alloc',
    'chain',
]
struct_anon_31._fields_ = [
    ('type', c_int),
    ('color', SYMBCOLOR),
    ('fcolor', SYMBCOLOR),
    ('count', c_int),
    ('alloc', c_int),
    ('chain', POINTER(POINTER(SYMBCHAIN))),
]

SYMBPART = struct_anon_31 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 65

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 72
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'scale',
    'count',
    'alloc',
    'part',
]
struct_anon_32._fields_ = [
    ('scale', c_double),
    ('count', c_int),
    ('alloc', c_int),
    ('part', POINTER(POINTER(SYMBPART))),
]

SYMBOL = struct_anon_32 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/symbol.h: 72

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 8
class struct_color_rgba(Structure):
    pass

struct_color_rgba.__slots__ = [
    'r',
    'g',
    'b',
    'a',
]
struct_color_rgba._fields_ = [
    ('r', c_ubyte),
    ('g', c_ubyte),
    ('b', c_ubyte),
    ('a', c_ubyte),
]

RGBA_Color = struct_color_rgba # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 13

enum_clip_mode = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 20

M_NONE = 0 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 20

M_CULL = (M_NONE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 20

M_CLIP = (M_CULL + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 20

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 5
if hasattr(_libs['grass_display.7.0.4'], 'D_update_conversions'):
    D_update_conversions = _libs['grass_display.7.0.4'].D_update_conversions
    D_update_conversions.restype = None
    D_update_conversions.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 6
if hasattr(_libs['grass_display.7.0.4'], 'D_fit_d_to_u'):
    D_fit_d_to_u = _libs['grass_display.7.0.4'].D_fit_d_to_u
    D_fit_d_to_u.restype = None
    D_fit_d_to_u.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 7
if hasattr(_libs['grass_display.7.0.4'], 'D_fit_u_to_d'):
    D_fit_u_to_d = _libs['grass_display.7.0.4'].D_fit_u_to_d
    D_fit_u_to_d.restype = None
    D_fit_u_to_d.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 8
if hasattr(_libs['grass_display.7.0.4'], 'D_show_conversions'):
    D_show_conversions = _libs['grass_display.7.0.4'].D_show_conversions
    D_show_conversions.restype = None
    D_show_conversions.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 10
if hasattr(_libs['grass_display.7.0.4'], 'D_do_conversions'):
    D_do_conversions = _libs['grass_display.7.0.4'].D_do_conversions
    D_do_conversions.restype = None
    D_do_conversions.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 12
if hasattr(_libs['grass_display.7.0.4'], 'D_is_lat_lon'):
    D_is_lat_lon = _libs['grass_display.7.0.4'].D_is_lat_lon
    D_is_lat_lon.restype = c_int
    D_is_lat_lon.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 14
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_to_a_xconv'):
    D_get_d_to_a_xconv = _libs['grass_display.7.0.4'].D_get_d_to_a_xconv
    D_get_d_to_a_xconv.restype = c_double
    D_get_d_to_a_xconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 15
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_to_a_yconv'):
    D_get_d_to_a_yconv = _libs['grass_display.7.0.4'].D_get_d_to_a_yconv
    D_get_d_to_a_yconv.restype = c_double
    D_get_d_to_a_yconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 16
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_to_u_xconv'):
    D_get_d_to_u_xconv = _libs['grass_display.7.0.4'].D_get_d_to_u_xconv
    D_get_d_to_u_xconv.restype = c_double
    D_get_d_to_u_xconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 17
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_to_u_yconv'):
    D_get_d_to_u_yconv = _libs['grass_display.7.0.4'].D_get_d_to_u_yconv
    D_get_d_to_u_yconv.restype = c_double
    D_get_d_to_u_yconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 18
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_to_u_xconv'):
    D_get_a_to_u_xconv = _libs['grass_display.7.0.4'].D_get_a_to_u_xconv
    D_get_a_to_u_xconv.restype = c_double
    D_get_a_to_u_xconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 19
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_to_u_yconv'):
    D_get_a_to_u_yconv = _libs['grass_display.7.0.4'].D_get_a_to_u_yconv
    D_get_a_to_u_yconv.restype = c_double
    D_get_a_to_u_yconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 20
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_to_d_xconv'):
    D_get_a_to_d_xconv = _libs['grass_display.7.0.4'].D_get_a_to_d_xconv
    D_get_a_to_d_xconv.restype = c_double
    D_get_a_to_d_xconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 21
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_to_d_yconv'):
    D_get_a_to_d_yconv = _libs['grass_display.7.0.4'].D_get_a_to_d_yconv
    D_get_a_to_d_yconv.restype = c_double
    D_get_a_to_d_yconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 22
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_to_d_xconv'):
    D_get_u_to_d_xconv = _libs['grass_display.7.0.4'].D_get_u_to_d_xconv
    D_get_u_to_d_xconv.restype = c_double
    D_get_u_to_d_xconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 23
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_to_d_yconv'):
    D_get_u_to_d_yconv = _libs['grass_display.7.0.4'].D_get_u_to_d_yconv
    D_get_u_to_d_yconv.restype = c_double
    D_get_u_to_d_yconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 24
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_to_a_xconv'):
    D_get_u_to_a_xconv = _libs['grass_display.7.0.4'].D_get_u_to_a_xconv
    D_get_u_to_a_xconv.restype = c_double
    D_get_u_to_a_xconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 25
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_to_a_yconv'):
    D_get_u_to_a_yconv = _libs['grass_display.7.0.4'].D_get_u_to_a_yconv
    D_get_u_to_a_yconv.restype = c_double
    D_get_u_to_a_yconv.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 27
if hasattr(_libs['grass_display.7.0.4'], 'D_get_ns_resolution'):
    D_get_ns_resolution = _libs['grass_display.7.0.4'].D_get_ns_resolution
    D_get_ns_resolution.restype = c_double
    D_get_ns_resolution.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 28
if hasattr(_libs['grass_display.7.0.4'], 'D_get_ew_resolution'):
    D_get_ew_resolution = _libs['grass_display.7.0.4'].D_get_ew_resolution
    D_get_ew_resolution.restype = c_double
    D_get_ew_resolution.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 30
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_west'):
    D_get_u_west = _libs['grass_display.7.0.4'].D_get_u_west
    D_get_u_west.restype = c_double
    D_get_u_west.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 31
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_east'):
    D_get_u_east = _libs['grass_display.7.0.4'].D_get_u_east
    D_get_u_east.restype = c_double
    D_get_u_east.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 32
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_north'):
    D_get_u_north = _libs['grass_display.7.0.4'].D_get_u_north
    D_get_u_north.restype = c_double
    D_get_u_north.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 33
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u_south'):
    D_get_u_south = _libs['grass_display.7.0.4'].D_get_u_south
    D_get_u_south.restype = c_double
    D_get_u_south.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 34
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_west'):
    D_get_a_west = _libs['grass_display.7.0.4'].D_get_a_west
    D_get_a_west.restype = c_double
    D_get_a_west.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 35
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_east'):
    D_get_a_east = _libs['grass_display.7.0.4'].D_get_a_east
    D_get_a_east.restype = c_double
    D_get_a_east.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 36
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_north'):
    D_get_a_north = _libs['grass_display.7.0.4'].D_get_a_north
    D_get_a_north.restype = c_double
    D_get_a_north.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 37
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a_south'):
    D_get_a_south = _libs['grass_display.7.0.4'].D_get_a_south
    D_get_a_south.restype = c_double
    D_get_a_south.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 38
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_west'):
    D_get_d_west = _libs['grass_display.7.0.4'].D_get_d_west
    D_get_d_west.restype = c_double
    D_get_d_west.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 39
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_east'):
    D_get_d_east = _libs['grass_display.7.0.4'].D_get_d_east
    D_get_d_east.restype = c_double
    D_get_d_east.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 40
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_north'):
    D_get_d_north = _libs['grass_display.7.0.4'].D_get_d_north
    D_get_d_north.restype = c_double
    D_get_d_north.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 41
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d_south'):
    D_get_d_south = _libs['grass_display.7.0.4'].D_get_d_south
    D_get_d_south.restype = c_double
    D_get_d_south.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 43
if hasattr(_libs['grass_display.7.0.4'], 'D_set_region'):
    D_set_region = _libs['grass_display.7.0.4'].D_set_region
    D_set_region.restype = None
    D_set_region.argtypes = [POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 44
if hasattr(_libs['grass_display.7.0.4'], 'D_set_src'):
    D_set_src = _libs['grass_display.7.0.4'].D_set_src
    D_set_src.restype = None
    D_set_src.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 45
if hasattr(_libs['grass_display.7.0.4'], 'D_get_src'):
    D_get_src = _libs['grass_display.7.0.4'].D_get_src
    D_get_src.restype = None
    D_get_src.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 46
if hasattr(_libs['grass_display.7.0.4'], 'D_set_grid'):
    D_set_grid = _libs['grass_display.7.0.4'].D_set_grid
    D_set_grid.restype = None
    D_set_grid.argtypes = [c_int, c_int, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 47
if hasattr(_libs['grass_display.7.0.4'], 'D_get_grid'):
    D_get_grid = _libs['grass_display.7.0.4'].D_get_grid
    D_get_grid.restype = None
    D_get_grid.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 48
if hasattr(_libs['grass_display.7.0.4'], 'D_set_dst'):
    D_set_dst = _libs['grass_display.7.0.4'].D_set_dst
    D_set_dst.restype = None
    D_set_dst.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 49
if hasattr(_libs['grass_display.7.0.4'], 'D_get_dst'):
    D_get_dst = _libs['grass_display.7.0.4'].D_get_dst
    D_get_dst.restype = None
    D_get_dst.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 51
if hasattr(_libs['grass_display.7.0.4'], 'D_get_u'):
    D_get_u = _libs['grass_display.7.0.4'].D_get_u
    D_get_u.restype = None
    D_get_u.argtypes = [(c_double * 2) * 2]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 52
if hasattr(_libs['grass_display.7.0.4'], 'D_get_a'):
    D_get_a = _libs['grass_display.7.0.4'].D_get_a
    D_get_a.restype = None
    D_get_a.argtypes = [(c_int * 2) * 2]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 53
if hasattr(_libs['grass_display.7.0.4'], 'D_get_d'):
    D_get_d = _libs['grass_display.7.0.4'].D_get_d
    D_get_d.restype = None
    D_get_d.argtypes = [(c_double * 2) * 2]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 55
if hasattr(_libs['grass_display.7.0.4'], 'D_d_to_a_row'):
    D_d_to_a_row = _libs['grass_display.7.0.4'].D_d_to_a_row
    D_d_to_a_row.restype = c_double
    D_d_to_a_row.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 56
if hasattr(_libs['grass_display.7.0.4'], 'D_d_to_a_col'):
    D_d_to_a_col = _libs['grass_display.7.0.4'].D_d_to_a_col
    D_d_to_a_col.restype = c_double
    D_d_to_a_col.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 57
if hasattr(_libs['grass_display.7.0.4'], 'D_d_to_u_row'):
    D_d_to_u_row = _libs['grass_display.7.0.4'].D_d_to_u_row
    D_d_to_u_row.restype = c_double
    D_d_to_u_row.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 58
if hasattr(_libs['grass_display.7.0.4'], 'D_d_to_u_col'):
    D_d_to_u_col = _libs['grass_display.7.0.4'].D_d_to_u_col
    D_d_to_u_col.restype = c_double
    D_d_to_u_col.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 59
if hasattr(_libs['grass_display.7.0.4'], 'D_a_to_u_row'):
    D_a_to_u_row = _libs['grass_display.7.0.4'].D_a_to_u_row
    D_a_to_u_row.restype = c_double
    D_a_to_u_row.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 60
if hasattr(_libs['grass_display.7.0.4'], 'D_a_to_u_col'):
    D_a_to_u_col = _libs['grass_display.7.0.4'].D_a_to_u_col
    D_a_to_u_col.restype = c_double
    D_a_to_u_col.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 61
if hasattr(_libs['grass_display.7.0.4'], 'D_a_to_d_row'):
    D_a_to_d_row = _libs['grass_display.7.0.4'].D_a_to_d_row
    D_a_to_d_row.restype = c_double
    D_a_to_d_row.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 62
if hasattr(_libs['grass_display.7.0.4'], 'D_a_to_d_col'):
    D_a_to_d_col = _libs['grass_display.7.0.4'].D_a_to_d_col
    D_a_to_d_col.restype = c_double
    D_a_to_d_col.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 63
if hasattr(_libs['grass_display.7.0.4'], 'D_u_to_d_row'):
    D_u_to_d_row = _libs['grass_display.7.0.4'].D_u_to_d_row
    D_u_to_d_row.restype = c_double
    D_u_to_d_row.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 64
if hasattr(_libs['grass_display.7.0.4'], 'D_u_to_d_col'):
    D_u_to_d_col = _libs['grass_display.7.0.4'].D_u_to_d_col
    D_u_to_d_col.restype = c_double
    D_u_to_d_col.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 65
if hasattr(_libs['grass_display.7.0.4'], 'D_u_to_a_row'):
    D_u_to_a_row = _libs['grass_display.7.0.4'].D_u_to_a_row
    D_u_to_a_row.restype = c_double
    D_u_to_a_row.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 66
if hasattr(_libs['grass_display.7.0.4'], 'D_u_to_a_col'):
    D_u_to_a_col = _libs['grass_display.7.0.4'].D_u_to_a_col
    D_u_to_a_col.restype = c_double
    D_u_to_a_col.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 70
if hasattr(_libs['grass_display.7.0.4'], 'D_set_clip'):
    D_set_clip = _libs['grass_display.7.0.4'].D_set_clip
    D_set_clip.restype = None
    D_set_clip.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 71
if hasattr(_libs['grass_display.7.0.4'], 'D_clip_to_map'):
    D_clip_to_map = _libs['grass_display.7.0.4'].D_clip_to_map
    D_clip_to_map.restype = None
    D_clip_to_map.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 72
if hasattr(_libs['grass_display.7.0.4'], 'D_set_clip_mode'):
    D_set_clip_mode = _libs['grass_display.7.0.4'].D_set_clip_mode
    D_set_clip_mode.restype = None
    D_set_clip_mode.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 73
if hasattr(_libs['grass_display.7.0.4'], 'D_set_reduction'):
    D_set_reduction = _libs['grass_display.7.0.4'].D_set_reduction
    D_set_reduction.restype = None
    D_set_reduction.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 75
if hasattr(_libs['grass_display.7.0.4'], 'D_line_width'):
    D_line_width = _libs['grass_display.7.0.4'].D_line_width
    D_line_width.restype = None
    D_line_width.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 76
if hasattr(_libs['grass_display.7.0.4'], 'D_get_text_box'):
    D_get_text_box = _libs['grass_display.7.0.4'].D_get_text_box
    D_get_text_box.restype = None
    D_get_text_box.argtypes = [String, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 78
if hasattr(_libs['grass_display.7.0.4'], 'D_pos_abs'):
    D_pos_abs = _libs['grass_display.7.0.4'].D_pos_abs
    D_pos_abs.restype = None
    D_pos_abs.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 79
if hasattr(_libs['grass_display.7.0.4'], 'D_pos_rel'):
    D_pos_rel = _libs['grass_display.7.0.4'].D_pos_rel
    D_pos_rel.restype = None
    D_pos_rel.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 80
if hasattr(_libs['grass_display.7.0.4'], 'D_move_abs'):
    D_move_abs = _libs['grass_display.7.0.4'].D_move_abs
    D_move_abs.restype = None
    D_move_abs.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 81
if hasattr(_libs['grass_display.7.0.4'], 'D_move_rel'):
    D_move_rel = _libs['grass_display.7.0.4'].D_move_rel
    D_move_rel.restype = None
    D_move_rel.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 82
if hasattr(_libs['grass_display.7.0.4'], 'D_cont_abs'):
    D_cont_abs = _libs['grass_display.7.0.4'].D_cont_abs
    D_cont_abs.restype = None
    D_cont_abs.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 83
if hasattr(_libs['grass_display.7.0.4'], 'D_cont_rel'):
    D_cont_rel = _libs['grass_display.7.0.4'].D_cont_rel
    D_cont_rel.restype = None
    D_cont_rel.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 84
if hasattr(_libs['grass_display.7.0.4'], 'D_line_abs'):
    D_line_abs = _libs['grass_display.7.0.4'].D_line_abs
    D_line_abs.restype = None
    D_line_abs.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 85
if hasattr(_libs['grass_display.7.0.4'], 'D_line_rel'):
    D_line_rel = _libs['grass_display.7.0.4'].D_line_rel
    D_line_rel.restype = None
    D_line_rel.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 86
if hasattr(_libs['grass_display.7.0.4'], 'D_polydots_abs'):
    D_polydots_abs = _libs['grass_display.7.0.4'].D_polydots_abs
    D_polydots_abs.restype = None
    D_polydots_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 87
if hasattr(_libs['grass_display.7.0.4'], 'D_polydots_rel'):
    D_polydots_rel = _libs['grass_display.7.0.4'].D_polydots_rel
    D_polydots_rel.restype = None
    D_polydots_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 88
if hasattr(_libs['grass_display.7.0.4'], 'D_polyline_abs'):
    D_polyline_abs = _libs['grass_display.7.0.4'].D_polyline_abs
    D_polyline_abs.restype = None
    D_polyline_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 89
if hasattr(_libs['grass_display.7.0.4'], 'D_polyline_rel'):
    D_polyline_rel = _libs['grass_display.7.0.4'].D_polyline_rel
    D_polyline_rel.restype = None
    D_polyline_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 90
if hasattr(_libs['grass_display.7.0.4'], 'D_polygon_abs'):
    D_polygon_abs = _libs['grass_display.7.0.4'].D_polygon_abs
    D_polygon_abs.restype = None
    D_polygon_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 91
if hasattr(_libs['grass_display.7.0.4'], 'D_polygon_rel'):
    D_polygon_rel = _libs['grass_display.7.0.4'].D_polygon_rel
    D_polygon_rel.restype = None
    D_polygon_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 92
if hasattr(_libs['grass_display.7.0.4'], 'D_box_abs'):
    D_box_abs = _libs['grass_display.7.0.4'].D_box_abs
    D_box_abs.restype = None
    D_box_abs.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 93
if hasattr(_libs['grass_display.7.0.4'], 'D_box_rel'):
    D_box_rel = _libs['grass_display.7.0.4'].D_box_rel
    D_box_rel.restype = None
    D_box_rel.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 95
if hasattr(_libs['grass_display.7.0.4'], 'D_begin'):
    D_begin = _libs['grass_display.7.0.4'].D_begin
    D_begin.restype = None
    D_begin.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 96
if hasattr(_libs['grass_display.7.0.4'], 'D_end'):
    D_end = _libs['grass_display.7.0.4'].D_end
    D_end.restype = None
    D_end.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 97
if hasattr(_libs['grass_display.7.0.4'], 'D_close'):
    D_close = _libs['grass_display.7.0.4'].D_close
    D_close.restype = None
    D_close.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 98
if hasattr(_libs['grass_display.7.0.4'], 'D_stroke'):
    D_stroke = _libs['grass_display.7.0.4'].D_stroke
    D_stroke.restype = None
    D_stroke.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 99
if hasattr(_libs['grass_display.7.0.4'], 'D_fill'):
    D_fill = _libs['grass_display.7.0.4'].D_fill
    D_fill.restype = None
    D_fill.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 100
if hasattr(_libs['grass_display.7.0.4'], 'D_dots'):
    D_dots = _libs['grass_display.7.0.4'].D_dots
    D_dots.restype = None
    D_dots.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 103
if hasattr(_libs['grass_display.7.0.4'], 'D_plot_icon'):
    D_plot_icon = _libs['grass_display.7.0.4'].D_plot_icon
    D_plot_icon.restype = None
    D_plot_icon.argtypes = [c_double, c_double, c_int, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 106
if hasattr(_libs['grass_display.7.0.4'], 'D_draw_raster'):
    D_draw_raster = _libs['grass_display.7.0.4'].D_draw_raster
    D_draw_raster.restype = c_int
    D_draw_raster.argtypes = [c_int, POINTER(None), POINTER(struct_Colors), RASTER_MAP_TYPE]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 107
if hasattr(_libs['grass_display.7.0.4'], 'D_draw_d_raster'):
    D_draw_d_raster = _libs['grass_display.7.0.4'].D_draw_d_raster
    D_draw_d_raster.restype = c_int
    D_draw_d_raster.argtypes = [c_int, POINTER(DCELL), POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 108
if hasattr(_libs['grass_display.7.0.4'], 'D_draw_f_raster'):
    D_draw_f_raster = _libs['grass_display.7.0.4'].D_draw_f_raster
    D_draw_f_raster.restype = c_int
    D_draw_f_raster.argtypes = [c_int, POINTER(FCELL), POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 109
if hasattr(_libs['grass_display.7.0.4'], 'D_draw_c_raster'):
    D_draw_c_raster = _libs['grass_display.7.0.4'].D_draw_c_raster
    D_draw_c_raster.restype = c_int
    D_draw_c_raster.argtypes = [c_int, POINTER(CELL), POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 110
if hasattr(_libs['grass_display.7.0.4'], 'D_raster_draw_begin'):
    D_raster_draw_begin = _libs['grass_display.7.0.4'].D_raster_draw_begin
    D_raster_draw_begin.restype = None
    D_raster_draw_begin.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 111
if hasattr(_libs['grass_display.7.0.4'], 'D_draw_raster_RGB'):
    D_draw_raster_RGB = _libs['grass_display.7.0.4'].D_draw_raster_RGB
    D_draw_raster_RGB.restype = c_int
    D_draw_raster_RGB.argtypes = [c_int, POINTER(None), POINTER(None), POINTER(None), POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_Colors), RASTER_MAP_TYPE, RASTER_MAP_TYPE, RASTER_MAP_TYPE]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 114
if hasattr(_libs['grass_display.7.0.4'], 'D_raster_draw_end'):
    D_raster_draw_end = _libs['grass_display.7.0.4'].D_raster_draw_end
    D_raster_draw_end.restype = None
    D_raster_draw_end.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 117
if hasattr(_libs['grass_display.7.0.4'], 'D_set_overlay_mode'):
    D_set_overlay_mode = _libs['grass_display.7.0.4'].D_set_overlay_mode
    D_set_overlay_mode.restype = c_int
    D_set_overlay_mode.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 118
if hasattr(_libs['grass_display.7.0.4'], 'D_color'):
    D_color = _libs['grass_display.7.0.4'].D_color
    D_color.restype = c_int
    D_color.argtypes = [CELL, POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 119
if hasattr(_libs['grass_display.7.0.4'], 'D_c_color'):
    D_c_color = _libs['grass_display.7.0.4'].D_c_color
    D_c_color.restype = c_int
    D_c_color.argtypes = [CELL, POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 120
if hasattr(_libs['grass_display.7.0.4'], 'D_d_color'):
    D_d_color = _libs['grass_display.7.0.4'].D_d_color
    D_d_color.restype = c_int
    D_d_color.argtypes = [DCELL, POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 121
if hasattr(_libs['grass_display.7.0.4'], 'D_f_color'):
    D_f_color = _libs['grass_display.7.0.4'].D_f_color
    D_f_color.restype = c_int
    D_f_color.argtypes = [FCELL, POINTER(struct_Colors)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 122
if hasattr(_libs['grass_display.7.0.4'], 'D_color_of_type'):
    D_color_of_type = _libs['grass_display.7.0.4'].D_color_of_type
    D_color_of_type.restype = c_int
    D_color_of_type.argtypes = [POINTER(None), POINTER(struct_Colors), RASTER_MAP_TYPE]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 125
if hasattr(_libs['grass_display.7.0.4'], 'D_setup'):
    D_setup = _libs['grass_display.7.0.4'].D_setup
    D_setup.restype = None
    D_setup.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 126
if hasattr(_libs['grass_display.7.0.4'], 'D_setup_unity'):
    D_setup_unity = _libs['grass_display.7.0.4'].D_setup_unity
    D_setup_unity.restype = None
    D_setup_unity.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 127
if hasattr(_libs['grass_display.7.0.4'], 'D_setup2'):
    D_setup2 = _libs['grass_display.7.0.4'].D_setup2
    D_setup2.restype = None
    D_setup2.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 130
if hasattr(_libs['grass_display.7.0.4'], 'D_symbol'):
    D_symbol = _libs['grass_display.7.0.4'].D_symbol
    D_symbol.restype = None
    D_symbol.argtypes = [POINTER(SYMBOL), c_double, c_double, POINTER(RGBA_Color), POINTER(RGBA_Color)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 132
if hasattr(_libs['grass_display.7.0.4'], 'D_symbol2'):
    D_symbol2 = _libs['grass_display.7.0.4'].D_symbol2
    D_symbol2.restype = None
    D_symbol2.argtypes = [POINTER(SYMBOL), c_double, c_double, POINTER(RGBA_Color), POINTER(RGBA_Color)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 136
if hasattr(_libs['grass_display.7.0.4'], 'D_translate_color'):
    D_translate_color = _libs['grass_display.7.0.4'].D_translate_color
    D_translate_color.restype = c_int
    D_translate_color.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 137
if hasattr(_libs['grass_display.7.0.4'], 'D_parse_color'):
    D_parse_color = _libs['grass_display.7.0.4'].D_parse_color
    D_parse_color.restype = c_int
    D_parse_color.argtypes = [String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 138
if hasattr(_libs['grass_display.7.0.4'], 'D_use_color'):
    D_use_color = _libs['grass_display.7.0.4'].D_use_color
    D_use_color.restype = c_int
    D_use_color.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 139
if hasattr(_libs['grass_display.7.0.4'], 'D_color_number_to_RGB'):
    D_color_number_to_RGB = _libs['grass_display.7.0.4'].D_color_number_to_RGB
    D_color_number_to_RGB.restype = c_int
    D_color_number_to_RGB.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 140
if hasattr(_libs['grass_display.7.0.4'], 'D_RGB_color'):
    D_RGB_color = _libs['grass_display.7.0.4'].D_RGB_color
    D_RGB_color.restype = None
    D_RGB_color.argtypes = [c_int, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 143
if hasattr(_libs['grass_display.7.0.4'], 'D_erase'):
    D_erase = _libs['grass_display.7.0.4'].D_erase
    D_erase.restype = None
    D_erase.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 147
if hasattr(_libs['grass_display.7.0.4'], 'D_open_driver'):
    D_open_driver = _libs['grass_display.7.0.4'].D_open_driver
    D_open_driver.restype = c_int
    D_open_driver.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 148
if hasattr(_libs['grass_display.7.0.4'], 'D_close_driver'):
    D_close_driver = _libs['grass_display.7.0.4'].D_close_driver
    D_close_driver.restype = None
    D_close_driver.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 149
if hasattr(_libs['grass_display.7.0.4'], 'D_save_command'):
    D_save_command = _libs['grass_display.7.0.4'].D_save_command
    D_save_command.restype = c_int
    D_save_command.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 151
if hasattr(_libs['grass_display.7.0.4'], 'D__erase'):
    D__erase = _libs['grass_display.7.0.4'].D__erase
    D__erase.restype = None
    D__erase.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 153
if hasattr(_libs['grass_display.7.0.4'], 'D_text_size'):
    D_text_size = _libs['grass_display.7.0.4'].D_text_size
    D_text_size.restype = None
    D_text_size.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 154
if hasattr(_libs['grass_display.7.0.4'], 'D_text_rotation'):
    D_text_rotation = _libs['grass_display.7.0.4'].D_text_rotation
    D_text_rotation.restype = None
    D_text_rotation.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 155
if hasattr(_libs['grass_display.7.0.4'], 'D_text'):
    D_text = _libs['grass_display.7.0.4'].D_text
    D_text.restype = None
    D_text.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 157
if hasattr(_libs['grass_display.7.0.4'], 'D_font'):
    D_font = _libs['grass_display.7.0.4'].D_font
    D_font.restype = None
    D_font.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 158
if hasattr(_libs['grass_display.7.0.4'], 'D_encoding'):
    D_encoding = _libs['grass_display.7.0.4'].D_encoding
    D_encoding.restype = None
    D_encoding.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 159
if hasattr(_libs['grass_display.7.0.4'], 'D_font_list'):
    D_font_list = _libs['grass_display.7.0.4'].D_font_list
    D_font_list.restype = None
    D_font_list.argtypes = [POINTER(POINTER(POINTER(c_char))), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 160
if hasattr(_libs['grass_display.7.0.4'], 'D_font_info'):
    D_font_info = _libs['grass_display.7.0.4'].D_font_info
    D_font_info.restype = None
    D_font_info.argtypes = [POINTER(POINTER(POINTER(c_char))), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 162
if hasattr(_libs['grass_display.7.0.4'], 'D_get_clip_window'):
    D_get_clip_window = _libs['grass_display.7.0.4'].D_get_clip_window
    D_get_clip_window.restype = None
    D_get_clip_window.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 163
if hasattr(_libs['grass_display.7.0.4'], 'D_set_clip_window'):
    D_set_clip_window = _libs['grass_display.7.0.4'].D_set_clip_window
    D_set_clip_window.restype = None
    D_set_clip_window.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 164
if hasattr(_libs['grass_display.7.0.4'], 'D_get_frame'):
    D_get_frame = _libs['grass_display.7.0.4'].D_get_frame
    D_get_frame.restype = None
    D_get_frame.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 165
if hasattr(_libs['grass_display.7.0.4'], 'D_get_screen'):
    D_get_screen = _libs['grass_display.7.0.4'].D_get_screen
    D_get_screen.restype = None
    D_get_screen.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 166
if hasattr(_libs['grass_display.7.0.4'], 'D_set_clip_window_to_map_window'):
    D_set_clip_window_to_map_window = _libs['grass_display.7.0.4'].D_set_clip_window_to_map_window
    D_set_clip_window_to_map_window.restype = None
    D_set_clip_window_to_map_window.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 167
if hasattr(_libs['grass_display.7.0.4'], 'D_set_clip_window_to_screen_window'):
    D_set_clip_window_to_screen_window = _libs['grass_display.7.0.4'].D_set_clip_window_to_screen_window
    D_set_clip_window_to_screen_window.restype = None
    D_set_clip_window_to_screen_window.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/display.h: 169
if hasattr(_libs['grass_display.7.0.4'], 'D_get_file'):
    D_get_file = _libs['grass_display.7.0.4'].D_get_file
    D_get_file.restype = ReturnString
    D_get_file.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 16
try:
    RGBA_COLOR_OPAQUE = 255
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 16
try:
    RGBA_COLOR_TRANSPARENT = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 16
try:
    RGBA_COLOR_NONE = 0
except:
    pass

color_rgba = struct_color_rgba # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/display.h: 8

# No inserted files
