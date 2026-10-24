def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += a[i] 
    print(ans)

if __name__ == "__main__":
    main()
