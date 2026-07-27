def main():
    import sys

    input = sys.stdin.readline

    k = int(input())

    if k % 2 != 0 and k % 5 != 0:
        ans = 1
        amari = 7 % k
        while amari != 0:
            ans += 1
            amari = (amari * 10 + 7) % k
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
