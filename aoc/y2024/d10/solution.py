from aoc import read
from operator import add
from itertools import starmap
from collections import defaultdict


MAP = list(read(lambda r: [int(i) for i in r]))

def moves(position):
  py, px = position
  candidates = (1,0), (0,1), (-1,0), (0,-1)
  for c in candidates:
    y, x = tuple(starmap(add, zip(c, position)))
    if (
      (0 <= y < len(MAP) and 0 <= x < len(MAP[0]))
      and
      (MAP[y][x] == MAP[py][px] + 1)
    ):
      yield y, x


def trailheads(val=0):
  return [
    (y, x)
    for y, r in enumerate(MAP)
    for x, el in enumerate(r)
    if el == val
  ]


def travel(pt1=True):
  trail = []
  trails = defaultdict(set)
  for start in trailheads():
    trail = [start]
    while trail:
      position = trail.pop(0)
      for y, x in moves(position):
        trail.append((y, x))
        if pt1 and MAP[y][x] == 9:
          trails[start].add((y, x))
        elif not pt1:
          trails[(y, x)].add(position)

  return trails

def pt1():
  scores = travel()
  return sum(len(score) for _, score in scores.items())


def pt2():
  trails = travel(False)
  total = 0  
  for nine in trailheads(9):
    cnt = 1
    trail = [nine]
    while trail:
      position = trail.pop(0)
      paths = trails[position]
      cnt += max(0, len(paths) - 1)
      trail.extend(list(paths))
    total += cnt

  return total



def test_pt1():
  assert pt1() == 36


def test_pt2():
  assert pt2() == 81
