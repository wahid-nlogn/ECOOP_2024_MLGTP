from retic.runtime import *
from retic.guarded import *
from retic.transient import *
from retic.typing import *
import time

num = 100000

def f1(v):
    v = (v + 1)
    return v

# v :: Int => *

def f2(v):
    v = (v + 1)
    return retic_cast(v, Int, Dyn, '\nfun.py:11:4: A return value of type Dyn was expected but a value %s was returned instead. (code RETURN_ERROR)')

def f3(v:Int) -> Int:
    v = (v + 1)
    return v

def f4(f,v):
    return f(v)

# range :: * => Int -> *

# f :: * => * -> *

def main():
    #h1 
    # f1 :: * -> * => *
    
    l = ([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    
    
    t0 = time.time()
    for i in range(num):
        check_type_list(l)
    t1 = time.time()
    print((t1 - t0), 'check_type_list', num, 'times: ')
   
    t0 = time.time()
    for i in range(2*num):
        check_type_list(l)
    t1 = time.time()
    print((t1 - t0), 'check_type_list', 2*num, 'times: ')

    longlist = [i for i in range(20000)]

    t0 = time.time()
    for i in range(num):
        check_type_list(longlist)
    t1 = time.time()
    print((t1 - t0), 'check_type_list for long_list', num, 'times: ')
   
    t0 = time.time()
    for i in range(2*num):
        check_type_list(longlist)
    t1 = time.time()
    print((t1 - t0), 'check_type_list for long_list', 2*num, 'times: ')

    t0 = time.time()
    for i in range(num):
        check_type_function(range)(5)
    t1 = time.time()
    print((t1 - t0), 'check_type_func with function called', num, 'times: ')
   
    t0 = time.time()
    for i in range(2*num):
        check_type_function(range)(5)
    t1 = time.time()
    print((t1 - t0), 'check_type_func with function called', 2*num, 'times: ')

    t0 = time.time()
    for i in range(num):
        check_type_function(range)
    t1 = time.time()
    print((t1 - t0), 'check_type_func', num, 'times: ')
   
    t0 = time.time()
    for i in range(2*num):
        check_type_function(range)
    t1 = time.time()
    print((t1 - t0), 'check_type_func', 2*num, 'times: ')

   
    t0 = time.time()
    for i in range(num):
        check_type_function(f4)(f2,5)
    t1 = time.time()
    print((t1 - t0), 'check_type_func with function called', num, 'times: ')
   
    t0 = time.time()
    for i in range(2*num):
        check_type_function(f4)(f2,5)
    t1 = time.time()
    print((t1 - t0), 'check_type_func with function called', 2*num, 'times: ')

    t0 = time.time()
    for i in range(num):
        check_type_function(f4)
    t1 = time.time()
    print((t1 - t0), 'check_type_func', num, 'times: ')
   
    t0 = time.time()
    for i in range(2*num):
        check_type_function(f4)
    t1 = time.time()
    print((t1 - t0), 'check_type_func', 2*num, 'times: ')
      
main()
