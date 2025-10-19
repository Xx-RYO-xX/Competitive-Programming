import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, k = map(int, input().split())
    s = list(input())

    ans = defaultdict(int)
    for i in range(n - k + 1):
        t = s[i : i + k]
        ans[tuple(t)] += 1

    ans_lst = [key for key, value in ans.items() if value == max(ans.values())]

    print(max(ans.values()))
    for a in sorted(ans_lst):
        print("".join(a))


if __name__ == "__main__":
    main()
