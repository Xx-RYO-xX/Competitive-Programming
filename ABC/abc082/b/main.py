import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = sorted(input())
    x = sorted(input(), reverse=True)
    
    print("Yes" if s < x else "No")
    


if __name__ == '__main__':
    sys.exit(main())
