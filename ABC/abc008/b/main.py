import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    n = int(input())
    s = defaultdict(int)
    for _ in range(n):
        s[input()] += 1
    
    print(max(s, key=s.get))


if __name__ == '__main__':
    sys.exit(main())
