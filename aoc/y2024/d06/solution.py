from aoc import read


lines = list(read())
width = len(lines[0])
board = [c for l in lines for c in list(l)]
p = board.index('^')
directions = ['up', 'right', 'down', 'left']
direction = 0

nxt = {
  'up': lambda p: p - width if p - width > 0 else None,
  'right': lambda p: p + 1 if (p + 1) % width > 0 else None,
  'down': lambda p: p + width if p + width < len(board) else None,
  'left': lambda p: p - 1 if p % width > 0 else None,
}


def pt1():
  global p, board, nxt, direction, directions
  while True:
    board[p] = 'X'
    n = nxt[directions[direction % len(directions)]](p)
    if n is None:
      return board.count('X')
    elif board[n] == '#':
      direction += 1
    else:
      p = n


trail = {
  'up': '|',
  'down': '|',
  'left': '-',
  'right': '-',
  '|': {
    'left': '+',
    'right': '+'
  },
  '-': {
    'up': '+',
    'down': '+'
  }
}


def pt2():
  global p, board, nxt, direction, directions
  while True:
    n = nxt[directions[direction % len(directions)]](p)
    if n is None:
      return board.count('X')
    elif board[n] == '#':
      direction += 1
    else:
      p = n


def test_pt1():
  assert pt1() == 41


def test_pt2():
  assert pt2() == True
