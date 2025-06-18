import sys


def input():return sys.stdin.readline().rstrip()


def main():
    h1 = int(input())
    h2 = int(input())
    
    print(h1-h2)

if __name__ == '__main__':
    main()
