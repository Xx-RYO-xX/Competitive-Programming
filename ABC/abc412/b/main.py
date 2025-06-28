import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()
    for i in range(1, len(s)):
        if s[i].isupper() and s[i-1] not in t:
            print("No")
            return
    print("Yes")
    


if __name__ == '__main__':
    main()
