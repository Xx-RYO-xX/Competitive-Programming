import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sympy import factorint

    k = int(input())

    soinnsu = factorint(k)

    ans = 0
    for num, sisuu in soinnsu.items():
        cnt = sisuu
        for i in range(1, sisuu + 1):
            now = num * i
            while now % num == 0:
                now //= num
                cnt -= 1
            if cnt <= 0:
                break
        ans = max(ans, num * i)

    print(ans)


if __name__ == "__main__":
    main()
