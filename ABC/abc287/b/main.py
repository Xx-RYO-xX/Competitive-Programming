import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    t = []
    for _ in range(m):
        t.append(input())

    ans = 0
    for S in s:
        for T in t:
            if S[-3:] == T:
                ans += 1
                break
    print(ans)


if __name__ == "__main__":
    main()
