import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    
    ans = 0.5 * abs(xa*(yb - yc) + xb*(yc - ya) + xc*(ya - yb))
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
