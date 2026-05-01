import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = []
    for i in range(n):
        at = []
        for j in range(i + 1):
            if j == 0 or j == i:
                at.append(1)
            else:
                at.append(a[i - 1][j - 1] + a[i - 1][j])
        print(*at)
        a.append(at)


if __name__ == "__main__":
    main()
