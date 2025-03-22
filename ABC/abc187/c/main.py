import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ss = set()
    bikkuri = set()
    for _ in range(n):
        s = input()
        if s[0] == "!":
            bikkuri.add(s)
        else:
            ss.add(s)
    
    for sss in ss:
        if "!"+sss in bikkuri:
            print(sss)
            return
    
    print("satisfiable")

if __name__ == '__main__':
    main()
