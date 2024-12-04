from aoc import read


XMAS = 'XMAS'

def matrix():
  return list(read())

def rotate(matrix):
  width = len(matrix[0])
  flattened = ''.join(matrix)
  return [flattened[width - i - 1::width] for i in range(width)]

def diagonal(matrix):
  height, width = len(matrix), len(matrix[0])
  rows, max_cols = height + width - 1, min(height, width)
  flattened = ''.join(matrix)
  for r in range(rows):
    cols = min(max_cols, r + 1, rows - r)
    start = r * width if r < height else ((height - 1) * width) + (r + 1 - height)
    yield flattened[start::-(width - 1)][:cols]


def count(lists):
  return sum(row.count(XMAS) + row.count(XMAS[::-1]) for row in lists)

def pt1():
  m = matrix()
  rot_m = rotate(m)
  diag_m = list(diagonal(m))
  diag_rot_m = list(diagonal(rot_m))

  return count(m + rot_m + diag_m + diag_rot_m)


def is_xmas(i, j, m):
  top, bottom = i - 1, i + 1
  left, right = j - 1, j + 1
  c1 = ''.join(sorted([m[bottom][left], m[top][right]]))
  c2 = ''.join(sorted([m[top][left], m[bottom][right]]))
  return c1 == c2 == 'MS'

def pt2():
  m = list(read())
  height, width = len(m), len(m[0])
  return sum(
    1
    for i in range(1, height-1)
    for j in range(1, width-1)
    if m[i][j] == 'A' and is_xmas(i, j, m)
  )


def test_pt1():
  assert pt1() == 18


def test_pt2():
  assert pt2() == 9
