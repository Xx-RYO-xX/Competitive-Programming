import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    senshu = [0] * (n + 1)
    for _ in range(q):
        num, x = map(int, input().split())
        if num == 1:
            senshu[x] += 1
        elif num == 2:
            senshu[x] += 2
        else:
            print("Yes" if senshu[x] >= 2 else "No")


if __name__ == "__main__":
    main()
