import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    # dp = 
    max_bit = 2**n
    for i in range(max_bit):
        ans = 0
        ans2 = 0
        for j in range(n):
            bit = (2 ** j)
            # print(i, bit)
            if (i // bit) % 2 == 1:
                ans += a[j]
            if ((max_bit-1-i) // bit ) % 2 == 1:
                ans2 += a[j]
        if ans == s or ans2 == s:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    main()
