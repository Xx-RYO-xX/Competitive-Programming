import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    masu = [0]*(n+2)
    cnt = 0
    ans = []
    for x in a:
        l, r = masu[x-1], masu[x+1]
        if masu[x] == 0:
            if l == 0 and r == 0:
                cnt += 1
            elif l == 1 and r == 1:
                cnt -= 1
            masu[x] = 1
        else:
            if l == 0 and r == 0:
                cnt -= 1
            elif l == 1 and r == 1:
                cnt += 1
            masu[x] = 0
        ans.append(str(cnt))
    
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
