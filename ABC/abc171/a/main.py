import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a = input()
    
    if a.islower():
        print("a")
    else:
        print("A")


if __name__ == '__main__':
    sys.exit(main())
