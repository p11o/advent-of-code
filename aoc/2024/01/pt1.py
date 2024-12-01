from heapq import heappush, heappop
from aoc import read


def main():
    total = 0

    a_list = []
    b_list = []
    for a, b in read(lambda x: map(int, x.split())):
        heappush(a_list, a)
        heappush(b_list, b)
    
    while a_list:
        a, b = heappop(a_list), heappop(b_list)
        total += abs(a - b)

    return total


if __name__ == '__main__':
    print(main())