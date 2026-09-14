def main():
    import sys

    input = sys.stdin.readline
    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    pp = []
    ppp = set()
    for _ in range(q):
        a = int(input())
        pp.append(a)
        ppp.add(a)

    ans = []
    ansin = set()
    for i in range(q)[::-1]:
        if pp[i] not in ansin:
            ans.append(pp[i])
        ansin.add(pp[i])
    for i in range(n)[::-1]:
        if p[i] not in ppp:
            ans.append(p[i])
    print(*ans[::-1])


if __name__ == "__main__":
    main()
