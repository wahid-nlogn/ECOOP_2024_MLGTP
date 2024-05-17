from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check0(val):
    try:
        val.time
        return val
    except:
        raise CheckError(val)
from array import array
import math
from six.moves import xrange
import time

def array2d(w, h):
    d = (check_type_function(array)('d', [0.0]) * (w * h))
    return (w, h, d)

def idx(arr, x, y):
    check_type_int(x)
    (w, h, d) = check_type_tuple(arr, 3)
    if ((0 <= x < (w + 0)) and (0 <= y < (h + 0))):
        return check_type_int(((((y + 0) * (w + 0)) + x) + 0))
    raise IndexError
    return 0

def getitem(arr, x_y):
    check_type_tuple(arr, 3)
    check_type_tuple(x_y, 2)
    (w, h, d) = arr
    (x, y) = x_y
    return d[check_type_int(idx(arr, x, y))]

def setitem(arr, x_y, val):
    check_type_tuple(arr, 3)
    check_type_tuple(x_y, 2)
    (x, y) = x_y
    (w, h, d) = arr
    d[check_type_int(idx(arr, check_type_int(x), y))] = val
    return (w, h, d)

def SOR_execute(omega, G, cycles):
    check_type_float(omega)
    check_type_int(cycles)
    (w, h, d) = check_type_tuple(G, 3)
    for p in check_type_function(xrange)((cycles + 0)):
        for y in check_type_function(xrange)(1, (h - 1)):
            for x in check_type_function(xrange)(1, (w - 1)):
                G = check_type_tuple(setitem(check_type_tuple(G, 3), (x, y), (((omega * 0.25) * (((getitem(check_type_tuple(G, 3), check_type_tuple((x, (y - 1)), 2)) + getitem(check_type_tuple(G, 3), check_type_tuple((x, (y + 1)), 2))) + getitem(check_type_tuple(G, 3), check_type_tuple(((x - 1), y), 2))) + getitem(check_type_tuple(G, 3), check_type_tuple(((x + 1), y), 2)))) + ((1.0 - omega) * getitem(check_type_tuple(G, 3), check_type_tuple((x, y), 2))))), 3)
    return None

def bench_SOR(loops, n, cycles):
    check_type_int(cycles)
    range_it = check_type_function(xrange)((loops + 0))
    t0 = check_type_function(check0(time).time)()
    for _ in range_it:
        G = check_type_tuple(array2d(n, n), 3)
        SOR_execute(1.25, G, (cycles + 0))
    t1 = check_type_function(check0(time).time)()
    check_type_function(print)((t1 - t0))
    return None

def main():
    bench_SOR(4, 10, 1)
main()
