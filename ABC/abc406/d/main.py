import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    h, w, n = map(int, input().split())
    
    x_to_y = defaultdict(set)
    y_to_x = defaultdict(set)
    for _ in range(n):
        x, y = map(int, input().split())
        x_to_y[x].add(y)
        y_to_x[y].add(x)
    q = int(input())
    for _ in range(q):
        qq, num = map(int, input().split())
        if qq == 1:
            print(len(x_to_y[num]))
            for Y in x_to_y.pop(num):
                y_to_x[Y].discard(num)
        else:
            print(len(y_to_x[num]))
            for X in y_to_x.pop(num):
                x_to_y[X].discard(num)


if __name__ == '__main__':
    sys.exit(main())
