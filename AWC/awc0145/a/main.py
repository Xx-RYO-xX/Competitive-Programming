def main():
    import sys

    input = sys.stdin.readline
    n, m, p = map(int, input().split())
    ans = 0
    for _ in range(n):
        d, v = map(int, input().split())
        if d <= m:
            ans +=v
    print(ans*(100-p)//100)

if __name__ == "__main__":
    main()
