import sys
import functools

STONES = next(sys.stdin).strip().split(' ')



@functools.cache
def blink(stone, times):
  if times == 0:
    return 1
  elif stone == '0':
    return blink('1', times - 1)
  elif len(stone) % 2:
    return blink(str(int(stone) * 2024), times - 1)
  else:
    mid = len(stone) // 2
    return sum([
      blink(stone[:mid], times - 1),
      blink(str(int(stone[mid:])), times - 1)
    ])


def pt1():
  return sum(blink(stone, 25) for stone in STONES)


def pt2():
  return sum(blink(stone, 75) for stone in STONES)


def test_pt1():
  assert pt1() == 55312


def test_pt2():
  assert True
