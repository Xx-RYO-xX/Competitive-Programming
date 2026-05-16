import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    x = int(input())
    q = int(input())
    kokubann = SortedList([x])
    for _ in range(q):
        a, b = map(int, input().split())
        kokubann.add(a)
        kokubann.add(b)
        n = len(kokubann)
        print(kokubann[n // 2])


if __name__ == "__main__":
    main()
