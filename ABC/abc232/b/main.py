import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = input()
    
    
    for k in range(1, 27):
        c = ""
        for ss in s:
            c += chr((ord(ss)+k)%26 + ord("a"))
        if c == t:
            print("Yes")
            return
    print("No")
    

if __name__ == '__main__':
    main()
