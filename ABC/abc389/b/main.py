import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    
    ans = 1
    for i in range(1, 1000):
        ans *= i
        if ans == x:
            print(i)
            exit()


if __name__ == '__main__':
    sys.exit(main())
