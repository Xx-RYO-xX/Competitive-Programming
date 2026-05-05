import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    even = []
    odd = []

    for i in range(n):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])

    even.sort(), odd.sort()

    if len(even) == len(odd) == 1:
        print(-1)
        return

    ans = []
    if len(even) >= 2:
        ans.append(even[-1] + even[-2])
    if len(odd) >= 2:
        ans.append(odd[-1] + odd[-2])

    print(max(ans))


if __name__ == "__main__":
    main()
