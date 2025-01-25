import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from sortedcontainers import SortedList
    import bisect
    
    n, m, sx, sy = map(int, input().split())
    x_y = defaultdict(list)
    y_x = defaultdict(list)

    for _ in range(n):
        x, y = map(int, input().split())
        x_y[x].append(y)
        y_x[y].append(x)

    for xy in x_y:
        x_y[xy].sort()
    
    for yx in y_x:
        y_x[yx].sort()
    
    def direction(D, C):
        return dict({"U": (0, C), "D":(0, -C), "L":(-C, 0), "R":(C, 0)})[D]

    visited = set()
    for _ in range(m):
        d, c = input().split()
        c = int(c)
        dx, dy = direction(d, c)

        new_x, new_y = sx + dx, sy + dy
        if dx == 0:
            down, up = sorted([sy, new_y])
            y_lst = x_y[sx]
            
            left_idx = bisect.bisect_left(y_lst, down)
            right_idx = bisect.bisect_right(y_lst, up)
            
            for yy in y_lst[left_idx:right_idx]:
                visited.add((sx, yy))
        else:  
            left, right = sorted([sx, new_x])
            x_lst = y_x[sy]
            
            left_idx = bisect.bisect_left(x_lst, left)
            right_idx = bisect.bisect_right(x_lst, right)
            
            for xx in x_lst[left_idx:right_idx]:
                visited.add((xx, sy))

        sx, sy = new_x, new_y

    print(sx, sy, len(visited))


if __name__ == '__main__':
    sys.exit(main())
