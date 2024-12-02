from itertools import pairwise
from aoc import read


def main():
  diffs = [[y - x for x, y in pairwise(l)] for l in read(lambda x: map(int, x.split()))]
  fns = [lambda l: all(0 < x < 4 for x in l), lambda l: all(-4 < x < 0 for x in l)]
  return sum(len(list(filter(fn, diffs))) for fn in fns)

if __name__ == '__main__':
    print(main())