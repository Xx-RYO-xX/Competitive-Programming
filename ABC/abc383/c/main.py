import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    # import networkx as nx
    # import matplotlib.pyplot as plt
    from collections import deque
    
    h, w, d = map(int, input().split())
    s = []
    humid = []
    humid_masu = []  
    queue = deque()
    
    for i in range(h):
        s.append(input())
        humid.append([-1]*w)  
        for j in range(w):
            if s[i][j] == "H":
                humid_masu.append((i, j))  
    
    for y, x in humid_masu:
        humid[y][x] = 0
        queue.append((y, x, 0))
    
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x, dist = queue.popleft()
        if dist >= d:
            continue
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and s[ny][nx] != '#' and humid[ny][nx] == -1:
                humid[ny][nx] = dist + 1
                queue.append((ny, nx, dist+1))
    
    count = 0
    for y in range(h):
        for x in range(w):
            if s[y][x] in {'.', 'H'} and 0 <= humid[y][x] <= d:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
