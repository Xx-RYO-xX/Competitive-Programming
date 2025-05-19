import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c, d = map(int, input().split())
    end = a*60+b
    s = c*60+d
    print("Yes" if s < end else "No")
    


if __name__ == '__main__':
    sys.exit(main())
