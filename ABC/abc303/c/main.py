def main():
    from collections import defaultdict
    n, m, h, k = map(int, input().split())
    s = input()
    x_y = defaultdict(set)
    for _ in range(m):
        x, y = map(int, input().split())
        x_y[x].add(y)
    
    direction = {"U": (0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0), "UL":(-1, -1), "UR":(1, -1), "DL":(-1, 1), "DR":(1, 1)}
    
    tx, ty = 0, 0
    for S in s:
        dx, dy = direction[S]
        tx += dx
        ty += dy
        h -= 1
        if h < 0:
            print("No")
            exit()
        if h < k and ty in x_y[tx]:
            x_y[tx].remove(ty)
            h = k
    print("Yes")


if __name__ == '__main__':
    main()