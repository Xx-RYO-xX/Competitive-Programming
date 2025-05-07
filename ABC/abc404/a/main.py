import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    az = set("abcdefghijklmnopqrstuvwxyz")
    ans = az-set(s)
    print(list(ans)[0])


if __name__ == '__main__':
    sys.exit(main())
