def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    from collections import defaultdict

    b = defaultdict(int)
    ans = 0
    idx = set()
    for _ in range(q):
        que = list(map(int, input().split()))
        if que[0] == 1:
            x = que[1]
            ans ^= b[x]
            b[x] += 1
            ans ^= b[x]
            idx.add(x)
        else:
            anst = 0
            rem = set()
            for B in idx:
                b[B] -= 1
                if b[B] == 0:
                    rem.add(B)
                anst ^= b[B]
            for re in rem:
                idx.remove(re)
            ans = anst
        print(ans)


if __name__ == "__main__":
    main()
