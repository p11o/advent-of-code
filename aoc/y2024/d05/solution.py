from aoc import read
from collections import defaultdict


def prepare():
  rules = defaultdict(lambda: [])
  updates = []
  for line in read():
    if line == '': break
    rule = line.split('|')
    for el in rule:
      rules[el].append(rule)
  for line in read():
    updates.append(line.split(','))
  return rules, updates


def valid(update, rule):
  x, y = rule
  if x in update and y in update:
    a, b = [update.index(el) for el in rule]
    return a < b
  return False


def pt1():
  rules, updates = prepare()
  middles = []
  for update in updates:
    update_rules = [
      (a,b) for el in update
      for (a, b) in rules[el]
      if a in update and b in update
    ]
    if all(valid(update, rule) for rule in update_rules):
      middles.append(int(update[len(update) // 2]))
  s = sum(middles)
  return sum(middles)



def pt2():
  rules, updates = prepare()
  middles = {}
  def reorder(update, rules, remaining):
    if not remaining and all(valid(update, rule) for rule in rules):
      middles[str(sorted(update))] = int(update[len(update)//2])
    for j, val in enumerate(remaining):
      for i in range(len(update) + 1):
        update.insert(i, val)
        reorder(update, rules, remaining[j+1:])
        update.pop(i)

  for update in updates:
    update_rules = [
      (a, b) for el in update
      for (a, b) in rules[el]
      if a in update and b in update
    ]
    statuses = [valid(update, rule) for rule in update_rules]
    if not all(statuses):
      invalid_rules = [update_rules[i] for i, status in enumerate(statuses) if not status]
      invalids = set()
      for a, b in invalid_rules:
        if a in update:
          update.remove(a)
        if b in update:
          update.remove(b)
        invalids.add(a)
        invalids.add(b)

      reorder(update, update_rules, list(invalids))

  return sum(middles.values())


def test_pt1():
  assert pt1() == 143


def test_pt2():
  assert pt2() == 123
