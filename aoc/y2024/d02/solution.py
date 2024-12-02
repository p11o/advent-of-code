
from itertools import pairwise
from functools import reduce
from aoc import read


def pt1():
  diffs = [[y - x for x, y in pairwise(l)] for l in read(lambda x: map(int, x.split()))]
  fns = [lambda l: all(0 < x < 4 for x in l), lambda l: all(-4 < x < 0 for x in l)]
  return sum(len(list(filter(fn, diffs))) for fn in fns)


def pt2():
  reports = read(lambda x: list(map(int, x.split())))
  def test(acc, levels):
    for i in range(len(levels)):
      tmp = levels[:i] + levels[i+1:]
      diffs = [y - x for x, y in pairwise(tmp)]
      asc = [0 < d < 4 for d in diffs]
      desc = [-4 < d < 0 for d in diffs]
      if all(asc) or all(desc):
         return acc + 1
    return acc

  return reduce(test, reports, 0)


def test_pt1():
  assert pt1() == 2

def test_pt2():
  assert pt2() == 4
