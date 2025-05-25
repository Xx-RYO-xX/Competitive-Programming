import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    n = int(input())
    s = defaultdict(int)
    for _ in range(n):
        s[input()] += 1
    
    max_value = max(s.values())
    ans = set()
    for S in s:
        if s[S] == max_value:
            ans.add(S)
    
    print(*sorted(ans), sep="\n")


if __name__ == '__main__':
    main()
