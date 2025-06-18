import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = input()
    if a == "a":
        print(-1)
    elif len(a) != 1:
        print(a[:-1])
    else:
        print(chr(ord(a)-1))


if __name__ == '__main__':
    sys.exit(main())
