from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check0(val):
    try:
        val.perf_counter
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.extend
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.iterations
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.Runner
        return val
    except:
        raise CheckError(val)

def check4(val):
    try:
        val.metadata
        return val
    except:
        raise CheckError(val)

def check5(val):
    try:
        val.argparser
        return val
    except:
        raise CheckError(val)

def check6(val):
    try:
        val.add_argument
        return val
    except:
        raise CheckError(val)

def check7(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check8(val):
    try:
        val.bench_time_func
        return val
    except:
        raise CheckError(val)

def check9(val):
    try:
        val.reference
        return val
    except:
        raise CheckError(val)
import pyperf
__contact__ = 'collinwinter@google.com (Collin Winter)'
DEFAULT_ITERATIONS = 20000
DEFAULT_REFERENCE = 'sun'

def combinations(l):
    result = []
    for x in check_type_function(range)((check_type_function(len)(l) - 1)):
        ls = l[(x + 1):]
        for y in ls:
            check_type_void(check_type_function(result.append)((l[x], y)))
    return result
PI = 3.141592653589793
SOLAR_MASS = ((4 * PI) * PI)
DAYS_PER_YEAR = 365.24
BODIES = check_type_dict({'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS), 'jupiter': ([4.841431442464721, (- 1.1603200440274284), (- 0.10362204447112311)], [(0.001660076642744037 * DAYS_PER_YEAR), (0.007699011184197404 * DAYS_PER_YEAR), ((- 6.90460016972063e-05) * DAYS_PER_YEAR)], (0.0009547919384243266 * SOLAR_MASS)), 'saturn': ([8.34336671824458, 4.124798564124305, (- 0.4035234171143214)], [((- 0.002767425107268624) * DAYS_PER_YEAR), (0.004998528012349172 * DAYS_PER_YEAR), (2.3041729757376393e-05 * DAYS_PER_YEAR)], (0.0002858859806661308 * SOLAR_MASS)), 'uranus': ([12.894369562139131, (- 15.111151401698631), (- 0.22330757889265573)], [(0.002964601375647616 * DAYS_PER_YEAR), (0.0023784717395948095 * DAYS_PER_YEAR), ((- 2.9658956854023756e-05) * DAYS_PER_YEAR)], (4.366244043351563e-05 * SOLAR_MASS)), 'neptune': ([15.379697114850917, (- 25.919314609987964), 0.17925877295037118], [(0.0026806777249038932 * DAYS_PER_YEAR), (0.001628241700382423 * DAYS_PER_YEAR), ((- 9.515922545197159e-05) * DAYS_PER_YEAR)], (5.1513890204661145e-05 * SOLAR_MASS)), })
SYSTEM = check_type_function(list)(check_type_function(BODIES.values)())
PAIRS = combinations(SYSTEM)

def advance(dt, n, bodies=SYSTEM, pairs=PAIRS):
    for i in check_type_function(range)(n):
        for (([x1, y1, z1], v1, m1), ([x2, y2, z2], v2, m2)) in pairs:
            check_type_tuple((([x1, y1, z1], v1, m1), ([x2, y2, z2], v2, m2)), 2)
            dx = (x1 - x2)
            dy = (y1 - y2)
            dz = (z1 - z2)
            mag = (dt * ((((dx * dx) + (dy * dy)) + (dz * dz)) ** (- 1.5)))
            b1m = (m1 * mag)
            b2m = (m2 * mag)
            v1[0] = (v1[0] - (dx * b2m))
            v1[1] = (v1[1] - (dy * b2m))
            v1[2] = (v1[2] - (dz * b2m))
            v2[0] = (v2[0] + (dx * b1m))
            v2[1] = (v2[1] + (dy * b1m))
            v2[2] = (v2[2] + (dz * b1m))
        for (r, [vx, vy, vz], m) in bodies:
            check_type_tuple((r, [vx, vy, vz], m), 3)
            r[0] = (r[0] + (dt * vx))
            r[1] = (r[1] + (dt * vy))
            r[2] = (r[2] + (dt * vz))

def report_energy(bodies=SYSTEM, pairs=PAIRS, e=0.0):
    for (((x1, y1, z1), v1, m1), ((x2, y2, z2), v2, m2)) in pairs:
        check_type_tuple((((x1, y1, z1), v1, m1), ((x2, y2, z2), v2, m2)), 2)
        dx = (x1 - x2)
        dy = (y1 - y2)
        dz = (z1 - z2)
        e = (e - ((m1 * m2) / ((((dx * dx) + (dy * dy)) + (dz * dz)) ** 0.5)))
    for (r, [vx, vy, vz], m) in bodies:
        check_type_tuple((r, [vx, vy, vz], m), 3)
        e = (e + ((m * (((vx * vx) + (vy * vy)) + (vz * vz))) / 2.0))
    return e

def offset_momentum(ref, bodies=SYSTEM, px=0.0, py=0.0, pz=0.0):
    for (r, [vx, vy, vz], m) in bodies:
        check_type_tuple((r, [vx, vy, vz], m), 3)
        px = (px - (vx * m))
        py = (py - (vy * m))
        pz = (pz - (vz * m))
    (r, v, m) = check_type_tuple(ref, 3)
    v[0] = (px / m)
    v[1] = (py / m)
    v[2] = (pz / m)

def bench_nbody(loops, reference, iterations):
    offset_momentum(check_type_tuple(BODIES[check_type_string(reference)], 3))
    range_it = check_type_function(range)(loops)
    t0 = check_type_function(check0(pyperf).perf_counter)()
    for _ in range_it:
        report_energy()
        advance(0.01, iterations)
        report_energy()
    return (check_type_function(check0(pyperf).perf_counter)() - t0)

def add_cmdline_args(cmd, args):
    check_type_function(check1(cmd).extend)(('--iterations', check_type_function(str)(check2(args).iterations)))
if (__name__ == '__main__'):
    runner = check_type_function(check3(pyperf).Runner)(add_cmdline_args=add_cmdline_args)
    check4(runner).metadata['description'] = 'n-body benchmark'
    check_type_function(check6(check5(runner).argparser).add_argument)('--iterations', type=int, default=DEFAULT_ITERATIONS, help=('Number of nbody advance() iterations (default: %s)' % DEFAULT_ITERATIONS))
    check_type_function(check6(check5(runner).argparser).add_argument)('--reference', type=str, default=DEFAULT_REFERENCE, help=('nbody reference (default: %s)' % DEFAULT_REFERENCE))
    args = check_type_function(check7(runner).parse_args)()
    check_type_function(check8(runner).bench_time_func)('nbody', bench_nbody, check9(args).reference, check2(args).iterations)
