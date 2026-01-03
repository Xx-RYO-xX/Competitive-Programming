import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import bisect
    from collections import defaultdict

    n = int(input())
    a = list(map(int, input().split()))
    a_to_idx = defaultdict(list)
    for i in range(n):
        a_to_idx[a[i]].append(i + 1)

    print(ans)


if __name__ == "__main__":
    main()
