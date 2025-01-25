import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, = int(input())
    a = list(map(int, input().split()))
    
    even = []
    odd = []
    
    for i in range(n):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    
    even.sort(), odd.sort()

    


if __name__ == '__main__':
    main()
