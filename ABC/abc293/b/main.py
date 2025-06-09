import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    yobu = set()
    for i in range(1, n+1):
        if i not in yobu:
            yobu.add(a[i-1])
    
    # print(yobu)
    
    print(n-len(yobu))
    for i in range(1, n+1):
        if i not in yobu:
            print(i, end=" ")


if __name__ == '__main__':
    sys.exit(main())
