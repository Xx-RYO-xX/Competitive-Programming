import sys 
from numba import njit


def input():return sys.stdin.readline().rstrip()


@njit
def solve(n, l):
    ans = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                    ans += l[c] < l[a]+l[b]
    return ans


def main():
    n = int(input())
    l = sorted(map(int, input().split()))
    
    
    print(solve(n, l))


if __name__ == '__main__':
    sys.exit(main())
