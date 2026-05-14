import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = list(input())
    if len(a) == 1:
        print(0)
        return
    re_a = a[::-1].copy()

    dist = 0
    for i in range(len(a)):
        if a[i] != re_a[i]:
            dist += 1

    if dist == 2:
        print(25 * (len(a) - 2) + 24 * 2)
    elif dist == 0 and len(a) % 2 != 0:
        print(25 * (len(a) - 1))
    else:
        print(25 * len(a))


if __name__ == "__main__":
    main()
