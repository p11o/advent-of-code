import sys


def read(fn = lambda x: x):
    for line in sys.stdin:
        yield fn(line.strip('\n'))