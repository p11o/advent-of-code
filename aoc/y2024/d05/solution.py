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
  return True


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
  return sum(middles)



def pt2():
  rules, updates = prepare()
  middles = {}
  def reorder(update, rules, remaining, idx):
    if not remaining and all(valid(update, rule) for rule in rules):
      mid = int(update[len(update)//2])
      middles[f"{idx}-{str(sorted(update))}"] = mid

    elif all(valid(update, rule) for rule in rules) and f"{idx}-{str(sorted(update+remaining))}" not in middles:
      for j, val in enumerate(remaining):
        for i in range(len(update) + 1):
          update.insert(i, val)
          reorder(update, rules, remaining[:j] + remaining[j+1:], idx)
          update.pop(i)

  for i, update in enumerate(updates):
    update_rules = [
      (a, b) for el in update
      for (a, b) in rules[el]
      if a in update and b in update
    ]
    statuses = [valid(update, rule) for rule in update_rules]
    if not all(statuses):
      reorder([], update_rules, update, i)

  return sum(middles.values())


def test_pt1():
  assert pt1() == 143


def test_pt2():
  assert pt2() == 123
