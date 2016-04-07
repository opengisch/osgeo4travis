'''Wrapper for rtree.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include -I/usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_rtree.7.0.2 /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h -o OBJ.x86_64-unknown-linux-gnu/rtree.py

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

_libs["grass_rtree.7.0.2"] = load_library("grass_rtree.7.0.2")

# 1 libraries
# End libraries

# No modules

__off_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 141

off_t = __off_t # /usr/include/x86_64-linux-gnu/sys/types.h: 87

RectReal = c_double # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 28

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 57
class struct_RTree_Rect(Structure):
    pass

struct_RTree_Rect.__slots__ = [
    'boundary',
]
struct_RTree_Rect._fields_ = [
    ('boundary', POINTER(RectReal)),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 77
class struct_RTree_Node(Structure):
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 64
class union_RTree_Child(Union):
    pass

union_RTree_Child.__slots__ = [
    'id',
    'ptr',
    'pos',
]
union_RTree_Child._fields_ = [
    ('id', c_int),
    ('ptr', POINTER(struct_RTree_Node)),
    ('pos', off_t),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 71
class struct_RTree_Branch(Structure):
    pass

struct_RTree_Branch.__slots__ = [
    'rect',
    'child',
]
struct_RTree_Branch._fields_ = [
    ('rect', struct_RTree_Rect),
    ('child', union_RTree_Child),
]

struct_RTree_Node.__slots__ = [
    'count',
    'level',
    'branch',
]
struct_RTree_Node._fields_ = [
    ('count', c_int),
    ('level', c_int),
    ('branch', POINTER(struct_RTree_Branch)),
]

SearchHitCallback = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(struct_RTree_Rect), POINTER(None)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 91

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 128
class struct_RTree(Structure):
    pass

rt_search_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 95

rt_insert_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, c_int, POINTER(struct_RTree)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 97

rt_delete_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, POINTER(struct_RTree)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 98

rt_valid_child_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(union_RTree_Child)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 99

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 103
class struct_nstack(Structure):
    pass

struct_nstack.__slots__ = [
    'sn',
    'branch_id',
    'pos',
]
struct_nstack._fields_ = [
    ('sn', POINTER(struct_RTree_Node)),
    ('branch_id', c_int),
    ('pos', off_t),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 111
class struct_NodeBuffer(Structure):
    pass

struct_NodeBuffer.__slots__ = [
    'n',
    'pos',
    'dirty',
]
struct_NodeBuffer._fields_ = [
    ('n', struct_RTree_Node),
    ('pos', off_t),
    ('dirty', c_char),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 119
class struct_RTree_PartitionVars(Structure):
    pass

struct_RTree_PartitionVars.__slots__ = [
    'partition',
    'total',
    'minfill',
    'taken',
    'count',
    'cover',
    'area',
]
struct_RTree_PartitionVars._fields_ = [
    ('partition', c_int * (9 + 1)),
    ('total', c_int),
    ('minfill', c_int),
    ('taken', c_int * (9 + 1)),
    ('count', c_int * 2),
    ('cover', struct_RTree_Rect * 2),
    ('area', RectReal * 2),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 155
class struct__recycle(Structure):
    pass

struct__recycle.__slots__ = [
    'avail',
    'alloc',
    'pos',
]
struct__recycle._fields_ = [
    ('avail', c_int),
    ('alloc', c_int),
    ('pos', POINTER(off_t)),
]

struct_RTree.__slots__ = [
    'fd',
    'ndims',
    'nsides',
    'ndims_alloc',
    'nsides_alloc',
    'nodesize',
    'branchsize',
    'rectsize',
    'n_nodes',
    'n_leafs',
    'rootlevel',
    'nodecard',
    'leafcard',
    'min_node_fill',
    'min_leaf_fill',
    'minfill_node_split',
    'minfill_leaf_split',
    'overflow',
    'free_nodes',
    'nb',
    'used',
    'insert_rect',
    'delete_rect',
    'search_rect',
    'valid_child',
    'root',
    'ns',
    'p',
    'BranchBuf',
    'tmpb1',
    'tmpb2',
    'c',
    'BranchCount',
    'rect_0',
    'rect_1',
    'upperrect',
    'orect',
    'center_n',
    'rootpos',
]
struct_RTree._fields_ = [
    ('fd', c_int),
    ('ndims', c_ubyte),
    ('nsides', c_ubyte),
    ('ndims_alloc', c_ubyte),
    ('nsides_alloc', c_ubyte),
    ('nodesize', c_int),
    ('branchsize', c_int),
    ('rectsize', c_int),
    ('n_nodes', c_int),
    ('n_leafs', c_int),
    ('rootlevel', c_int),
    ('nodecard', c_int),
    ('leafcard', c_int),
    ('min_node_fill', c_int),
    ('min_leaf_fill', c_int),
    ('minfill_node_split', c_int),
    ('minfill_leaf_split', c_int),
    ('overflow', c_char),
    ('free_nodes', struct__recycle),
    ('nb', POINTER(POINTER(struct_NodeBuffer))),
    ('used', POINTER(POINTER(c_int))),
    ('insert_rect', POINTER(rt_insert_fn)),
    ('delete_rect', POINTER(rt_delete_fn)),
    ('search_rect', POINTER(rt_search_fn)),
    ('valid_child', POINTER(rt_valid_child_fn)),
    ('root', POINTER(struct_RTree_Node)),
    ('ns', POINTER(struct_nstack)),
    ('p', struct_RTree_PartitionVars),
    ('BranchBuf', POINTER(struct_RTree_Branch)),
    ('tmpb1', struct_RTree_Branch),
    ('tmpb2', struct_RTree_Branch),
    ('c', struct_RTree_Branch),
    ('BranchCount', c_int),
    ('rect_0', struct_RTree_Rect),
    ('rect_1', struct_RTree_Rect),
    ('upperrect', struct_RTree_Rect),
    ('orect', struct_RTree_Rect),
    ('center_n', POINTER(RectReal)),
    ('rootpos', off_t),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 196
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeSearch'):
    RTreeSearch = _libs['grass_rtree.7.0.2'].RTreeSearch
    RTreeSearch.restype = c_int
    RTreeSearch.argtypes = [POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 198
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeInsertRect'):
    RTreeInsertRect = _libs['grass_rtree.7.0.2'].RTreeInsertRect
    RTreeInsertRect.restype = c_int
    RTreeInsertRect.argtypes = [POINTER(struct_RTree_Rect), c_int, POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 199
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeSetRect1D'):
    RTreeSetRect1D = _libs['grass_rtree.7.0.2'].RTreeSetRect1D
    RTreeSetRect1D.restype = None
    RTreeSetRect1D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 201
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeSetRect2D'):
    RTreeSetRect2D = _libs['grass_rtree.7.0.2'].RTreeSetRect2D
    RTreeSetRect2D.restype = None
    RTreeSetRect2D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 203
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeSetRect3D'):
    RTreeSetRect3D = _libs['grass_rtree.7.0.2'].RTreeSetRect3D
    RTreeSetRect3D.restype = None
    RTreeSetRect3D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 206
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeSetRect4D'):
    RTreeSetRect4D = _libs['grass_rtree.7.0.2'].RTreeSetRect4D
    RTreeSetRect4D.restype = None
    RTreeSetRect4D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 209
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeDeleteRect'):
    RTreeDeleteRect = _libs['grass_rtree.7.0.2'].RTreeDeleteRect
    RTreeDeleteRect.restype = c_int
    RTreeDeleteRect.argtypes = [POINTER(struct_RTree_Rect), c_int, POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 210
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreePrintRect'):
    RTreePrintRect = _libs['grass_rtree.7.0.2'].RTreePrintRect
    RTreePrintRect.restype = None
    RTreePrintRect.argtypes = [POINTER(struct_RTree_Rect), c_int, POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 211
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeCreateTree'):
    RTreeCreateTree = _libs['grass_rtree.7.0.2'].RTreeCreateTree
    RTreeCreateTree.restype = POINTER(struct_RTree)
    RTreeCreateTree.argtypes = [c_int, off_t, c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 212
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeSetOverflow'):
    RTreeSetOverflow = _libs['grass_rtree.7.0.2'].RTreeSetOverflow
    RTreeSetOverflow.restype = None
    RTreeSetOverflow.argtypes = [POINTER(struct_RTree), c_char]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 213
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeDestroyTree'):
    RTreeDestroyTree = _libs['grass_rtree.7.0.2'].RTreeDestroyTree
    RTreeDestroyTree.restype = None
    RTreeDestroyTree.argtypes = [POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 214
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeOverlap'):
    RTreeOverlap = _libs['grass_rtree.7.0.2'].RTreeOverlap
    RTreeOverlap.restype = c_int
    RTreeOverlap.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree_Rect), POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 215
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeContained'):
    RTreeContained = _libs['grass_rtree.7.0.2'].RTreeContained
    RTreeContained.restype = c_int
    RTreeContained.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree_Rect), POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 216
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeContains'):
    RTreeContains = _libs['grass_rtree.7.0.2'].RTreeContains
    RTreeContains.restype = c_int
    RTreeContains.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree_Rect), POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 219
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeAllocNode'):
    RTreeAllocNode = _libs['grass_rtree.7.0.2'].RTreeAllocNode
    RTreeAllocNode.restype = POINTER(struct_RTree_Node)
    RTreeAllocNode.argtypes = [POINTER(struct_RTree), c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 220
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeInitNode'):
    RTreeInitNode = _libs['grass_rtree.7.0.2'].RTreeInitNode
    RTreeInitNode.restype = None
    RTreeInitNode.argtypes = [POINTER(struct_RTree), POINTER(struct_RTree_Node), c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 221
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeCopyNode'):
    RTreeCopyNode = _libs['grass_rtree.7.0.2'].RTreeCopyNode
    RTreeCopyNode.restype = None
    RTreeCopyNode.argtypes = [POINTER(struct_RTree_Node), POINTER(struct_RTree_Node), POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 222
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeFreeNode'):
    RTreeFreeNode = _libs['grass_rtree.7.0.2'].RTreeFreeNode
    RTreeFreeNode.restype = None
    RTreeFreeNode.argtypes = [POINTER(struct_RTree_Node)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 223
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeDestroyNode'):
    RTreeDestroyNode = _libs['grass_rtree.7.0.2'].RTreeDestroyNode
    RTreeDestroyNode.restype = None
    RTreeDestroyNode.argtypes = [POINTER(struct_RTree_Node), c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 226
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeAllocRect'):
    RTreeAllocRect = _libs['grass_rtree.7.0.2'].RTreeAllocRect
    RTreeAllocRect.restype = POINTER(struct_RTree_Rect)
    RTreeAllocRect.argtypes = [POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 227
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeFreeRect'):
    RTreeFreeRect = _libs['grass_rtree.7.0.2'].RTreeFreeRect
    RTreeFreeRect.restype = None
    RTreeFreeRect.argtypes = [POINTER(struct_RTree_Rect)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 228
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeAllocBoundary'):
    RTreeAllocBoundary = _libs['grass_rtree.7.0.2'].RTreeAllocBoundary
    RTreeAllocBoundary.restype = POINTER(RectReal)
    RTreeAllocBoundary.argtypes = [POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 229
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeFreeBoundary'):
    RTreeFreeBoundary = _libs['grass_rtree.7.0.2'].RTreeFreeBoundary
    RTreeFreeBoundary.restype = None
    RTreeFreeBoundary.argtypes = [POINTER(struct_RTree_Rect)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 232
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeReadNode'):
    RTreeReadNode = _libs['grass_rtree.7.0.2'].RTreeReadNode
    RTreeReadNode.restype = c_size_t
    RTreeReadNode.argtypes = [POINTER(struct_RTree_Node), off_t, POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 233
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeWriteNode'):
    RTreeWriteNode = _libs['grass_rtree.7.0.2'].RTreeWriteNode
    RTreeWriteNode.restype = c_size_t
    RTreeWriteNode.argtypes = [POINTER(struct_RTree_Node), POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 234
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeGetNodePos'):
    RTreeGetNodePos = _libs['grass_rtree.7.0.2'].RTreeGetNodePos
    RTreeGetNodePos.restype = off_t
    RTreeGetNodePos.argtypes = [POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 235
if hasattr(_libs['grass_rtree.7.0.2'], 'RTreeFlushBuffer'):
    RTreeFlushBuffer = _libs['grass_rtree.7.0.2'].RTreeFlushBuffer
    RTreeFlushBuffer.restype = None
    RTreeFlushBuffer.argtypes = [POINTER(struct_RTree)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 35
try:
    TRUE = 1
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 37
try:
    FALSE = 0
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 44
try:
    MAXCARD = 9
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 44
try:
    NODECARD = MAXCARD
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 44
try:
    LEAFCARD = MAXCARD
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 47
try:
    MAXLEVEL = 20
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 49
try:
    NODE_BUFFER_SIZE = 32
except:
    pass

RTree_Rect = struct_RTree_Rect # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 57

RTree_Node = struct_RTree_Node # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 77

RTree_Child = union_RTree_Child # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 64

RTree_Branch = struct_RTree_Branch # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 71

RTree = struct_RTree # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 128

nstack = struct_nstack # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 103

NodeBuffer = struct_NodeBuffer # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 111

RTree_PartitionVars = struct_RTree_PartitionVars # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 119

_recycle = struct__recycle # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/rtree.h: 155

# No inserted files

