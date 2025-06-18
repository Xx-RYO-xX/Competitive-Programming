import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import decimal
    sx, sy, gx, gy = map(decimal.Decimal, input().split())
    
    ans = (sx*gy + gx*sy)/(sy+gy)
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
