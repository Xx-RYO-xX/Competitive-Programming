import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            katamuki = (y2-y1)/(x2-x1)
            if -1 <= katamuki <= 1:
                ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()
