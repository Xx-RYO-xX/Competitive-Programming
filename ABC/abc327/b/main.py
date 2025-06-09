import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    b = int(input())
    
    for i in range(20):
        if i**i == b:
            print(i)
            return
    
    print(-1)
    


if __name__ == '__main__':
    sys.exit(main())
