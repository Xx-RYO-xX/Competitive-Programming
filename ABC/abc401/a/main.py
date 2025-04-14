import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = int(input())
    
    if 200 <= s <= 299:
        print("Success")
    else:
        print("Failure")


if __name__ == '__main__':
    sys.exit(main())
