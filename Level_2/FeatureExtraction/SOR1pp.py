#The name of retic.py:  retic.retic
#Cost of the cast Dyn => Function(['String', 'List(Float)'], Dyn) is 30.009999999999998
#Cost of the cast Dyn => Function(['String', 'List(Float)'], Dyn) is 30.009999999999998 repeated 0
##Inside array2d, the total cast cost is 30.009999999999998
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
##Inside idx, the total cast cost is 0.43
#Cost of the cast Dyn => Tuple(Dyn,Dyn) is 23.200000000000003
#Cost of the cast Dyn => Tuple(Dyn,Dyn) is 23.200000000000003 repeated 0
##Inside getitem, the total cast cost is 23.200000000000003
##Inside setitem, the total cast cost is 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
#Cost of the cast Void => Dyn is 0.43
#Cost of the cast Void => Dyn is 0.43 repeated 0
##Inside SOR_execute, the total cast cost is 89.08000000000003
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624 repeated 0
#Cost of the cast Dyn => Function([], Dyn) is 10.08
#Cost of the cast Dyn => Function([], Dyn) is 10.08 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624 repeated 0
#Cost of the cast Dyn => Function([], Dyn) is 10.08
#Cost of the cast Dyn => Function([], Dyn) is 10.08 repeated 0
#Cost of the cast Dyn => Function(['Dyn'], Dyn) is 10.08
#Cost of the cast Dyn => Function(['Dyn'], Dyn) is 10.08 repeated 0
#Cost of the cast Void => Dyn is 0.43
#Cost of the cast Void => Dyn is 0.43 repeated 0
##Inside bench_SOR, the total cast cost is 32.778
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
##Inside main, the total cast cost is 1.29
from retic.runtime import *
from retic.guarded import *
from retic.typing import *
import pickle
CIDict = {}
CIDict['fci1'] = 0
CIDict['fci2'] = 0
CIDict['fci3'] = 0
CIDict['fci4'] = 0
from array import array
import math
from six.moves import xrange
import time

def array2d(w, h):
    d = (retic_cast(array, Dyn, Function(AnonymousParameters([String, List(Float)]), Dyn), "\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:17:8: Expected function of type Function(['String', 'List(Float)'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")('d', [0.0]) * (w * h))
    return (w, h, d)

def idx(arr, x, y):
    (w, h, d) = arr
    if ((0 <= x < (w + 0)) and (0 <= y < (h + 0))):
        return ((((y + 0) * (w + 0)) + x) + 0)
    raise IndexError
    return retic_cast(0, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:27:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def getitem(arr, x_y):
    (w, h, d) = arr
    (x, y) = retic_cast(x_y, Dyn, Tuple(Dyn, Dyn), '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:31:4: Right hand side of assignment was expected to be of type Tuple(Dyn,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    return d[idx(arr, x, y)]

def setitem(arr, x_y, val):
    (x, y) = x_y
    (w, h, d) = arr
    d[idx(arr, x, y)] = val
    return (w, h, d)

def SOR_execute(omega, G, cycles):
    CIDict['localci1'] = 0
    CIDict['localci2'] = 0
    CIDict['localci3'] = 0
    (w, h, d) = G
    for p in retic_cast(xrange((cycles + 0)), Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:42:4: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
        CIDict['fci1'] += 1
        CIDict['localci1'] += 1
        for y in retic_cast(xrange(retic_cast(1, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:43:17: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), (h - 1)), Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:43:8: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
            CIDict['fci2'] += 1
            CIDict['localci2'] += 1
            for x in retic_cast(xrange(retic_cast(1, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:44:21: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), (w - 1)), Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:44:12: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
                CIDict['fci3'] += 1
                CIDict['localci3'] += 1
                G = setitem(G, (x, y), (((omega * 0.25) * (((getitem(G, retic_cast((x, (y - 1)), Tuple(Dyn, Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:45:55: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')) + getitem(G, retic_cast((x, (y + 1)), Tuple(Dyn, Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:45:79: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))) + getitem(G, retic_cast(((x - 1), y), Tuple(Dyn, Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:45:103: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))) + getitem(G, retic_cast(((x + 1), y), Tuple(Dyn, Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:46:55: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')))) + ((1.0 - omega) * getitem(G, retic_cast((x, y), Tuple(Dyn, Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:47:45: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')))))
    return retic_cast(None, Void, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:48:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def bench_SOR(loops, n, cycles):
    CIDict['localci4'] = 0
    range_it = xrange((loops + 0))
    t0 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:52:9: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:52:9: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
    for _ in retic_cast(range_it, Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:54:4: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
        CIDict['fci4'] += 1
        CIDict['localci4'] += 1
        G = array2d(n, n)
        SOR_execute(retic_cast(1.25, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:56:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), G, (cycles + 0))
    t1 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:57:9: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:57:9: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
    retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:58:4: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
    return retic_cast(None, Void, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:59:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def main():
    bench_SOR(retic_cast(4, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:65:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(10, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:65:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(1, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\scimark\\SOR1.py:65:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
main()
with open('nli.txt', 'wb') as f:
    pickle.dump(CIDict, f)
with open('nlireadable.txt', 'w+') as f:
    f.write(str(CIDict))
