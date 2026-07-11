import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())
    a = list(map(int, input().split()))

    value = defaultdict(list)
    for i in range(n):
        value[a[i]].append(i)

    ans = float("inf")
    for key, lst in value.items():
        for i in range(len(lst) - 1):
            ans = min(ans, lst[i + 1] - lst[i] + 1)
    print(ans if ans != float("inf") else -1)


if __name__ == "__main__":
    main()
