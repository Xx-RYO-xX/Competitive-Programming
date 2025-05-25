import sys 


def input():return sys.stdin.readline().rstrip()


def print_2d(lst, sep=None):
    """
    2次元配列を出力する関数

    Parameters
    ----------
    lst : list
        出力したい2次元配列
    sep : str
        区切り文字(デフォルトはNone)
    """
    for LIST in lst:
        print(*LIST, sep=sep)




def main():
    r, c = map(int, input().split())
    b = []
    bombs = []
    for y in range(r):
        tmp = list(input())
        b.append(tmp)
        for x in range(c):
            if tmp[x] != "#" and tmp[x] != ".":
                bombs.append((x, y, int(tmp[x])))
    
    for bomb in bombs:
        xx, yy, iryoku = bomb
        for y in range(r):
            for x in range(c):
                if abs(x-xx)+abs(y-yy)<=iryoku:
                    b[y][x] = "."
    
    
    print_2d(b, sep="")
    


if __name__ == '__main__':
    sys.exit(main())
