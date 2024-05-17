#!/usr/bin/env python3

import os, sys, io
import subprocess

pyfiles = {}
trfiles = {}
mofiles = {}

trpassed = 0
mopassed = 0
trtests = 0
motests = 0

PYVERSION = 'python3'
CALL = (PYVERSION + ' ../retic.py').split()

print('Starting regression tests.')


def test(file, sem, expected):
    exc = False

    print('Reticulating {} using {}'.format(file, sem))
    try: 
        result = subprocess.check_output(CALL + [pyfiles[file]] + [sem], 
                                         stderr=subprocess.STDOUT).decode('utf-8').strip()
    except Exception as e:
        exc = e.output.decode('utf-8').strip()
        human_exc = '...\n' + exc[exc.rfind('File "'):]

    if exc:
        success = expected.startswith('EXCEPTION') and \
                  (exc.find(expected[len('EXCEPTION'):].strip()) >= 0)
        message = 'Unexpected exception raised:\n{}\nWas expecting\n{}'.format(human_exc, 
                                                                                expected)
    elif expected.startswith('SEARCH'):
        success = (result.find(expected[len('SEARCH'):].strip()) >= 0)
        message = 'Unexpected output:\n{}\nDoes not contain\n{}'.format(result, expected[len('SEARCH'):].strip())
    else:
        success = result == expected
        message = 'Unexpected output:\n{}\n=/=\n{}'.format(result, expected)

    if success:
        return 1
    else:
        print('{} failure reticulating {}:\n   {}'.format(sem, file, message))
        return 0


try:
    pyfiles = {f[:-3]: f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.py')}
    trfiles = {f[:-4]: open(f, 'r') for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.trx')}
    mofiles = {f[:-4]: open(f, 'r') for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.mox')}
 
    for file in sorted(pyfiles):
        if file in trfiles:
            trpassed += test(file, '--transient', trfiles[file].read().strip())
            trtests += 1
        if file in mofiles:
            mopassed += test(file, '--monotonic', mofiles[file].read().strip())
            motests += 1
            

    print('{}/{} tests passed with transient'.format(trpassed, trtests))
    print('{}/{} tests passed with monotonic'.format(mopassed, motests))
finally:
    for file in trfiles:
        trfiles[file].close()
