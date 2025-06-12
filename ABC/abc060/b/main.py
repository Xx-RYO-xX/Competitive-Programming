import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    
    for i in range(10**8):
        if (a*i) % b == c:
            print("YES")
            return
    print("NO")


if __name__ == '__main__':
    sys.exit(main())
