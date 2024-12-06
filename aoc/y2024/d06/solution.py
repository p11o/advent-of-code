from aoc import read
from copy import deepcopy

lines = list(read())
width = len(lines[0])
board = [c for l in lines for c in list(l)]
start = board.index('^')
directions = ['up', 'right', 'down', 'left']


nxt = {
  'up': lambda p: p - width if p - width > 0 else None,
  'right': lambda p: p + 1 if (p + 1) % width > 0 else None,
  'down': lambda p: p + width if p + width < len(board) else None,
  'left': lambda p: p - 1 if p % width > 0 else None,
}


def navigate(board):
  global start, nxt, direction, directions
  board = deepcopy(board)
  p = start
  direction = 0
  while True:
    board[p] = 'X'
    n = nxt[directions[direction]](p)
    if n is None:
      return board
    elif board[n] == '#':
      direction = (direction + 1) % len(directions)
    else:
      p = n

def pt1():
  global board
  return navigate(board).count('X')


def is_loop(are, board):
  global start, nxt, direction, directions
  board = deepcopy(board)
  p = start
  direction = 0
  board[are] = 'O'
  seen_are = False
  memory = set()
  while True:
    n = nxt[directions[direction]](p)
    if (p, n) in memory:
      return 1
    if n is None:
      return 0
    elif board[n] == '#' or n == are:
      direction = (direction + 1) % len(directions)
      board[p] = '+'

      if seen_are:
        memory.add((p, n))
    else:
      p = n
      board[p] = str(direction)
    if n == are:
      seen_are = True

def pt2():
  global start, board
  ares = [i for i, c in enumerate(navigate(board)) if c == 'X' and c != start]

  s = sum(is_loop(are, board) for are in ares)
  return s


def test_pt1():
  assert pt1() == 41


def test_pt2():
  assert pt2() == 6
