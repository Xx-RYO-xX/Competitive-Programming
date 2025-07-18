import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    l_cnt = 0
    s = ""
    for i in range(n):
        c, l = input().split()
        l_cnt += int(l)
        if 100 < l_cnt:
            print("Too Long")
            return
        s += c*int(l)
    print(s)


if __name__ == '__main__':
    main()
