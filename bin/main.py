import importlib
import sys


solution_path = sys.argv[-1]
solution = importlib.import_module(solution_path)

print('pt1:', solution.pt1())
sys.stdin.seek(0)
print('pt2:', solution.pt2())
