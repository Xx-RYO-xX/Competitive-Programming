import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    s, k = input().split()
    k = int(k)
    
    s = sorted(set(permutations(s)))
    print("".join(s[k-1]))

if __name__ == '__main__':
    main()
