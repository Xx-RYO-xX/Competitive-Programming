import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    AZ = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for _ in range(h):
        a = list(map(int, input().split()))
        s = ""
        for A in a:
            s += AZ[A]
        print(s)


if __name__ == '__main__':
    sys.exit(main())
