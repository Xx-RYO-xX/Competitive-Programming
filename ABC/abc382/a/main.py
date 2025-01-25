import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, d = map(int, input().split())
    s = input()
    
    aki = s.count(".")
    print(aki+d)


if __name__ == '__main__':
    main()
