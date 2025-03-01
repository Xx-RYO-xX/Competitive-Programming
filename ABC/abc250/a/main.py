import sys


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())

    ans = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if abs(i-r)+abs(j-c) == 1:
                ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()
