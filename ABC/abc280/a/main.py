import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    ans = 0
    for _ in range(h):
        ans += input().count("#")
    print(ans)


if __name__ == "__main__":
    main()
