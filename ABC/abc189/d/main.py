import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())

    y = [[1, 1]]
    for i in range(n):
        yt, yf = y[-1]
        if s[i] == "AND":
            t = yt
            f = yt + 2 * yf
            y.append([t, f])
        else:
            t = 2 * yt + yf
            f = yf
            y.append([t, f])
    print(y[-1][0])


if __name__ == "__main__":
    main()
