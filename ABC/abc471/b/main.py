def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    from collections import defaultdict

    ans = defaultdict(int)
    for _ in range(n):
        s = input()[:-1]
        ans[s.upper()] += 1

    print(max(ans.values()))


if __name__ == "__main__":
    main()
