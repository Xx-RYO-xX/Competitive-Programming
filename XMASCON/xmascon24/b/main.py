import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    T = input()
    count = defaultdict(lambda: [0]*len(T))
    print(count[1])
    




if __name__ == '__main__':
    sys.exit(main())
