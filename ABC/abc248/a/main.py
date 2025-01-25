import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    for i in range(10):
        if str(i) not in s:
            print(i)
            exit()


if __name__ == '__main__':
    main()
