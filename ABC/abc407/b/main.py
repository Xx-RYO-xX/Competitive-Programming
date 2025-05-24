import sys


def input():return sys.stdin.readline().rstrip()


def main():
    x, y = map(int, input().split())
    
    ans = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i+j >= x or abs(i-j) >= y:
                ans += 1
    
    
    print(ans/36)


if __name__ == '__main__':
    sys.exit(main())
