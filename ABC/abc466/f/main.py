def main():
    import sys

    input = sys.stdin.readline

    for _ in range(int(input())):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))

        def f(xx):
            print(xx)
            for A in a:
                xx %= A
                print(xx)
            print()
            return xx

        ans = 0
        lst = []
        for i in range(1, x + 1):
            if f(i) == 0:
                ans += 1
                lst.append(i)

        print(lst)
        print(ans)


if __name__ == "__main__":
    main()
