import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = SortedList(map(int, input().split()))
        b = list(map(int, input().split()))
        
        ans = 0
        for B in b:
            idx = a.bisect_left((m-B)%m)
            if idx == len(a):
                idx = 0
            poped = a.pop(idx)
            ans += (poped+B)%m
        
        
        print(ans)


if __name__ == '__main__':
    main()
