from aoc import read
from collections import defaultdict
from functools import cmp_to_key

def prepare():
  rules = defaultdict(list)
  for line in read():
    if line == '': break
    a, b = line.split('|')
    rules[a].append(b)
  updates = [line.split(',') for line in read()]
  return rules, updates


rules, updates = prepare()


def valid(update):
  return not any(r in update[:i] for i, u in enumerate(update) for r in rules[u])


def pt1():
  return sum(
    int(update[len(update) // 2])
    for update in updates
    if valid(update)
  )


def pt2():
  cmp = cmp_to_key(lambda a, b: -1 if b in rules[a] else 1)

  return sum(
    int(sorted(update, key=cmp)[len(update) // 2])
    for update in updates
    if not valid(update)
  )


def test_pt1():
  assert pt1() == 143


def test_pt2():
  assert pt2() == 123
