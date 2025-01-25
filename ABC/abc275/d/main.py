import sys 

sys.setrecursionlimit(10**9)   

def input():return sys.stdin.readline().rstrip()


def main():
    from functools import cache
    n = int(input())
    
    @cache
    def f(n):
        if n == 0:
            return 1
        
        return f(n//2) + f(n//3)

    print(f(n))


if __name__ == '__main__':
    sys.exit(main())
