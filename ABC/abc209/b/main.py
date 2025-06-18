import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    for i in range(n):
        if i % 2 != 0:
            a[i] -= 1
    
    # print(sum(a))
    print("Yes" if sum(a) <= x else "No")
    

if __name__ == '__main__':
    sys.exit(main())
