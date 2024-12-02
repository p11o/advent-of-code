import unittest
import importlib
import sys

day = sys.argv[-1]
solution = importlib.import_module(f'aoc.y2024.d{day}.solution')

class TestSolution(unittest.TestCase):
  def setUp(self):
    sys.stdin.seek(0)

  def test_pt1(self):
    solution.test_pt1()

  def test_pt2(self):
    solution.test_pt2()

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromTestCase(TestSolution))
unittest.TextTestRunner().run(suite)
