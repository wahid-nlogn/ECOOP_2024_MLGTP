from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check0(val):
    try:
        val.time
        return val
    except:
        raise CheckError(val)
import time

def pascal_upp(n):
    check_type_int(n)
    s = check_type_list([check_type_list([0 for _ in check_type_function(range)(n)]) for _ in check_type_function(range)(n)])
    s[0] = check_type_list([1 for _ in check_type_function(range)(n)])
    for i in check_type_function(range)(1, n):
        for j in check_type_function(range)(i, n):
            check_type_list(s[check_type_int(i)])[check_type_int(j)] = (check_type_int(check_type_list(s[check_type_int((i - 1))])[check_type_int((j - 1))]) + check_type_int(check_type_list(s[check_type_int(i)])[check_type_int((j - 1))]))
    return s

def pascal_low(n):
    check_type_int(n)
    return check_type_list([check_type_function(list)(x) for x in check_type_function(zip)(*pascal_upp(n))])

def pascal_sym(n):
    check_type_int(n)
    s = check_type_list([check_type_list([1 for _ in check_type_function(range)(n)]) for _ in check_type_function(range)(n)])
    for i in check_type_function(range)(1, n):
        for j in check_type_function(range)(1, n):
            check_type_list(s[check_type_int(i)])[check_type_int(j)] = (check_type_int(check_type_list(s[check_type_int((i - 1))])[check_type_int(j)]) + check_type_int(check_type_list(s[check_type_int(i)])[check_type_int((j - 1))]))
    return s

def printMatrix(matrix):
    return

def printMatrixes(n):
    check_type_int(n)
    printMatrix(pascal_upp(n))
    printMatrix(pascal_low(n))
    printMatrix(pascal_sym(n))

def nextperm(a):
    n = check_type_function(len)(a)
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

def perm3(n, flag):
    check_type_bool(flag)
    if flag:
        if (n < 1):
            return []
        z = check_type_function(range)(n)
    else:
        z = check_type_function(sorted)(n)
    a = check_type_function(list)(z)
    u = [check_type_function(list)(a)]
    while nextperm(a):
        check_type_void(check_type_function(u.append)(check_type_function(list)(a)))
    return u

def main(x, y, z):
    check_type_int(x)
    check_type_bool(z)
    for p in perm3(x, z):
        break
    for i in check_type_function(range)(1000):
        printMatrixes(check_type_int(y))
t0 = check_type_function(check0(time).time)()
main(3, 3, True)
t1 = check_type_function(check0(time).time)()
check_type_function(print)((t1 - t0))
