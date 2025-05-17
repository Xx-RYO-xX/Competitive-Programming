import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    r, x = map(int, input().split())
    if x == 1:
        print("Yes" if 1600 <= r <= 2999 else "No")
    else:
        print("Yes" if 1200 <= r <= 2399 else "No")
        
        


if __name__ == '__main__':
    sys.exit(main())
