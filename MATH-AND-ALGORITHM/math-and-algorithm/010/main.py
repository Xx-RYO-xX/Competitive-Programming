import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    
    n = int(input())
    
    print(math.factorial(n))


if __name__ == '__main__':
    main()
