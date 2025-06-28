import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
    t = input()
    
    for i in range(n):
        if not (s[i] == t[i] or (s[i] in '1l' and t[i] in '1l') or (s[i] in '0o' and t[i] in '0o')):
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()
