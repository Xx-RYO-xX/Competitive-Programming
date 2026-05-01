import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = sorted(a)
    if a == ans:
        print("Yes")
        return

    ak = [[] for _ in range(k)]

    for i in range(n):
        ak[i % k].append(a[i])

    for i in range(k):
        ak[i].sort(reverse=True)

    swap = []
    for i in range(n):
        swap.append(ak[i % k].pop())

    if swap == ans:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
