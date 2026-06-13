import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    b = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        ka = list(map(int, input().split()))
        for A in ka[1:]:
            b[A].append(i)

    for i in range(1, n + 1):
        print(len(b[i]), *b[i])


if __name__ == "__main__":
    main()
