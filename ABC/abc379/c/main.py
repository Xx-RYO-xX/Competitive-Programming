import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    xt = list(map(int, input().split()))
    at = list(map(int, input().split()))
    if n != sum(at):
        print(-1)
        exit()
    xa = [list(item) for item in sorted(zip(xt, at))]
    if xa[0][0] != 1:
        print(-1)
        exit()
    
    ans = 0
    for i in range(m):
        x, a = xa[i]
        # print(x, a)
        if i != m-1:
            nx, na = xa[i+1]
            sa = nx-x
            if sa <= a:
                xa[i+1][1] += a-sa
                ans += (sa*(sa-1))//2+sa*(a-sa)
            else:
                print(-1)
                exit()
        else:
            if n-x+1 == a:
                ans += (a*(a-1))//2
            else:
                print(-1)
                exit()
    
    print(ans)



if __name__ == '__main__':
    main()
