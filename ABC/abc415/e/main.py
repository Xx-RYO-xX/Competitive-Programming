import sys


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    
    
    from collections import deque, defaultdict
    def bfs(x):
        coins = defaultdict(lambda: defaultdict(lambda:-1))
        
        coin0 = x+a[0][0]-p[0]
        if coin0 < 0:
            return False
        coins[0][0] = coin0
        
        q = deque([(0, 0, coin0)])
        while q:
            i, j, coin = q.popleft()
            if i == h-1 and j == w-1:
                return True
            for di, dj in ((0, 1), (1, 0)):
                ni, nj = i+di, j+dj
                if ni < h and nj < w:
                    day = ni+nj
                    ncoin = coin + a[ni][nj]-p[day]
                    if ncoin >= 0 and ncoin > coins[ni][nj]:
                        coins[ni][nj] = ncoin
                        q.append((ni, nj, ncoin))
        return False


    left, right = 0, 10**9
    while left < right:
        mid = (left+right)//2
        if bfs(mid):
            right = mid
        else:
            left = mid+ 1
    
    print(left)


if __name__ == '__main__':
    main()
