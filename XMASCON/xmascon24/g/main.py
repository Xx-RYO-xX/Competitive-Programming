import sys 


def input():return sys.stdin.readline().rstrip()



def main():
    a, b, c, d, t = map(int, input().split())
    for _ in range(t):
        n = int(input())
        x = list(map(int, input().split()))
        
        if sum(x) % 2 == 0:
            print("Black")
        else:
            print("White")


if __name__ == '__main__':
    sys.exit(main())
