import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())

    junni = list([False] * m for i in range(n))

    for _ in range(k):
        a, b = map(lambda x: int(x) - 1, input().split())
        junni[a][b] = True
        if all(junni[a]):
            print(a + 1, end=" ")


if __name__ == "__main__":
    main()
