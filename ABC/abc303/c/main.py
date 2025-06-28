import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m, h, k = map(int, input().split())
    s = input()
    kaihuku = set()
    for _ in range(m):
        x, y = map(int, input().split())
        kaihuku.add((x, y))
    
    direction = {"U": (0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0), 
            "UL":(-1, -1), "UR":(1, -1), "DL":(-1, 1), "DR":(1, 1)}
    X, Y = 0, 0
    for S in s:
        dx, dy = direction[S]
        X += dx
        Y += dy
        h -= 1
        if h < 0:
            print("No")
            return
        if (X, Y) in kaihuku and h < k:
            h = k
            kaihuku.remove((X, Y))
    
    print("Yes")
    


if __name__ == '__main__':
    main()
