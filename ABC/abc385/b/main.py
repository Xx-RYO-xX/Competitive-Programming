import sys 


def input():return sys.stdin.readline().rstrip()


direction = {"U": (0, -1), "D":(0, 1), "L":(-1, 0), "R":(1, 0), "UL":(-1, -1), "UR":(1, -1), "DL":(-1, 1), "DR":(1, 1)}


def is_end(x: int, y: int, max_x: int, max_y: int, muki: str) -> bool: 
    return {"U": y == 0, "D": y == max_y, "L": x == 0, "R": x == max_x}[muki]


def main():
    h, w, X, Y = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    t = input()
    X -= 1
    Y -= 1
    visited_houses = set()
    if s[X][Y] == "@":
        visited_houses.add((Y, X))

    for c in t:
        dx, dy = direction[c][::-1]
        if not is_end(X+dx, Y+dy, h-1, w-1, c) and s[X+dx][Y+dy] in (".", "@"):
            X += dx
            Y += dy
            if s[X][Y] == "@":
                visited_houses.add((Y, X))

    print(X+1, Y+1, len(visited_houses))


if __name__ == '__main__':
    sys.exit(main())
