import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    print("Yes" if "A" in s and "B" in s else "No")
    


if __name__ == '__main__':
    sys.exit(main())
