import sys
import time
import yappi

from subprocess import Popen

yappi.set_clock_type('cpu')
yappi.start(builtins=True)


def profile(output='test.out'):
    start = time.time()
    # Function here
    duration = time.time() - start
    stats = yappi.get_func_stats()
    stats.save(output, type="callgrind")


def visualize(filename):
    Popen(['kcachegrind', filename])

if __name__ == '__main__':
    output = sys.argv[1]
    profile(output=output)
    visualize(output)
