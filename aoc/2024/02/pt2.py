from itertools import pairwise

from aoc import read


def main():
  reports = read(lambda x: list(map(int, x.split())))
  def test(levels):
    length = len(levels)
    for i in range(length):
      tmp = levels[0:i] + levels[i+1:length]
      diffs = [y - x for x, y in pairwise(tmp)]
      asc = [0 < d < 4 for d in diffs]
      desc = [-4 < d < 0 for d in diffs]
      if all(asc) or all(desc):
         return True
    return False

  return len([
    levels
    for levels in reports
    if test(levels)
  ])

if __name__ == '__main__':
    print(main())