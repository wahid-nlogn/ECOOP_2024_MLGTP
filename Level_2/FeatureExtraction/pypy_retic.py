from retic.runtime import *
from retic.guarded import *
from retic.typing import *
import time

def pascal_upp(n):
    s = [[0 for _ in range(n)] for _ in range(n)]
    s[0] = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n):
            s[retic_cast(i, Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] = (s[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] + s[retic_cast(i, Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
    return s
pascal_upp = retic_cast(pascal_upp, Dyn, Function(NamedParameters([('n', Int)]), List(List(Float))), "\npascal1000.py:3:0: Function %s does not match specified type Function(['n:Int'], List(List(Float))). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def pascal_upp_fast(n):
    s = [[0 for _ in range(n)] for _ in range(n)]
    s[0] = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n):
            s[retic_cast(i, Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] = (s[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] + s[retic_cast(i, Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal1000.py:8: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
    return s
pascal_upp_fast = pascal_upp_fast

def pascal_low(n):
    return retic_cast([list(x) for x in retic_cast(retic_cast(zip, Dyn, Function(DynParameters, Dyn), '\npascal1000.py:12:29: Expected function of type Function(DynParameters, Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')(*pascal_upp(retic_cast(n, Dyn, Int, '\npascal1000.py:12:34: Expected argument of type Int but value %s was provided instead. (code ARG_ERROR)'))), Dyn, Iterable(Dyn), '\npascal1000.py:12: Iteration target was expected to be of type Iterable(Dyn), but value %s was provided instead. (code ITER_ERROR)')], List(List(Dyn)), Dyn, '\npascal1000.py:12:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')
pascal_low = retic_cast(pascal_low, Dyn, Function(NamedParameters([('n', Dyn)]), Dyn), "\npascal1000.py:10:0: Function %s does not match specified type Function(['n:Dyn'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def pascal_low_fast(n):
    return retic_cast([list(x) for x in retic_cast(retic_cast(zip, Dyn, Function(DynParameters, Dyn), '\npascal1000.py:12:29: Expected function of type Function(DynParameters, Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')(*pascal_upp_fast(n)), Dyn, Iterable(Dyn), '\npascal1000.py:12: Iteration target was expected to be of type Iterable(Dyn), but value %s was provided instead. (code ITER_ERROR)')], List(List(Dyn)), Dyn, '\npascal1000.py:12:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')
pascal_low_fast = pascal_low_fast

def pascal_sym(n):
    s = [[float(1) for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            s[retic_cast(i, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] = (s[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] + s[retic_cast(i, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
    return s
pascal_sym = retic_cast(pascal_sym, Dyn, Function(NamedParameters([('n', Int)]), List(List(Float))), "\npascal1000.py:13:0: Function %s does not match specified type Function(['n:Int'], List(List(Float))). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def pascal_sym_fast(n):
    s = [[float(1) for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            s[retic_cast(i, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] = (s[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast(j, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] + s[retic_cast(i, Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(List(Float)), use a value of type Int instead. (code BAD_INDEX)')][retic_cast((j - 1), Dyn, Int, '\npascal1000.py:17: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
    return s
pascal_sym_fast = pascal_sym_fast

def printMatrix(matrix):
    return
printMatrix = retic_cast(printMatrix, Dyn, Function(NamedParameters([('matrix', Dyn)]), Dyn), "\npascal1000.py:19:0: Function %s does not match specified type Function(['matrix:Dyn'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def printMatrix_fast(matrix):
    return
printMatrix_fast = printMatrix_fast

def printMatrixes(n):
    printMatrix_fast(retic_cast(pascal_upp_fast(n), List(List(Float)), Dyn, '\npascal1000.py:25:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    printMatrix_fast(retic_cast(pascal_low_fast(n), List(List(Dyn)), Dyn, '\npascal1000.py:27:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    printMatrix_fast(retic_cast(pascal_sym_fast(n), List(List(Float)), Dyn, '\npascal1000.py:29:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
printMatrixes = retic_cast(printMatrixes, Dyn, Function(NamedParameters([('n', Int)]), Dyn), "\npascal1000.py:23:0: Function %s does not match specified type Function(['n:Int'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def printMatrixes_fast(n):
    printMatrix_fast(retic_cast(pascal_upp_fast(n), List(List(Float)), Dyn, '\npascal1000.py:25:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    printMatrix_fast(retic_cast(pascal_low_fast(n), List(List(Dyn)), Dyn, '\npascal1000.py:27:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    printMatrix_fast(retic_cast(pascal_sym_fast(n), List(List(Float)), Dyn, '\npascal1000.py:29:4: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
printMatrixes_fast = printMatrixes_fast

def nextperm(a):
    n = len(retic_cast(a, List(Float), Dyn, '\npascal1000.py:31:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    i = (n - 1)
    while ((i > 0) and (a[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:33: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] > a[retic_cast(i, Dyn, Int, '\npascal1000.py:33: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])):
        i = (i - 1)
    j = i
    k = (n - 1)
    while (j < k):
        (a[retic_cast(j, Dyn, Int, '\npascal1000.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast(k, Dyn, Int, '\npascal1000.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')]) = (a[retic_cast(k, Dyn, Int, '\npascal1000.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast(j, Dyn, Int, '\npascal1000.py:38: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
        j = (j + 1)
        k = (k - 1)
    if (i == 0):
        return False
    else:
        j = i
        while (a[retic_cast(j, Dyn, Int, '\npascal1000.py:45: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')] < a[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:45: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')]):
            j = (j + 1)
        (a[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast(j, Dyn, Int, '\npascal1000.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')]) = (a[retic_cast(j, Dyn, Int, '\npascal1000.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')], a[retic_cast((i - 1), Dyn, Int, '\npascal1000.py:47: Cannot use a value %s as an index into a List(Float), use a value of type Int instead. (code BAD_INDEX)')])
        return True
nextperm = retic_cast(nextperm, Dyn, Function(NamedParameters([('a', List(Float))]), Bool), "\npascal1000.py:30:0: Function %s does not match specified type Function(['a:List(Float)'], Bool). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def nextperm_fast(a):
    n = len(retic_cast(a, List(Float), Dyn, '\npascal1000.py:31:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    i = (n - 1)
    while ((i > 0) and (a[(i - 1)] > a[i])):
        i = (i - 1)
    j = i
    k = (n - 1)
    while (j < k):
        (a[j], a[k]) = (a[k], a[j])
        j = (j + 1)
        k = (k - 1)
    if (i == 0):
        return False
    else:
        j = i
        while (a[j] < a[(i - 1)]):
            j = (j + 1)
        (a[(i - 1)], a[j]) = (a[j], a[(i - 1)])
        return True
nextperm_fast = nextperm_fast

def perm3(n, flag):
    if flag:
        if (n < 1):
            return retic_cast([], List(Dyn), Dyn, '\npascal1000.py:52:12: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')
        z = range(n)
    else:
        z = sorted(n)
    a = list(z)
    u = [list(a)]
    while nextperm(retic_cast(a, Dyn, List(Float), '\npascal1000.py:58:10: Expected argument of type List(Float) but value %s was provided instead. (code ARG_ERROR)')):
        retic_cast(u, Dyn, Object('', {'append': Dyn, }), '\npascal1000.py:59:8: Accessing nonexistant object attribute append from value %s. (code WIDTH_DOWNCAST)').append(retic_cast(list(a), List(Dyn), Dyn, '\npascal1000.py:59:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    return u
perm3 = retic_cast(perm3, Dyn, Function(NamedParameters([('n', Dyn), ('flag', Bool)]), Dyn), "\npascal1000.py:49:0: Function %s does not match specified type Function(['n:Dyn', 'flag:Bool'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def perm3_fast(n, flag):
    if flag:
        if (n < 1):
            return retic_cast([], List(Dyn), Dyn, '\npascal1000.py:52:12: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')
        z = range(n)
    else:
        z = sorted(n)
    a = list(z)
    u = [list(retic_cast(a, List(Dyn), Dyn, '\npascal1000.py:57:9: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))]
    while nextperm(retic_cast(a, List(Dyn), List(Float), '\npascal1000.py:58:10: Expected argument of type List(Float) but value %s was provided instead. (code ARG_ERROR)')):
        retic_cast(u, Object('', {'clear': Dyn, '__iter__': Dyn, '__reversed__': Dyn, '__eq__': Dyn, '__iadd__': Dyn, '__delitem__': Dyn, '__doc__': Dyn, '__rmul__': Dyn, '__subclasshook__': Dyn, '__class__': Dyn, 'append': Function(AnonymousParameters([List(Dyn)]), Void), '__hash__': Dyn, 'copy': Dyn, '__init__': Dyn, '__sizeof__': Dyn, '__getattribute__': Dyn, '__lt__': Dyn, 'extend': Function(DynParameters, Void), '__le__': Dyn, '__reduce_ex__': Dyn, '__len__': Dyn, 'pop': Function(DynParameters, List(Dyn)), 'index': Function(DynParameters, Int), '__gt__': Dyn, 'insert': Function(AnonymousParameters([Int, List(Dyn)]), Void), '__contains__': Dyn, '__ne__': Dyn, '__getitem__': Function(AnonymousParameters([Int]), List(Dyn)), '__reduce__': Dyn, '__setitem__': Function(AnonymousParameters([Int, List(Dyn)]), Void), 'remove': Dyn, 'count': Dyn, 'reverse': Dyn, '__dir__': Dyn, '__format__': Dyn, '__mul__': Dyn, '__setattr__': Dyn, '__repr__': Dyn, '__imul__': Dyn, '__new__': Dyn, '__add__': Dyn, '__delattr__': Dyn, '__ge__': Dyn, '__str__': Dyn, 'sort': Dyn, }), Object('', {'append': Dyn, }), '\npascal1000.py:59:8: Accessing nonexistant object attribute append from value %s. (code WIDTH_DOWNCAST)').append(retic_cast(list(retic_cast(a, List(Dyn), Dyn, '\npascal1000.py:59:17: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)')), List(Dyn), Dyn, '\npascal1000.py:59:8: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
    return u
perm3_fast = perm3_fast

def main(x, y, z):
    for p in perm3(x, z):
        break
    for i in range(1000):
        printMatrixes(retic_cast(y, Dyn, Int, '\npascal1000.py:65:12: Expected argument of type Int but value %s was provided instead. (code ARG_ERROR)'))
main = retic_cast(main, Dyn, Function(NamedParameters([('x', Dyn), ('y', Dyn), ('z', Bool)]), Dyn), "\npascal1000.py:61:0: Function %s does not match specified type Function(['x:Dyn', 'y:Dyn', 'z:Bool'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def main_fast(x, y, z):
    #for p in perm3_fast(x, z):
    #    break
    for i in range(10):
        printMatrixes_fast(y)
main_fast = main_fast
t0 = retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\npascal1000.py:67:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time()
main_fast(3, 3, True)
t1 = retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\npascal1000.py:69:5: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time()
retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\npascal1000.py:70:0: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((t1 - t0))
