import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
    
    cond = False
    for i in range(n):
        if s[i] == "|":
            cond = not cond
        if s[i] == "*" and cond:
            print("in")
            exit()
    

if __name__ == '__main__':
    main()
