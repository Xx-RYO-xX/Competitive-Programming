import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))[::-1]

    x = str(bin(x))[2:].zfill(n)

    ans = 0
    for i in range(n):
        if x[i] == "1":
            ans += a[i]

    print(ans)


if __name__ == "__main__":
    main()
