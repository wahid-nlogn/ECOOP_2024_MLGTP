#!/usr/bin/env python3
from __future__ import print_function
import sys, argparse, ast, os, os.path
import time
import cProfile
import pickle
import __main__
from collections import deque
import logging

# print('#The name of retic.py: ', __name__)
if __name__ == '__main__' or __name__ == 'retic':
    import typing, flags, utils, exc, repl, typecheck, runtime, static, object_check_collector
    from importer import make_importer
    if flags.PY_VERSION == 3:
        from exec3 import _exec
    else: from exec2 import _exec
    import settings
    from settings import functionCosts, callGraph, definedFuncs, nli, functionCostsNli, callGraphNli, parCastedTimesAll, valuesCastedWithinFunc, contains_classes

else:
    from . import typing, flags, utils, exc, repl, typecheck, runtime, static, object_check_collector
    from .importer import make_importer
    from .settings import functionCosts, callGraph, definedFuncs, nli, functionCostsNli, callGraphNli, parCastedTimesAll, valuesCastedWithinFunc, contains_classes
    from . import settings

    if flags.PY_VERSION == 3:
        from .exec3 import _exec
    else: from .exec2 import _exec

## Type for 'open'ed files
if flags.PY_VERSION == 2:
    file_type = file
elif flags.PY_VERSION == 3:
    import io
    file_type = io.TextIOBase

def reachableFuncs(cg):
    reachable = ['TopLevel']
    d = deque(['TopLevel'])
    
    while d:
        item = d.popleft()
        reachable_from_d = [i for i in cg.get(item,[]) if i not in reachable]
        reachable += cg.get(item,[])
        d.extend( reachable_from_d )

    return set(reachable)
    
def removeUnreachable(cg,reachable):
    ncg = {}
    for caller in cg:
        if caller in reachable:
            ncg[caller] = cg[caller]
            
    return ncg
         
def simplifyCG(cg,definedFuncs):
    ncg = removeLibrary(cg,definedFuncs)
    
    reachable = reachableFuncs(ncg)
    
    return removeUnreachable(ncg,reachable)
    
def simplifyCGNli(cg_nli,cg,definedFuncs):
    ncg_nli = removeLibraryNli(cg_nli,definedFuncs)
    
    reachable = reachableFuncs ( removeLibrary(cg, definedFuncs) )
    
    return removeUnreachable(ncg_nli,reachable)
    
def removeLibrary(cg,definedFuncs):    
    ncg = {}
    for caller in cg:
        callee = cg[caller]
        newce = [x for x in callee if x in definedFuncs]
        ncg[caller] = newce

    return ncg
    
def removeLibraryNli(cg,definedFuncs):    
    ncg = {}
    for caller in cg:
        callee = cg[caller]
        newce = [(x,n) for (x,n) in callee if x in definedFuncs]
        ncg[caller] = newce

    return ncg    

def add_parent_link(root):
    for node in ast.walk(root):
        for child in ast.iter_child_nodes(node):
            child.parent = node


def reticulate(input, prog_args=None, flag_sets=None, answer_var=None, **individual_flags):
    global functionCosts
    global callGraph, definedFuncs, callGraphNli

    if prog_args == None:
        prog_args = []
    if flag_sets is None:
        flag_sets = flags.defaults(individual_flags)
    flags.set(flag_sets)
    
    path = os.getcwd()
    if input is None:
        return repl.repl()
    elif isinstance(input, str):
        py_ast = ast.parse(input)
        module_name = '__text__'
    elif isinstance(input, ast.Module):
        py_ast = input
        module_name = '__ast__'
    elif isinstance(input, file_type):
        py_ast = ast.parse(input.read())
        module_name = input.name
        path = os.path.abspath(module_name)[0:-len(os.path.basename(module_name))]
        sys.path.insert(1, path)
    flags.PATH = path

    type_system = static.StaticTypeSystem()

    add_parent_link(py_ast)


    if flags.NUMBER_LOOP_ITERATIONS:
        with open('nli.txt', 'rb') as f:
            settings.nli = pickle.loads(f.read())
            settings.nli['once'] = 1
            # print(settings.nli)

    if flags.DRY_RUN:
        typed_ast = py_ast
    else:
        try:
            # Actually perform typechecking
            t0 = time.time()
            typed_ast, _ = type_system.typecheck_module(py_ast, module_name)
            t1 = time.time()
            #print("The time to typecheck is: {0}".format(t1-t0))
        except exc.StaticTypeError as e:
            utils.handle_static_type_error(e, exit=flags.DIE_ON_STATIC_ERROR)
            return

    # print("#" + str(callGraph))
    
    if flags.BIT_STRING_GENERATION:
        with open('bit_strings.txt','a+') as file:
            file.write(flags.program+'\n')
            file.write(settings.bit_string_info[:-1]+'\n')
            
        return
    
    callGraph = simplifyCG(callGraph,definedFuncs)
    
    callGraphNli = simplifyCGNli(callGraphNli, callGraph, definedFuncs)
    
    # print("#" + str(callGraph))
    # print("#" + str(callGraphNli))  
    # print("#" + str(definedFuncs))
    if flags.CALL_GRAPH_GENERATION:
        with open('cg.txt', 'w+') as f:
            f.write(str(callGraph))
            
        if flags.NUMBER_LOOP_ITERATIONS:    
            with open('cg_nli.txt', 'w+') as f:
                f.write(str(callGraphNli))
            
    with open('fc_nonli.txt','a+') as f:
        f.write(flag_sets.program.split('\\')[-1] + '\n')
        if not settings.contains_classes:
            f.write(str(removeUnreachable(functionCosts,reachableFuncs(callGraph))))
        else:
            f.write(str(functionCosts))
        f.write('\n')
        
    # print(flag_sets.program.split('\\')[-1] + '\n')
    # print(str(removeUnreachable(functionCosts,reachableFuncs(callGraph))))
    if flags.SEMANTICS == 'TRANS':        
        flag_sets.feature_file = 'trans_' + flag_sets.feature_file

    if flags.NUMBER_LOOP_ITERATIONS:        
        with open(flag_sets.feature_file,'a+') as f:
            f.write(flag_sets.program.split('\\')[-1] + '\n')
            if not settings.contains_classes:
                functionCost = removeUnreachable(functionCostsNli,reachableFuncs(callGraph))
            else:
                functionCost = functionCostsNli

            if flags.SEMANTICS == 'GUARDED':            
                for fn in parCastedTimesAll:
                    if fn.endswith('__Class'):
                        continue
                        
                    funcParCasted = parCastedTimesAll[fn]
                    for pi in funcParCasted:
                        functionCost[fn+'par'+str(pi)] = funcParCasted[pi]
            
            f.write(str(functionCost))
            f.write('\n')
    # print(flag_sets.program.split('\\')[-1] + '\n')
    # print(str(removeUnreachable(functionCostsNli,reachableFuncs(callGraph))))
                
    # if flags.SEMANTICS in ['TRANS', 'MGDTRANS'] and flags.YANK_OBJECT_CHECKS:
        # typed_ast = object_check_collector.CheckCollectionVisitor().preorder(typed_ast)

    # if flags.OUTPUT_AST:
    if not flags.NUMBER_LOOP_ITERATIONS:
        from . import unparse
        unparse.unparse(typed_ast)
        return
    
    logging.info("@@@@Parameter casted information")
    for fn in parCastedTimesAll:
        logging.info('%s\n%s',fn,parCastedTimesAll[fn])
        
    logging.info("@@@@Arguments casted information")
    for fn in parCastedTimesAll:
        logging.info('%s\n%s',fn,valuesCastedWithinFunc[fn])
    
    return 
#    from .visitors import LocationFreeFinder
#    LocationFreeFinder().preorder(typed_ast)

    code = compile(typed_ast, module_name, 'exec')

    sys.argv = [module_name] + prog_args

    if flags.SEMANTICS == 'TRANS':
        from . import transient as cast_semantics
    elif flags.SEMANTICS == 'MGDTRANS':
        from . import mgd_transient as cast_semantics
    elif flags.SEMANTICS == 'MONO':
        from . import monotonic as cast_semantics
    elif flags.SEMANTICS == 'GUARDED':
        if __name__ == '__main__' or __name__ == 'retic':
            import guarded as cast_semantics
        else:
            from . import guarded as cast_semantics
    elif flags.SEMANTICS == 'NOOP':
        from . import noop as cast_semantics
    else:
        assert False, 'Unknown semantics ' + flags.SEMANTICS
        

    omain = __main__.__dict__.copy()

    code_context = {}
    code_context.update(typing.__dict__)
    if not flags.DRY_RUN:
        code_context.update(cast_semantics.__dict__)
        code_context.update(runtime.__dict__)
        
    __main__.__dict__.update(code_context)
    __main__.__dict__.update(omain)
    __main__.__file__ = module_name
    try:
        if flags.TYPECHECK_IMPORTS:
            importer = make_importer(code_context, type_system)
            if flags.TYPECHECK_LIBRARY:
                sys.path_importer_cache.clear()
            sys.path_hooks.insert(0, importer)

        try:
            _exec(code, __main__.__dict__)
        except Exception:
            utils.handle_runtime_error(exit=True)
            return
        except exc.RuntimeTypeError:
            utils.handle_runtime_error(exit=True)
            return

        if answer_var != None:
            return code_context[answer_var]
    finally:
        # Fix up __main__, in case reticulate called again.
        killset = []
        __main__.__dict__.update(omain)
        for x in __main__.__dict__:
            if x not in omain:
                killset.append(x)
        for x in killset:
            del __main__.__dict__[x]

def main():
    global prog_name
    
    parser = argparse.ArgumentParser(description='Typecheck and run a ' + 
                                     'Python program with type casts')
    parser.add_argument('-v', '--verbosity', metavar='N', dest='warnings', nargs=1, default=[flags.WARNINGS], 
                        help='amount of information displayed at typechecking, 0-3')
    parser.add_argument('-e', '--no-static-errors', dest='static_errors', action='store_false', 
                        default=True, help='force statically-detected errors to trigger at runtime instead')
    parser.add_argument('-cg', '--call-graph-generation', dest='call_graph_generation', action='store_true', 
                        default=False, help='write the call graph information into the file cg.txt')
    parser.add_argument('-ff', '--feature-file', dest='feature_file', action='store', 
                        default='fc_nli.txt', help='specify the file name that feature values will be written to')
                        
    parser.add_argument('-bsg', '--bit-string-generation', dest='bit_string_generation', action='store_true', 
                        default=False, help='write the bit string of typed/untyped of each parameter and return type into bits.txt')                        
    parser.add_argument('-nli', '--number-loop-iterations', dest='number_loop_iterations', action='store_true', 
                        default=False, help='write the call graph information into the file cg.txt')
    parser.add_argument('-p', '--print', dest='output_ast', action='store_true', 
                        default=False, help='instead of executing the program, print out the modified program (comments and formatting will be lost)')
    parser.add_argument('-ni', '--no-imports', dest='typecheck_imports', action='store_false', 
                        default=True, help='do not typecheck or cast-insert imported modules')
    typings = parser.add_mutually_exclusive_group()
    typings.add_argument('--transient', '--casts-as-check', dest='semantics', action='store_const', const='TRANS',
                         help='use the casts-as-checks runtime semantics (the default)')
    typings.add_argument('--mgd-transient', dest='semantics', action='store_const', const='MGDTRANS',
                         help='use the managed casts-as-checks runtime semantics (the default)')
    typings.add_argument('--monotonic', dest='semantics', action='store_const', const='MONO',
                         help='use the monotonic objects runtime semantics')
    typings.add_argument('--guarded', dest='semantics', action='store_const', const='GUARDED',
                         help='use the guarded objects runtime semantics')
    typings.add_argument('--static-only', '--linting', '--noop', dest='semantics', action='store_const', const='NOOP',
                         help='do not perform runtime checks (static linting only)')
    typings.set_defaults(semantics='GUARDED')
    parser.add_argument('program', help='a Python program to be executed (.py extension required)', default=None, nargs='?')
    parser.add_argument('args', help='arguments to the program in question (in quotes)', default='', nargs='?')
    
    args = parser.parse_args(sys.argv[1:])
    args.die_on_static_error = True

    logging.basicConfig(filename='running.log', level=logging.INFO)
       
    logging.info(args)

    if args.program is None:
        reticulate(None, prog_args=args.args.split(), flag_sets=args)
    else:
        try:
            with open(args.program, 'r') as program:
                reticulate(program, prog_args=args.args.split(), flag_sets=args)
        except IOError as e:
            print(e)
if __name__ == '__main__':
    main()
