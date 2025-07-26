import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = []
    
    sharped = False
    for S in s:
        if S == '#':
            t.append('#')
            sharped = False
        else:
            if not sharped:
                t.append('o')
                sharped = True
            else:
                t.append('.')
    
    print(*t, sep="")


if __name__ == '__main__':
    main()
