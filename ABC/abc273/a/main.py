import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    def f(x):
        if x == 0:
            return 1
        return x*f(x-1)
    
    print(f(n))


if __name__ == '__main__':
    sys.exit(main())
