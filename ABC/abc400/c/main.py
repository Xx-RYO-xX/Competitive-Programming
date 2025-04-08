import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    n = int(input())

    ans = 0
    a = 1
    while True:
        a2 = 2**a
        if n < a2: break
        max_a = int(math.isqrt(n // a2))
        odd = (max_a+1)//2
        ans += odd
        a += 1
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
