import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x, p, a, b = map(int, input().split())
    xt = x**a
    ans = xt%p
    for i in range(b-a):
        xt *= x
        anst = xt%p
        ans = min(ans, anst)
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
