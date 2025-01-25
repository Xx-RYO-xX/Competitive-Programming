import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, d = map(int, input().split())
    t = []
    l = []
    for _ in range(n):
        tt, lt = map(int, input().split())
        t.append(tt)
        l.append(lt)
    for k in range(1, d+1):
        ans = []
        for i in range(n):
            ans.append(t[i]*(l[i]+k))
        print(max(ans))


if __name__ == '__main__':
    sys.exit(main())
