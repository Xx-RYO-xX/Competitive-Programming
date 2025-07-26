import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, l, r = map(int, input().split())
    s = input()
    
    for i in range(l-1, r):
        if s[i] == "x":
            print("No")
            return
    print("Yes")
    
    


if __name__ == '__main__':
    main()
