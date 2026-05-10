import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split()))[1:])
    c = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append((i, len(a[i]) * c[i]))

    # print(b)
    k -= 1
    for idx, cnt in b:
        if k - cnt < 0:
            # print(k)
            print(a[idx][k % len(a[idx])])
            return
        else:
            k -= cnt


if __name__ == "__main__":
    main()
