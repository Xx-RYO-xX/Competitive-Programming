import sys


def input():return sys.stdin.readline().rstrip()


def e(n):
    return 10**(n-1)


def main():
    n = input()
    MOD = 998244353
    nn = int(n) - e(len(n)) + 1
    ans = nn*(nn+1)//2
    ans %= MOD
    for i in range(len(n)-1)[::-1]:
        nn = e(i+2)-e(i+1)
        ans = (ans + nn*(nn+1)//2) % MOD
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
