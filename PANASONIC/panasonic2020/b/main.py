import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    
    ans = (h*w+1) // 2
    
    if h == 1 or w == 1:
        ans = 1
    
    print(ans)


if __name__ == '__main__':
    main()
