#The name of retic.py:  retic.retic
# Dict creation detected at D:\r\MLGTP\PyBenches\nbody_features\nbody1.py 23
# Dict creation detected at D:\r\MLGTP\PyBenches\nbody_features\nbody1.py 23
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Dyn => Function(['Dyn', 'Dyn', 'Int'], Dyn) is 10.51
#Cost of the cast Dyn => Function(['Dyn', 'Dyn', 'Int'], Dyn) is 10.51 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3
#Cost of the cast Tuple(Dyn,Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
##Inside combinations, the total cast cost is 28.67
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
# Dict creation detected at D:\r\MLGTP\PyBenches\nbody_features\nbody1.py 23
#Cost of the cast Dict(String, Tuple(List(Float),List(Float),Dyn)) => Dict(String, Tuple(List(Float),List(Dyn),Dyn)) is 130.04500000000002
#Cost of the cast Dict(String, Tuple(List(Float),List(Float),Dyn)) => Dict(String, Tuple(List(Float),List(Dyn),Dyn)) is 130.04500000000002 repeated 0
#Cost of the cast List(Dyn) => Dyn is 46.5
#Cost of the cast List(Dyn) => Dyn is 46.5 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
##Inside advance, the total cast cost is 0.43
##Inside report_energy, the total cast cost is 0
#Cost of the cast Dyn => Tuple(Dyn,Dyn,Dyn) is 23.200000000000003
#Cost of the cast Dyn => Tuple(Dyn,Dyn,Dyn) is 23.200000000000003 repeated 0
#Cost of the cast Void => Dyn is 0.43
#Cost of the cast Void => Dyn is 0.43 repeated 0
##Inside offset_momentum, the total cast cost is 23.630000000000003
#Cost of the cast Dyn => String is 0.557
#Cost of the cast Dyn => String is 0.557 repeated 0
# Dict index detected at D:\r\MLGTP\PyBenches\nbody_features\nbody1.py 106
#Cost of the cast Tuple(List(Float),List(Dyn),Dyn) => Dyn is 17.3
#Cost of the cast Tuple(List(Float),List(Dyn),Dyn) => Dyn is 17.3 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast List(Dyn) => Dyn is 46.5
#Cost of the cast List(Dyn) => Dyn is 46.5 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast List(Dyn) => Dyn is 46.5
#Cost of the cast List(Dyn) => Dyn is 46.5 repeated 0
#Cost of the cast List(Dyn) => Dyn is 46.5
#Cost of the cast List(Dyn) => Dyn is 46.5 repeated 0
#Cost of the cast Float => Dyn is 0.43
#Cost of the cast Float => Dyn is 0.43 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
#Cost of the cast Void => Dyn is 0.43
#Cost of the cast Void => Dyn is 0.43 repeated 0
##Inside bench_nbody, the total cast cost is 160.79700000000003
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast String => Dyn is 0.43
#Cost of the cast String => Dyn is 0.43 repeated 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
##Inside main, the total cast cost is 1.29
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624 repeated 0
#Cost of the cast Dyn => Function([], Dyn) is 10.08
#Cost of the cast Dyn => Function([], Dyn) is 10.08 repeated 0
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624 repeated 0
#Cost of the cast Dyn => Function([], Dyn) is 10.08
#Cost of the cast Dyn => Function([], Dyn) is 10.08 repeated 0
#Cost of the cast Dyn => Function(['Dyn'], Dyn) is 10.08
#Cost of the cast Dyn => Function(['Dyn'], Dyn) is 10.08 repeated 0
from retic.runtime import *
from retic.guarded import *
from retic.typing import *
import pickle
CIDict = {}
CIDict['fci1'] = 0
CIDict['fci2'] = 0
CIDict['fci3'] = 0
CIDict['fci4'] = 0
CIDict['fci5'] = 0
CIDict['fci6'] = 0
CIDict['fci7'] = 0
CIDict['fci8'] = 0
CIDict['fci9'] = 0
from six.moves import xrange
import pdb
from itertools import islice
import time
__contact__ = 'collinwinter@google.com (Collin Winter)'
DEFAULT_ITERATIONS = 10000
DEFAULT_REFERENCE = 'sun'

def combinations(l):
    CIDict['localci1'] = 0
    CIDict['localci2'] = 0
    result = []
    for x in retic_cast(xrange(retic_cast((len(l) - 1), Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:12:13: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')), Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:12:4: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
        CIDict['fci1'] += 1
        CIDict['localci1'] += 1
        ls = retic_cast(islice, Dyn, Function(AnonymousParameters([Dyn, Dyn, Int]), Dyn), "\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:13:13: Expected function of type Function(['Dyn', 'Dyn', 'Int'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(l, (x + 1), len(l))
        for y in ls:
            CIDict['fci2'] += 1
            CIDict['localci2'] += 1
            result.append(retic_cast((l[x], y), Tuple(Dyn, Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:15:12: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    return result
PI = 3.141592653589793
SOLAR_MASS = retic_cast(((4 * PI) * PI), Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:20:0: Right hand side of assignment was expected to be of type Dyn, but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
DAYS_PER_YEAR = 365.24
BODIES = retic_cast({'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS), 'jupiter': ([4.841431442464721, (- 1.1603200440274284), (- 0.10362204447112311)], [(0.001660076642744037 * DAYS_PER_YEAR), (0.007699011184197404 * DAYS_PER_YEAR), ((- 6.90460016972063e-05) * DAYS_PER_YEAR)], (0.0009547919384243266 * SOLAR_MASS)), 'saturn': ([8.34336671824458, 4.124798564124305, (- 0.4035234171143214)], [((- 0.002767425107268624) * DAYS_PER_YEAR), (0.004998528012349172 * DAYS_PER_YEAR), (2.3041729757376393e-05 * DAYS_PER_YEAR)], (0.0002858859806661308 * SOLAR_MASS)), 'uranus': ([12.894369562139131, (- 15.111151401698631), (- 0.22330757889265573)], [(0.002964601375647616 * DAYS_PER_YEAR), (0.0023784717395948095 * DAYS_PER_YEAR), ((- 2.9658956854023756e-05) * DAYS_PER_YEAR)], (4.366244043351563e-05 * SOLAR_MASS)), 'neptune': ([15.379697114850917, (- 25.919314609987964), 0.17925877295037118], [(0.0026806777249038932 * DAYS_PER_YEAR), (0.001628241700382423 * DAYS_PER_YEAR), ((- 9.515922545197159e-05) * DAYS_PER_YEAR)], (5.1513890204661145e-05 * SOLAR_MASS)), }, Dict(String, Tuple(List(Float), List(Float), Dyn)), Dict(String, Tuple(List(Float), List(Dyn), Dyn)), '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:23:0: Right hand side of assignment was expected to be of type Dict(String, Tuple(List(Float),List(Dyn),Dyn)), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
SYSTEM = retic_cast(list(BODIES.values()), List(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:59:0: Right hand side of assignment was expected to be of type Dyn, but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
PAIRS = combinations(SYSTEM)

def advance(dt, n, bodies, pairs):
    CIDict['localci3'] = 0
    CIDict['localci4'] = 0
    CIDict['localci5'] = 0
    for i in retic_cast(xrange(n), Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:63:4: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
        CIDict['fci3'] += 1
        CIDict['localci3'] += 1
        for (([x1, y1, z1], v1, m1), ([x2, y2, z2], v2, m2)) in pairs:
            CIDict['fci4'] += 1
            CIDict['localci4'] += 1
            dx = ((0.0 + x1) - x2)
            dy = ((0.0 + y1) - y2)
            dz = ((0.0 + z1) - z2)
            mag = ((1.0 * dt) * (((((1.0 * dx) * dx) + ((1.0 * dy) * dy)) + ((1.0 * dz) * dz)) ** (- 1.5)))
            b1m = (m1 * mag)
            b2m = (m2 * mag)
            v1[0] = (v1[0] - (dx * b2m))
            v1[1] = (v1[1] - (dy * b2m))
            v1[2] = (v1[2] - (dz * b2m))
            v2[0] = (v2[0] + (dx * b1m))
            v2[1] = (v2[1] + (dy * b1m))
            v2[2] = (v2[2] + (dz * b1m))
        for (r, [vx, vy, vz], m) in bodies:
            CIDict['fci5'] += 1
            CIDict['localci5'] += 1
            r[0] = (r[0] + (dt * vx))
            r[1] = (r[1] + (dt * vy))
            r[2] = (r[2] + (dt * vz))

def report_energy(bodies, pairs, e):
    CIDict['localci6'] = 0
    CIDict['localci7'] = 0
    for (((x1, y1, z1), v1, m1), ((x2, y2, z2), v2, m2)) in pairs:
        CIDict['fci6'] += 1
        CIDict['localci6'] += 1
        dx = (x1 - x2)
        dy = (y1 - y2)
        dz = (z1 - z2)
        e = (e - ((m1 * m2) / ((((dx * dx) + (dy * dy)) + (dz * dz)) ** 0.5)))
    for (r, [vx, vy, vz], m) in bodies:
        CIDict['fci7'] += 1
        CIDict['localci7'] += 1
        e = (e + ((m * (((vx * vx) + (vy * vy)) + (vz * vz))) / 2.0))
    return e

def offset_momentum(ref, bodies, px, py, pz):
    CIDict['localci8'] = 0
    for (r, [vx, vy, vz], m) in bodies:
        CIDict['fci8'] += 1
        CIDict['localci8'] += 1
        px = (px - (vx * m))
        py = (py - (vy * m))
        pz = (pz - (vz * m))
    (r, v, m) = retic_cast(ref, Dyn, Tuple(Dyn, Dyn, Dyn), '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:99:4: Right hand side of assignment was expected to be of type Tuple(Dyn,Dyn,Dyn), but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    a = [((0.0 + px) / m), ((0.0 + py) / m), ((0.0 + pz) / m)]
    return retic_cast(None, Void, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:101:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def bench_nbody(loops, reference, iterations):
    CIDict['localci9'] = 0
    offset_momentum(retic_cast(BODIES[retic_cast(reference, Dyn, String, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:106: Cannot use a value %s as an index into a Dict(String, Tuple(List(Float),List(Dyn),Dyn)), use a value of type String instead. (code BAD_INDEX)')], Tuple(List(Float), List(Dyn), Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:106:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), SYSTEM, retic_cast(0.0, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:106:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(0.0, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:106:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(0.0, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:106:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    range_it = xrange(loops)
    for _ in retic_cast(range_it, Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:110:4: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
        CIDict['fci9'] += 1
        CIDict['localci9'] += 1
        report_energy(SYSTEM, retic_cast(PAIRS, List(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:111:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(0.0, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:111:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
        advance(retic_cast(0.01, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:112:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), iterations, SYSTEM, retic_cast(PAIRS, List(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:112:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
        report_energy(SYSTEM, retic_cast(PAIRS, List(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:113:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(0.0, Float, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:113:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    return retic_cast(None, Void, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:114:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def main():
    bench_nbody(retic_cast(1, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:117:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(DEFAULT_REFERENCE, String, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:117:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(DEFAULT_ITERATIONS, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:117:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
t0 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:119:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:119:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
main()
t1 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:121:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:121:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nD:\\r\\MLGTP\\PyBenches\\nbody_features\\nbody1.py:122:0: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
with open('nli.txt', 'wb') as f:
    pickle.dump(CIDict, f)

with open('nlireadable.txt', 'w+') as f:
    f.write(str(CIDict))
