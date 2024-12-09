from aoc import read
from itertools import count, starmap
from dataclasses import dataclass

@dataclass
class FileNode:
  i: int
  size: int
  free: int


def prepare():
  l = list(map(int, next(read(list)) + ['0']))
  # id, size, free
  return list(starmap(FileNode, zip(count(), l[::2], l[1::2])))


def compact():
  segment = prepare()
  r = len(segment) - 1
  right = segment[r]
  i = 0
  while i <= r:
    left, right = segment[i], segment[r]
    yield FileNode(left.i, left.size, 0)
    while left.i < r and 0 < left.free:
      right = segment[r]
      if right.size <= left.free:
        right = FileNode(right.i, right.size, 0)
        yield right
        left.free -= right.size
        r -= 1
      else:
        yield FileNode(right.i, left.free, 0)
        right.size -= left.free
        left.free = 0
    i += 1
 

def checksum(f):
  position, c = 0, 0
  for node in f:
    c += node.i * (node.size * position + (node.size * (node.size - 1) // 2))
    position += node.size + node.free
  return c


def pt1():
  return checksum(compact())


def compact_nodes(segment):
  i, r = 0, len(segment) - 1
  while 0 < r:
    i = 0
    left, right = segment[i], segment[r]
    while i < r and left.free < right.size:
      i += 1
      left = segment[i]
    if i != r:
      right = segment.pop(r)
      segment[r - 1].free += right.size + right.free
      segment.insert(i + 1, right)
      right.free = left.free - right.size
      left.free = 0
    else:
      r -= 1


def pt2():
  segment = prepare()
  compact_nodes(segment)
  return checksum(segment)


def test_pt1():
  assert pt1() == 1928


def test_pt2():
  assert pt2() == 2858
