import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    l1, r1, l2, r2 = map(int, input().split())
    x = [0] * (100 + 1)

    for i in range(101):
        if l1 <= i <= r1:
            x[i] += 1
        if l2 <= i <= r2:
            x[i] += 1

    print(x.count(2) - 1 if x.count(2) - 1 > 0 else 0)


if __name__ == "__main__":
    main()
