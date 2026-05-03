import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = sorted(map(int, input().split()), key=abs)

    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1

    if cnt % 2 == 0:
        print(sum([abs(A) for A in a]))
    else:
        print(-1 * abs(a[0]) + sum([abs(a[i]) for i in range(1, n)]))


if __name__ == "__main__":
    main()
