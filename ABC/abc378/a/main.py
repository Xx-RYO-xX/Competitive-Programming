import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    a = Counter(map(int, input().split()))
    
    ans = 0
    for A in a:
        ans += a[A] // 2

    print(ans)

if __name__ == '__main__':
    main()
