import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()
    print("Yes" if s == t[:len(s)] else "No")
    

if __name__ == '__main__':
    main()
