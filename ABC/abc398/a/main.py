import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    if n % 2 == 0:
        if n == 2:
            print("==")
        else:
            print("-"*(n//2-1)+"=="+"-"*(n//2-1))
    else:
        if n == 1:
            print("=")
        else:
            print("-"*(n//2)+"="+"-"*(n//2))



if __name__ == '__main__':
    sys.exit(main())
