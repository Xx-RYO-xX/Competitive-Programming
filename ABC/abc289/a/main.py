import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    
    for S in s:
        print(1-int(S), end="")
    print()


if __name__ == '__main__':
    main()
