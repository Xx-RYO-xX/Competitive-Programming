import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    n, k = map(int, input().split())
    s = list(input())
    
    a = list(permutations(s))
    print(len(a))


if __name__ == '__main__':
    sys.exit(main())
