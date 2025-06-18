import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    k = int(input())
    a, b = map(int, input().split())

    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            return

    print("NG")
    return


if __name__ == '__main__':
    sys.exit(main())
