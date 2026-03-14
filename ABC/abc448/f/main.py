import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    n = int(input())

    fx, fy = map(int, input().split())
    xy = []
    num = dict()
    for i in range(2, n + 1):
        x, y = map(int, input().split())
        xy.append((x, y))
        num[(x, y)] = i

    xy.sort(key=lambda x: abs(x[0] - fx) + abs(x[1] - fy))

    print(1, end=" ")
    for x, y in xy:
        print(num[(x, y)], end=" ")


if __name__ == "__main__":
    main()
