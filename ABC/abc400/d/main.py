import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    a, b, c, d = map(int, input().split())
    
    start = (a-1, b-1)
    end = (c-1, d-1)
    inf = 10**9
    dist = [[inf] * w for _ in range(h)]
    dist[start[0]][start[1]] = 0

    kicked = [[False]*w for _ in range(h)]
    
    deque = deque()
    deque.append(start)    
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while deque:
        x, y = deque.popleft()
        if (x, y) == end:
            print(dist[x][y])
            return
        now = dist[x][y]
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if s[nx][ny] == '.' and dist[nx][ny] > now:
                    dist[nx][ny] = now
                    deque.appendleft((nx, ny))
                    
        for dx, dy in direction:
            for step in range(1, 3):
                nx = x + dx * step
                ny = y + dy * step
                if not (0 <= nx < h and 0 <= ny < w):
                    break
                if dist[nx][ny] <= now + 1:
                    continue
                new_cost = now + 1
                if s[nx][ny] == '#':
                    if not kicked[nx][ny]:
                        kicked[nx][ny] = True
                        dist[nx][ny] = new_cost
                        deque.append((nx, ny))
                    else:
                        if dist[nx][ny] > new_cost:
                            dist[nx][ny] = new_cost
                            deque.append((nx, ny))
                else:
                    dist[nx][ny] = new_cost
                    deque.append((nx, ny))
                    
                    
                    
                    
    print(-1)

if __name__ == '__main__':
    sys.exit(main())