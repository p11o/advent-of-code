from aoc import read
from operator import mul, add
from itertools import product
from functools import reduce


def data():
  for res, nums in read(lambda x: x.split(': ')):
    yield (int(res), list(map(int, nums.split(' '))))


def compute(ops=[mul, add]):
  def reducer(acc, op_val):
    op, val = op_val
    return op(acc, val)
  
  return sum(
    res
    for res, values in data()
    if any(
      reduce(reducer, zip(p, values[1:]), values[0]) == res 
      for p in product(ops, repeat=len(values) - 1)
    )
  )


def pt1():
  return compute()


def pt2():
  def concat(x, y): return int(f"{x}{y}")
  return compute([mul, add, concat])


def test_pt1():
  assert pt1() == 3749


def test_pt2():
  assert pt2() == 11387
