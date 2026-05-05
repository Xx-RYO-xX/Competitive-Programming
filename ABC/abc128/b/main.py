import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    sp = []
    for i in range(n):
        s, p = input().split()
        sp.append((s, int(p), i + 1))

    sp.sort(key=lambda x: (x[0], -x[1]))

    for s, p, i in sp:
        print(i)


if __name__ == "__main__":
    main()
