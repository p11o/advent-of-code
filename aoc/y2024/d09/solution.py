from aoc import read
from itertools import count


def prepare():
  l = list(map(int, next(read(list)) + ['0']))
  # id, size, free
  return list(map(list, zip(count(), l[::2], l[1::2])))


def compact():
  segment = prepare()
  r = len(segment) - 1
  for i, s, f in segment:
    if i <= r:
      yield i, s
    while i < r and 0 < f:
      ri, rs, _ = segment[r]
      if rs <= f:
        f = f - rs
        yield ri, rs
        r -= 1
      else:
        yield ri, f
        segment[r][1] = rs - f
        f = 0


def checksum(f):
  position, c = 0, 0
  for i, s in f:
    c += i * sum(range(position, position + s))
    position += s
  return c


def pt1():
  return checksum(compact())


class FileNode:
  def __init__(self, i, s, f, n=None, p=None):
    self.i = i
    self.size = s
    self.free = f
    self.nxt = n
    self.prv = p

  def insert(self, other):
    # remove other
    other.prv.nxt = other.nxt
    other.nxt.prv = other.prv
    other.prv.free += other.size + other.free

    # insert other
    tmp = self.nxt
    self.nxt = other
    other.nxt = tmp
    other.prv = self
    tmp.prv = other
    other.free = self.free - other.size

    # inserted after self
    self.free = 0


def link_nodes():
  segment = prepare()
  tail = FileNode(None, None, None)
  head = n = FileNode(None, None, None)
  for s in segment:
    tmp = FileNode(*s, p=n)
    n.nxt = tmp
    tmp.prv = n
    n = tmp
  n.nxt = tail
  tail.prv = n
  return head, tail

def compact_nodes(h, t):
  r = t.prv # tail is a pointer to the end
  l = h.nxt # head is pointer to beginning
  while r.prv:
    prv, l = r.prv, h.nxt
    while prv != h and prv.i > r.i:
      prv = prv.prv
    while l != t.prv and l.free < r.size and l != r:
      l = l.nxt
    if l != r:
      l.insert(r)
    r = prv
  return h


def pt2():
  h, t = link_nodes()
  compact_nodes(h, t)

  # checksum
  l, p, checksum = h.nxt, 0, 0
  while l != t:
    checksum += sum(range(p, p + l.size)) * l.i
    p += l.size + l.free
    l = l.nxt
  return checksum


def test_pt1():
  assert pt1() == 1928


def test_pt2():
  assert pt2() == 2858
