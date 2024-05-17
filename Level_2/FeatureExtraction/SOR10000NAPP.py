from retic.runtime import *
from retic.guarded import *
from retic.typing import *
from array import array
import math
from six.moves import xrange
import time
import cProfile

def array2d(w, h):
    d = (retic_cast(array, Dyn, Function(AnonymousParameters([String, List(Float)]), Dyn), "\n.\\SOR10000NA.py:18:8: Expected function of type Function(['String', 'List(Float)'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")('d', [0.0]) * (w * h))
    return (w, h, d)

def idx(arr, x, y):
    (w, h, d) = arr
    if ((0 <= x < (w + 0)) and (0 <= y < (h + 0))):
        return retic_cast(((((y + 0) * (w + 0)) + x) + 0), Dyn, Int, '\n.\\SOR10000NA.py:26:8: A return value of type Int was expected but a value %s was returned instead. (code RETURN_ERROR)')
    raise IndexError
    return 0

def getitem(arr, x_y):
    (w, h, d) = arr
    (x, y) = x_y
    return d[idx(retic_cast(arr, Tuple(Dyn, Dyn, Dyn), Tuple(Int, Int, Dyn), '\n.\\SOR10000NA.py:33:13: Expected argument of type Tuple(Int,Int,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast(x, Dyn, Int, '\n.\\SOR10000NA.py:33:13: Expected argument of type Int but value %s was provided instead. (code ARG_ERROR)'), retic_cast(y, Int, Dyn, '\n.\\SOR10000NA.py:33:13: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))]

def setitem(arr, x_y, val):
    (x, y) = retic_cast(x_y, Dyn, Tuple(Dyn, Dyn), '\n.\\SOR10000NA.py:36:4: Right hand side of assignment was expected to be of type Tuple(Dyn,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    (w, h, d) = retic_cast(arr, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:37:4: Right hand side of assignment was expected to be of type Tuple(Dyn,Dyn,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    d[idx(retic_cast(arr, Dyn, Tuple(Int, Int, Dyn), '\n.\\SOR10000NA.py:38:6: Expected argument of type Tuple(Int,Int,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast(x, Dyn, Int, '\n.\\SOR10000NA.py:38:6: Expected argument of type Int but value %s was provided instead. (code ARG_ERROR)'), y)] = retic_cast(val, Float, Dyn, '\n.\\SOR10000NA.py:38:4: Right hand side of assignment was expected to be of type Dyn, but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    return (w, h, d)

def SOR_execute(omega, G, cycles):
    (w, h, d) = retic_cast(G, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:42:4: Right hand side of assignment was expected to be of type Tuple(Dyn,Dyn,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    for p in retic_cast(xrange, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\n.\\SOR10000NA.py:43:13: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((cycles + 0)):
        for y in retic_cast(xrange, Dyn, Function(AnonymousParameters([Int, Dyn]), Dyn), "\n.\\SOR10000NA.py:44:17: Expected function of type Function(['Int', 'Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(1, (h - 1)):
            for x in retic_cast(xrange, Dyn, Function(AnonymousParameters([Int, Dyn]), Dyn), "\n.\\SOR10000NA.py:45:21: Expected function of type Function(['Int', 'Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(1, (w - 1)):
                G = retic_cast(setitem(G, retic_cast((x, y), Tuple(Dyn, Dyn), Dyn, '\n.\\SOR10000NA.py:46:20: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast((((omega * 0.25) * (((getitem(retic_cast(G, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:46:55: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast((x, (y - 1)), Tuple(Dyn, Dyn), Tuple(Dyn, Int), '\n.\\SOR10000NA.py:46:55: Expected argument of type Tuple(Dyn,Int) but value %s was provided instead. (code ARG_ERROR)')) + getitem(retic_cast(G, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:46:79: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast((x, (y + 1)), Tuple(Dyn, Dyn), Tuple(Dyn, Int), '\n.\\SOR10000NA.py:46:79: Expected argument of type Tuple(Dyn,Int) but value %s was provided instead. (code ARG_ERROR)'))) + getitem(retic_cast(G, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:46:103: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast(((x - 1), y), Tuple(Dyn, Dyn), Tuple(Dyn, Int), '\n.\\SOR10000NA.py:46:103: Expected argument of type Tuple(Dyn,Int) but value %s was provided instead. (code ARG_ERROR)'))) + getitem(retic_cast(G, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:47:55: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast(((x + 1), y), Tuple(Dyn, Dyn), Tuple(Dyn, Int), '\n.\\SOR10000NA.py:47:55: Expected argument of type Tuple(Dyn,Int) but value %s was provided instead. (code ARG_ERROR)')))) + ((1.0 - omega) * getitem(retic_cast(G, Dyn, Tuple(Dyn, Dyn, Dyn), '\n.\\SOR10000NA.py:48:45: Expected argument of type Tuple(Dyn,Dyn,Dyn) but value %s was provided instead. (code ARG_ERROR)'), retic_cast((x, y), Tuple(Dyn, Dyn), Tuple(Dyn, Int), '\n.\\SOR10000NA.py:48:45: Expected argument of type Tuple(Dyn,Int) but value %s was provided instead. (code ARG_ERROR)')))), Dyn, Float, '\n.\\SOR10000NA.py:46:20: Expected argument of type Float but value %s was provided instead. (code ARG_ERROR)')), Tuple(Dyn, Dyn, Dyn), Dyn, '\n.\\SOR10000NA.py:46:16: Right hand side of assignment was expected to be of type Dyn, but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    return retic_cast(None, Void, Dyn, '\n.\\SOR10000NA.py:49:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def bench_SOR(loops, n, cycles):
    range_it = retic_cast(xrange, Dyn, Function(AnonymousParameters([Int]), Dyn), "\n.\\SOR10000NA.py:52:15: Expected function of type Function(['Int'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((loops + 0))
    for _ in range_it:
        G = array2d(retic_cast(n, Int, Dyn, '\n.\\SOR10000NA.py:55:12: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(n, Int, Dyn, '\n.\\SOR10000NA.py:55:12: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
        SOR_execute(1.25, retic_cast(G, Tuple(Dyn, Dyn, Dyn), Dyn, '\n.\\SOR10000NA.py:56:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast((cycles + 0), Int, Dyn, '\n.\\SOR10000NA.py:56:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    return retic_cast(None, Void, Dyn, '\n.\\SOR10000NA.py:57:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def main():
    bench_SOR(4, 10, 1)
t0 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\n.\\SOR10000NA.py:65:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\n.\\SOR10000NA.py:65:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
main()
t1 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\n.\\SOR10000NA.py:67:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\n.\\SOR10000NA.py:67:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\n.\\SOR10000NA.py:68:0: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
retic_cast(retic_cast(cProfile, Dyn, Object('', {'run': Dyn, }), '\n.\\SOR10000NA.py:69:0: Accessing nonexistant object attribute run from value %s. (code WIDTH_DOWNCAST)').run, Dyn, Function(AnonymousParameters([String]), Dyn), "\n.\\SOR10000NA.py:69:0: Expected function of type Function(['String'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")('main()')
