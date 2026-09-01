def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    sums = sum(a)
    sums2 = 0
    for i in range(n):
        sums2 += a[i]
        if sums2 >= sums/2:
            print(i+1)
            return


if __name__ == "__main__":
    main()
