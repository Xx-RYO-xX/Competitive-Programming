import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for A in list(combinations(a, 2)):
        ans = max(ans, sum(A))

    print(ans)

if __name__ == '__main__':
    main()
