from retic.runtime import *
from retic.guarded import *
from retic.typing import *
import time

def pascal_upp(n):
    s = [[0 for _ in range(n)] for _ in range(n)]
    s[0] = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n):
            s[retic_cast(i, Dyn, Int, '\npascal10.py:8: Cannot use a value %s as an index into a List(List(Int)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal10.py:8: Cannot use a value %s as an index into a List(Int), use a value of type Int instead. (code BAD_INDEX)')] = (s[retic_cast((i - 1), Dyn, Int, '\npascal10.py:8: Cannot use a value %s as an index into a List(List(Int)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal10.py:8: Cannot use a value %s as an index into a List(Int), use a value of type Int instead. (code BAD_INDEX)')] + s[retic_cast(i, Dyn, Int, '\npascal10.py:8: Cannot use a value %s as an index into a List(List(Int)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal10.py:8: Cannot use a value %s as an index into a List(Int), use a value of type Int instead. (code BAD_INDEX)')])
    return s
pascal_upp = retic_cast(pascal_upp, Dyn, Function(NamedParameters([('n', Int)]), List(List(Float))), "\npascal10.py:3:0: Function %s does not match specified type Function(['n:Int'], List(List(Float))). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def pascal_low(n):
    return retic_cast([list(x) for x in retic_cast(retic_cast(zip, Dyn, Function(DynParameters, Dyn), '\npascal10.py:12:29: Expected function of type Function(DynParameters, Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')(*pascal_upp(n)), Dyn, Iterable(Dyn), '\npascal10.py:12: Iteration target was expected to be of type Iterable(Dyn), but value %s was provided instead. (code ITER_ERROR)')], List(List(Dyn)), List(List(Float)), '\npascal10.py:12:4: A return value of type List(List(Float)) was expected but a value %s was returned instead. (code RETURN_ERROR)')
pascal_low = retic_cast(pascal_low, Dyn, Function(NamedParameters([('n', Int)]), List(List(Float))), "\npascal10.py:10:0: Function %s does not match specified type Function(['n:Int'], List(List(Float))). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def pascal_sym(n):
    s = [[float(1) for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            s[retic_cast(i, Dyn, Int, '\npascal10.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal10.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] = (s[retic_cast((i - 1), Dyn, Int, '\npascal10.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal10.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] + s[retic_cast(i, Dyn, Int, '\npascal10.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal10.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
    return s
pascal_sym = retic_cast(pascal_sym, Dyn, Function(NamedParameters([('n', Int)]), List(List(Float))), "\npascal10.py:13:0: Function %s does not match specified type Function(['n:Int'], List(List(Float))). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def printMatrix(matrix):
    return
printMatrix = retic_cast(printMatrix, Dyn, Function(NamedParameters([('matrix', List(List(Float)))]), Dyn), "\npascal10.py:19:0: Function %s does not match specified type Function(['matrix:List(List(Float))'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def printMatrixes(n):
    printMatrix(pascal_upp(n))
    printMatrix(pascal_low(n))
    printMatrix(pascal_sym(n))
printMatrixes = retic_cast(printMatrixes, Dyn, Function(NamedParameters([('n', Int)]), Dyn), "\npascal10.py:23:0: Function %s does not match specified type Function(['n:Int'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def nextperm(a):
    n = len(retic_cast(a, List(Float), Dyn, '\npascal10.py:31:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    i = (n - 1)
    while ((i > 0) and (a[retic_cast((i - 1), Dyn, Int, '\npascal10.py:33: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] > a[retic_cast(i, Dyn, Int, '\npascal10.py:33: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])):
        i = (i - 1)
    j = i
    k = (n - 1)
    while (j < k):
        (a[retic_cast(j, Dyn, Int, '\npascal10.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast(k, Dyn, Int, '\npascal10.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')]) = (a[retic_cast(k, Dyn, Int, '\npascal10.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast(j, Dyn, Int, '\npascal10.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
        j = (j + 1)
        k = (k - 1)
    if (i == 0):
        return False
    else:
        j = i
        while (a[retic_cast(j, Dyn, Int, '\npascal10.py:45: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] < a[retic_cast((i - 1), Dyn, Int, '\npascal10.py:45: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')]):
            j = (j + 1)
        (a[retic_cast((i - 1), Dyn, Int, '\npascal10.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast(j, Dyn, Int, '\npascal10.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')]) = (a[retic_cast(j, Dyn, Int, '\npascal10.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast((i - 1), Dyn, Int, '\npascal10.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
        return True
nextperm = retic_cast(nextperm, Dyn, Function(NamedParameters([('a', List(Float))]), Bool), "\npascal10.py:30:0: Function %s does not match specified type Function(['a:List(Float)'], Bool). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def perm3(n, flag):
    if flag:
        if (n < 1):
            return []
        z = range(n)
    else:
        z = sorted(n)
    a = list(z)
    u = [list(retic_cast(a, List(Dyn), Dyn, '\npascal10.py:57:9: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))]
    while nextperm(retic_cast(a, List(Dyn), List(Float), '\npascal10.py:58:10: Expected argument of type List(Float) but value %s was provided instead. (code ARG_ERROR)')):
        u.append(list(retic_cast(a, List(Dyn), Dyn, '\npascal10.py:59:17: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')))
    return u
perm3 = retic_cast(perm3, Dyn, Function(NamedParameters([('n', Int), ('flag', Dyn)]), Dyn), "\npascal10.py:49:0: Function %s does not match specified type Function(['n:Int', 'flag:Dyn'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def main(x, y, z):
    for p in perm3(x, z):
        print("foo")
    for i in range(1000):
        printMatrixes(retic_cast(y, Dyn, Int, '\npascal10.py:65:12: Expected argument of type Int but value %s was provided instead. (code ARG_ERROR)'))
main = retic_cast(main, Dyn, Function(NamedParameters([('x', Int), ('y', Dyn), ('z', Bool)]), Dyn), "\npascal10.py:61:0: Function %s does not match specified type Function(['x:Int', 'y:Dyn', 'z:Bool'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")
t0 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\npascal10.py:67:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\npascal10.py:67:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
main(3, 3, True)
t1 = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\npascal10.py:69:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\npascal10.py:69:5: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\npascal10.py:70:0: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
