import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    s = []
    for _ in range(m):
        s.append(list(map(int, input().split()))[1:])
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2**n):
        led = 0
        for j in range(m):
            cnt = 0
            for switch in s[j]:
                bit = 2 ** (switch - 1)
                if (i // bit) % 2 == 1:
                    cnt += 1
            led += cnt % 2 == p[j]
        ans += led == m

    print(ans)


if __name__ == "__main__":
    main()
