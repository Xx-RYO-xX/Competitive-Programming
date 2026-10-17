def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    s = list(input())[:-1]
    t = list(input())[:-1]

    s_in = []
    for i in range(len(s) - len(t) + 1):
        # print(t, s[i : i + len(t)])
        if t == s[i : i + len(t)]:
            s_in.append((i + 1, i + len(t)))

    from bisect import bisect_right

    for _ in range(q):
        l, r = map(int, input().split())
        idx = bisect_right(s_in, (l, r))
        print(s_in[idx])


if __name__ == "__main__":
    main()
