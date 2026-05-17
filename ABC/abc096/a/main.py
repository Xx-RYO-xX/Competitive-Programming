import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(1, a + 1):
        for j in range(1, 31):
            ans += i == j
            if a == i and b == j:
                print(ans)
                return


if __name__ == "__main__":
    main()
