from itertools import pairwise

from aoc import read


def main():
  reports = read(lambda x: list(map(int, x.split())))
  total = 0
  def test(levels):
    diffs = [y - x for x, y in pairwise(levels)]
    asc = [0 < d < 4 for d in diffs]
    desc = [-4 < d < 0 for d in diffs]
    return all(asc) or all(desc)

  for levels in reports:
    if test(levels):
      total += 1
    else:
      length = len(levels)
      for i in range(length):
        if test(levels[0:i] + levels[i+1:length]):
          total += 1
          break
      
    
  return total

if __name__ == '__main__':
    print(main())