import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    w = list(input().split())
    moji = {"and", "not", "that", "the", "you"}
    for ww in w:
        if ww in moji:
            print("Yes")
            return
    print("No")
    


if __name__ == '__main__':
    sys.exit(main())
