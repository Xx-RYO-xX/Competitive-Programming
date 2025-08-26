import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, Counter

    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())

    ans = defaultdict(int)
    for i in range(m):
        cnt = Counter(S[i] for S in s)
        if cnt["1"] == 0 or cnt["0"] == 0:
            for j in range(1, n + 1):
                ans[j] += 1
        elif cnt["0"] < cnt["1"]:
            for j in range(1, n + 1):
                ans[j] += 1 if s[j - 1][i] == "0" else 0
        else:
            for j in range(1, n + 1):
                ans[j] += 1 if s[j - 1][i] == "1" else 0

    print(*sorted(k for k, v in ans.items() if v == max(ans.values())))


if __name__ == "__main__":
    main()
