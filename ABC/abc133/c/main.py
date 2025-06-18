import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    l, r = map(int, input().split())
    
    ans = float("inf")
    for i in range(l, min(l+2019, r)+1):
        for j in range(i+1, min(l+2019, r)+1):
            # print(ans)
            ans = min(ans, (i*j)%2019)

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
