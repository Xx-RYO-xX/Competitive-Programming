import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    
    s = sorted(s, key=lambda x:len(x))
    print("".join(s))


if __name__ == '__main__':
    sys.exit(main())
