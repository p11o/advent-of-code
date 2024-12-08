from aoc import read
from itertools import combinations, groupby
from operator import add, sub
from functools import reduce, partial
from math import gcd

def prepare():
  m = list(read(list))
  groups = groupby(
    sorted([(e, x, y) for x, r in enumerate(m) for y, e in enumerate(r) if e != '.']),
    lambda e: e[0]
  )
  return m, groups


def compute(op, a, b):
  return tuple(map(partial(reduce, op), zip(a, b)))

def antinodes(a, b, m, inline=False):
  diff = compute(sub, a, b)
  if inline:
    dx, dy = diff
    d = gcd(dx, dy)
    diff = dx // d, dy // d
  directions = [(add, a), (sub, b)]
  for op, p in directions:
    c = 0
    nxt = compute(op, p, diff)
    while inboard(*nxt, m) and (c < 1 or inline):
      c += 1
      yield nxt
      nxt = compute(op, nxt, diff)

def inboard(x, y, m):
  return 0 <= x and 0 <= y and x < len(m) and y < len(m[0])

def pt1():
  m, groups = prepare()

  for g, positions in groups:
    for i, j in combinations(positions, 2):
      for x, y in antinodes(i[1:], j[1:], m):
        m[x][y] = '#'

  return sum(l.count('#') for l in m)


def pt2():
  m, groups = prepare()

  for g, positions in groups:
    for i, j in combinations(positions, 2):
      for x, y in antinodes(i[1:], j[1:], m, inline=True):
        m[x][y] = '#'

  return sum(len(l) - l.count('.') for l in m)


def test_pt1():
  assert pt1() == 14


def test_pt2():
  assert pt2() == 34
