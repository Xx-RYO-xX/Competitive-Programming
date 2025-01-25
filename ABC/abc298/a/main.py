import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
    
    if "o" in s and "x" not in s:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()
