import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()

    atcoder = set({"a", "t", "c", "o", "d", "e", "r", "@"})
    
    for i in range(len(s)):
        if s[i] == "@" and t[i] not in atcoder:
            print("You will lose")
            return
        elif t[i] == "@" and s[i] not in atcoder:
            print("You will lose")
            return
        elif s[i] != t[i] and (s[i] != "@" and t[i] != "@"):
            print("You will lose")
            return
    
    print("You can win")

if __name__ == '__main__':
    main()
