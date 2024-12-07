from aoc import read
from operator import mul, add
from itertools import product
from functools import reduce


def prepare():
  return [
    (int(res), list(map(int, nums.split(' '))))
    for res, nums in read(lambda x: x.split(': '))
  ]

def compute(ops=[mul, add]):
  eqs = prepare()
  def reducer(acc, op_val):
    op, val = op_val
    return op(acc, val)
  
  return sum(
    res
    for res, values in eqs
    if any(
      reduce(reducer, zip(p, values[1:]), values[0]) == res 
      for p in product(ops, repeat=len(values) - 1)
    )
  )


def pt1():
  return compute()


def pt2():
  concat = lambda x, y: int(f"{x}{y}")
  return compute([mul, add, concat])


def test_pt1():
  assert pt1() == 3749


def test_pt2():
  assert pt2() == 11387
