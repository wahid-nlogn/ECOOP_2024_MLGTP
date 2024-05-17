import time
import tracemalloc
import linecache
import os
#import tracemalloc
from datetime import datetime
from queue import Queue, Empty
#from resource import getrusage, RUSAGE_SELF
from threading import Thread
from time import sleep

def memory_monitor(command_queue: Queue, poll_interval=1):
    tracemalloc.start()
    old_max = 0
    snapshot = None
    while True:
        try:
            command_queue.get(timeout=poll_interval)
            if snapshot is not None:
                #print(datetime.now())
                display_top(snapshot)

            return
        except Empty:
#            max_rss = getrusage(RUSAGE_SELF).ru_maxrss
            max_rss = 9088

            if max_rss > old_max:
                old_max = max_rss
                snapshot = tracemalloc.take_snapshot()
                #print(datetime.now(), 'max RSS', max_rss)

def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    #print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        #print("#%s: %s:%s: %.1f KiB"
        #      % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        #if line:
        #    print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        #print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("%.1f" % (total / 1024))

def _exec_other(obj, globs=None, locs=None):
    queue = Queue()
    poll_interval = 0.001
    monitor_thread = Thread(target=memory_monitor, args=(queue, poll_interval))
    monitor_thread.start()
    try:
        exec (obj, globs, locs)
    finally:
        queue.put('stop')
        monitor_thread.join()

def _exec(obj, globs=None, locs=None):
    exec (obj, globs, locs)

