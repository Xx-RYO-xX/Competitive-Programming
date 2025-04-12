import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    h = n//3600
    m = n%3600//60
    s = n%60
    
    print(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2), sep=":")


if __name__ == '__main__':
    main()
