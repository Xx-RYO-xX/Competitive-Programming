import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    masu = []
    for _ in range(h):
        masu.append(list(map(int, input().split())))
    
    ans = []
    sum_x = []
    for y in range(h):
        sum_x.append(sum(masu[y]))
    # print(sum_x)
    sum_y = []    
    for x in range(w):
        sum_y.append(sum(masu[y][x] for y in range(h)))
    # print(sum_y)
    
    for y in range(h):
        yoko = []
        for x in range(w):
            yoko.append(sum_x[y]+sum_y[x]-masu[y][x])
        ans.append(yoko)
    for A in ans:
        print(*A)


if __name__ == '__main__':
    sys.exit(main())
