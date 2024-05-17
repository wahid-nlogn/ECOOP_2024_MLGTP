#The name of retic.py:  retic.retic
#Cost of the cast Dyn => Object(, {}) is 0.624
#Cost of the cast Dyn => Object(, {}) is 0.624 repeated 0
#Cost of the cast Dyn => Object(, {}) is 0.624
#Cost of the cast Dyn => Object(, {}) is 0.624 repeated 0
#Cost of the cast Dyn => Object(, {}) is 0.624
#Cost of the cast Dyn => Object(, {}) is 0.624 repeated 0
#Cost of the cast Dyn => Object(, {}) is 0.624
#Cost of the cast Dyn => Object(, {}) is 0.624 repeated 0
##Inside __init__, the total cast cost is 2.496
##Inside stream_first, the total cast cost is 0
##Inside stream_rest, the total cast cost is 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Function([], Object(Stream, {'rest': Dyn, 'first': Dyn})) => Dyn is 10.799999999999999
#Cost of the cast Function([], Object(Stream, {'rest': Dyn, 'first': Dyn})) => Dyn is 10.799999999999999 repeated 0
#Cost of the cast Dyn => Object(Stream, {'rest': Dyn, 'first': Dyn}) is 0.624
#Cost of the cast Dyn => Object(Stream, {'rest': Dyn, 'first': Dyn}) is 0.624 repeated 0
##Inside make_stream, the total cast cost is 11.854
#Cost of the cast Dyn => Function([], Dyn) is 10.08
#Cost of the cast Dyn => Function([], Dyn) is 10.08 repeated 0
#Cost of the cast Tuple(Dyn,Dyn) => Tuple(Int,Object(Stream, {'rest': Dyn, 'first': Dyn})) is 21.0
#Cost of the cast Tuple(Dyn,Dyn) => Tuple(Int,Object(Stream, {'rest': Dyn, 'first': Dyn})) is 21.0 repeated 0
##Inside stream_unfold, the total cast cost is 31.08
##Inside stream_get, the total cast cost is 0
#Cost of the cast List(Dyn) => List(Int) is 76.5735
#Cost of the cast List(Dyn) => List(Int) is 76.5735 repeated 0
##Inside stream_take, the total cast cost is 76.5735
##Inside count_from, the total cast cost is 0
#Cost of the cast Function([], Dyn) => Function([], Object(Stream, {'rest': Dyn, 'first': Dyn})) is 12.1
#Cost of the cast Function([], Dyn) => Function([], Object(Stream, {'rest': Dyn, 'first': Dyn})) is 12.1 repeated 0
##Inside sift, the total cast cost is 12.1
#Cost of the cast Dyn => Object(Stream, {'rest': Dyn, 'first': Dyn}) is 0.624
#Cost of the cast Dyn => Object(Stream, {'rest': Dyn, 'first': Dyn}) is 0.624 repeated 0
##Inside sieve, the total cast cost is 0.624
#Cost of the cast Object(Stream, {'rest': Dyn, 'first': Dyn}) => Dyn is 0.624
#Cost of the cast Object(Stream, {'rest': Dyn, 'first': Dyn}) => Dyn is 0.624 repeated 0
##Inside primes, the total cast cost is 0.624
#Cost of the cast Dyn => Object(Stream, {'rest': Dyn, 'first': Dyn}) is 0.624
#Cost of the cast Dyn => Object(Stream, {'rest': Dyn, 'first': Dyn}) is 0.624 repeated 0
##Inside main, the total cast cost is 0.624
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624
#Cost of the cast Dyn => Object(, {'time': Dyn}) is 0.624 repeated 0
#Cost of the cast Dyn => Function([], Dyn) is 10.08
#Cost of the cast Dyn => Function([], Dyn) is 10.08 repeated 0
#Cost of the cast Int => Dyn is 0.43
#Cost of the cast Int => Dyn is 0.43 repeated 0
#Cost of the cast Iterable(Dyn) => Dyn is 0.43
#Cost of the cast Iterable(Dyn) => Dyn is 0.43 repeated 0
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
import time


class Stream:
    retic_class_type = Class('Stream', {'rest': Dyn, 'first': Dyn, '__init__': Function(NamedParameters([('self', Dyn), ('first', Dyn), ('rest', Dyn)]), Dyn), }, {})
    first = None
    rest = None

    def __init__(self, first, rest):
        retic_cast(self, Dyn, Object('', {}), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:8:8: Cannot write to attribute first in value %s because it is not an object. (code NON_OBJECT_WRITE)').first = first
        retic_cast(self, Dyn, Object('', {}), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:9:8: Cannot write to attribute rest in value %s because it is not an object. (code NON_OBJECT_WRITE)').rest = rest

def stream_first(st):
    return st.first

def stream_rest(st):
    return st.rest

def make_stream(hd, thunk):
    return retic_cast(Stream(retic_cast(hd, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:17:11: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'), retic_cast(thunk, Function(AnonymousParameters([]), Object('Stream', {'rest': Dyn, 'first': Dyn, })), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:17:11: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')), Dyn, Object('Stream', {'rest': Dyn, 'first': Dyn, }), "\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:17:11: Constructed object value %s does not match type Object(Stream, {'rest': Dyn, 'first': Dyn}),  expected for instances of Class(Stream, {'rest': Dyn, 'first': Dyn, '__init__': Function(['self:Dyn', 'first:Dyn', 'rest:Dyn'], Dyn)}, ). Consider changing the type or setting it to Dyn. (code BAD_OBJECT_INJECTION)")

def stream_unfold(st):
    return retic_cast((stream_first(st), retic_cast(stream_rest(st), Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:19:30: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()), Tuple(Dyn, Dyn), Tuple(Int, Object('Stream', {'rest': Dyn, 'first': Dyn, })), "\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:19:4: A return value of type Tuple(Int,Object(Stream, {'rest': Dyn, 'first': Dyn})) was expected but a value %s was returned instead. (code RETURN_ERROR)")

def stream_get(st, i):
    (hd, tl) = stream_unfold(st)
    return (hd if (i == 0) else stream_get(tl, (i - 1)))

def stream_take(st, n):
    if (n == 0):
        return retic_cast([], List(Dyn), List(Int), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:25:9: A return value of type List(Int) was expected but a value %s was returned instead. (code RETURN_ERROR)')
    else:
        (hd, tl) = stream_unfold(st)
        return ([hd] + stream_take(tl, (n - 1)))

def count_from(n):
    return make_stream(n, (lambda : count_from((n + 1))))

def sift(n, st):
    (hd, tl) = stream_unfold(st)
    return (sift(n, tl) if ((hd % n) == 0) else make_stream(hd, retic_cast((lambda : sift(n, tl)), Function(NamedParameters([]), Dyn), Function(NamedParameters([]), Object('Stream', {'rest': Dyn, 'first': Dyn, })), "\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:33:44: Expected argument of type Function([], Object(Stream, {'rest': Dyn, 'first': Dyn})) but value %s was provided instead. (code ARG_ERROR)")))

def sieve(st):
    (hd, tl) = stream_unfold(st)
    return make_stream(hd, (lambda : sieve(retic_cast(sift(hd, tl), Dyn, Object('Stream', {'rest': Dyn, 'first': Dyn, }), "\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:36:36: Expected argument of type Object(Stream, {'rest': Dyn, 'first': Dyn}) but value %s was provided instead. (code ARG_ERROR)"))))

def primes():
    return retic_cast(sieve(count_from(2)), Object('Stream', {'rest': Dyn, 'first': Dyn, }), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:41:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')
N_1 = 9

def main():
    stream_get(retic_cast(primes(), Dyn, Object('Stream', {'rest': Dyn, 'first': Dyn, }), "\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:49:2: Expected argument of type Object(Stream, {'rest': Dyn, 'first': Dyn}) but value %s was provided instead. (code ARG_ERROR)"), N_1)
t0 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:51:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:51:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
for i in retic_cast(range(retic_cast(10, Int, Dyn, '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:52:9: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')), Iterable(Dyn), Dyn, '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:52:0: Iteration target was expected to be of type Dyn, but value %s was provided instead. (code ITER_ERROR)'):
    CIDict['fci1'] += 1
    main()
t1 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:54:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:54:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nD:\\r\\MLGTP\\PyBenches\\sieve\\sieve7679NA.py:55:0: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
with open('nli.txt', 'wb') as f:
    pickle.dump(CIDict, f)
    
with open('readable.txt', 'w+') as f:
    f.write(str(CIDict))
