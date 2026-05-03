import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(2**n):
        x = 0
        y = 0
        for j in range(n):
            bit = 2**j
            if (i // bit) % 2 == 1:
                x += v[j]
                y += c[j]
        ans = max(ans, x - y)

    print(ans)


if __name__ == "__main__":
    main()
