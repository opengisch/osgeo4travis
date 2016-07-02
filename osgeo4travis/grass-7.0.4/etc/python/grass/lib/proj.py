'''Wrapper for gprojects.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gproj.7.0.4 -I/home/travis/osgeo4travis/include/ -I/home/travis/osgeo4travis/include /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h -o OBJ.x86_64-pc-linux-gnu/proj.py

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

_libs["grass_gproj.7.0.4"] = load_library("grass_gproj.7.0.4")

# 1 libraries
# End libraries

# No modules

projPJ = POINTER(None) # /home/travis/osgeo4travis/include/proj_api.h: 57

OGRSpatialReferenceH = POINTER(None) # /home/travis/osgeo4travis/include/ogr_srs_api.h: 312

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 33
class struct_pj_info(Structure):
    pass

struct_pj_info.__slots__ = [
    'pj',
    'meters',
    'zone',
    'proj',
]
struct_pj_info._fields_ = [
    ('pj', projPJ),
    ('meters', c_double),
    ('zone', c_int),
    ('proj', c_char * 100),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 41
class struct_gpj_datum(Structure):
    pass

struct_gpj_datum.__slots__ = [
    'name',
    'longname',
    'ellps',
    'dx',
    'dy',
    'dz',
]
struct_gpj_datum._fields_ = [
    ('name', String),
    ('longname', String),
    ('ellps', String),
    ('dx', c_double),
    ('dy', c_double),
    ('dz', c_double),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 47
class struct_gpj_datum_transform_list(Structure):
    pass

struct_gpj_datum_transform_list.__slots__ = [
    'count',
    'params',
    'where_used',
    'comment',
    'next',
]
struct_gpj_datum_transform_list._fields_ = [
    ('count', c_int),
    ('params', String),
    ('where_used', String),
    ('comment', String),
    ('next', POINTER(struct_gpj_datum_transform_list)),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 63
class struct_gpj_ellps(Structure):
    pass

struct_gpj_ellps.__slots__ = [
    'name',
    'longname',
    'a',
    'es',
    'rf',
]
struct_gpj_ellps._fields_ = [
    ('name', String),
    ('longname', String),
    ('a', c_double),
    ('es', c_double),
    ('rf', c_double),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 73
class struct_anon_50(Structure):
    pass

struct_anon_50.__slots__ = [
    'u',
    'v',
]
struct_anon_50._fields_ = [
    ('u', c_double),
    ('v', c_double),
]

LP = struct_anon_50 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 73

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 75
class struct_DERIVS(Structure):
    pass

struct_DERIVS.__slots__ = [
    'x_l',
    'x_p',
    'y_l',
    'y_p',
]
struct_DERIVS._fields_ = [
    ('x_l', c_double),
    ('x_p', c_double),
    ('y_l', c_double),
    ('y_p', c_double),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 80
class struct_FACTORS(Structure):
    pass

struct_FACTORS.__slots__ = [
    'der',
    'h',
    'k',
    'omega',
    'thetap',
    'conv',
    's',
    'a',
    'b',
    'code',
]
struct_FACTORS._fields_ = [
    ('der', struct_DERIVS),
    ('h', c_double),
    ('k', c_double),
    ('omega', c_double),
    ('thetap', c_double),
    ('conv', c_double),
    ('s', c_double),
    ('a', c_double),
    ('b', c_double),
    ('code', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 5
if hasattr(_libs['grass_gproj.7.0.4'], 'pj_do_proj'):
    pj_do_proj = _libs['grass_gproj.7.0.4'].pj_do_proj
    pj_do_proj.restype = c_int
    pj_do_proj.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 6
if hasattr(_libs['grass_gproj.7.0.4'], 'pj_do_transform'):
    pj_do_transform = _libs['grass_gproj.7.0.4'].pj_do_transform
    pj_do_transform.restype = c_int
    pj_do_transform.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 10
class struct_Key_Value(Structure):
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 10
if hasattr(_libs['grass_gproj.7.0.4'], 'pj_get_kv'):
    pj_get_kv = _libs['grass_gproj.7.0.4'].pj_get_kv
    pj_get_kv.restype = c_int
    pj_get_kv.argtypes = [POINTER(struct_pj_info), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 11
if hasattr(_libs['grass_gproj.7.0.4'], 'pj_get_string'):
    pj_get_string = _libs['grass_gproj.7.0.4'].pj_get_string
    pj_get_string.restype = c_int
    pj_get_string.argtypes = [POINTER(struct_pj_info), String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 12
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_equivalent_latlong'):
    GPJ_get_equivalent_latlong = _libs['grass_gproj.7.0.4'].GPJ_get_equivalent_latlong
    GPJ_get_equivalent_latlong.restype = c_int
    GPJ_get_equivalent_latlong.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 13
if hasattr(_libs['grass_gproj.7.0.4'], 'set_proj_lib'):
    set_proj_lib = _libs['grass_gproj.7.0.4'].set_proj_lib
    set_proj_lib.restype = ReturnString
    set_proj_lib.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 14
if hasattr(_libs['grass_gproj.7.0.4'], 'pj_print_proj_params'):
    pj_print_proj_params = _libs['grass_gproj.7.0.4'].pj_print_proj_params
    pj_print_proj_params.restype = c_int
    pj_print_proj_params.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 17
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_grass_to_wkt'):
    GPJ_grass_to_wkt = _libs['grass_gproj.7.0.4'].GPJ_grass_to_wkt
    GPJ_grass_to_wkt.restype = ReturnString
    GPJ_grass_to_wkt.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 19
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_grass_to_osr'):
    GPJ_grass_to_osr = _libs['grass_gproj.7.0.4'].GPJ_grass_to_osr
    GPJ_grass_to_osr.restype = OGRSpatialReferenceH
    GPJ_grass_to_osr.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 20
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_set_csv_loc'):
    GPJ_set_csv_loc = _libs['grass_gproj.7.0.4'].GPJ_set_csv_loc
    GPJ_set_csv_loc.restype = ReturnString
    GPJ_set_csv_loc.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 21
class struct_Cell_head(Structure):
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 21
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_osr_to_grass'):
    GPJ_osr_to_grass = _libs['grass_gproj.7.0.4'].GPJ_osr_to_grass
    GPJ_osr_to_grass.restype = c_int
    GPJ_osr_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), OGRSpatialReferenceH, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 24
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_wkt_to_grass'):
    GPJ_wkt_to_grass = _libs['grass_gproj.7.0.4'].GPJ_wkt_to_grass
    GPJ_wkt_to_grass.restype = c_int
    GPJ_wkt_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 28
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_datum_by_name'):
    GPJ_get_datum_by_name = _libs['grass_gproj.7.0.4'].GPJ_get_datum_by_name
    GPJ_get_datum_by_name.restype = c_int
    GPJ_get_datum_by_name.argtypes = [String, POINTER(struct_gpj_datum)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 29
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_default_datum_params_by_name'):
    GPJ_get_default_datum_params_by_name = _libs['grass_gproj.7.0.4'].GPJ_get_default_datum_params_by_name
    GPJ_get_default_datum_params_by_name.restype = c_int
    GPJ_get_default_datum_params_by_name.argtypes = [String, POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 30
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_datum_params'):
    GPJ_get_datum_params = _libs['grass_gproj.7.0.4'].GPJ_get_datum_params
    GPJ_get_datum_params.restype = c_int
    GPJ_get_datum_params.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 31
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ__get_datum_params'):
    GPJ__get_datum_params = _libs['grass_gproj.7.0.4'].GPJ__get_datum_params
    GPJ__get_datum_params.restype = c_int
    GPJ__get_datum_params.argtypes = [POINTER(struct_Key_Value), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 32
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_free_datum'):
    GPJ_free_datum = _libs['grass_gproj.7.0.4'].GPJ_free_datum
    GPJ_free_datum.restype = None
    GPJ_free_datum.argtypes = [POINTER(struct_gpj_datum)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 33
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_datum_transform_by_name'):
    GPJ_get_datum_transform_by_name = _libs['grass_gproj.7.0.4'].GPJ_get_datum_transform_by_name
    GPJ_get_datum_transform_by_name.restype = POINTER(struct_gpj_datum_transform_list)
    GPJ_get_datum_transform_by_name.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 34
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_free_datum_transform'):
    GPJ_free_datum_transform = _libs['grass_gproj.7.0.4'].GPJ_free_datum_transform
    GPJ_free_datum_transform.restype = None
    GPJ_free_datum_transform.argtypes = [POINTER(struct_gpj_datum_transform_list)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 37
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_ellipsoid_by_name'):
    GPJ_get_ellipsoid_by_name = _libs['grass_gproj.7.0.4'].GPJ_get_ellipsoid_by_name
    GPJ_get_ellipsoid_by_name.restype = c_int
    GPJ_get_ellipsoid_by_name.argtypes = [String, POINTER(struct_gpj_ellps)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 38
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_get_ellipsoid_params'):
    GPJ_get_ellipsoid_params = _libs['grass_gproj.7.0.4'].GPJ_get_ellipsoid_params
    GPJ_get_ellipsoid_params.restype = c_int
    GPJ_get_ellipsoid_params.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 39
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ__get_ellipsoid_params'):
    GPJ__get_ellipsoid_params = _libs['grass_gproj.7.0.4'].GPJ__get_ellipsoid_params
    GPJ__get_ellipsoid_params.restype = c_int
    GPJ__get_ellipsoid_params.argtypes = [POINTER(struct_Key_Value), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 41
if hasattr(_libs['grass_gproj.7.0.4'], 'GPJ_free_ellps'):
    GPJ_free_ellps = _libs['grass_gproj.7.0.4'].GPJ_free_ellps
    GPJ_free_ellps.restype = None
    GPJ_free_ellps.argtypes = [POINTER(struct_gpj_ellps)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 48
if hasattr(_libs['grass_gproj.7.0.4'], 'pj_factors'):
    pj_factors = _libs['grass_gproj.7.0.4'].pj_factors
    pj_factors.restype = c_int
    pj_factors.argtypes = [LP, POINTER(None), c_double, POINTER(struct_FACTORS)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 27
try:
    ELLIPSOIDTABLE = '/etc/proj/ellipse.table'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 27
try:
    DATUMTABLE = '/etc/proj/datum.table'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 27
try:
    DATUMTRANSFORMTABLE = '/etc/proj/datumtransform.table'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 28
try:
    GRIDDIR = '/etc/proj/nad'
except:
    pass

pj_info = struct_pj_info # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 33

gpj_datum = struct_gpj_datum # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 41

gpj_datum_transform_list = struct_gpj_datum_transform_list # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 47

gpj_ellps = struct_gpj_ellps # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 63

DERIVS = struct_DERIVS # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 75

FACTORS = struct_FACTORS # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gprojects.h: 80

Key_Value = struct_Key_Value # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 10

Cell_head = struct_Cell_head # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gprojects.h: 21

# No inserted files

