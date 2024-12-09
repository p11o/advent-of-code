from aoc import read
from itertools import combinations, groupby, starmap
from operator import add, sub
from math import gcd


def prepare():
  global MAP, HEIGHT, WIDTH
  MAP = list(read(list))
  HEIGHT = len(MAP)
  WIDTH = len(MAP[0])
  groups = groupby(
    sorted([(e, x, y) for x, r in enumerate(MAP) for y, e in enumerate(r) if e != '.']),
    lambda e: e[0]
  )
  return groups


def compute(op, a, b):
  return tuple(starmap(op, zip(a, b)))


def antinodes(a, b, inline=False):
  diff = compute(sub, a, b)
  if inline:
    diff = tuple(d // gcd(*diff) for d in diff)
  for op, p in [(add, a), (sub, b)]:
    once = not inline
    nxt = compute(op, p, diff)
    while inboard(*nxt) and (inline or once):
      once = False
      yield nxt
      nxt = compute(op, nxt, diff)

def inboard(x, y):
  return 0 <= x and 0 <= y and x < HEIGHT and y < WIDTH


def solve(inline=False):
  groups = prepare()
  for _, positions in groups:
    for i, j in combinations(positions, 2):
      for x, y in antinodes(i[1:], j[1:], inline):
        MAP[x][y] = '#'

def pt1():
  solve()
  return sum(r.count('#') for r in MAP)


def pt2():
  solve(inline=True)
  return sum(len(r) - r.count('.') for r in MAP)


def test_pt1():
  assert pt1() == 14


def test_pt2():
  assert pt2() == 34
