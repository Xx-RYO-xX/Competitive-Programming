import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    
    while "#" in s:
        for i in range(len(s)):
            if s[i] == "#":
                print(i+1, end=",")
                s[i] = "."
                break
        for i in range(len(s)):
            if s[i] == "#":
                print(i+1)
                s[i] = "."
                break

if __name__ == '__main__':
    main()
