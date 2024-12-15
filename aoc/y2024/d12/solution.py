from collections import defaultdict
from itertools import groupby
import sys



def segments():
  MAP = [line.strip() for line in sys.stdin]

  for line in MAP:
      i = 0
      yield [(k, i, i:=i+len(list(v))) for k, v in groupby(line)]


def regions():
  # prev, curr - {g -> rng -> id}
  # regions - id -> p, a
  regions, id, prev = defaultdict(dict), 0, defaultdict(lambda: defaultdict(dict))
  for segment in segments():
    curr = defaultdict(lambda: defaultdict(dict))
    for g, x1, x2 in segment:
      region = regions[g]
      perimeter, area, sides = 2 * (x2 - x1) + 2, x2 - x1, 4
      # merge with above segments
      intersections = defaultdict(list)
      for prng, pid in prev[g].items():
        px1, px2 = prng
        if intersection := set(range(x1, x2)).intersection(set(range(px1, px2))):
          perimeter -= 2 * len(intersection)
          sides += sum([
            -2 if px1 == x1 else 0, # flush with left
            -2 if px2 == x2 else 0, # flush with right
          ])
          intersections[pid].append((px1, px2))

      nextid = min({*intersections.keys(), id})

      pperim, parea, psides = tuple(map(sum, zip(*[region[k] for k in intersections]))) if intersections else (0, 0, 0)
      region[nextid] = perimeter + pperim, area + parea, sides + psides
      for k, prngs in intersections.items():
        for prng in prngs:
          prev[g][prng] = nextid
        if k != nextid:
          region.pop(k)
      curr[g][(x1, x2)] = nextid
      id += 1
    prev = curr      
  return regions

def pt1():
  return sum([p * a for _, grps in regions().items() for p, a, _ in grps.values()])


def pt2():
  return sum([s * a for _, grps in regions().items() for _, a, s in grps.values()])


def test_pt1():
  assert pt1() == 1930


def test_pt2():
  v = pt2()
  print(v)
  assert v == 1206
