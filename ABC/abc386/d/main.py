import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, m = map(int, input().split())

    row = defaultdict(dict)
    col = defaultdict(dict)
    for _ in range(m):
        x, y, c = input().split()
        x = int(x)
        y = int(y)
        row[x][y] = c
        col[y][x] = c


    def check(data, other, is_row):
        for key, dict_ in data.items():
            last_black = max((pos for pos, color in dict_.items() if color == 'B'), default=-1)
            first_white = min((pos for pos, color in dict_.items() if color == 'W'), default=n+2)

            if last_black >= first_white:
                return False

            if is_row:
                for pos in range(last_black + 1):
                    other[pos][key] = 'B'
                for pos in range(first_white, n):
                    other[pos][key] = 'W'
            else:
                for pos in range(last_black + 1):
                    other[key][pos] = 'B'
                for pos in range(first_white, n):
                    other[key][pos] = 'W'
        return True


    if not check(row, col, is_row=True) or not check(col, row, is_row=False):
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    sys.exit(main())
