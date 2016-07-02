'''Wrapper for gis.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gis.7.0.4 /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h -o OBJ.x86_64-pc-linux-gnu/gis.py

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

_libs["grass_gis.7.0.4"] = load_library("grass_gis.7.0.4")

# 1 libraries
# End libraries

# No modules

__dev_t = c_ulong # /usr/include/x86_64-linux-gnu/bits/types.h: 134

__uid_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 135

__gid_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 136

__ino_t = c_ulong # /usr/include/x86_64-linux-gnu/bits/types.h: 137

__mode_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 139

__nlink_t = c_ulong # /usr/include/x86_64-linux-gnu/bits/types.h: 140

__off_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 141

__off64_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 142

__time_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 149

__blksize_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 164

__blkcnt_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 169

# /usr/include/libio.h: 273
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 49

_IO_lock_t = None # /usr/include/libio.h: 182

# /usr/include/libio.h: 188
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

off_t = __off_t # /usr/include/stdio.h: 91

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 27
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'mode',
    '_from',
    'to',
    'fracsec',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'positive',
    'tz',
]
struct_DateTime._fields_ = [
    ('mode', c_int),
    ('_from', c_int),
    ('to', c_int),
    ('fracsec', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('second', c_double),
    ('positive', c_int),
    ('tz', c_int),
]

DateTime = struct_DateTime # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 27

enum_anon_6 = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_UNDEFINED = 0 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_SQL = (G_OPT_UNDEFINED + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_WHERE = (G_OPT_DB_SQL + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_TABLE = (G_OPT_DB_WHERE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_DRIVER = (G_OPT_DB_TABLE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_DATABASE = (G_OPT_DB_DRIVER + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_SCHEMA = (G_OPT_DB_DATABASE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_COLUMN = (G_OPT_DB_SCHEMA + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_COLUMNS = (G_OPT_DB_COLUMN + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_DB_KEYCOLUMN = (G_OPT_DB_COLUMNS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_I_GROUP = (G_OPT_DB_KEYCOLUMN + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_I_SUBGROUP = (G_OPT_I_GROUP + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_INPUT = (G_OPT_I_SUBGROUP + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_INPUTS = (G_OPT_R_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_OUTPUT = (G_OPT_R_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_OUTPUTS = (G_OPT_R_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_MAP = (G_OPT_R_OUTPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_MAPS = (G_OPT_R_MAP + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_BASE = (G_OPT_R_MAPS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_COVER = (G_OPT_R_BASE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_ELEV = (G_OPT_R_COVER + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_ELEVS = (G_OPT_R_ELEV + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_INTERP_TYPE = (G_OPT_R_ELEVS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_BASENAME_INPUT = (G_OPT_R_INTERP_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R_BASENAME_OUTPUT = (G_OPT_R_BASENAME_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_INPUT = (G_OPT_R_BASENAME_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_INPUTS = (G_OPT_R3_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_OUTPUT = (G_OPT_R3_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_MAP = (G_OPT_R3_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_MAPS = (G_OPT_R3_MAP + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_TYPE = (G_OPT_R3_MAPS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_PRECISION = (G_OPT_R3_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_TILE_DIMENSION = (G_OPT_R3_PRECISION + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_R3_COMPRESSION = (G_OPT_R3_TILE_DIMENSION + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_INPUT = (G_OPT_R3_COMPRESSION + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_INPUTS = (G_OPT_V_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_OUTPUT = (G_OPT_V_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_MAP = (G_OPT_V_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_MAPS = (G_OPT_V_MAP + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_TYPE = (G_OPT_V_MAPS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V3_TYPE = (G_OPT_V_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_FIELD = (G_OPT_V3_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_FIELD_ALL = (G_OPT_V_FIELD + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_CAT = (G_OPT_V_FIELD_ALL + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_CATS = (G_OPT_V_CAT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_ID = (G_OPT_V_CATS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_V_IDS = (G_OPT_V_ID + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_F_INPUT = (G_OPT_V_IDS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_F_BIN_INPUT = (G_OPT_F_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_F_OUTPUT = (G_OPT_F_BIN_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_F_SEP = (G_OPT_F_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_C = (G_OPT_F_SEP + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_CN = (G_OPT_C + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_UNITS = (G_OPT_CN + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_DATATYPE = (G_OPT_M_UNITS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_MAPSET = (G_OPT_M_DATATYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_LOCATION = (G_OPT_M_MAPSET + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_DBASE = (G_OPT_M_LOCATION + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_COORDS = (G_OPT_M_DBASE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_COLR = (G_OPT_M_COORDS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_DIR = (G_OPT_M_COLR + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_REGION = (G_OPT_M_DIR + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_M_NULL_VALUE = (G_OPT_M_REGION + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STDS_INPUT = (G_OPT_M_NULL_VALUE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STDS_INPUTS = (G_OPT_STDS_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STDS_OUTPUT = (G_OPT_STDS_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STRDS_INPUT = (G_OPT_STDS_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STRDS_INPUTS = (G_OPT_STRDS_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STRDS_OUTPUT = (G_OPT_STRDS_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STR3DS_INPUT = (G_OPT_STRDS_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STR3DS_INPUTS = (G_OPT_STR3DS_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STR3DS_OUTPUT = (G_OPT_STR3DS_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STVDS_INPUT = (G_OPT_STR3DS_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STVDS_INPUTS = (G_OPT_STVDS_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STVDS_OUTPUT = (G_OPT_STVDS_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_MAP_INPUT = (G_OPT_STVDS_OUTPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_MAP_INPUTS = (G_OPT_MAP_INPUT + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_STDS_TYPE = (G_OPT_MAP_INPUTS + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_MAP_TYPE = (G_OPT_STDS_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_T_TYPE = (G_OPT_MAP_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_T_WHERE = (G_OPT_T_TYPE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

G_OPT_T_SAMPLE = (G_OPT_T_WHERE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

STD_OPT = enum_anon_6 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 301

enum_anon_7 = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 317

G_FLG_UNDEFINED = 0 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 317

G_FLG_V_TABLE = (G_FLG_UNDEFINED + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 317

G_FLG_V_TOPO = (G_FLG_V_TABLE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 317

STD_FLG = enum_anon_7 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 317

enum_rule_type = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

RULE_EXCLUSIVE = 0 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

RULE_REQUIRED = (RULE_EXCLUSIVE + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

RULE_REQUIRES = (RULE_REQUIRED + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

RULE_REQUIRES_ALL = (RULE_REQUIRES + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

RULE_EXCLUDES = (RULE_REQUIRES_ALL + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

RULE_COLLECTIVE = (RULE_EXCLUDES + 1) # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 320

enum_anon_8 = c_int # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_RASTER = 1 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_RASTER3D = 2 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_VECTOR = 3 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_ASCIIVECTOR = 4 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_LABEL = 5 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_REGION = 6 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

G_ELEMENT_GROUP = 7 # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 366

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

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 444
class struct_G_3dview(Structure):
    pass

struct_G_3dview.__slots__ = [
    'pgm_id',
    'from_to',
    'fov',
    'twist',
    'exag',
    'mesh_freq',
    'poly_freq',
    'display_type',
    'lightson',
    'dozero',
    'colorgrid',
    'shading',
    'fringe',
    'surfonly',
    'doavg',
    'grid_col',
    'bg_col',
    'other_col',
    'lightpos',
    'lightcol',
    'ambient',
    'shine',
    'vwin',
]
struct_G_3dview._fields_ = [
    ('pgm_id', c_char * 40),
    ('from_to', (c_float * 3) * 2),
    ('fov', c_float),
    ('twist', c_float),
    ('exag', c_float),
    ('mesh_freq', c_int),
    ('poly_freq', c_int),
    ('display_type', c_int),
    ('lightson', c_int),
    ('dozero', c_int),
    ('colorgrid', c_int),
    ('shading', c_int),
    ('fringe', c_int),
    ('surfonly', c_int),
    ('doavg', c_int),
    ('grid_col', c_char * 40),
    ('bg_col', c_char * 40),
    ('other_col', c_char * 40),
    ('lightpos', c_float * 4),
    ('lightcol', c_float * 3),
    ('ambient', c_float),
    ('shine', c_float),
    ('vwin', struct_Cell_head),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 471
class struct_Key_Value(Structure):
    pass

struct_Key_Value.__slots__ = [
    'nitems',
    'nalloc',
    'key',
    'value',
]
struct_Key_Value._fields_ = [
    ('nitems', c_int),
    ('nalloc', c_int),
    ('key', POINTER(POINTER(c_char))),
    ('value', POINTER(POINTER(c_char))),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 501
class struct_Option(Structure):
    pass

struct_Option.__slots__ = [
    'key',
    'type',
    'required',
    'multiple',
    'options',
    'opts',
    'key_desc',
    'label',
    'description',
    'descriptions',
    'descs',
    'answer',
    '_def',
    'answers',
    'next_opt',
    'gisprompt',
    'guisection',
    'guidependency',
    'checker',
    'count',
]
struct_Option._fields_ = [
    ('key', String),
    ('type', c_int),
    ('required', c_int),
    ('multiple', c_int),
    ('options', String),
    ('opts', POINTER(POINTER(c_char))),
    ('key_desc', String),
    ('label', String),
    ('description', String),
    ('descriptions', String),
    ('descs', POINTER(POINTER(c_char))),
    ('answer', String),
    ('_def', String),
    ('answers', POINTER(POINTER(c_char))),
    ('next_opt', POINTER(struct_Option)),
    ('gisprompt', String),
    ('guisection', String),
    ('guidependency', String),
    ('checker', CFUNCTYPE(UNCHECKED(c_int), String)),
    ('count', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 530
class struct_Flag(Structure):
    pass

struct_Flag.__slots__ = [
    'key',
    'answer',
    'suppress_required',
    'label',
    'description',
    'guisection',
    'next_flag',
]
struct_Flag._fields_ = [
    ('key', c_char),
    ('answer', c_char),
    ('suppress_required', c_char),
    ('label', String),
    ('description', String),
    ('guisection', String),
    ('next_flag', POINTER(struct_Flag)),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 546
class struct_GModule(Structure):
    pass

struct_GModule.__slots__ = [
    'label',
    'description',
    'keywords',
    'overwrite',
    'verbose',
]
struct_GModule._fields_ = [
    ('label', String),
    ('description', String),
    ('keywords', POINTER(POINTER(c_char))),
    ('overwrite', c_int),
    ('verbose', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 556
class struct_TimeStamp(Structure):
    pass

struct_TimeStamp.__slots__ = [
    'dt',
    'count',
]
struct_TimeStamp._fields_ = [
    ('dt', DateTime * 2),
    ('count', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 562
class struct_Counter(Structure):
    pass

struct_Counter.__slots__ = [
    'value',
]
struct_Counter._fields_ = [
    ('value', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 566
class struct_Popen(Structure):
    pass

struct_Popen.__slots__ = [
    'fp',
    'pid',
]
struct_Popen._fields_ = [
    ('fp', POINTER(FILE)),
    ('pid', c_int),
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

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 641
class struct_ilist(Structure):
    pass

struct_ilist.__slots__ = [
    'value',
    'n_values',
    'alloc_values',
]
struct_ilist._fields_ = [
    ('value', POINTER(c_int)),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

__jmp_buf = c_long * 8 # /usr/include/x86_64-linux-gnu/bits/setjmp.h: 32

# /usr/include/x86_64-linux-gnu/bits/sigset.h: 32
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    '__val',
]
struct_anon_11._fields_ = [
    ('__val', c_ulong * (1024 / (8 * sizeof(c_ulong)))),
]

__sigset_t = struct_anon_11 # /usr/include/x86_64-linux-gnu/bits/sigset.h: 32

# /usr/include/setjmp.h: 35
class struct___jmp_buf_tag(Structure):
    pass

struct___jmp_buf_tag.__slots__ = [
    '__jmpbuf',
    '__mask_was_saved',
    '__saved_mask',
]
struct___jmp_buf_tag._fields_ = [
    ('__jmpbuf', __jmp_buf),
    ('__mask_was_saved', c_int),
    ('__saved_mask', __sigset_t),
]

jmp_buf = struct___jmp_buf_tag * 1 # /usr/include/setjmp.h: 49

# /usr/include/time.h: 120
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]

# /usr/include/x86_64-linux-gnu/bits/stat.h: 46
class struct_stat(Structure):
    pass

struct_stat.__slots__ = [
    'st_dev',
    'st_ino',
    'st_nlink',
    'st_mode',
    'st_uid',
    'st_gid',
    '__pad0',
    'st_rdev',
    'st_size',
    'st_blksize',
    'st_blocks',
    'st_atim',
    'st_mtim',
    'st_ctim',
    '__unused',
]
struct_stat._fields_ = [
    ('st_dev', __dev_t),
    ('st_ino', __ino_t),
    ('st_nlink', __nlink_t),
    ('st_mode', __mode_t),
    ('st_uid', __uid_t),
    ('st_gid', __gid_t),
    ('__pad0', c_int),
    ('st_rdev', __dev_t),
    ('st_size', __off_t),
    ('st_blksize', __blksize_t),
    ('st_blocks', __blkcnt_t),
    ('st_atim', struct_timespec),
    ('st_mtim', struct_timespec),
    ('st_ctim', struct_timespec),
    ('__unused', c_long * 3),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 72
if hasattr(_libs['grass_gis.7.0.4'], 'G_adjust_Cell_head'):
    G_adjust_Cell_head = _libs['grass_gis.7.0.4'].G_adjust_Cell_head
    G_adjust_Cell_head.restype = None
    G_adjust_Cell_head.argtypes = [POINTER(struct_Cell_head), c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 73
if hasattr(_libs['grass_gis.7.0.4'], 'G_adjust_Cell_head3'):
    G_adjust_Cell_head3 = _libs['grass_gis.7.0.4'].G_adjust_Cell_head3
    G_adjust_Cell_head3.restype = None
    G_adjust_Cell_head3.argtypes = [POINTER(struct_Cell_head), c_int, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 79
if hasattr(_libs['grass_gis.7.0.4'], 'G__malloc'):
    G__malloc = _libs['grass_gis.7.0.4'].G__malloc
    G__malloc.restype = POINTER(None)
    G__malloc.argtypes = [String, c_int, c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 80
if hasattr(_libs['grass_gis.7.0.4'], 'G__calloc'):
    G__calloc = _libs['grass_gis.7.0.4'].G__calloc
    G__calloc.restype = POINTER(None)
    G__calloc.argtypes = [String, c_int, c_size_t, c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 81
if hasattr(_libs['grass_gis.7.0.4'], 'G__realloc'):
    G__realloc = _libs['grass_gis.7.0.4'].G__realloc
    G__realloc.restype = POINTER(None)
    G__realloc.argtypes = [String, c_int, POINTER(None), c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 82
if hasattr(_libs['grass_gis.7.0.4'], 'G_free'):
    G_free = _libs['grass_gis.7.0.4'].G_free
    G_free.restype = None
    G_free.argtypes = [POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 98
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_cell_area_calculations'):
    G_begin_cell_area_calculations = _libs['grass_gis.7.0.4'].G_begin_cell_area_calculations
    G_begin_cell_area_calculations.restype = c_int
    G_begin_cell_area_calculations.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 99
if hasattr(_libs['grass_gis.7.0.4'], 'G_area_of_cell_at_row'):
    G_area_of_cell_at_row = _libs['grass_gis.7.0.4'].G_area_of_cell_at_row
    G_area_of_cell_at_row.restype = c_double
    G_area_of_cell_at_row.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 100
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_polygon_area_calculations'):
    G_begin_polygon_area_calculations = _libs['grass_gis.7.0.4'].G_begin_polygon_area_calculations
    G_begin_polygon_area_calculations.restype = c_int
    G_begin_polygon_area_calculations.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 101
if hasattr(_libs['grass_gis.7.0.4'], 'G_area_of_polygon'):
    G_area_of_polygon = _libs['grass_gis.7.0.4'].G_area_of_polygon
    G_area_of_polygon.restype = c_double
    G_area_of_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 104
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_zone_area_on_ellipsoid'):
    G_begin_zone_area_on_ellipsoid = _libs['grass_gis.7.0.4'].G_begin_zone_area_on_ellipsoid
    G_begin_zone_area_on_ellipsoid.restype = None
    G_begin_zone_area_on_ellipsoid.argtypes = [c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 105
if hasattr(_libs['grass_gis.7.0.4'], 'G_darea0_on_ellipsoid'):
    G_darea0_on_ellipsoid = _libs['grass_gis.7.0.4'].G_darea0_on_ellipsoid
    G_darea0_on_ellipsoid.restype = c_double
    G_darea0_on_ellipsoid.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 106
if hasattr(_libs['grass_gis.7.0.4'], 'G_area_for_zone_on_ellipsoid'):
    G_area_for_zone_on_ellipsoid = _libs['grass_gis.7.0.4'].G_area_for_zone_on_ellipsoid
    G_area_for_zone_on_ellipsoid.restype = c_double
    G_area_for_zone_on_ellipsoid.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 109
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_ellipsoid_polygon_area'):
    G_begin_ellipsoid_polygon_area = _libs['grass_gis.7.0.4'].G_begin_ellipsoid_polygon_area
    G_begin_ellipsoid_polygon_area.restype = None
    G_begin_ellipsoid_polygon_area.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 110
if hasattr(_libs['grass_gis.7.0.4'], 'G_ellipsoid_polygon_area'):
    G_ellipsoid_polygon_area = _libs['grass_gis.7.0.4'].G_ellipsoid_polygon_area
    G_ellipsoid_polygon_area.restype = c_double
    G_ellipsoid_polygon_area.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 113
if hasattr(_libs['grass_gis.7.0.4'], 'G_planimetric_polygon_area'):
    G_planimetric_polygon_area = _libs['grass_gis.7.0.4'].G_planimetric_polygon_area
    G_planimetric_polygon_area.restype = c_double
    G_planimetric_polygon_area.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 116
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_zone_area_on_sphere'):
    G_begin_zone_area_on_sphere = _libs['grass_gis.7.0.4'].G_begin_zone_area_on_sphere
    G_begin_zone_area_on_sphere.restype = None
    G_begin_zone_area_on_sphere.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 117
if hasattr(_libs['grass_gis.7.0.4'], 'G_darea0_on_sphere'):
    G_darea0_on_sphere = _libs['grass_gis.7.0.4'].G_darea0_on_sphere
    G_darea0_on_sphere.restype = c_double
    G_darea0_on_sphere.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 118
if hasattr(_libs['grass_gis.7.0.4'], 'G_area_for_zone_on_sphere'):
    G_area_for_zone_on_sphere = _libs['grass_gis.7.0.4'].G_area_for_zone_on_sphere
    G_area_for_zone_on_sphere.restype = c_double
    G_area_for_zone_on_sphere.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 121
if hasattr(_libs['grass_gis.7.0.4'], 'G_ascii_check'):
    G_ascii_check = _libs['grass_gis.7.0.4'].G_ascii_check
    G_ascii_check.restype = None
    G_ascii_check.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 133
if hasattr(_libs['grass_gis.7.0.4'], 'G_vasprintf'):
    G_vasprintf = _libs['grass_gis.7.0.4'].G_vasprintf
    G_vasprintf.restype = c_int
    G_vasprintf.argtypes = [POINTER(POINTER(c_char)), String, c_void_p]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 134
if hasattr(_libs['grass_gis.7.0.4'], 'G_asprintf'):
    _func = _libs['grass_gis.7.0.4'].G_asprintf
    _restype = c_int
    _argtypes = [POINTER(POINTER(c_char)), String]
    G_asprintf = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 137
if hasattr(_libs['grass_gis.7.0.4'], 'G_rasprintf'):
    _func = _libs['grass_gis.7.0.4'].G_rasprintf
    _restype = c_int
    _argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t), String]
    G_rasprintf = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 141
if hasattr(_libs['grass_gis.7.0.4'], 'G_basename'):
    G_basename = _libs['grass_gis.7.0.4'].G_basename
    G_basename.restype = ReturnString
    G_basename.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 142
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_num_decimals'):
    G_get_num_decimals = _libs['grass_gis.7.0.4'].G_get_num_decimals
    G_get_num_decimals.restype = c_size_t
    G_get_num_decimals.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 143
if hasattr(_libs['grass_gis.7.0.4'], 'G_double_to_basename_format'):
    G_double_to_basename_format = _libs['grass_gis.7.0.4'].G_double_to_basename_format
    G_double_to_basename_format.restype = ReturnString
    G_double_to_basename_format.argtypes = [c_double, c_size_t, c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 144
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_basename_separator'):
    G_get_basename_separator = _libs['grass_gis.7.0.4'].G_get_basename_separator
    G_get_basename_separator.restype = ReturnString
    G_get_basename_separator.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 145
if hasattr(_libs['grass_gis.7.0.4'], 'G_join_basename_strings'):
    G_join_basename_strings = _libs['grass_gis.7.0.4'].G_join_basename_strings
    G_join_basename_strings.restype = ReturnString
    G_join_basename_strings.argtypes = [POINTER(POINTER(c_char)), c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 146
if hasattr(_libs['grass_gis.7.0.4'], 'G_generate_basename'):
    G_generate_basename = _libs['grass_gis.7.0.4'].G_generate_basename
    G_generate_basename.restype = ReturnString
    G_generate_basename.argtypes = [String, c_double, c_size_t, c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 149
if hasattr(_libs['grass_gis.7.0.4'], 'G_bresenham_line'):
    G_bresenham_line = _libs['grass_gis.7.0.4'].G_bresenham_line
    G_bresenham_line.restype = None
    G_bresenham_line.argtypes = [c_int, c_int, c_int, c_int, CFUNCTYPE(UNCHECKED(c_int), c_int, c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 152
if hasattr(_libs['grass_gis.7.0.4'], 'G_clicker'):
    G_clicker = _libs['grass_gis.7.0.4'].G_clicker
    G_clicker.restype = None
    G_clicker.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 155
if hasattr(_libs['grass_gis.7.0.4'], 'G_color_rules_options'):
    G_color_rules_options = _libs['grass_gis.7.0.4'].G_color_rules_options
    G_color_rules_options.restype = ReturnString
    G_color_rules_options.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 156
if hasattr(_libs['grass_gis.7.0.4'], 'G_color_rules_descriptions'):
    G_color_rules_descriptions = _libs['grass_gis.7.0.4'].G_color_rules_descriptions
    G_color_rules_descriptions.restype = ReturnString
    G_color_rules_descriptions.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 157
if hasattr(_libs['grass_gis.7.0.4'], 'G_list_color_rules'):
    G_list_color_rules = _libs['grass_gis.7.0.4'].G_list_color_rules
    G_list_color_rules.restype = None
    G_list_color_rules.argtypes = [POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 158
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_color_rule'):
    G_find_color_rule = _libs['grass_gis.7.0.4'].G_find_color_rule
    G_find_color_rule.restype = c_int
    G_find_color_rule.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 161
if hasattr(_libs['grass_gis.7.0.4'], 'G_num_standard_colors'):
    G_num_standard_colors = _libs['grass_gis.7.0.4'].G_num_standard_colors
    G_num_standard_colors.restype = c_int
    G_num_standard_colors.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 164
if hasattr(_libs['grass_gis.7.0.4'], 'G_insert_commas'):
    G_insert_commas = _libs['grass_gis.7.0.4'].G_insert_commas
    G_insert_commas.restype = c_int
    G_insert_commas.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 165
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove_commas'):
    G_remove_commas = _libs['grass_gis.7.0.4'].G_remove_commas
    G_remove_commas.restype = None
    G_remove_commas.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 168
if hasattr(_libs['grass_gis.7.0.4'], 'G_recursive_copy'):
    G_recursive_copy = _libs['grass_gis.7.0.4'].G_recursive_copy
    G_recursive_copy.restype = c_int
    G_recursive_copy.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 171
if hasattr(_libs['grass_gis.7.0.4'], 'G_copy_file'):
    G_copy_file = _libs['grass_gis.7.0.4'].G_copy_file
    G_copy_file.restype = c_int
    G_copy_file.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 174
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_initialized'):
    G_is_initialized = _libs['grass_gis.7.0.4'].G_is_initialized
    G_is_initialized.restype = c_int
    G_is_initialized.argtypes = [POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 175
if hasattr(_libs['grass_gis.7.0.4'], 'G_initialize_done'):
    G_initialize_done = _libs['grass_gis.7.0.4'].G_initialize_done
    G_initialize_done.restype = None
    G_initialize_done.argtypes = [POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 176
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_counter'):
    G_init_counter = _libs['grass_gis.7.0.4'].G_init_counter
    G_init_counter.restype = None
    G_init_counter.argtypes = [POINTER(struct_Counter), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 177
if hasattr(_libs['grass_gis.7.0.4'], 'G_counter_next'):
    G_counter_next = _libs['grass_gis.7.0.4'].G_counter_next
    G_counter_next.restype = c_int
    G_counter_next.argtypes = [POINTER(struct_Counter)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 180
if hasattr(_libs['grass_gis.7.0.4'], 'G_date'):
    G_date = _libs['grass_gis.7.0.4'].G_date
    G_date.restype = ReturnString
    G_date.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 183
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_datum_by_name'):
    G_get_datum_by_name = _libs['grass_gis.7.0.4'].G_get_datum_by_name
    G_get_datum_by_name.restype = c_int
    G_get_datum_by_name.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 184
if hasattr(_libs['grass_gis.7.0.4'], 'G_datum_name'):
    G_datum_name = _libs['grass_gis.7.0.4'].G_datum_name
    G_datum_name.restype = ReturnString
    G_datum_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 185
if hasattr(_libs['grass_gis.7.0.4'], 'G_datum_description'):
    G_datum_description = _libs['grass_gis.7.0.4'].G_datum_description
    G_datum_description.restype = ReturnString
    G_datum_description.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 186
if hasattr(_libs['grass_gis.7.0.4'], 'G_datum_ellipsoid'):
    G_datum_ellipsoid = _libs['grass_gis.7.0.4'].G_datum_ellipsoid
    G_datum_ellipsoid.restype = ReturnString
    G_datum_ellipsoid.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 187
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_datumparams_from_projinfo'):
    G_get_datumparams_from_projinfo = _libs['grass_gis.7.0.4'].G_get_datumparams_from_projinfo
    G_get_datumparams_from_projinfo.restype = c_int
    G_get_datumparams_from_projinfo.argtypes = [POINTER(struct_Key_Value), String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 188
if hasattr(_libs['grass_gis.7.0.4'], 'G_read_datum_table'):
    G_read_datum_table = _libs['grass_gis.7.0.4'].G_read_datum_table
    G_read_datum_table.restype = None
    G_read_datum_table.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 192
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_debug'):
    G_init_debug = _libs['grass_gis.7.0.4'].G_init_debug
    G_init_debug.restype = None
    G_init_debug.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 193
if hasattr(_libs['grass_gis.7.0.4'], 'G_debug'):
    _func = _libs['grass_gis.7.0.4'].G_debug
    _restype = c_int
    _argtypes = [c_int, String]
    G_debug = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 196
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_distance_calculations'):
    G_begin_distance_calculations = _libs['grass_gis.7.0.4'].G_begin_distance_calculations
    G_begin_distance_calculations.restype = c_int
    G_begin_distance_calculations.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 197
if hasattr(_libs['grass_gis.7.0.4'], 'G_distance'):
    G_distance = _libs['grass_gis.7.0.4'].G_distance
    G_distance.restype = c_double
    G_distance.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 198
if hasattr(_libs['grass_gis.7.0.4'], 'G_distance_between_line_segments'):
    G_distance_between_line_segments = _libs['grass_gis.7.0.4'].G_distance_between_line_segments
    G_distance_between_line_segments.restype = c_double
    G_distance_between_line_segments.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 200
if hasattr(_libs['grass_gis.7.0.4'], 'G_distance_point_to_line_segment'):
    G_distance_point_to_line_segment = _libs['grass_gis.7.0.4'].G_distance_point_to_line_segment
    G_distance_point_to_line_segment.restype = c_double
    G_distance_point_to_line_segment.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 204
if hasattr(_libs['grass_gis.7.0.4'], 'G_done_msg'):
    _func = _libs['grass_gis.7.0.4'].G_done_msg
    _restype = None
    _argtypes = [String]
    G_done_msg = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 207
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_little_endian'):
    G_is_little_endian = _libs['grass_gis.7.0.4'].G_is_little_endian
    G_is_little_endian.restype = c_int
    G_is_little_endian.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 210
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_env'):
    G_init_env = _libs['grass_gis.7.0.4'].G_init_env
    G_init_env.restype = None
    G_init_env.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 211
if hasattr(_libs['grass_gis.7.0.4'], 'G_getenv'):
    G_getenv = _libs['grass_gis.7.0.4'].G_getenv
    G_getenv.restype = ReturnString
    G_getenv.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 212
if hasattr(_libs['grass_gis.7.0.4'], 'G_getenv2'):
    G_getenv2 = _libs['grass_gis.7.0.4'].G_getenv2
    G_getenv2.restype = ReturnString
    G_getenv2.argtypes = [String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 213
if hasattr(_libs['grass_gis.7.0.4'], 'G_getenv_nofatal'):
    G_getenv_nofatal = _libs['grass_gis.7.0.4'].G_getenv_nofatal
    G_getenv_nofatal.restype = ReturnString
    G_getenv_nofatal.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 214
if hasattr(_libs['grass_gis.7.0.4'], 'G_getenv_nofatal2'):
    G_getenv_nofatal2 = _libs['grass_gis.7.0.4'].G_getenv_nofatal2
    G_getenv_nofatal2.restype = ReturnString
    G_getenv_nofatal2.argtypes = [String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 215
if hasattr(_libs['grass_gis.7.0.4'], 'G_setenv'):
    G_setenv = _libs['grass_gis.7.0.4'].G_setenv
    G_setenv.restype = None
    G_setenv.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 216
if hasattr(_libs['grass_gis.7.0.4'], 'G_setenv2'):
    G_setenv2 = _libs['grass_gis.7.0.4'].G_setenv2
    G_setenv2.restype = None
    G_setenv2.argtypes = [String, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 217
if hasattr(_libs['grass_gis.7.0.4'], 'G_setenv_nogisrc'):
    G_setenv_nogisrc = _libs['grass_gis.7.0.4'].G_setenv_nogisrc
    G_setenv_nogisrc.restype = None
    G_setenv_nogisrc.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 218
if hasattr(_libs['grass_gis.7.0.4'], 'G_setenv_nogisrc2'):
    G_setenv_nogisrc2 = _libs['grass_gis.7.0.4'].G_setenv_nogisrc2
    G_setenv_nogisrc2.restype = None
    G_setenv_nogisrc2.argtypes = [String, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 219
if hasattr(_libs['grass_gis.7.0.4'], 'G_unsetenv'):
    G_unsetenv = _libs['grass_gis.7.0.4'].G_unsetenv
    G_unsetenv.restype = None
    G_unsetenv.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 220
if hasattr(_libs['grass_gis.7.0.4'], 'G_unsetenv2'):
    G_unsetenv2 = _libs['grass_gis.7.0.4'].G_unsetenv2
    G_unsetenv2.restype = None
    G_unsetenv2.argtypes = [String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 221
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_env_name'):
    G_get_env_name = _libs['grass_gis.7.0.4'].G_get_env_name
    G_get_env_name.restype = ReturnString
    G_get_env_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 222
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_gisrc_mode'):
    G_set_gisrc_mode = _libs['grass_gis.7.0.4'].G_set_gisrc_mode
    G_set_gisrc_mode.restype = None
    G_set_gisrc_mode.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 223
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_gisrc_mode'):
    G_get_gisrc_mode = _libs['grass_gis.7.0.4'].G_get_gisrc_mode
    G_get_gisrc_mode.restype = c_int
    G_get_gisrc_mode.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 224
if hasattr(_libs['grass_gis.7.0.4'], 'G_create_alt_env'):
    G_create_alt_env = _libs['grass_gis.7.0.4'].G_create_alt_env
    G_create_alt_env.restype = None
    G_create_alt_env.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 225
if hasattr(_libs['grass_gis.7.0.4'], 'G_switch_env'):
    G_switch_env = _libs['grass_gis.7.0.4'].G_switch_env
    G_switch_env.restype = None
    G_switch_env.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 226
if hasattr(_libs['grass_gis.7.0.4'], 'G__read_mapset_env'):
    G__read_mapset_env = _libs['grass_gis.7.0.4'].G__read_mapset_env
    G__read_mapset_env.restype = None
    G__read_mapset_env.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 227
if hasattr(_libs['grass_gis.7.0.4'], 'G__read_gisrc_env'):
    G__read_gisrc_env = _libs['grass_gis.7.0.4'].G__read_gisrc_env
    G__read_gisrc_env.restype = None
    G__read_gisrc_env.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 230
if hasattr(_libs['grass_gis.7.0.4'], 'G_fatal_longjmp'):
    G_fatal_longjmp = _libs['grass_gis.7.0.4'].G_fatal_longjmp
    G_fatal_longjmp.restype = POINTER(jmp_buf)
    G_fatal_longjmp.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 231
if hasattr(_libs['grass_gis.7.0.4'], 'G_info_format'):
    G_info_format = _libs['grass_gis.7.0.4'].G_info_format
    G_info_format.restype = c_int
    G_info_format.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 232
if hasattr(_libs['grass_gis.7.0.4'], 'G_message'):
    _func = _libs['grass_gis.7.0.4'].G_message
    _restype = None
    _argtypes = [String]
    G_message = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 233
if hasattr(_libs['grass_gis.7.0.4'], 'G_verbose_message'):
    _func = _libs['grass_gis.7.0.4'].G_verbose_message
    _restype = None
    _argtypes = [String]
    G_verbose_message = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 235
if hasattr(_libs['grass_gis.7.0.4'], 'G_important_message'):
    _func = _libs['grass_gis.7.0.4'].G_important_message
    _restype = None
    _argtypes = [String]
    G_important_message = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 237
if hasattr(_libs['grass_gis.7.0.4'], 'G_fatal_error'):
    _func = _libs['grass_gis.7.0.4'].G_fatal_error
    _restype = None
    _argtypes = [String]
    G_fatal_error = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 239
if hasattr(_libs['grass_gis.7.0.4'], 'G_warning'):
    _func = _libs['grass_gis.7.0.4'].G_warning
    _restype = None
    _argtypes = [String]
    G_warning = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 240
if hasattr(_libs['grass_gis.7.0.4'], 'G_suppress_warnings'):
    G_suppress_warnings = _libs['grass_gis.7.0.4'].G_suppress_warnings
    G_suppress_warnings.restype = c_int
    G_suppress_warnings.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 241
if hasattr(_libs['grass_gis.7.0.4'], 'G_sleep_on_error'):
    G_sleep_on_error = _libs['grass_gis.7.0.4'].G_sleep_on_error
    G_sleep_on_error.restype = c_int
    G_sleep_on_error.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 242
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_error_routine'):
    G_set_error_routine = _libs['grass_gis.7.0.4'].G_set_error_routine
    G_set_error_routine.restype = None
    G_set_error_routine.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 243
if hasattr(_libs['grass_gis.7.0.4'], 'G_unset_error_routine'):
    G_unset_error_routine = _libs['grass_gis.7.0.4'].G_unset_error_routine
    G_unset_error_routine.restype = None
    G_unset_error_routine.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 244
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_logging'):
    G_init_logging = _libs['grass_gis.7.0.4'].G_init_logging
    G_init_logging.restype = None
    G_init_logging.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 247
if hasattr(_libs['grass_gis.7.0.4'], 'G_file_name'):
    G_file_name = _libs['grass_gis.7.0.4'].G_file_name
    G_file_name.restype = ReturnString
    G_file_name.argtypes = [String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 248
if hasattr(_libs['grass_gis.7.0.4'], 'G_file_name_misc'):
    G_file_name_misc = _libs['grass_gis.7.0.4'].G_file_name_misc
    G_file_name_misc.restype = ReturnString
    G_file_name_misc.argtypes = [String, String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 252
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_file'):
    G_find_file = _libs['grass_gis.7.0.4'].G_find_file
    G_find_file.restype = ReturnString
    G_find_file.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 253
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_file2'):
    G_find_file2 = _libs['grass_gis.7.0.4'].G_find_file2
    G_find_file2.restype = ReturnString
    G_find_file2.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 254
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_file_misc'):
    G_find_file_misc = _libs['grass_gis.7.0.4'].G_find_file_misc
    G_find_file_misc.restype = ReturnString
    G_find_file_misc.argtypes = [String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 255
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_file2_misc'):
    G_find_file2_misc = _libs['grass_gis.7.0.4'].G_find_file2_misc
    G_find_file2_misc.restype = ReturnString
    G_find_file2_misc.argtypes = [String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 259
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_etc'):
    G_find_etc = _libs['grass_gis.7.0.4'].G_find_etc
    G_find_etc.restype = ReturnString
    G_find_etc.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 262
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_raster'):
    G_find_raster = _libs['grass_gis.7.0.4'].G_find_raster
    G_find_raster.restype = ReturnString
    G_find_raster.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 263
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_raster2'):
    G_find_raster2 = _libs['grass_gis.7.0.4'].G_find_raster2
    G_find_raster2.restype = ReturnString
    G_find_raster2.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 266
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_raster3d'):
    G_find_raster3d = _libs['grass_gis.7.0.4'].G_find_raster3d
    G_find_raster3d.restype = ReturnString
    G_find_raster3d.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 269
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_vector'):
    G_find_vector = _libs['grass_gis.7.0.4'].G_find_vector
    G_find_vector.restype = ReturnString
    G_find_vector.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 270
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_vector2'):
    G_find_vector2 = _libs['grass_gis.7.0.4'].G_find_vector2
    G_find_vector2.restype = ReturnString
    G_find_vector2.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 273
if hasattr(_libs['grass_gis.7.0.4'], 'G_zlib_compress'):
    G_zlib_compress = _libs['grass_gis.7.0.4'].G_zlib_compress
    G_zlib_compress.restype = c_int
    G_zlib_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 274
if hasattr(_libs['grass_gis.7.0.4'], 'G_zlib_expand'):
    G_zlib_expand = _libs['grass_gis.7.0.4'].G_zlib_expand
    G_zlib_expand.restype = c_int
    G_zlib_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 275
if hasattr(_libs['grass_gis.7.0.4'], 'G_zlib_write'):
    G_zlib_write = _libs['grass_gis.7.0.4'].G_zlib_write
    G_zlib_write.restype = c_int
    G_zlib_write.argtypes = [c_int, POINTER(c_ubyte), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 276
if hasattr(_libs['grass_gis.7.0.4'], 'G_zlib_read'):
    G_zlib_read = _libs['grass_gis.7.0.4'].G_zlib_read
    G_zlib_read.restype = c_int
    G_zlib_read.argtypes = [c_int, c_int, POINTER(c_ubyte), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 277
if hasattr(_libs['grass_gis.7.0.4'], 'G_zlib_write_noCompress'):
    G_zlib_write_noCompress = _libs['grass_gis.7.0.4'].G_zlib_write_noCompress
    G_zlib_write_noCompress.restype = c_int
    G_zlib_write_noCompress.argtypes = [c_int, POINTER(c_ubyte), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 280
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_geodesic_equation'):
    G_begin_geodesic_equation = _libs['grass_gis.7.0.4'].G_begin_geodesic_equation
    G_begin_geodesic_equation.restype = c_int
    G_begin_geodesic_equation.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 281
if hasattr(_libs['grass_gis.7.0.4'], 'G_geodesic_lat_from_lon'):
    G_geodesic_lat_from_lon = _libs['grass_gis.7.0.4'].G_geodesic_lat_from_lon
    G_geodesic_lat_from_lon.restype = c_double
    G_geodesic_lat_from_lon.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 284
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_geodesic_distance'):
    G_begin_geodesic_distance = _libs['grass_gis.7.0.4'].G_begin_geodesic_distance
    G_begin_geodesic_distance.restype = None
    G_begin_geodesic_distance.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 285
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_geodesic_distance_lat1'):
    G_set_geodesic_distance_lat1 = _libs['grass_gis.7.0.4'].G_set_geodesic_distance_lat1
    G_set_geodesic_distance_lat1.restype = None
    G_set_geodesic_distance_lat1.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 286
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_geodesic_distance_lat2'):
    G_set_geodesic_distance_lat2 = _libs['grass_gis.7.0.4'].G_set_geodesic_distance_lat2
    G_set_geodesic_distance_lat2.restype = None
    G_set_geodesic_distance_lat2.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 287
if hasattr(_libs['grass_gis.7.0.4'], 'G_geodesic_distance_lon_to_lon'):
    G_geodesic_distance_lon_to_lon = _libs['grass_gis.7.0.4'].G_geodesic_distance_lon_to_lon
    G_geodesic_distance_lon_to_lon.restype = c_double
    G_geodesic_distance_lon_to_lon.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 288
if hasattr(_libs['grass_gis.7.0.4'], 'G_geodesic_distance'):
    G_geodesic_distance = _libs['grass_gis.7.0.4'].G_geodesic_distance
    G_geodesic_distance.restype = c_double
    G_geodesic_distance.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 291
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_ellipsoid_parameters'):
    G_get_ellipsoid_parameters = _libs['grass_gis.7.0.4'].G_get_ellipsoid_parameters
    G_get_ellipsoid_parameters.restype = c_int
    G_get_ellipsoid_parameters.argtypes = [POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 292
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_spheroid_by_name'):
    G_get_spheroid_by_name = _libs['grass_gis.7.0.4'].G_get_spheroid_by_name
    G_get_spheroid_by_name.restype = c_int
    G_get_spheroid_by_name.argtypes = [String, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 293
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_ellipsoid_by_name'):
    G_get_ellipsoid_by_name = _libs['grass_gis.7.0.4'].G_get_ellipsoid_by_name
    G_get_ellipsoid_by_name.restype = c_int
    G_get_ellipsoid_by_name.argtypes = [String, POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 294
if hasattr(_libs['grass_gis.7.0.4'], 'G_ellipsoid_name'):
    G_ellipsoid_name = _libs['grass_gis.7.0.4'].G_ellipsoid_name
    G_ellipsoid_name.restype = ReturnString
    G_ellipsoid_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 295
if hasattr(_libs['grass_gis.7.0.4'], 'G_ellipsoid_description'):
    G_ellipsoid_description = _libs['grass_gis.7.0.4'].G_ellipsoid_description
    G_ellipsoid_description.restype = ReturnString
    G_ellipsoid_description.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 296
if hasattr(_libs['grass_gis.7.0.4'], 'G_read_ellipsoid_table'):
    G_read_ellipsoid_table = _libs['grass_gis.7.0.4'].G_read_ellipsoid_table
    G_read_ellipsoid_table.restype = c_int
    G_read_ellipsoid_table.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 299
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_projunits'):
    G_get_projunits = _libs['grass_gis.7.0.4'].G_get_projunits
    G_get_projunits.restype = POINTER(struct_Key_Value)
    G_get_projunits.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 300
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_projinfo'):
    G_get_projinfo = _libs['grass_gis.7.0.4'].G_get_projinfo
    G_get_projinfo.restype = POINTER(struct_Key_Value)
    G_get_projinfo.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 301
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_projepsg'):
    G_get_projepsg = _libs['grass_gis.7.0.4'].G_get_projepsg
    G_get_projepsg.restype = POINTER(struct_Key_Value)
    G_get_projepsg.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 304
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_window'):
    G_get_window = _libs['grass_gis.7.0.4'].G_get_window
    G_get_window.restype = None
    G_get_window.argtypes = [POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 305
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_default_window'):
    G_get_default_window = _libs['grass_gis.7.0.4'].G_get_default_window
    G_get_default_window.restype = None
    G_get_default_window.argtypes = [POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 306
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_element_window'):
    G_get_element_window = _libs['grass_gis.7.0.4'].G_get_element_window
    G_get_element_window.restype = None
    G_get_element_window.argtypes = [POINTER(struct_Cell_head), String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 310
if hasattr(_libs['grass_gis.7.0.4'], 'G_getl'):
    G_getl = _libs['grass_gis.7.0.4'].G_getl
    G_getl.restype = c_int
    G_getl.argtypes = [String, c_int, POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 311
if hasattr(_libs['grass_gis.7.0.4'], 'G_getl2'):
    G_getl2 = _libs['grass_gis.7.0.4'].G_getl2
    G_getl2.restype = c_int
    G_getl2.argtypes = [String, c_int, POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 314
if hasattr(_libs['grass_gis.7.0.4'], 'G_gisbase'):
    G_gisbase = _libs['grass_gis.7.0.4'].G_gisbase
    G_gisbase.restype = ReturnString
    G_gisbase.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 317
if hasattr(_libs['grass_gis.7.0.4'], 'G_gisdbase'):
    G_gisdbase = _libs['grass_gis.7.0.4'].G_gisdbase
    G_gisdbase.restype = ReturnString
    G_gisdbase.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 320
if hasattr(_libs['grass_gis.7.0.4'], 'G__gisinit'):
    G__gisinit = _libs['grass_gis.7.0.4'].G__gisinit
    G__gisinit.restype = None
    G__gisinit.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 321
if hasattr(_libs['grass_gis.7.0.4'], 'G__no_gisinit'):
    G__no_gisinit = _libs['grass_gis.7.0.4'].G__no_gisinit
    G__no_gisinit.restype = None
    G__no_gisinit.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 322
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_all'):
    G_init_all = _libs['grass_gis.7.0.4'].G_init_all
    G_init_all.restype = None
    G_init_all.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 325
if hasattr(_libs['grass_gis.7.0.4'], 'G_add_error_handler'):
    G_add_error_handler = _libs['grass_gis.7.0.4'].G_add_error_handler
    G_add_error_handler.restype = None
    G_add_error_handler.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 326
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove_error_handler'):
    G_remove_error_handler = _libs['grass_gis.7.0.4'].G_remove_error_handler
    G_remove_error_handler.restype = None
    G_remove_error_handler.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 329
if hasattr(_libs['grass_gis.7.0.4'], 'G_home'):
    G_home = _libs['grass_gis.7.0.4'].G_home
    G_home.restype = ReturnString
    G_home.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 330
if hasattr(_libs['grass_gis.7.0.4'], 'G_config_path'):
    G_config_path = _libs['grass_gis.7.0.4'].G_config_path
    G_config_path.restype = ReturnString
    G_config_path.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 333
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_ilist'):
    G_init_ilist = _libs['grass_gis.7.0.4'].G_init_ilist
    G_init_ilist.restype = None
    G_init_ilist.argtypes = [POINTER(struct_ilist)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 334
if hasattr(_libs['grass_gis.7.0.4'], 'G_free_ilist'):
    G_free_ilist = _libs['grass_gis.7.0.4'].G_free_ilist
    G_free_ilist.restype = None
    G_free_ilist.argtypes = [POINTER(struct_ilist)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 335
if hasattr(_libs['grass_gis.7.0.4'], 'G_new_ilist'):
    G_new_ilist = _libs['grass_gis.7.0.4'].G_new_ilist
    G_new_ilist.restype = POINTER(struct_ilist)
    G_new_ilist.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 336
if hasattr(_libs['grass_gis.7.0.4'], 'G_ilist_add'):
    G_ilist_add = _libs['grass_gis.7.0.4'].G_ilist_add
    G_ilist_add.restype = None
    G_ilist_add.argtypes = [POINTER(struct_ilist), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 339
if hasattr(_libs['grass_gis.7.0.4'], 'G_intersect_line_segments'):
    G_intersect_line_segments = _libs['grass_gis.7.0.4'].G_intersect_line_segments
    G_intersect_line_segments.restype = c_int
    G_intersect_line_segments.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 344
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_gisbase'):
    G_is_gisbase = _libs['grass_gis.7.0.4'].G_is_gisbase
    G_is_gisbase.restype = c_int
    G_is_gisbase.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 345
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_location'):
    G_is_location = _libs['grass_gis.7.0.4'].G_is_location
    G_is_location.restype = c_int
    G_is_location.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 346
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_mapset'):
    G_is_mapset = _libs['grass_gis.7.0.4'].G_is_mapset
    G_is_mapset.restype = c_int
    G_is_mapset.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 349
if hasattr(_libs['grass_gis.7.0.4'], 'G_create_key_value'):
    G_create_key_value = _libs['grass_gis.7.0.4'].G_create_key_value
    G_create_key_value.restype = POINTER(struct_Key_Value)
    G_create_key_value.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 350
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_key_value'):
    G_set_key_value = _libs['grass_gis.7.0.4'].G_set_key_value
    G_set_key_value.restype = None
    G_set_key_value.argtypes = [String, String, POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 351
if hasattr(_libs['grass_gis.7.0.4'], 'G_find_key_value'):
    G_find_key_value = _libs['grass_gis.7.0.4'].G_find_key_value
    G_find_key_value.restype = ReturnString
    G_find_key_value.argtypes = [String, POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 352
if hasattr(_libs['grass_gis.7.0.4'], 'G_free_key_value'):
    G_free_key_value = _libs['grass_gis.7.0.4'].G_free_key_value
    G_free_key_value.restype = None
    G_free_key_value.argtypes = [POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 355
if hasattr(_libs['grass_gis.7.0.4'], 'G_fwrite_key_value'):
    G_fwrite_key_value = _libs['grass_gis.7.0.4'].G_fwrite_key_value
    G_fwrite_key_value.restype = c_int
    G_fwrite_key_value.argtypes = [POINTER(FILE), POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 356
if hasattr(_libs['grass_gis.7.0.4'], 'G_fread_key_value'):
    G_fread_key_value = _libs['grass_gis.7.0.4'].G_fread_key_value
    G_fread_key_value.restype = POINTER(struct_Key_Value)
    G_fread_key_value.argtypes = [POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 359
if hasattr(_libs['grass_gis.7.0.4'], 'G_write_key_value_file'):
    G_write_key_value_file = _libs['grass_gis.7.0.4'].G_write_key_value_file
    G_write_key_value_file.restype = None
    G_write_key_value_file.argtypes = [String, POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 360
if hasattr(_libs['grass_gis.7.0.4'], 'G_read_key_value_file'):
    G_read_key_value_file = _libs['grass_gis.7.0.4'].G_read_key_value_file
    G_read_key_value_file.restype = POINTER(struct_Key_Value)
    G_read_key_value_file.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 363
if hasattr(_libs['grass_gis.7.0.4'], 'G_update_key_value_file'):
    G_update_key_value_file = _libs['grass_gis.7.0.4'].G_update_key_value_file
    G_update_key_value_file.restype = None
    G_update_key_value_file.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 364
if hasattr(_libs['grass_gis.7.0.4'], 'G_lookup_key_value_from_file'):
    G_lookup_key_value_from_file = _libs['grass_gis.7.0.4'].G_lookup_key_value_from_file
    G_lookup_key_value_from_file.restype = c_int
    G_lookup_key_value_from_file.argtypes = [String, String, POINTER(c_char), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 367
if hasattr(_libs['grass_gis.7.0.4'], 'G_legal_filename'):
    G_legal_filename = _libs['grass_gis.7.0.4'].G_legal_filename
    G_legal_filename.restype = c_int
    G_legal_filename.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 368
if hasattr(_libs['grass_gis.7.0.4'], 'G_check_input_output_name'):
    G_check_input_output_name = _libs['grass_gis.7.0.4'].G_check_input_output_name
    G_check_input_output_name.restype = c_int
    G_check_input_output_name.argtypes = [String, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 371
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_distance_to_line_tolerance'):
    G_set_distance_to_line_tolerance = _libs['grass_gis.7.0.4'].G_set_distance_to_line_tolerance
    G_set_distance_to_line_tolerance.restype = None
    G_set_distance_to_line_tolerance.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 372
if hasattr(_libs['grass_gis.7.0.4'], 'G_distance2_point_to_line'):
    G_distance2_point_to_line = _libs['grass_gis.7.0.4'].G_distance2_point_to_line
    G_distance2_point_to_line.restype = c_double
    G_distance2_point_to_line.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 376
if hasattr(_libs['grass_gis.7.0.4'], 'G_list_element'):
    G_list_element = _libs['grass_gis.7.0.4'].G_list_element
    G_list_element.restype = None
    G_list_element.argtypes = [String, String, String, CFUNCTYPE(UNCHECKED(c_int), String, String, String)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 378
if hasattr(_libs['grass_gis.7.0.4'], 'G_list'):
    G_list = _libs['grass_gis.7.0.4'].G_list
    G_list.restype = POINTER(POINTER(c_char))
    G_list.argtypes = [c_int, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 379
if hasattr(_libs['grass_gis.7.0.4'], 'G_free_list'):
    G_free_list = _libs['grass_gis.7.0.4'].G_free_list
    G_free_list.restype = None
    G_free_list.argtypes = [POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 382
if hasattr(_libs['grass_gis.7.0.4'], 'G_lat_format'):
    G_lat_format = _libs['grass_gis.7.0.4'].G_lat_format
    G_lat_format.restype = None
    G_lat_format.argtypes = [c_double, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 383
if hasattr(_libs['grass_gis.7.0.4'], 'G_lat_format_string'):
    G_lat_format_string = _libs['grass_gis.7.0.4'].G_lat_format_string
    G_lat_format_string.restype = ReturnString
    G_lat_format_string.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 384
if hasattr(_libs['grass_gis.7.0.4'], 'G_lon_format'):
    G_lon_format = _libs['grass_gis.7.0.4'].G_lon_format
    G_lon_format.restype = None
    G_lon_format.argtypes = [c_double, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 385
if hasattr(_libs['grass_gis.7.0.4'], 'G_lon_format_string'):
    G_lon_format_string = _libs['grass_gis.7.0.4'].G_lon_format_string
    G_lon_format_string.restype = ReturnString
    G_lon_format_string.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 386
if hasattr(_libs['grass_gis.7.0.4'], 'G_llres_format'):
    G_llres_format = _libs['grass_gis.7.0.4'].G_llres_format
    G_llres_format.restype = None
    G_llres_format.argtypes = [c_double, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 387
if hasattr(_libs['grass_gis.7.0.4'], 'G_llres_format_string'):
    G_llres_format_string = _libs['grass_gis.7.0.4'].G_llres_format_string
    G_llres_format_string.restype = ReturnString
    G_llres_format_string.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 388
if hasattr(_libs['grass_gis.7.0.4'], 'G_lat_parts'):
    G_lat_parts = _libs['grass_gis.7.0.4'].G_lat_parts
    G_lat_parts.restype = None
    G_lat_parts.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_double), String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 389
if hasattr(_libs['grass_gis.7.0.4'], 'G_lon_parts'):
    G_lon_parts = _libs['grass_gis.7.0.4'].G_lon_parts
    G_lon_parts.restype = None
    G_lon_parts.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_double), String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 392
if hasattr(_libs['grass_gis.7.0.4'], 'G_lat_scan'):
    G_lat_scan = _libs['grass_gis.7.0.4'].G_lat_scan
    G_lat_scan.restype = c_int
    G_lat_scan.argtypes = [String, POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 393
if hasattr(_libs['grass_gis.7.0.4'], 'G_lon_scan'):
    G_lon_scan = _libs['grass_gis.7.0.4'].G_lon_scan
    G_lon_scan.restype = c_int
    G_lon_scan.argtypes = [String, POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 394
if hasattr(_libs['grass_gis.7.0.4'], 'G_llres_scan'):
    G_llres_scan = _libs['grass_gis.7.0.4'].G_llres_scan
    G_llres_scan.restype = c_int
    G_llres_scan.argtypes = [String, POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 397
if hasattr(_libs['grass_gis.7.0.4'], 'G_location'):
    G_location = _libs['grass_gis.7.0.4'].G_location
    G_location.restype = ReturnString
    G_location.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 398
if hasattr(_libs['grass_gis.7.0.4'], 'G_location_path'):
    G_location_path = _libs['grass_gis.7.0.4'].G_location_path
    G_location_path.restype = ReturnString
    G_location_path.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 401
if hasattr(_libs['grass_gis.7.0.4'], 'G_srand48'):
    G_srand48 = _libs['grass_gis.7.0.4'].G_srand48
    G_srand48.restype = None
    G_srand48.argtypes = [c_long]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 402
if hasattr(_libs['grass_gis.7.0.4'], 'G_srand48_auto'):
    G_srand48_auto = _libs['grass_gis.7.0.4'].G_srand48_auto
    G_srand48_auto.restype = c_long
    G_srand48_auto.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 403
if hasattr(_libs['grass_gis.7.0.4'], 'G_lrand48'):
    G_lrand48 = _libs['grass_gis.7.0.4'].G_lrand48
    G_lrand48.restype = c_long
    G_lrand48.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 404
if hasattr(_libs['grass_gis.7.0.4'], 'G_mrand48'):
    G_mrand48 = _libs['grass_gis.7.0.4'].G_mrand48
    G_mrand48.restype = c_long
    G_mrand48.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 405
if hasattr(_libs['grass_gis.7.0.4'], 'G_drand48'):
    G_drand48 = _libs['grass_gis.7.0.4'].G_drand48
    G_drand48.restype = c_double
    G_drand48.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 408
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_ls_filter'):
    G_set_ls_filter = _libs['grass_gis.7.0.4'].G_set_ls_filter
    G_set_ls_filter.restype = None
    G_set_ls_filter.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 409
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_ls_exclude_filter'):
    G_set_ls_exclude_filter = _libs['grass_gis.7.0.4'].G_set_ls_exclude_filter
    G_set_ls_exclude_filter.restype = None
    G_set_ls_exclude_filter.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 410
if hasattr(_libs['grass_gis.7.0.4'], 'G_ls2'):
    G_ls2 = _libs['grass_gis.7.0.4'].G_ls2
    G_ls2.restype = POINTER(POINTER(c_char))
    G_ls2.argtypes = [String, POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 411
if hasattr(_libs['grass_gis.7.0.4'], 'G_ls'):
    G_ls = _libs['grass_gis.7.0.4'].G_ls
    G_ls.restype = None
    G_ls.argtypes = [String, POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 412
if hasattr(_libs['grass_gis.7.0.4'], 'G_ls_format'):
    G_ls_format = _libs['grass_gis.7.0.4'].G_ls_format
    G_ls_format.restype = None
    G_ls_format.argtypes = [POINTER(POINTER(c_char)), c_int, c_int, POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 416
if hasattr(_libs['grass_gis.7.0.4'], 'G_ls_regex_filter'):
    G_ls_regex_filter = _libs['grass_gis.7.0.4'].G_ls_regex_filter
    G_ls_regex_filter.restype = POINTER(None)
    G_ls_regex_filter.argtypes = [String, c_int, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 417
if hasattr(_libs['grass_gis.7.0.4'], 'G_ls_glob_filter'):
    G_ls_glob_filter = _libs['grass_gis.7.0.4'].G_ls_glob_filter
    G_ls_glob_filter.restype = POINTER(None)
    G_ls_glob_filter.argtypes = [String, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 418
if hasattr(_libs['grass_gis.7.0.4'], 'G_free_ls_filter'):
    G_free_ls_filter = _libs['grass_gis.7.0.4'].G_free_ls_filter
    G_free_ls_filter.restype = None
    G_free_ls_filter.argtypes = [POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 422
if hasattr(_libs['grass_gis.7.0.4'], 'G_make_location'):
    G_make_location = _libs['grass_gis.7.0.4'].G_make_location
    G_make_location.restype = c_int
    G_make_location.argtypes = [String, POINTER(struct_Cell_head), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 424
if hasattr(_libs['grass_gis.7.0.4'], 'G_compare_projections'):
    G_compare_projections = _libs['grass_gis.7.0.4'].G_compare_projections
    G_compare_projections.restype = c_int
    G_compare_projections.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 428
if hasattr(_libs['grass_gis.7.0.4'], 'G_make_mapset'):
    G_make_mapset = _libs['grass_gis.7.0.4'].G_make_mapset
    G_make_mapset.restype = c_int
    G_make_mapset.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 431
if hasattr(_libs['grass_gis.7.0.4'], 'G_tolcase'):
    G_tolcase = _libs['grass_gis.7.0.4'].G_tolcase
    G_tolcase.restype = ReturnString
    G_tolcase.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 432
if hasattr(_libs['grass_gis.7.0.4'], 'G_toucase'):
    G_toucase = _libs['grass_gis.7.0.4'].G_toucase
    G_toucase.restype = ReturnString
    G_toucase.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 435
if hasattr(_libs['grass_gis.7.0.4'], 'G_mapset'):
    G_mapset = _libs['grass_gis.7.0.4'].G_mapset
    G_mapset.restype = ReturnString
    G_mapset.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 436
if hasattr(_libs['grass_gis.7.0.4'], 'G_mapset_path'):
    G_mapset_path = _libs['grass_gis.7.0.4'].G_mapset_path
    G_mapset_path.restype = ReturnString
    G_mapset_path.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 439
if hasattr(_libs['grass_gis.7.0.4'], 'G_make_mapset_element'):
    G_make_mapset_element = _libs['grass_gis.7.0.4'].G_make_mapset_element
    G_make_mapset_element.restype = c_int
    G_make_mapset_element.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 440
if hasattr(_libs['grass_gis.7.0.4'], 'G__make_mapset_element_misc'):
    G__make_mapset_element_misc = _libs['grass_gis.7.0.4'].G__make_mapset_element_misc
    G__make_mapset_element_misc.restype = c_int
    G__make_mapset_element_misc.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 441
if hasattr(_libs['grass_gis.7.0.4'], 'G_mapset_permissions'):
    G_mapset_permissions = _libs['grass_gis.7.0.4'].G_mapset_permissions
    G_mapset_permissions.restype = c_int
    G_mapset_permissions.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 442
if hasattr(_libs['grass_gis.7.0.4'], 'G_mapset_permissions2'):
    G_mapset_permissions2 = _libs['grass_gis.7.0.4'].G_mapset_permissions2
    G_mapset_permissions2.restype = c_int
    G_mapset_permissions2.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 445
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_mapset_name'):
    G_get_mapset_name = _libs['grass_gis.7.0.4'].G_get_mapset_name
    G_get_mapset_name.restype = ReturnString
    G_get_mapset_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 446
if hasattr(_libs['grass_gis.7.0.4'], 'G_create_alt_search_path'):
    G_create_alt_search_path = _libs['grass_gis.7.0.4'].G_create_alt_search_path
    G_create_alt_search_path.restype = None
    G_create_alt_search_path.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 447
if hasattr(_libs['grass_gis.7.0.4'], 'G_switch_search_path'):
    G_switch_search_path = _libs['grass_gis.7.0.4'].G_switch_search_path
    G_switch_search_path.restype = None
    G_switch_search_path.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 448
if hasattr(_libs['grass_gis.7.0.4'], 'G_reset_mapsets'):
    G_reset_mapsets = _libs['grass_gis.7.0.4'].G_reset_mapsets
    G_reset_mapsets.restype = None
    G_reset_mapsets.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 449
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_available_mapsets'):
    G_get_available_mapsets = _libs['grass_gis.7.0.4'].G_get_available_mapsets
    G_get_available_mapsets.restype = POINTER(POINTER(c_char))
    G_get_available_mapsets.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 450
if hasattr(_libs['grass_gis.7.0.4'], 'G_add_mapset_to_search_path'):
    G_add_mapset_to_search_path = _libs['grass_gis.7.0.4'].G_add_mapset_to_search_path
    G_add_mapset_to_search_path.restype = None
    G_add_mapset_to_search_path.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 451
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_mapset_in_search_path'):
    G_is_mapset_in_search_path = _libs['grass_gis.7.0.4'].G_is_mapset_in_search_path
    G_is_mapset_in_search_path.restype = c_int
    G_is_mapset_in_search_path.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 454
if hasattr(_libs['grass_gis.7.0.4'], 'G_myname'):
    G_myname = _libs['grass_gis.7.0.4'].G_myname
    G_myname.restype = ReturnString
    G_myname.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 457
if hasattr(_libs['grass_gis.7.0.4'], 'G_color_values'):
    G_color_values = _libs['grass_gis.7.0.4'].G_color_values
    G_color_values.restype = c_int
    G_color_values.argtypes = [String, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 458
if hasattr(_libs['grass_gis.7.0.4'], 'G_color_name'):
    G_color_name = _libs['grass_gis.7.0.4'].G_color_name
    G_color_name.restype = ReturnString
    G_color_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 461
if hasattr(_libs['grass_gis.7.0.4'], 'G_newlines_to_spaces'):
    G_newlines_to_spaces = _libs['grass_gis.7.0.4'].G_newlines_to_spaces
    G_newlines_to_spaces.restype = None
    G_newlines_to_spaces.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 464
if hasattr(_libs['grass_gis.7.0.4'], 'G_name_is_fully_qualified'):
    G_name_is_fully_qualified = _libs['grass_gis.7.0.4'].G_name_is_fully_qualified
    G_name_is_fully_qualified.restype = c_int
    G_name_is_fully_qualified.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 465
if hasattr(_libs['grass_gis.7.0.4'], 'G_fully_qualified_name'):
    G_fully_qualified_name = _libs['grass_gis.7.0.4'].G_fully_qualified_name
    G_fully_qualified_name.restype = ReturnString
    G_fully_qualified_name.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 466
if hasattr(_libs['grass_gis.7.0.4'], 'G_unqualified_name'):
    G_unqualified_name = _libs['grass_gis.7.0.4'].G_unqualified_name
    G_unqualified_name.restype = c_int
    G_unqualified_name.argtypes = [String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 469
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_new'):
    G_open_new = _libs['grass_gis.7.0.4'].G_open_new
    G_open_new.restype = c_int
    G_open_new.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 470
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_old'):
    G_open_old = _libs['grass_gis.7.0.4'].G_open_old
    G_open_old.restype = c_int
    G_open_old.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 471
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_update'):
    G_open_update = _libs['grass_gis.7.0.4'].G_open_update
    G_open_update.restype = c_int
    G_open_update.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 472
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_new'):
    G_fopen_new = _libs['grass_gis.7.0.4'].G_fopen_new
    G_fopen_new.restype = POINTER(FILE)
    G_fopen_new.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 473
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_old'):
    G_fopen_old = _libs['grass_gis.7.0.4'].G_fopen_old
    G_fopen_old.restype = POINTER(FILE)
    G_fopen_old.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 474
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_append'):
    G_fopen_append = _libs['grass_gis.7.0.4'].G_fopen_append
    G_fopen_append.restype = POINTER(FILE)
    G_fopen_append.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 475
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_modify'):
    G_fopen_modify = _libs['grass_gis.7.0.4'].G_fopen_modify
    G_fopen_modify.restype = POINTER(FILE)
    G_fopen_modify.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 478
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_new_misc'):
    G_open_new_misc = _libs['grass_gis.7.0.4'].G_open_new_misc
    G_open_new_misc.restype = c_int
    G_open_new_misc.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 479
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_old_misc'):
    G_open_old_misc = _libs['grass_gis.7.0.4'].G_open_old_misc
    G_open_old_misc.restype = c_int
    G_open_old_misc.argtypes = [String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 480
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_update_misc'):
    G_open_update_misc = _libs['grass_gis.7.0.4'].G_open_update_misc
    G_open_update_misc.restype = c_int
    G_open_update_misc.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 481
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_new_misc'):
    G_fopen_new_misc = _libs['grass_gis.7.0.4'].G_fopen_new_misc
    G_fopen_new_misc.restype = POINTER(FILE)
    G_fopen_new_misc.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 482
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_old_misc'):
    G_fopen_old_misc = _libs['grass_gis.7.0.4'].G_fopen_old_misc
    G_fopen_old_misc.restype = POINTER(FILE)
    G_fopen_old_misc.argtypes = [String, String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 484
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_append_misc'):
    G_fopen_append_misc = _libs['grass_gis.7.0.4'].G_fopen_append_misc
    G_fopen_append_misc.restype = POINTER(FILE)
    G_fopen_append_misc.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 485
if hasattr(_libs['grass_gis.7.0.4'], 'G_fopen_modify_misc'):
    G_fopen_modify_misc = _libs['grass_gis.7.0.4'].G_fopen_modify_misc
    G_fopen_modify_misc.restype = POINTER(FILE)
    G_fopen_modify_misc.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 488
if hasattr(_libs['grass_gis.7.0.4'], 'G_check_overwrite'):
    G_check_overwrite = _libs['grass_gis.7.0.4'].G_check_overwrite
    G_check_overwrite.restype = c_int
    G_check_overwrite.argtypes = [c_int, POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 491
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_pager'):
    G_open_pager = _libs['grass_gis.7.0.4'].G_open_pager
    G_open_pager.restype = POINTER(FILE)
    G_open_pager.argtypes = [POINTER(struct_Popen)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 492
if hasattr(_libs['grass_gis.7.0.4'], 'G_close_pager'):
    G_close_pager = _libs['grass_gis.7.0.4'].G_close_pager
    G_close_pager.restype = None
    G_close_pager.argtypes = [POINTER(struct_Popen)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 493
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_mail'):
    G_open_mail = _libs['grass_gis.7.0.4'].G_open_mail
    G_open_mail.restype = POINTER(FILE)
    G_open_mail.argtypes = [POINTER(struct_Popen)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 494
if hasattr(_libs['grass_gis.7.0.4'], 'G_close_mail'):
    G_close_mail = _libs['grass_gis.7.0.4'].G_close_mail
    G_close_mail.restype = None
    G_close_mail.argtypes = [POINTER(struct_Popen)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 497
if hasattr(_libs['grass_gis.7.0.4'], 'G_disable_interactive'):
    G_disable_interactive = _libs['grass_gis.7.0.4'].G_disable_interactive
    G_disable_interactive.restype = None
    G_disable_interactive.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 498
if hasattr(_libs['grass_gis.7.0.4'], 'G_define_module'):
    G_define_module = _libs['grass_gis.7.0.4'].G_define_module
    G_define_module.restype = POINTER(struct_GModule)
    G_define_module.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 499
if hasattr(_libs['grass_gis.7.0.4'], 'G_define_flag'):
    G_define_flag = _libs['grass_gis.7.0.4'].G_define_flag
    G_define_flag.restype = POINTER(struct_Flag)
    G_define_flag.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 500
if hasattr(_libs['grass_gis.7.0.4'], 'G_define_option'):
    G_define_option = _libs['grass_gis.7.0.4'].G_define_option
    G_define_option.restype = POINTER(struct_Option)
    G_define_option.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 501
if hasattr(_libs['grass_gis.7.0.4'], 'G_define_standard_option'):
    G_define_standard_option = _libs['grass_gis.7.0.4'].G_define_standard_option
    G_define_standard_option.restype = POINTER(struct_Option)
    G_define_standard_option.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 502
if hasattr(_libs['grass_gis.7.0.4'], 'G_define_standard_flag'):
    G_define_standard_flag = _libs['grass_gis.7.0.4'].G_define_standard_flag
    G_define_standard_flag.restype = POINTER(struct_Flag)
    G_define_standard_flag.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 503
if hasattr(_libs['grass_gis.7.0.4'], 'G_parser'):
    G_parser = _libs['grass_gis.7.0.4'].G_parser
    G_parser.restype = c_int
    G_parser.argtypes = [c_int, POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 504
if hasattr(_libs['grass_gis.7.0.4'], 'G_usage'):
    G_usage = _libs['grass_gis.7.0.4'].G_usage
    G_usage.restype = None
    G_usage.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 505
if hasattr(_libs['grass_gis.7.0.4'], 'G_recreate_command'):
    G_recreate_command = _libs['grass_gis.7.0.4'].G_recreate_command
    G_recreate_command.restype = ReturnString
    G_recreate_command.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 506
if hasattr(_libs['grass_gis.7.0.4'], 'G_add_keyword'):
    G_add_keyword = _libs['grass_gis.7.0.4'].G_add_keyword
    G_add_keyword.restype = None
    G_add_keyword.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 507
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_keywords'):
    G_set_keywords = _libs['grass_gis.7.0.4'].G_set_keywords
    G_set_keywords.restype = None
    G_set_keywords.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 508
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_overwrite'):
    G_get_overwrite = _libs['grass_gis.7.0.4'].G_get_overwrite
    G_get_overwrite.restype = c_int
    G_get_overwrite.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 509
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_to_separator'):
    G_option_to_separator = _libs['grass_gis.7.0.4'].G_option_to_separator
    G_option_to_separator.restype = ReturnString
    G_option_to_separator.argtypes = [POINTER(struct_Option)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 510
if hasattr(_libs['grass_gis.7.0.4'], 'G_open_option_file'):
    G_open_option_file = _libs['grass_gis.7.0.4'].G_open_option_file
    G_open_option_file.restype = POINTER(FILE)
    G_open_option_file.argtypes = [POINTER(struct_Option)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 511
if hasattr(_libs['grass_gis.7.0.4'], 'G_close_option_file'):
    G_close_option_file = _libs['grass_gis.7.0.4'].G_close_option_file
    G_close_option_file.restype = None
    G_close_option_file.argtypes = [POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 514
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_rule'):
    G_option_rule = _libs['grass_gis.7.0.4'].G_option_rule
    G_option_rule.restype = None
    G_option_rule.argtypes = [c_int, c_int, POINTER(POINTER(None))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 515
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_exclusive'):
    _func = _libs['grass_gis.7.0.4'].G_option_exclusive
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_exclusive = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 516
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_required'):
    _func = _libs['grass_gis.7.0.4'].G_option_required
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_required = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 517
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_requires'):
    _func = _libs['grass_gis.7.0.4'].G_option_requires
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_requires = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 518
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_requires_all'):
    _func = _libs['grass_gis.7.0.4'].G_option_requires_all
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_requires_all = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 519
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_excludes'):
    _func = _libs['grass_gis.7.0.4'].G_option_excludes
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_excludes = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 520
if hasattr(_libs['grass_gis.7.0.4'], 'G_option_collective'):
    _func = _libs['grass_gis.7.0.4'].G_option_collective
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_collective = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 523
if hasattr(_libs['grass_gis.7.0.4'], 'G_mkdir'):
    G_mkdir = _libs['grass_gis.7.0.4'].G_mkdir
    G_mkdir.restype = c_int
    G_mkdir.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 524
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_dirsep'):
    G_is_dirsep = _libs['grass_gis.7.0.4'].G_is_dirsep
    G_is_dirsep.restype = c_int
    G_is_dirsep.argtypes = [c_char]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 525
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_absolute_path'):
    G_is_absolute_path = _libs['grass_gis.7.0.4'].G_is_absolute_path
    G_is_absolute_path.restype = c_int
    G_is_absolute_path.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 526
if hasattr(_libs['grass_gis.7.0.4'], 'G_convert_dirseps_to_host'):
    G_convert_dirseps_to_host = _libs['grass_gis.7.0.4'].G_convert_dirseps_to_host
    G_convert_dirseps_to_host.restype = ReturnString
    G_convert_dirseps_to_host.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 527
if hasattr(_libs['grass_gis.7.0.4'], 'G_convert_dirseps_from_host'):
    G_convert_dirseps_from_host = _libs['grass_gis.7.0.4'].G_convert_dirseps_from_host
    G_convert_dirseps_from_host.restype = ReturnString
    G_convert_dirseps_from_host.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 528
if hasattr(_libs['grass_gis.7.0.4'], 'G_lstat'):
    G_lstat = _libs['grass_gis.7.0.4'].G_lstat
    G_lstat.restype = c_int
    G_lstat.argtypes = [String, POINTER(struct_stat)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 529
if hasattr(_libs['grass_gis.7.0.4'], 'G_stat'):
    G_stat = _libs['grass_gis.7.0.4'].G_stat
    G_stat.restype = c_int
    G_stat.argtypes = [String, POINTER(struct_stat)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 530
if hasattr(_libs['grass_gis.7.0.4'], 'G_owner'):
    G_owner = _libs['grass_gis.7.0.4'].G_owner
    G_owner.restype = c_int
    G_owner.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 533
if hasattr(_libs['grass_gis.7.0.4'], 'G_percent'):
    G_percent = _libs['grass_gis.7.0.4'].G_percent
    G_percent.restype = None
    G_percent.argtypes = [c_long, c_long, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 534
if hasattr(_libs['grass_gis.7.0.4'], 'G_percent_reset'):
    G_percent_reset = _libs['grass_gis.7.0.4'].G_percent_reset
    G_percent_reset.restype = None
    G_percent_reset.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 535
if hasattr(_libs['grass_gis.7.0.4'], 'G_progress'):
    G_progress = _libs['grass_gis.7.0.4'].G_progress
    G_progress.restype = None
    G_progress.argtypes = [c_long, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 536
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_percent_routine'):
    G_set_percent_routine = _libs['grass_gis.7.0.4'].G_set_percent_routine
    G_set_percent_routine.restype = None
    G_set_percent_routine.argtypes = [CFUNCTYPE(UNCHECKED(c_int), c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 537
if hasattr(_libs['grass_gis.7.0.4'], 'G_unset_percent_routine'):
    G_unset_percent_routine = _libs['grass_gis.7.0.4'].G_unset_percent_routine
    G_unset_percent_routine.restype = None
    G_unset_percent_routine.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 540
if hasattr(_libs['grass_gis.7.0.4'], 'G_popen_clear'):
    G_popen_clear = _libs['grass_gis.7.0.4'].G_popen_clear
    G_popen_clear.restype = None
    G_popen_clear.argtypes = [POINTER(struct_Popen)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 541
if hasattr(_libs['grass_gis.7.0.4'], 'G_popen_write'):
    G_popen_write = _libs['grass_gis.7.0.4'].G_popen_write
    G_popen_write.restype = POINTER(FILE)
    G_popen_write.argtypes = [POINTER(struct_Popen), String, POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 542
if hasattr(_libs['grass_gis.7.0.4'], 'G_popen_read'):
    G_popen_read = _libs['grass_gis.7.0.4'].G_popen_read
    G_popen_read.restype = POINTER(FILE)
    G_popen_read.argtypes = [POINTER(struct_Popen), String, POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 543
if hasattr(_libs['grass_gis.7.0.4'], 'G_popen_close'):
    G_popen_close = _libs['grass_gis.7.0.4'].G_popen_close
    G_popen_close.restype = None
    G_popen_close.argtypes = [POINTER(struct_Popen)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 546
if hasattr(_libs['grass_gis.7.0.4'], 'G_setup_plot'):
    G_setup_plot = _libs['grass_gis.7.0.4'].G_setup_plot
    G_setup_plot.restype = None
    G_setup_plot.argtypes = [c_double, c_double, c_double, c_double, CFUNCTYPE(UNCHECKED(c_int), c_int, c_int), CFUNCTYPE(UNCHECKED(c_int), c_int, c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 548
if hasattr(_libs['grass_gis.7.0.4'], 'G_setup_fill'):
    G_setup_fill = _libs['grass_gis.7.0.4'].G_setup_fill
    G_setup_fill.restype = None
    G_setup_fill.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 549
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_where_xy'):
    G_plot_where_xy = _libs['grass_gis.7.0.4'].G_plot_where_xy
    G_plot_where_xy.restype = None
    G_plot_where_xy.argtypes = [c_double, c_double, POINTER(c_int), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 550
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_where_en'):
    G_plot_where_en = _libs['grass_gis.7.0.4'].G_plot_where_en
    G_plot_where_en.restype = None
    G_plot_where_en.argtypes = [c_int, c_int, POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 551
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_point'):
    G_plot_point = _libs['grass_gis.7.0.4'].G_plot_point
    G_plot_point.restype = None
    G_plot_point.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 552
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_line'):
    G_plot_line = _libs['grass_gis.7.0.4'].G_plot_line
    G_plot_line.restype = None
    G_plot_line.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 553
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_line2'):
    G_plot_line2 = _libs['grass_gis.7.0.4'].G_plot_line2
    G_plot_line2.restype = None
    G_plot_line2.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 554
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_polygon'):
    G_plot_polygon = _libs['grass_gis.7.0.4'].G_plot_polygon
    G_plot_polygon.restype = c_int
    G_plot_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 555
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_area'):
    G_plot_area = _libs['grass_gis.7.0.4'].G_plot_area
    G_plot_area.restype = c_int
    G_plot_area.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(c_int), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 556
if hasattr(_libs['grass_gis.7.0.4'], 'G_plot_fx'):
    G_plot_fx = _libs['grass_gis.7.0.4'].G_plot_fx
    G_plot_fx.restype = None
    G_plot_fx.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double), c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 559
if hasattr(_libs['grass_gis.7.0.4'], 'G_pole_in_polygon'):
    G_pole_in_polygon = _libs['grass_gis.7.0.4'].G_pole_in_polygon
    G_pole_in_polygon.restype = c_int
    G_pole_in_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 562
if hasattr(_libs['grass_gis.7.0.4'], 'G_program_name'):
    G_program_name = _libs['grass_gis.7.0.4'].G_program_name
    G_program_name.restype = ReturnString
    G_program_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 563
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_program_name'):
    G_set_program_name = _libs['grass_gis.7.0.4'].G_set_program_name
    G_set_program_name.restype = None
    G_set_program_name.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 566
if hasattr(_libs['grass_gis.7.0.4'], 'G_projection'):
    G_projection = _libs['grass_gis.7.0.4'].G_projection
    G_projection.restype = c_int
    G_projection.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 569
if hasattr(_libs['grass_gis.7.0.4'], 'G_projection_units'):
    G_projection_units = _libs['grass_gis.7.0.4'].G_projection_units
    G_projection_units.restype = c_int
    G_projection_units.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 570
if hasattr(_libs['grass_gis.7.0.4'], 'G_projection_name'):
    G_projection_name = _libs['grass_gis.7.0.4'].G_projection_name
    G_projection_name.restype = ReturnString
    G_projection_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 573
if hasattr(_libs['grass_gis.7.0.4'], 'G_database_unit_name'):
    G_database_unit_name = _libs['grass_gis.7.0.4'].G_database_unit_name
    G_database_unit_name.restype = ReturnString
    G_database_unit_name.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 574
if hasattr(_libs['grass_gis.7.0.4'], 'G_database_projection_name'):
    G_database_projection_name = _libs['grass_gis.7.0.4'].G_database_projection_name
    G_database_projection_name.restype = ReturnString
    G_database_projection_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 575
if hasattr(_libs['grass_gis.7.0.4'], 'G_database_datum_name'):
    G_database_datum_name = _libs['grass_gis.7.0.4'].G_database_datum_name
    G_database_datum_name.restype = ReturnString
    G_database_datum_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 576
if hasattr(_libs['grass_gis.7.0.4'], 'G_database_ellipse_name'):
    G_database_ellipse_name = _libs['grass_gis.7.0.4'].G_database_ellipse_name
    G_database_ellipse_name.restype = ReturnString
    G_database_ellipse_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 577
if hasattr(_libs['grass_gis.7.0.4'], 'G_database_units_to_meters_factor'):
    G_database_units_to_meters_factor = _libs['grass_gis.7.0.4'].G_database_units_to_meters_factor
    G_database_units_to_meters_factor.restype = c_double
    G_database_units_to_meters_factor.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 578
if hasattr(_libs['grass_gis.7.0.4'], 'G_database_epsg_code'):
    G_database_epsg_code = _libs['grass_gis.7.0.4'].G_database_epsg_code
    G_database_epsg_code.restype = ReturnString
    G_database_epsg_code.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 581
if hasattr(_libs['grass_gis.7.0.4'], 'G_put_window'):
    G_put_window = _libs['grass_gis.7.0.4'].G_put_window
    G_put_window.restype = c_int
    G_put_window.argtypes = [POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 582
if hasattr(_libs['grass_gis.7.0.4'], 'G_put_element_window'):
    G_put_element_window = _libs['grass_gis.7.0.4'].G_put_element_window
    G_put_element_window.restype = c_int
    G_put_element_window.argtypes = [POINTER(struct_Cell_head), String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 585
if hasattr(_libs['grass_gis.7.0.4'], 'G_putenv'):
    G_putenv = _libs['grass_gis.7.0.4'].G_putenv
    G_putenv.restype = None
    G_putenv.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 588
if hasattr(_libs['grass_gis.7.0.4'], 'G_meridional_radius_of_curvature'):
    G_meridional_radius_of_curvature = _libs['grass_gis.7.0.4'].G_meridional_radius_of_curvature
    G_meridional_radius_of_curvature.restype = c_double
    G_meridional_radius_of_curvature.argtypes = [c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 589
if hasattr(_libs['grass_gis.7.0.4'], 'G_transverse_radius_of_curvature'):
    G_transverse_radius_of_curvature = _libs['grass_gis.7.0.4'].G_transverse_radius_of_curvature
    G_transverse_radius_of_curvature.restype = c_double
    G_transverse_radius_of_curvature.argtypes = [c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 590
if hasattr(_libs['grass_gis.7.0.4'], 'G_radius_of_conformal_tangent_sphere'):
    G_radius_of_conformal_tangent_sphere = _libs['grass_gis.7.0.4'].G_radius_of_conformal_tangent_sphere
    G_radius_of_conformal_tangent_sphere.restype = c_double
    G_radius_of_conformal_tangent_sphere.argtypes = [c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 593
if hasattr(_libs['grass_gis.7.0.4'], 'G__read_Cell_head'):
    G__read_Cell_head = _libs['grass_gis.7.0.4'].G__read_Cell_head
    G__read_Cell_head.restype = None
    G__read_Cell_head.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 594
if hasattr(_libs['grass_gis.7.0.4'], 'G__read_Cell_head_array'):
    G__read_Cell_head_array = _libs['grass_gis.7.0.4'].G__read_Cell_head_array
    G__read_Cell_head_array.restype = None
    G__read_Cell_head_array.argtypes = [POINTER(POINTER(c_char)), POINTER(struct_Cell_head), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 597
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove'):
    G_remove = _libs['grass_gis.7.0.4'].G_remove
    G_remove.restype = c_int
    G_remove.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 598
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove_misc'):
    G_remove_misc = _libs['grass_gis.7.0.4'].G_remove_misc
    G_remove_misc.restype = c_int
    G_remove_misc.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 601
if hasattr(_libs['grass_gis.7.0.4'], 'G_rename_file'):
    G_rename_file = _libs['grass_gis.7.0.4'].G_rename_file
    G_rename_file.restype = c_int
    G_rename_file.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 602
if hasattr(_libs['grass_gis.7.0.4'], 'G_rename'):
    G_rename = _libs['grass_gis.7.0.4'].G_rename
    G_rename.restype = c_int
    G_rename.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 605
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_rhumbline_equation'):
    G_begin_rhumbline_equation = _libs['grass_gis.7.0.4'].G_begin_rhumbline_equation
    G_begin_rhumbline_equation.restype = c_int
    G_begin_rhumbline_equation.argtypes = [c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 606
if hasattr(_libs['grass_gis.7.0.4'], 'G_rhumbline_lat_from_lon'):
    G_rhumbline_lat_from_lon = _libs['grass_gis.7.0.4'].G_rhumbline_lat_from_lon
    G_rhumbline_lat_from_lon.restype = c_double
    G_rhumbline_lat_from_lon.argtypes = [c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 609
if hasattr(_libs['grass_gis.7.0.4'], 'G_rotate_around_point'):
    G_rotate_around_point = _libs['grass_gis.7.0.4'].G_rotate_around_point
    G_rotate_around_point.restype = None
    G_rotate_around_point.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 610
if hasattr(_libs['grass_gis.7.0.4'], 'G_rotate_around_point_int'):
    G_rotate_around_point_int = _libs['grass_gis.7.0.4'].G_rotate_around_point_int
    G_rotate_around_point_int.restype = None
    G_rotate_around_point_int.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 613
if hasattr(_libs['grass_gis.7.0.4'], 'G_ftell'):
    G_ftell = _libs['grass_gis.7.0.4'].G_ftell
    G_ftell.restype = off_t
    G_ftell.argtypes = [POINTER(FILE)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 614
if hasattr(_libs['grass_gis.7.0.4'], 'G_fseek'):
    G_fseek = _libs['grass_gis.7.0.4'].G_fseek
    G_fseek.restype = None
    G_fseek.argtypes = [POINTER(FILE), off_t, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 617
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_set_window'):
    G_get_set_window = _libs['grass_gis.7.0.4'].G_get_set_window
    G_get_set_window.restype = None
    G_get_set_window.argtypes = [POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 618
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_window'):
    G_set_window = _libs['grass_gis.7.0.4'].G_set_window
    G_set_window.restype = None
    G_set_window.argtypes = [POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 619
if hasattr(_libs['grass_gis.7.0.4'], 'G_unset_window'):
    G_unset_window = _libs['grass_gis.7.0.4'].G_unset_window
    G_unset_window.restype = None
    G_unset_window.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 622
if hasattr(_libs['grass_gis.7.0.4'], 'G_shortest_way'):
    G_shortest_way = _libs['grass_gis.7.0.4'].G_shortest_way
    G_shortest_way.restype = None
    G_shortest_way.argtypes = [POINTER(c_double), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 625
if hasattr(_libs['grass_gis.7.0.4'], 'G_sleep'):
    G_sleep = _libs['grass_gis.7.0.4'].G_sleep
    G_sleep.restype = None
    G_sleep.argtypes = [c_uint]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 628
if hasattr(_libs['grass_gis.7.0.4'], 'G_snprintf'):
    _func = _libs['grass_gis.7.0.4'].G_snprintf
    _restype = c_int
    _argtypes = [String, c_size_t, String]
    G_snprintf = _variadic_function(_func,_restype,_argtypes)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 632
if hasattr(_libs['grass_gis.7.0.4'], 'G_strcasecmp'):
    G_strcasecmp = _libs['grass_gis.7.0.4'].G_strcasecmp
    G_strcasecmp.restype = c_int
    G_strcasecmp.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 633
if hasattr(_libs['grass_gis.7.0.4'], 'G_strncasecmp'):
    G_strncasecmp = _libs['grass_gis.7.0.4'].G_strncasecmp
    G_strncasecmp.restype = c_int
    G_strncasecmp.argtypes = [String, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 634
if hasattr(_libs['grass_gis.7.0.4'], 'G_store'):
    G_store = _libs['grass_gis.7.0.4'].G_store
    G_store.restype = ReturnString
    G_store.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 635
if hasattr(_libs['grass_gis.7.0.4'], 'G_store_upper'):
    G_store_upper = _libs['grass_gis.7.0.4'].G_store_upper
    G_store_upper.restype = ReturnString
    G_store_upper.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 636
if hasattr(_libs['grass_gis.7.0.4'], 'G_store_lower'):
    G_store_lower = _libs['grass_gis.7.0.4'].G_store_lower
    G_store_lower.restype = ReturnString
    G_store_lower.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 637
if hasattr(_libs['grass_gis.7.0.4'], 'G_strchg'):
    G_strchg = _libs['grass_gis.7.0.4'].G_strchg
    G_strchg.restype = ReturnString
    G_strchg.argtypes = [String, c_char, c_char]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 638
if hasattr(_libs['grass_gis.7.0.4'], 'G_str_replace'):
    G_str_replace = _libs['grass_gis.7.0.4'].G_str_replace
    G_str_replace.restype = ReturnString
    G_str_replace.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 639
if hasattr(_libs['grass_gis.7.0.4'], 'G_strip'):
    G_strip = _libs['grass_gis.7.0.4'].G_strip
    G_strip.restype = None
    G_strip.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 640
if hasattr(_libs['grass_gis.7.0.4'], 'G_chop'):
    G_chop = _libs['grass_gis.7.0.4'].G_chop
    G_chop.restype = ReturnString
    G_chop.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 641
if hasattr(_libs['grass_gis.7.0.4'], 'G_str_to_upper'):
    G_str_to_upper = _libs['grass_gis.7.0.4'].G_str_to_upper
    G_str_to_upper.restype = None
    G_str_to_upper.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 642
if hasattr(_libs['grass_gis.7.0.4'], 'G_str_to_lower'):
    G_str_to_lower = _libs['grass_gis.7.0.4'].G_str_to_lower
    G_str_to_lower.restype = None
    G_str_to_lower.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 643
if hasattr(_libs['grass_gis.7.0.4'], 'G_str_to_sql'):
    G_str_to_sql = _libs['grass_gis.7.0.4'].G_str_to_sql
    G_str_to_sql.restype = c_int
    G_str_to_sql.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 644
if hasattr(_libs['grass_gis.7.0.4'], 'G_squeeze'):
    G_squeeze = _libs['grass_gis.7.0.4'].G_squeeze
    G_squeeze.restype = None
    G_squeeze.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 645
if hasattr(_libs['grass_gis.7.0.4'], 'G_strcasestr'):
    G_strcasestr = _libs['grass_gis.7.0.4'].G_strcasestr
    G_strcasestr.restype = ReturnString
    G_strcasestr.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 648
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_tempfile'):
    G_init_tempfile = _libs['grass_gis.7.0.4'].G_init_tempfile
    G_init_tempfile.restype = None
    G_init_tempfile.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 649
if hasattr(_libs['grass_gis.7.0.4'], 'G_tempfile'):
    G_tempfile = _libs['grass_gis.7.0.4'].G_tempfile
    G_tempfile.restype = ReturnString
    G_tempfile.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 650
if hasattr(_libs['grass_gis.7.0.4'], 'G_tempfile_pid'):
    G_tempfile_pid = _libs['grass_gis.7.0.4'].G_tempfile_pid
    G_tempfile_pid.restype = ReturnString
    G_tempfile_pid.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 651
if hasattr(_libs['grass_gis.7.0.4'], 'G_temp_element'):
    G_temp_element = _libs['grass_gis.7.0.4'].G_temp_element
    G_temp_element.restype = None
    G_temp_element.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 654
if hasattr(_libs['grass_gis.7.0.4'], 'G_mktemp'):
    G_mktemp = _libs['grass_gis.7.0.4'].G_mktemp
    G_mktemp.restype = ReturnString
    G_mktemp.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 655
if hasattr(_libs['grass_gis.7.0.4'], 'G_mkstemp'):
    G_mkstemp = _libs['grass_gis.7.0.4'].G_mkstemp
    G_mkstemp.restype = c_int
    G_mkstemp.argtypes = [String, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 656
if hasattr(_libs['grass_gis.7.0.4'], 'G_mkstemp_fp'):
    G_mkstemp_fp = _libs['grass_gis.7.0.4'].G_mkstemp_fp
    G_mkstemp_fp.restype = POINTER(FILE)
    G_mkstemp_fp.argtypes = [String, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 659
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_timestamp'):
    G_init_timestamp = _libs['grass_gis.7.0.4'].G_init_timestamp
    G_init_timestamp.restype = None
    G_init_timestamp.argtypes = [POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 660
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_timestamp'):
    G_set_timestamp = _libs['grass_gis.7.0.4'].G_set_timestamp
    G_set_timestamp.restype = None
    G_set_timestamp.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 661
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_timestamp_range'):
    G_set_timestamp_range = _libs['grass_gis.7.0.4'].G_set_timestamp_range
    G_set_timestamp_range.restype = None
    G_set_timestamp_range.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime), POINTER(struct_DateTime)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 663
if hasattr(_libs['grass_gis.7.0.4'], 'G_write_timestamp'):
    G_write_timestamp = _libs['grass_gis.7.0.4'].G_write_timestamp
    G_write_timestamp.restype = c_int
    G_write_timestamp.argtypes = [POINTER(FILE), POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 664
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_timestamps'):
    G_get_timestamps = _libs['grass_gis.7.0.4'].G_get_timestamps
    G_get_timestamps.restype = None
    G_get_timestamps.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime), POINTER(struct_DateTime), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 665
if hasattr(_libs['grass_gis.7.0.4'], 'G_format_timestamp'):
    G_format_timestamp = _libs['grass_gis.7.0.4'].G_format_timestamp
    G_format_timestamp.restype = c_int
    G_format_timestamp.argtypes = [POINTER(struct_TimeStamp), String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 666
if hasattr(_libs['grass_gis.7.0.4'], 'G_scan_timestamp'):
    G_scan_timestamp = _libs['grass_gis.7.0.4'].G_scan_timestamp
    G_scan_timestamp.restype = c_int
    G_scan_timestamp.argtypes = [POINTER(struct_TimeStamp), String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 667
if hasattr(_libs['grass_gis.7.0.4'], 'G_has_raster_timestamp'):
    G_has_raster_timestamp = _libs['grass_gis.7.0.4'].G_has_raster_timestamp
    G_has_raster_timestamp.restype = c_int
    G_has_raster_timestamp.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 668
if hasattr(_libs['grass_gis.7.0.4'], 'G_read_raster_timestamp'):
    G_read_raster_timestamp = _libs['grass_gis.7.0.4'].G_read_raster_timestamp
    G_read_raster_timestamp.restype = c_int
    G_read_raster_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 669
if hasattr(_libs['grass_gis.7.0.4'], 'G_write_raster_timestamp'):
    G_write_raster_timestamp = _libs['grass_gis.7.0.4'].G_write_raster_timestamp
    G_write_raster_timestamp.restype = c_int
    G_write_raster_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 670
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove_raster_timestamp'):
    G_remove_raster_timestamp = _libs['grass_gis.7.0.4'].G_remove_raster_timestamp
    G_remove_raster_timestamp.restype = c_int
    G_remove_raster_timestamp.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 671
if hasattr(_libs['grass_gis.7.0.4'], 'G_has_vector_timestamp'):
    G_has_vector_timestamp = _libs['grass_gis.7.0.4'].G_has_vector_timestamp
    G_has_vector_timestamp.restype = c_int
    G_has_vector_timestamp.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 672
if hasattr(_libs['grass_gis.7.0.4'], 'G_read_vector_timestamp'):
    G_read_vector_timestamp = _libs['grass_gis.7.0.4'].G_read_vector_timestamp
    G_read_vector_timestamp.restype = c_int
    G_read_vector_timestamp.argtypes = [String, String, String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 673
if hasattr(_libs['grass_gis.7.0.4'], 'G_write_vector_timestamp'):
    G_write_vector_timestamp = _libs['grass_gis.7.0.4'].G_write_vector_timestamp
    G_write_vector_timestamp.restype = c_int
    G_write_vector_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 674
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove_vector_timestamp'):
    G_remove_vector_timestamp = _libs['grass_gis.7.0.4'].G_remove_vector_timestamp
    G_remove_vector_timestamp.restype = c_int
    G_remove_vector_timestamp.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 675
if hasattr(_libs['grass_gis.7.0.4'], 'G_has_raster3d_timestamp'):
    G_has_raster3d_timestamp = _libs['grass_gis.7.0.4'].G_has_raster3d_timestamp
    G_has_raster3d_timestamp.restype = c_int
    G_has_raster3d_timestamp.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 676
if hasattr(_libs['grass_gis.7.0.4'], 'G_read_raster3d_timestamp'):
    G_read_raster3d_timestamp = _libs['grass_gis.7.0.4'].G_read_raster3d_timestamp
    G_read_raster3d_timestamp.restype = c_int
    G_read_raster3d_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 677
if hasattr(_libs['grass_gis.7.0.4'], 'G_remove_raster3d_timestamp'):
    G_remove_raster3d_timestamp = _libs['grass_gis.7.0.4'].G_remove_raster3d_timestamp
    G_remove_raster3d_timestamp.restype = c_int
    G_remove_raster3d_timestamp.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 678
if hasattr(_libs['grass_gis.7.0.4'], 'G_write_raster3d_timestamp'):
    G_write_raster3d_timestamp = _libs['grass_gis.7.0.4'].G_write_raster3d_timestamp
    G_write_raster3d_timestamp.restype = c_int
    G_write_raster3d_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 681
if hasattr(_libs['grass_gis.7.0.4'], 'G_tokenize'):
    G_tokenize = _libs['grass_gis.7.0.4'].G_tokenize
    G_tokenize.restype = POINTER(POINTER(c_char))
    G_tokenize.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 682
if hasattr(_libs['grass_gis.7.0.4'], 'G_tokenize2'):
    G_tokenize2 = _libs['grass_gis.7.0.4'].G_tokenize2
    G_tokenize2.restype = POINTER(POINTER(c_char))
    G_tokenize2.argtypes = [String, String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 683
if hasattr(_libs['grass_gis.7.0.4'], 'G_number_of_tokens'):
    G_number_of_tokens = _libs['grass_gis.7.0.4'].G_number_of_tokens
    G_number_of_tokens.restype = c_int
    G_number_of_tokens.argtypes = [POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 684
if hasattr(_libs['grass_gis.7.0.4'], 'G_free_tokens'):
    G_free_tokens = _libs['grass_gis.7.0.4'].G_free_tokens
    G_free_tokens.restype = None
    G_free_tokens.argtypes = [POINTER(POINTER(c_char))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 687
if hasattr(_libs['grass_gis.7.0.4'], 'G_trim_decimal'):
    G_trim_decimal = _libs['grass_gis.7.0.4'].G_trim_decimal
    G_trim_decimal.restype = None
    G_trim_decimal.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 690
if hasattr(_libs['grass_gis.7.0.4'], 'G_meters_to_units_factor'):
    G_meters_to_units_factor = _libs['grass_gis.7.0.4'].G_meters_to_units_factor
    G_meters_to_units_factor.restype = c_double
    G_meters_to_units_factor.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 691
if hasattr(_libs['grass_gis.7.0.4'], 'G_meters_to_units_factor_sq'):
    G_meters_to_units_factor_sq = _libs['grass_gis.7.0.4'].G_meters_to_units_factor_sq
    G_meters_to_units_factor_sq.restype = c_double
    G_meters_to_units_factor_sq.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 692
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_units_name'):
    G_get_units_name = _libs['grass_gis.7.0.4'].G_get_units_name
    G_get_units_name.restype = ReturnString
    G_get_units_name.argtypes = [c_int, c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 693
if hasattr(_libs['grass_gis.7.0.4'], 'G_units'):
    G_units = _libs['grass_gis.7.0.4'].G_units
    G_units.restype = c_int
    G_units.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 694
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_units_type_spatial'):
    G_is_units_type_spatial = _libs['grass_gis.7.0.4'].G_is_units_type_spatial
    G_is_units_type_spatial.restype = c_int
    G_is_units_type_spatial.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 695
if hasattr(_libs['grass_gis.7.0.4'], 'G_is_units_type_temporal'):
    G_is_units_type_temporal = _libs['grass_gis.7.0.4'].G_is_units_type_temporal
    G_is_units_type_temporal.restype = c_int
    G_is_units_type_temporal.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 699
if hasattr(_libs['grass_gis.7.0.4'], 'G_rc_path'):
    G_rc_path = _libs['grass_gis.7.0.4'].G_rc_path
    G_rc_path.restype = ReturnString
    G_rc_path.argtypes = [String, String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 703
if hasattr(_libs['grass_gis.7.0.4'], 'G_verbose'):
    G_verbose = _libs['grass_gis.7.0.4'].G_verbose
    G_verbose.restype = c_int
    G_verbose.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 704
if hasattr(_libs['grass_gis.7.0.4'], 'G_verbose_min'):
    G_verbose_min = _libs['grass_gis.7.0.4'].G_verbose_min
    G_verbose_min.restype = c_int
    G_verbose_min.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 705
if hasattr(_libs['grass_gis.7.0.4'], 'G_verbose_std'):
    G_verbose_std = _libs['grass_gis.7.0.4'].G_verbose_std
    G_verbose_std.restype = c_int
    G_verbose_std.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 706
if hasattr(_libs['grass_gis.7.0.4'], 'G_verbose_max'):
    G_verbose_max = _libs['grass_gis.7.0.4'].G_verbose_max
    G_verbose_max.restype = c_int
    G_verbose_max.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 707
if hasattr(_libs['grass_gis.7.0.4'], 'G_set_verbose'):
    G_set_verbose = _libs['grass_gis.7.0.4'].G_set_verbose
    G_set_verbose.restype = c_int
    G_set_verbose.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 710
if hasattr(_libs['grass_gis.7.0.4'], 'G_3dview_warning'):
    G_3dview_warning = _libs['grass_gis.7.0.4'].G_3dview_warning
    G_3dview_warning.restype = None
    G_3dview_warning.argtypes = [c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 711
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_3dview_defaults'):
    G_get_3dview_defaults = _libs['grass_gis.7.0.4'].G_get_3dview_defaults
    G_get_3dview_defaults.restype = c_int
    G_get_3dview_defaults.argtypes = [POINTER(struct_G_3dview), POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 712
if hasattr(_libs['grass_gis.7.0.4'], 'G_put_3dview'):
    G_put_3dview = _libs['grass_gis.7.0.4'].G_put_3dview
    G_put_3dview.restype = c_int
    G_put_3dview.argtypes = [String, String, POINTER(struct_G_3dview), POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 714
if hasattr(_libs['grass_gis.7.0.4'], 'G_get_3dview'):
    G_get_3dview = _libs['grass_gis.7.0.4'].G_get_3dview
    G_get_3dview.restype = c_int
    G_get_3dview.argtypes = [String, String, POINTER(struct_G_3dview)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 717
if hasattr(_libs['grass_gis.7.0.4'], 'G_whoami'):
    G_whoami = _libs['grass_gis.7.0.4'].G_whoami
    G_whoami.restype = ReturnString
    G_whoami.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 720
if hasattr(_libs['grass_gis.7.0.4'], 'G_adjust_window_to_box'):
    G_adjust_window_to_box = _libs['grass_gis.7.0.4'].G_adjust_window_to_box
    G_adjust_window_to_box.restype = None
    G_adjust_window_to_box.argtypes = [POINTER(struct_Cell_head), POINTER(struct_Cell_head), c_int, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 724
if hasattr(_libs['grass_gis.7.0.4'], 'G_format_northing'):
    G_format_northing = _libs['grass_gis.7.0.4'].G_format_northing
    G_format_northing.restype = None
    G_format_northing.argtypes = [c_double, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 725
if hasattr(_libs['grass_gis.7.0.4'], 'G_format_easting'):
    G_format_easting = _libs['grass_gis.7.0.4'].G_format_easting
    G_format_easting.restype = None
    G_format_easting.argtypes = [c_double, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 726
if hasattr(_libs['grass_gis.7.0.4'], 'G_format_resolution'):
    G_format_resolution = _libs['grass_gis.7.0.4'].G_format_resolution
    G_format_resolution.restype = None
    G_format_resolution.argtypes = [c_double, String, c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 729
if hasattr(_libs['grass_gis.7.0.4'], 'G_point_in_region'):
    G_point_in_region = _libs['grass_gis.7.0.4'].G_point_in_region
    G_point_in_region.restype = c_int
    G_point_in_region.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 730
if hasattr(_libs['grass_gis.7.0.4'], 'G_point_in_window'):
    G_point_in_window = _libs['grass_gis.7.0.4'].G_point_in_window
    G_point_in_window.restype = c_int
    G_point_in_window.argtypes = [c_double, c_double, POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 733
if hasattr(_libs['grass_gis.7.0.4'], 'G_limit_east'):
    G_limit_east = _libs['grass_gis.7.0.4'].G_limit_east
    G_limit_east.restype = c_int
    G_limit_east.argtypes = [POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 734
if hasattr(_libs['grass_gis.7.0.4'], 'G_limit_west'):
    G_limit_west = _libs['grass_gis.7.0.4'].G_limit_west
    G_limit_west.restype = c_int
    G_limit_west.argtypes = [POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 735
if hasattr(_libs['grass_gis.7.0.4'], 'G_limit_north'):
    G_limit_north = _libs['grass_gis.7.0.4'].G_limit_north
    G_limit_north.restype = c_int
    G_limit_north.argtypes = [POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 736
if hasattr(_libs['grass_gis.7.0.4'], 'G_limit_south'):
    G_limit_south = _libs['grass_gis.7.0.4'].G_limit_south
    G_limit_south.restype = c_int
    G_limit_south.argtypes = [POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 739
if hasattr(_libs['grass_gis.7.0.4'], 'G_window_overlap'):
    G_window_overlap = _libs['grass_gis.7.0.4'].G_window_overlap
    G_window_overlap.restype = c_int
    G_window_overlap.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 741
if hasattr(_libs['grass_gis.7.0.4'], 'G_window_percentage_overlap'):
    G_window_percentage_overlap = _libs['grass_gis.7.0.4'].G_window_percentage_overlap
    G_window_percentage_overlap.restype = c_double
    G_window_percentage_overlap.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 745
if hasattr(_libs['grass_gis.7.0.4'], 'G_scan_northing'):
    G_scan_northing = _libs['grass_gis.7.0.4'].G_scan_northing
    G_scan_northing.restype = c_int
    G_scan_northing.argtypes = [String, POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 746
if hasattr(_libs['grass_gis.7.0.4'], 'G_scan_easting'):
    G_scan_easting = _libs['grass_gis.7.0.4'].G_scan_easting
    G_scan_easting.restype = c_int
    G_scan_easting.argtypes = [String, POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 747
if hasattr(_libs['grass_gis.7.0.4'], 'G_scan_resolution'):
    G_scan_resolution = _libs['grass_gis.7.0.4'].G_scan_resolution
    G_scan_resolution.restype = c_int
    G_scan_resolution.argtypes = [String, POINTER(c_double), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 750
if hasattr(_libs['grass_gis.7.0.4'], 'G_adjust_east_longitude'):
    G_adjust_east_longitude = _libs['grass_gis.7.0.4'].G_adjust_east_longitude
    G_adjust_east_longitude.restype = c_double
    G_adjust_east_longitude.argtypes = [c_double, c_double]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 751
if hasattr(_libs['grass_gis.7.0.4'], 'G_adjust_easting'):
    G_adjust_easting = _libs['grass_gis.7.0.4'].G_adjust_easting
    G_adjust_easting.restype = c_double
    G_adjust_easting.argtypes = [c_double, POINTER(struct_Cell_head)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 752
if hasattr(_libs['grass_gis.7.0.4'], 'G__init_window'):
    G__init_window = _libs['grass_gis.7.0.4'].G__init_window
    G__init_window.restype = None
    G__init_window.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 755
if hasattr(_libs['grass_gis.7.0.4'], 'G_begin_execute'):
    G_begin_execute = _libs['grass_gis.7.0.4'].G_begin_execute
    G_begin_execute.restype = None
    G_begin_execute.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None), POINTER(POINTER(None)), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 756
if hasattr(_libs['grass_gis.7.0.4'], 'G_end_execute'):
    G_end_execute = _libs['grass_gis.7.0.4'].G_end_execute
    G_end_execute.restype = None
    G_end_execute.argtypes = [POINTER(POINTER(None))]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 757
if hasattr(_libs['grass_gis.7.0.4'], 'G_init_workers'):
    G_init_workers = _libs['grass_gis.7.0.4'].G_init_workers
    G_init_workers.restype = None
    G_init_workers.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 758
if hasattr(_libs['grass_gis.7.0.4'], 'G_finish_workers'):
    G_finish_workers = _libs['grass_gis.7.0.4'].G_finish_workers
    G_finish_workers.restype = None
    G_finish_workers.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 761
if hasattr(_libs['grass_gis.7.0.4'], 'G__write_Cell_head'):
    G__write_Cell_head = _libs['grass_gis.7.0.4'].G__write_Cell_head
    G__write_Cell_head.restype = None
    G__write_Cell_head.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 762
if hasattr(_libs['grass_gis.7.0.4'], 'G__write_Cell_head3'):
    G__write_Cell_head3 = _libs['grass_gis.7.0.4'].G__write_Cell_head3
    G__write_Cell_head3.restype = None
    G__write_Cell_head3.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 765
if hasattr(_libs['grass_gis.7.0.4'], 'G_write_zeros'):
    G_write_zeros = _libs['grass_gis.7.0.4'].G_write_zeros
    G_write_zeros.restype = None
    G_write_zeros.argtypes = [c_int, c_size_t]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 768
if hasattr(_libs['grass_gis.7.0.4'], 'G_xdr_get_int'):
    G_xdr_get_int = _libs['grass_gis.7.0.4'].G_xdr_get_int
    G_xdr_get_int.restype = None
    G_xdr_get_int.argtypes = [POINTER(c_int), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 769
if hasattr(_libs['grass_gis.7.0.4'], 'G_xdr_put_int'):
    G_xdr_put_int = _libs['grass_gis.7.0.4'].G_xdr_put_int
    G_xdr_put_int.restype = None
    G_xdr_put_int.argtypes = [POINTER(None), POINTER(c_int)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 770
if hasattr(_libs['grass_gis.7.0.4'], 'G_xdr_get_float'):
    G_xdr_get_float = _libs['grass_gis.7.0.4'].G_xdr_get_float
    G_xdr_get_float.restype = None
    G_xdr_get_float.argtypes = [POINTER(c_float), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 771
if hasattr(_libs['grass_gis.7.0.4'], 'G_xdr_put_float'):
    G_xdr_put_float = _libs['grass_gis.7.0.4'].G_xdr_put_float
    G_xdr_put_float.restype = None
    G_xdr_put_float.argtypes = [POINTER(None), POINTER(c_float)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 772
if hasattr(_libs['grass_gis.7.0.4'], 'G_xdr_get_double'):
    G_xdr_get_double = _libs['grass_gis.7.0.4'].G_xdr_get_double
    G_xdr_get_double.restype = None
    G_xdr_get_double.argtypes = [POINTER(c_double), POINTER(None)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 773
if hasattr(_libs['grass_gis.7.0.4'], 'G_xdr_put_double'):
    G_xdr_put_double = _libs['grass_gis.7.0.4'].G_xdr_put_double
    G_xdr_put_double.restype = None
    G_xdr_put_double.argtypes = [POINTER(None), POINTER(c_double)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 776
if hasattr(_libs['grass_gis.7.0.4'], 'G_zero'):
    G_zero = _libs['grass_gis.7.0.4'].G_zero
    G_zero.restype = None
    G_zero.argtypes = [POINTER(None), c_int]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 779
if hasattr(_libs['grass_gis.7.0.4'], 'G_zone'):
    G_zone = _libs['grass_gis.7.0.4'].G_zone
    G_zone.restype = c_int
    G_zone.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 7
try:
    DATETIME_YEAR = 101
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 7
try:
    DATETIME_MONTH = 102
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 7
try:
    DATETIME_DAY = 103
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 7
try:
    DATETIME_HOUR = 104
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 7
try:
    DATETIME_MINUTE = 105
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 7
try:
    DATETIME_SECOND = 106
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 40
try:
    GIS_H_VERSION = '$Revision: 67364 $'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 40
try:
    GIS_H_DATE = '$Date: 2015-12-24 16:07:44 +0100 (Thu, 24 Dec 2015) $'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 41
def G_gisinit(pgm):
    return (G__gisinit (GIS_H_VERSION, pgm))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 41
try:
    G_no_gisinit = (G__no_gisinit (GIS_H_VERSION))
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 44
try:
    TRUE = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 47
try:
    FALSE = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 52
try:
    PRI_OFF_T = 'ld'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 55
try:
    NEWLINE = '\\n'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 58
try:
    HOST_NEWLINE = '\n'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_UNDEFINED = (-1)
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_UNKNOWN = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_ACRES = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_HECTARES = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_KILOMETERS = 3
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_METERS = 4
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_MILES = 5
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_FEET = 6
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_RADIANS = 7
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_DEGREES = 8
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 63
try:
    U_USFEET = 9
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 64
try:
    U_YEARS = DATETIME_YEAR
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 64
try:
    U_MONTHS = DATETIME_MONTH
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 64
try:
    U_DAYS = DATETIME_DAY
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 64
try:
    U_HOURS = DATETIME_HOUR
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 64
try:
    U_MINUTES = DATETIME_MINUTE
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 64
try:
    U_SECONDS = DATETIME_SECOND
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 66
try:
    PROJECTION_XY = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 67
try:
    PROJECTION_UTM = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 68
try:
    PROJECTION_SP = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 69
try:
    PROJECTION_LL = 3
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 70
try:
    PROJECTION_OTHER = 99
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 71
try:
    PROJECTION_FILE = 'PROJ_INFO'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 71
try:
    UNIT_FILE = 'PROJ_UNITS'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 71
try:
    EPSG_FILE = 'PROJ_EPSG'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 75
try:
    CONFIG_DIR = '.grass7'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 79
try:
    M_PI = 3.141592653589793
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 81
try:
    M_PI_2 = 1.5707963267948966
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 83
try:
    M_PI_4 = 0.7853981633974483
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 85
try:
    GRASS_EPSILON = 1e-15
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 87
try:
    G_VAR_GISRC = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 87
try:
    G_VAR_MAPSET = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 89
try:
    G_GISRC_MODE_FILE = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 89
try:
    G_GISRC_MODE_MEMORY = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 91
try:
    TYPE_INTEGER = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 91
try:
    TYPE_DOUBLE = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 91
try:
    TYPE_STRING = 3
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 91
try:
    YES = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 91
try:
    NO = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 93
try:
    GNAME_MAX = 256
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 93
try:
    GMAPSET_MAX = 256
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 94
try:
    GPATH_MAX = 4096
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 96
try:
    GBASENAME_SEP = '_'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 109
def deserialize_int32_le(buf):
    return (((((buf [0]) << 0) | ((buf [1]) << 8)) | ((buf [2]) << 16)) | ((buf [3]) << 24))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 121
def deserialize_int32_be(buf):
    return (((((buf [0]) << 24) | ((buf [1]) << 16)) | ((buf [2]) << 8)) | ((buf [3]) << 0))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 126
try:
    GRASS_DIRSEP = '/'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 130
try:
    HOST_DIRSEP = '/'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 130
try:
    G_DEV_NULL = '/dev/null'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 330
try:
    G_INFO_FORMAT_STANDARD = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 330
try:
    G_INFO_FORMAT_GUI = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 330
try:
    G_INFO_FORMAT_SILENT = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 330
try:
    G_INFO_FORMAT_PLAIN = 3
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 332
try:
    G_ICON_CROSS = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 332
try:
    G_ICON_BOX = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 332
try:
    G_ICON_ARROW = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 334
try:
    DEFAULT_FG_COLOR = 'black'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 334
try:
    DEFAULT_BG_COLOR = 'white'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 336
try:
    G_FATAL_EXIT = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 336
try:
    G_FATAL_PRINT = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 336
try:
    G_FATAL_RETURN = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 338
try:
    ENDIAN_LITTLE = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 338
try:
    ENDIAN_BIG = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 338
try:
    ENDIAN_OTHER = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 343
try:
    GV_KEY_COLUMN = 'cat'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 57
def G_alloca(n):
    return (G_malloc (n))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 57
def G_freea(p):
    return (G_free (p))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 68
try:
    RELDIR = '?'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 75
def G_incr_void_ptr(ptr, size):
    return (ptr + size)

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 92
def G_malloc(n):
    return (G__malloc ('<ctypesgen>', 0, n))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 92
def G_calloc(m, n):
    return (G__calloc ('<ctypesgen>', 0, m, n))

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/defs/gis.h: 92
def G_realloc(p, n):
    return (G__realloc ('<ctypesgen>', 0, p, n))

Cell_head = struct_Cell_head # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 382

G_3dview = struct_G_3dview # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 444

Key_Value = struct_Key_Value # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 471

Option = struct_Option # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 501

Flag = struct_Flag # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 530

GModule = struct_GModule # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 546

TimeStamp = struct_TimeStamp # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 556

Counter = struct_Counter # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 562

Popen = struct_Popen # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 566

_Color_Value_ = struct__Color_Value_ # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 575

_Color_Rule_ = struct__Color_Rule_ # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 583

_Color_Info_ = struct__Color_Info_ # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 590

Colors = struct_Colors # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 617

ilist = struct_ilist # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 641

# No inserted files

