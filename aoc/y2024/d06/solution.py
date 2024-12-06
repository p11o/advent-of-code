from aoc import read
from copy import deepcopy
from itertools import cycle


LINES = list(read())
WIDTH = len(LINES[0])
BOARD = [c for l in LINES for c in list(l)]
START = BOARD.index('^')
DIRECTIONS = ['up', 'right', 'down', 'left']


nxt = {
  'up': lambda p: p - WIDTH if p - WIDTH > 0 else None,
  'right': lambda p: p + 1 if (p + 1) % WIDTH > 0 else None,
  'down': lambda p: p + WIDTH if p + WIDTH < len(BOARD) else None,
  'left': lambda p: p - 1 if p % WIDTH > 0 else None,
}


def navigate(board):
  board = deepcopy(board)
  p = START
  dirs = cycle(DIRECTIONS)
  direction = next(dirs)
  while True:
    board[p] = 'X'
    n = nxt[direction](p)
    if n is None:
      return board
    elif board[n] == '#':
      direction = next(dirs)
    else:
      p = n

def pt1():
  return navigate(BOARD).count('X')


def is_loop(are, board):
  board = deepcopy(board)
  p = START
  dirs = cycle(DIRECTIONS)
  direction = next(dirs)
  seen_are = False
  memory = set()
  while True:
    n = nxt[direction](p)
    if (p, n) in memory:
      return 1
    if n is None:
      return 0
    elif board[n] == '#' or n == are:
      direction = next(dirs)
      if seen_are:
        memory.add((p, n))
    else:
      p = n
    if n == are:
      seen_are = True

def pt2():
  ares = [i for i, c in enumerate(navigate(BOARD)) if c == 'X' and i != START]
  return sum(is_loop(are, BOARD) for are in ares)


def test_pt1():
  assert pt1() == 41


def test_pt2():
  assert pt2() == 6
