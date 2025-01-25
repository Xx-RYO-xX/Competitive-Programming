import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, t, sigma = map(int, input().split())
    wh = []
    for _ in range(n):
        wh.append(tuple(map(int, input().split())))
    
    print(wh)
    
    for _ in range(t):
        ans = []
        for i in range(n):
            w, h = wh[i]
            if w < h:
                w, h = h, w
            p = i


if __name__ == '__main__':
    main()
