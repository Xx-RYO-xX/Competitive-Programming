import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, s = map(int, input().split())
    t = [0] + list(map(int, input().split()))
    
    for i in range(n):
        
        if abs(t[i] - t[i+1]) > s:
            print("No")
            return
    
    print("Yes")
    


if __name__ == '__main__':
    sys.exit(main())
