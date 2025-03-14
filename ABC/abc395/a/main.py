import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-1):
        if a[i] >= a[i+1]:
            print("No")
            return
    
    print("Yes")
    


if __name__ == '__main__':
    sys.exit(main())
