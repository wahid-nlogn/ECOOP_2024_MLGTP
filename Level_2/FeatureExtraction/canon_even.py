from retic.runtime import *
from retic.guarded import *
from retic.typing import *
import time

def ident(x):
    return x
ident = retic_cast(ident, Dyn, Function(NamedParameters([('x', Bool)]), Bool), "\neven1.py:3:0: Function %s does not match specified type Function(['x:Bool'], Bool). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def even(n, k):
    return (retic_cast(k, Dyn, Function(AnonymousParameters([Bool]), Dyn), "\neven1.py:6:11: Expected function of type Function(['Bool'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(True) if (n <= 0) else odd((n - 1), k))
even = retic_cast(even, Dyn, Function(NamedParameters([('n', Dyn), ('k', Dyn)]), Dyn), "\neven1.py:5:0: Function %s does not match specified type Function(['n:Dyn', 'k:Dyn'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def odd(n, k):
    return (retic_cast(k, Dyn, Function(AnonymousParameters([Bool]), Dyn), "\neven1.py:8:11: Expected function of type Function(['Bool'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(False) if (n <= 0) else even((n - 1), k))
odd = retic_cast(odd, Dyn, Function(NamedParameters([('n', Dyn), ('k', Dyn)]), Dyn), "\neven1.py:7:0: Function %s does not match specified type Function(['n:Dyn', 'k:Dyn'], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)")

def main():
    for i in range(1000):
        even(50, retic_cast(ident, Function(NamedParameters([('x', Bool)]), Bool), Dyn, '\neven1.py:12:12: Expected argument of type Dyn but value %s was provided instead. (code ARG_ERROR)'))
main = retic_cast(main, Dyn, Function(NamedParameters([]), Dyn), '\neven1.py:10:0: Function %s does not match specified type Function([], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)')
start = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\neven1.py:14:8: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\neven1.py:14:8: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
main()
end = retic_cast(retic_cast(time, Dyn, Object('', {'time': Dyn, }), '\neven1.py:16:6: Accessing nonexistant object attribute time from value %s. (code WIDTH_DOWNCAST)').time, Dyn, Function(AnonymousParameters([]), Dyn), '\neven1.py:16:6: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
retic_cast(print, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\neven1.py:17:0: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")((end - start))
