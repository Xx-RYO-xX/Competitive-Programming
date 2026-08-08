def main():
    import sys

    input = sys.stdin.readline
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        if p < a[i]:
            print(i)
            return
        else:
            p -= a[i]
    print(n)


if __name__ == "__main__":
    main()
