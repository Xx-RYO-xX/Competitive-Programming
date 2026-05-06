import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    kk = 0
    ar = []
    for i in range(n):
        a, b = map(int, input().split())
        ar.append((a, b))

    for a, b in sorted(ar):
        kk += b
        if kk >= k:
            print(a)
            return


if __name__ == "__main__":
    main()
