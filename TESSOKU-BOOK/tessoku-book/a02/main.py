import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    a = set(map(int, input().split()))
    
    if x in a:
        print("Yes")
    else:
        print("No")
        


if __name__ == '__main__':
    main()
