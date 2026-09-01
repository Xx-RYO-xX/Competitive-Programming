def main():
    import sys

    input = sys.stdin.readline
    masu = set()
    ans = 0
    n, m = map(int, input().split())
    for _ in range(m):
        r, c = map(int, input().split())
        masus = [(r, c), (r+1, c), (r, c+1), (r+1, c+1)]
        for rc in masus:
            if rc in masu:
                break
        else:
            for rc in masus:
                masu.add(rc)
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
