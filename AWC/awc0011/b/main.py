import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w, k = map(int, input().split())
    c1, c2 = input().split()
    for _ in range(h):
        s = list(input())
        for __ in range(k):
            for S in s:
                if S == "#":
                    print(c1 * k, end="")
                else:
                    print(c2 * k, end="")
            print()


if __name__ == "__main__":
    main()
