import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        o, u, p, c = map(int, input().split())
        if p % 10 == 0 and o == u == p // 10 == c:
            print(p // 10)
        else:
            print(min([o, u, p, c]) - 1)


if __name__ == "__main__":
    main()
