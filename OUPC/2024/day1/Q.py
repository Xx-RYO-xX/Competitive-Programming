import sys


def input():return sys.stdin.readline().rstrip()


def main():
    H, M, D, K, A = map(int, input().split())
    xp = 1 - ((20-H)/20)**K
    # for i in range(1, 21):
    #     x += i*(((20-(i-1))/20)**K - ((20-i)/20)**K)
    y = 5.5*M + D
    
    # print(xp, y)
    ans = min(y*(1-xp), max(0, y-A))
    
    print(ans)

if __name__ == '__main__':
    main()
