import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    w = Counter(input())

    for ww in w:
        if w[ww] % 2 != 0:
            print("No")
            return

    print("Yes")
    


if __name__ == '__main__':
    sys.exit(main())
