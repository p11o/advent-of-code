from aoc import read
from collections import Counter

def main():
    a_list = []
    def build():
        for a, b in read(lambda x: map(int, x.split())):
            a_list.append(a)
            yield b
    b_counter = Counter(build())
        
    return sum(el * b_counter.get(el, 0) for el in a_list)


if __name__ == '__main__':
    print(main())