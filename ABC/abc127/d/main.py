import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    cb = []
    for _ in range(m):
        b, c = map(int, input().split())
        cb.append([c, b])
    cb.sort()

    for i in range(n):
        if cb:
            if a[i] < cb[-1][0]:
                a[i] = cb[-1][0]
                cb[-1][1] -= 1
                if cb[-1][1] == 0:
                    cb.pop()
        else:
            break

    print(sum(a))


if __name__ == "__main__":
    main()
