import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    q = []
    r = []
    for _ in range(n):
        qt, rt = map(int, input().split())
        q.append(qt)
        r.append(rt)
    qq = int(input())
    for _ in range(qq):
        t, d = map(int, input().split())
        t -= 1
        day = d+(r[t]- d%q[t]) % q[t]
        print(day)

if __name__ == '__main__':
    main()
