import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s, c = map(int, input().split())
    
    ans = 0
    print(2*s <= c)
    if  2*s <= c:
        ans = s
        c -= 2*s
        ans += c//3
    else:
        ans = c//2
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
