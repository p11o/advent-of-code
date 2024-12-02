from collections import Counter
from heapq import heappush, heappop

from aoc import read


def pt1():
    total = 0

    a_list = []
    b_list = []
    for a, b in read(lambda x: map(int, x.split())):
        heappush(a_list, a)
        heappush(b_list, b)
    
    while a_list:
        a, b = heappop(a_list), heappop(b_list)
        total += abs(a - b)

    return total


def test_pt1():
    assert pt1() == 11


def pt2():
    a_list = []
    def build():
        for a, b in read(lambda x: map(int, x.split())):
            a_list.append(a)
            yield b
    b_counter = Counter(build())
        
    return sum(el * b_counter.get(el, 0) for el in a_list)


def test_pt2():
    assert pt2() == 31