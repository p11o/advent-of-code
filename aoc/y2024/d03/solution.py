from aoc import read
import re


pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


def pt1():
  line = ''.join(read())
  return process(line)


def process(line):
  line = re.findall(pattern, line)
  return sum([int(x) * int(y) for x, y in line])


def pt2():
  total = 0
  line = ''.join(read())
  enabled = True
  i = 0
  while i >= 0:
    i = line.find("don't()" if enabled else "do()")
    total += process(line[:i]) if enabled else 0
    line = line[i+1:]
    enabled = not enabled

  return total


def test_pt1():
  assert pt1() == 161


def test_pt2():
  assert pt2() == 48
